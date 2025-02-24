import requests
from bs4 import BeautifulSoup
import re
import pandas as pd

def scrape_mercado_livre(search_query, until=1):
    base_url = "https://lista.mercadolivre.com.br"
    # base_url = "https://listado.mercadolibre.com.co"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    all_products = []
    link = ''
    page = 1

    while True:
        print(f"Coletando dados da página {page}...")
        # url = f"{base_url}/{search_query}_Desde_{(page - 1) * 50 + 1}"

        url = link

        if link == '': url = f"{base_url}/{search_query}"

        print(url)
        response = requests.get(url, headers=headers)

        if response.status_code != 200:
            print(f"Erro ao acessar a página {page}. Status code: {response.status_code}")
            break

        soup = BeautifulSoup(response.text, 'html.parser')
        products = soup.find_all('li', class_='ui-search-layout__item')

        if not products:
            print("Nenhum produto encontrado. Encerrando...")
            break

        for product in products:
            product_data = {}

            # Title
            title_element = product.find('h3', class_='poly-component__title-wrapper')
            product_data['title'] = title_element.text.strip() if title_element else ''

            # Price
            price_amount = product.find(class_='andes-money-amount--cents-superscript')
            product_data['price'] = float(price_amount.text[2:].replace('.', '').replace(',', '.')) if price_amount else 0.0

            # Vendidos
            # vendidos_element = product.find('span', class_='ui-search-item__group__element ui-search-item__sold')
            # product_data['vendidos'] = vendidos_element.text.strip() if vendidos_element else ''

            # Rating Average
            rating_element = product.find('span', class_='poly-reviews__rating')
            product_data['rating_average'] = float(rating_element.text.replace(',', '.')) if rating_element else 0.0

            # Total Reviews
            reviews_element = product.find('span', class_='poly-reviews__total')
            if reviews_element:
                reviews_text = reviews_element.text.strip()
                product_data['total_reviews'] = int(re.sub(r'\D', '', reviews_text))
            else:
                product_data['total_reviews'] = 0

            # Permalink
            link_element = product.find('a', class_='poly-component__title')
            product_data['permalink'] = link_element.get('href', '') if link_element else ''

            all_products.append(product_data)

        print(f"{len(products)} produtos coletados na página {page}.")

        # Verifica se há uma próxima página
        next_button = soup.find('li', class_='andes-pagination__button andes-pagination__button--next')
        if not next_button or 'andes-pagination__button--disabled' in next_button.get('class', []):
            print("Não há mais páginas. Encerrando...")
            break

        page += 1

        if page > until:

            print("Número máximo de páginas atingido. Encerrando...")
            break

        link = next_button.find('a', class_='andes-pagination__link').get('href')

    return all_products

# Exemplo de uso
# search_query = 'fone%20tranya'
# search_query = 'tranya'
# search_query = 'xiaomi%20poco%20F5%20pro'
# search_query = 'xiaomi-poco-f6-pro'
search_query = 'esp32s3'

produtos = scrape_mercado_livre(search_query)
print(f'\nProdutos no total {len(produtos)}')

# Exibir os dados coletados
# for produto in produtos:
#     print(produto)


# Convert to DataFrame and save to CSV
df = pd.DataFrame(produtos)
print(df.iloc[0])


# Ordenando o DataFrame pela coluna 'total_reviews' em ordem decrescente
df_ordenado = df.sort_values(by='total_reviews', ascending=False)

# Redefinir o índice
df_ordenado = df_ordenado.reset_index(drop=True)

print(df_ordenado.iloc[0])

# ordenar o original
# df.sort_values(by='total_reviews', ascending=False, inplace=True)



import ipdb; ipdb.set_trace()


