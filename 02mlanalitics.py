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

def pagslinlk(soup):
    btnlinks = {a.get_text(strip=True): a['href'] for a in soup.find_all('a', class_='andes-pagination__link') if 'href' in a.attrs}
    pglinks  = {int(k): v for k, v in btnlinks.items() if k.isdigit()}
    return pglinks

def export_csv(df, args, topage, count_nonzero, max_key_pags):
    output_dir = 'outcsv'
    time_atual = datetime.now().strftime('%Y%m%d%H%M%S')
    csv_filename =  f"{output_dir}/{time_atual}_{args.country}.csv"
    df.to_csv(csv_filename, index=False)

    info_string = (
        f"fileName = {time_atual}_{args.country}, "
        f"toPage = {topage}, "
        f"maxPages = {max_key_pags}, "
        f"numProd = {len(df)}, "
        f"nonZeroReviews = {count_nonzero}, "
        f"search = {args.search_query}"
    )

    with open(output_dir+"/info.md", 'a', encoding='utf-8') as arquivo:
        arquivo.write(info_string + '\n')

    print('\n'+info_string.replace(', ', '\n'))

    print(f"\nDados salvos em {csv_filename}")
    return csv_filename

def scrape_pages(search_query, all_products, pags_list, pagnum):
    print(f"\nColetando dados da página {pagnum}...")

    url = pags_list[pagnum]
    if pagnum == 1: pags_list.pop(1, None) 

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Erro ao acessar a página {pagnum}. Status code: {response.status_code}")
        return

    if not response.text.strip():
        print("A resposta da página está vazia!")
        return {}

    soup = BeautifulSoup(response.text, 'html.parser')

    if pagnum == 1 or pagnum == 10:
        pags_list.update(pagslinlk(soup))

    products = soup.find_all('li', class_='ui-search-layout__item')
    if not products:
        print("Nenhum produto encontrado. Encerrando...")
        return all_products, pags_list

    for product in products:
        all_products.append(parse_product(product, pagnum))

    return all_products, pags_list

#########################################################################

def main():
    parser = argparse.ArgumentParser(description="Scrape Mercado Livre")
    parser.add_argument("country", choices=["co", "br"], help="País do Mercado Livre")
    parser.add_argument("topage", type=int, help="Número de páginas para buscar")
    parser.add_argument("search_query", type=str, help="Consulta de pesquisa")
    args = parser.parse_args()
    search_query = args.search_query.replace(',', '%20')
    csv_filenam = ''
    all_products = []
    pags_list = {} 

    link = first_link(search_query, args.country)
    pags_list[1] = link
    print(link)
    print()

    all_products, pags_list = scrape_pages(search_query, all_products, pags_list, 1)
    
    if 10 in pags_list:
        all_products, pags_list = scrape_pages(search_query, all_products, pags_list, 10)

    max_key_pags = max(pags_list.keys(), default=None)

    if max_key_pags is not None:
        print(f"\nMax páginas encontradas: {max_key_pags}")

    for i in pags_list:
        if i not in {1, 10} and (max_key_pags < args.topage or i <= args.topage):
            all_products, pags_list = scrape_pages(search_query, all_products, pags_list, i)

    print(f'\nall_products len = {len(all_products)}')

    if not all_products:
        print("Nenhum produto encontrado.")
        return

    df = pd.DataFrame(all_products)
    df.sort_values(by='total_reviews', ascending=False).reset_index(drop=True)

    count_nonzero = (df['total_reviews'] != 0).sum()
    print(f'\ntotal_reviews non zero: {count_nonzero}')

    csv_filenam = export_csv(df, args, args.topage, count_nonzero, max_key_pags)

if __name__ == "__main__":
    main()
