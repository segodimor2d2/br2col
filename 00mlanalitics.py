import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
from datetime import datetime

def scrape_mercado_livre(search_query, until=1, country='co'):
    if country == 'co':
        base_url = "https://listado.mercadolibre.com.co"
    elif country == 'br':
        base_url = "https://lista.mercadolivre.com.br"
    else:
        raise ValueError("Country must be 'co' or 'br'")


    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    all_products = []
    link = ''
    page = 1

    while True:
        print(f"\nColetando dados da página {page}...")
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


def scrape_by_link(link):

    # URL do produto
    url = link

    # Headers para simular uma requisição de navegador
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    # Fazendo a requisição
    response = requests.get(url, headers=headers)

    # import ipdb; ipdb.set_trace()

    # Verificando se a requisição foi bem-sucedida
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Procurando o elemento que contém o número de vendidos
        vendidos_element = soup.find('span', class_='ui-pdp-subtitle')

        # Seller
        seller = soup.find(class_='ui-seller-data-header__title-container')
        seller = seller.text.strip().replace('Vendido por ', '') if seller else ''

        if vendidos_element:
            vendidos_text = vendidos_element.text.strip()
            # print(f"Número de vendidos: {vendidos_text}")
            return [vendidos_text, seller]
        else:
            # print("Elemento de vendidos não encontrado.")
            return None
    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        return None




# Exemplo de uso
# search_query = 'fone%20tranya'
# search_query = 'tranya'
# search_query = 'xiaomi%20poco%20F5%20pro'
# search_query = 'xiaomi-poco-f6-pro'
search_query = 'esp32s3'

# Solicita ao usuário que insira
in_search = input("\nserach: ")
search_query = in_search.replace(' ', '%20')
pags = int(input("pags: "))
country = input("county: ")

produtos = scrape_mercado_livre(search_query, pags, country)
print(f'\nProdutos no total {len(produtos)}')

# Exibir os dados coletados
# for produto in produtos:
#     print(produto)

# Convert to DataFrame
df = pd.DataFrame(produtos)
# print(df.iloc[0])

# Ordenando o DataFrame pela coluna 'total_reviews' em ordem decrescente
df_ordenado = df.sort_values(by='total_reviews', ascending=False)

# Redefinir o índice
df_ordenado = df_ordenado.reset_index(drop=True)
# ordenar o original df.sort_values(by='total_reviews', ascending=False, inplace=True)

# print(df_ordenado.iloc[0])


print()
print(df_ordenado)



# Função para processar cada linha
def processar_linha(row):
    print(row['title'])

    link = row['permalink']

    try:
        time.sleep(0.2)
        res = scrape_by_link(link)
        numeros = re.findall(r'\d+', res[0])
        seller = res[1]
        return [numeros[0], seller] if [numeros, seller] else [None, None]
        # return pd.Series([int(numeros[0]), seller]) if [numeros, seller] else pd.Series([None, None])

    except Exception as e:
        print(f"Erro ao processar o link {link}: {e}")
        return [None, None]


# Adicionando a nova coluna vazia
df_ordenado['sold_num'] = None  # Ou pd.NA, ou np.nan, dependendo do caso
df_ordenado['seller'] = None

print()
# Solicita ao usuário que insira o valor de rows_num
rows_num = int(input("\nDigite até que linhas que deseja processar: "))

# Aplica a função às primeiras linhas
res_linha = df_ordenado.head(rows_num).apply(processar_linha, axis=1)

for numitem in range(len(res_linha)):
    # Inserindo um valor
    df_ordenado.at[numitem, 'sold_num'] = res_linha[numitem][0]
    df_ordenado.at[numitem, 'seller'] = res_linha[numitem][1]
    
# df_ordenado['sold_num'], df_ordenado['seller']

# Exibe o DataFrame atualizado
print()
print(df_ordenado)

# Caminho para a pasta onde você quer salvar o arquivo CSV
caminho_da_pasta = 'outcsv/'

# Nome do arquivo CSV
time_atual = datetime.now().strftime('%Y%m%d%H%M%S')
nomfile = f'{time_atual}_{country}'
nomarquivo = f'{nomfile}.csv'

# Caminho completo para o arquivo CSV
caminho_completo = caminho_da_pasta + nomarquivo

# Exportando o DataFrame para CSV
df.to_csv(caminho_completo, index=False)

# string para outcsv/info
infostring = f'{nomfile}, res: {len(df_ordenado)}: search: {in_search}'

with open('outcsv/info.md', 'a', encoding='utf-8') as arquivo:
    arquivo.write(infostring + '\n')



