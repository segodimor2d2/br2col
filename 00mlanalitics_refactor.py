import requests
import time
import re
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime
from pathlib import Path
from tqdm import tqdm
import argparse

def scrape_mercado_livre(search_query, max_pages=1, country='co'):
    """Faz scraping dos produtos no Mercado Livre."""
    base_urls = {
        'co': "https://listado.mercadolibre.com.co",
        'br': "https://lista.mercadolivre.com.br"
    }
    
    if country not in base_urls:
        raise ValueError("País inválido. Escolha 'co' ou 'br'.")
    
    base_url = base_urls[country]
    headers = {"User-Agent": "Mozilla/5.0"}
    all_products = []
    page = 1
    link = f"{base_url}/{search_query}"
    
    while page <= max_pages:
        print(f"Coletando página {page}: {link}")
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
            all_products.append(parse_product(product))
        
        next_button = soup.select_one('li.andes-pagination__button--next a')
        if not next_button:
            break
        
        link = next_button['href']
        page += 1
    
    return all_products

def parse_product(product):
    """Extrai as informações de um produto."""
    return {
        'title': product.find('h3', class_='poly-component__title-wrapper').text.strip() if product.find('h3') else '',
        'price': extract_price(product),
        'rating_average': extract_float(product, 'span', 'poly-reviews__rating'),
        'total_reviews': extract_int(product, 'span', 'poly-reviews__total'),
        'permalink': product.find('a', class_='poly-component__title')['href'] if product.find('a') else ''
    }

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

def scrape_by_link(link):
    """Faz scraping da página de um produto específico."""
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(link, headers=headers)
    
    if response.status_code != 200:
        print(f"Erro ao acessar {link}: {response.status_code}")
        return None
    
    soup = BeautifulSoup(response.text, 'html.parser')
    vendidos = soup.find('span', class_='ui-pdp-subtitle')
    seller = soup.find(class_='ui-seller-data-header__title-container')
    
    vendidos_text = vendidos.text.strip() if vendidos else '0'
    seller_name = seller.text.strip().replace('Vendido por ', '') if seller else ''
    
    return [vendidos_text, seller_name]

def processar_linha(row):
    """Processa cada linha do DataFrame."""
    try:
        time.sleep(0.2)
        vendidos, seller = scrape_by_link(row['permalink']) or [None, None]
        return pd.Series([vendidos, seller])
    except Exception as e:
        print(f"Erro ao processar {row['permalink']}: {e}")
        return pd.Series([None, None])

def main():
    parser = argparse.ArgumentParser(description="Scrape Mercado Livre")
    parser.add_argument("country", choices=["co", "br"], help="País do Mercado Livre")
    parser.add_argument("pages", type=int, help="Número de páginas para buscar")
    parser.add_argument("search_query", type=str, help="Consulta de pesquisa")
    args = parser.parse_args()
    
    search_query = args.search_query.replace(',', '%20')
    produtos = scrape_mercado_livre(search_query, args.pages, args.country)
    
    if not produtos:
        print("Nenhum produto encontrado.")
        return
    
    df = pd.DataFrame(produtos)
    df = df.sort_values(by='price', ascending=False).reset_index(drop=True)
    
    tqdm.pandas(desc="Coletando detalhes")
    df[['sold_num', 'seller']] = df.progress_apply(processar_linha, axis=1)
    df['sold_num'] = df['sold_num'].fillna(0).astype(int)
    df.sort_values(by='sold_num', ascending=False, inplace=True)
    df.reset_index(drop=True, inplace=True)
    
    output_dir = Path("outcsv")
    output_dir.mkdir(exist_ok=True)
    
    time_atual = datetime.now().strftime('%Y%m%d%H%M%S')
    csv_filename = output_dir / f"{time_atual}_{args.country}.csv"
    df.to_csv(csv_filename, index=False)
    
    info_string = f"{time_atual}_{args.country}, numprod = {len(df)}, pags = {args.pages}, search = {args.search_query}"
    with open(output_dir / "info.md", 'a', encoding='utf-8') as arquivo:
        arquivo.write(info_string + '\n')
    
    print(f"Dados salvos em {csv_filename}")

if __name__ == "__main__":
    main()
