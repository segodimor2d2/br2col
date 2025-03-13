import requests
from bs4 import BeautifulSoup
import re, sys
import pandas as pd
import time
from datetime import datetime
import argparse

def extract_price(product):
    """Extrai o preço do produto."""
    price_element = product.find(class_='andes-money-amount--cents-superscript')
    return float(price_element.text[2:].replace('.', '').replace(',', '.')) if price_element else 0.0

def extract_float(product, tag, class_name):
    """Extrai valores float."""
    element = product.find(tag, class_=class_name)
    return float(element.text.replace(',', '.')) if element else 0.0

def extract_int(product, tag, class_name):
    """Extrai valores inteiros."""
    element = product.find(tag, class_=class_name)
    return int(re.sub(r'\D', '', element.text)) if element else 0


def parse_product(product, pagnum):
    return {
        'title': product.find('h3', class_='poly-component__title-wrapper').text.strip() if product.find('h3') else '',
        'price': extract_price(product),
        'rating_average': extract_float(product, 'span', 'poly-reviews__rating'),
        'total_reviews': extract_int(product, 'span', 'poly-reviews__total'),
        'pagnum': pagnum,
        'permalink': product.find('a', class_='poly-component__title')['href'] if product.find('a') else ''
    }


def export_csv(df, args, num_pages, count_nonzero):
    output_dir = 'outcsv'
    time_atual = datetime.now().strftime('%Y%m%d%H%M%S')
    csv_filename =  f"{output_dir}/{time_atual}_{args.country}.csv"
    df.to_csv(csv_filename, index=False)

    info_string = (
        f"filename = {time_atual}_{args.country}, "
        f"num_pages = {num_pages}, "
        f"numProd = {len(df)}, "
        f"nonzeroReviews = {count_nonzero}, "
        f"search = {args.search_query}"
    )

    print('\n'+info_string)

    with open(output_dir+"/info.md", 'a', encoding='utf-8') as arquivo:
        arquivo.write(info_string + '\n')

    print(f"\nDados salvos em {csv_filename}")
    return csv_filename

def scrape_mercado_livre(search_query, max_pages=1, country='co'):
    """Faz scraping dos produtos no Mercado Livre."""
    base_urls = {
        'co': "https://listado.mercadolibre.com.co",
        'br': "https://lista.mercadolivre.com.br"
    }
    
    if country not in base_urls:
        raise ValueError("País inválido. Escolha 'co' ou 'br'.")
    
    base_url = base_urls[country]
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    all_products = []
    page = 1
    link = f"{base_url}/{search_query}"
    
    while page <= max_pages:
        print(f"Coletando página {page}: {link}")
        time.sleep(1.5)

        response = requests.get(link, headers=headers)
        if response.status_code != 200:
            print(f"Erro {response.status_code} ao acessar a página {page}.")
            break
        
        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('li', class_='ui-search-layout__item')
        if not products:
            print("Nenhum produto encontrado. Encerrando...")
            break
        
        for product in products:
            all_products.append(parse_product(product, page))
        
        next_button = soup.find('li', class_='andes-pagination__button andes-pagination__button--next')
        if not next_button or 'andes-pagination__button--disabled' in next_button.get('class', []):
            print("Não há mais páginas. Encerrando...")
            break
        
        # link = next_button['href']
        link = next_button.find('a', class_='andes-pagination__link').get('href')

        page += 1
        time.sleep(0.2)
    
    return all_products, page

def scrape_pages(search_query, all_products, pags_list, pagnum):
    """Faz scraping das paginas do Mercado Livre."""
    
    time.sleep(1.5)

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

    link = pags_list[pagnum]

    response = requests.get(link, headers=headers)
    if response.status_code != 200:
        print(f"Erro {response.status_code} ao acessar a página {link}.")
        return all_products, pags_list
    
    soup = BeautifulSoup(response.text, 'html.parser')
    products = soup.find_all('li', class_='ui-search-layout__item')
    if not products:
        print("Nenhum produto encontrado. Encerrando...")
        return all_products, pags_list

    for product in products:
        all_products.append(parse_product(product, pagnum))

    # pags_links = soup.find_all('li', class_='andes-pagination__button')

    pags_links = soup.find_all('a', class_='andes-pagination__link')
    # resultados = [(paglink.get_text(strip=True), paglink.get('href')) for paglink in pags_links]
    resultados = {paglink.get_text(strip=True): paglink.get('href') for paglink in pags_links}
    pags_list.update(resultados)

    print(pags_list)
    import ipdb; ipdb.set_trace()

    # next_button = soup.find('li', class_='andes-pagination__button andes-pagination__button--next')
    # if not next_button or 'andes-pagination__button--disabled' in next_button.get('class', []):
    #     print("Não há mais páginas. Encerrando...")
    #     break
        
    # link = next_button['href']
    # link = next_button.find('a', class_='andes-pagination__link').get('href')

    return all_products, pags_list

def first_link(search_query, country):
    base_urls = {
        'co': "https://listado.mercadolibre.com.co",
        'br': "https://lista.mercadolivre.com.br"
    }
    
    if country not in base_urls:
        raise ValueError("País inválido. Escolha 'co' ou 'br'.")
    
    base_url = base_urls[country]

    link = f"{base_url}/{search_query}"
    return link

#########################################################################

def main():
    parser = argparse.ArgumentParser(description="Scrape Mercado Livre")
    parser.add_argument("country", choices=["co", "br"], help="País do Mercado Livre")
    parser.add_argument("pages", type=int, help="Número de páginas para buscar")
    parser.add_argument("search_query", type=str, help="Consulta de pesquisa")
    args = parser.parse_args()
    search_query = args.search_query.replace(',', '%20')
    csv_filenam = ''
    all_products = []
    pags_list = {} 

    # first_link(search_query, country)

    link = first_link(search_query, args.country)
    pags_list[1] = link

    all_products, index_pags_list = scrape_pages(search_query, all_products, pags_list, 1)

    print(all_products)

    # pags_list
    # pags_num

    # produtos, num_pages = scrape_mercado_livre(search_query, args.pages, args.country)

    # if not produtos:
    #     print("Nenhum produto encontrado.")
    #     return
    #
    # df = pd.DataFrame(produtos)
    # df.sort_values(by='total_reviews', ascending=False).reset_index(drop=True)
    #
    # count_nonzero = (df['total_reviews'] != 0).sum()
    # print(f'\ntotal_reviews non zero: {count_nonzero}')
    #
    # csv_filenam = export_csv(df, args, num_pages, count_nonzero)

if __name__ == "__main__":
    main()
