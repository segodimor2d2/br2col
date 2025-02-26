import requests
from pprint import pprint

# Substitua pelo seu access_token
access_token = 'APP_USR-293958870459442-022208-c7805683f2fa321a2d9d3d191480dd69-189502404'

# Defina o ID do produto
product_id = "MLB5056957218"

# URL da API para buscar o produto pelo ID
url = f"https://api.mercadolibre.com/items/{product_id}"

# Headers com o access_token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Fazendo a requisição
response = requests.get(url, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    data = response.json()
    pprint(data)

    # import ipdb; ipdb.set_trace()

else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)

# usando la api de mercadolivre, quero fazer uma busca de um produto usando o id do produto que é MLB5056957218
# curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN'  https://api.mercadolibre.com/sites/$SITE_ID/search?category=$CATEGORY_ID


import requests

# Defina o ID do produto
product_id = "MLB5056957218"

# 1. Buscar os dados do produto
item_url = f"https://api.mercadolibre.com/items/{product_id}"
response_item = requests.get(item_url)

if response_item.status_code == 200:
    product_data = response_item.json()
    
    # Extrair informações básicas
    sold_quantity = product_data.get("sold_quantity", 0)  # Número de vendidos
    title = product_data.get("title", "Produto sem título")
    
    print(f"Produto: {title}")
    print(f"Número de vendidos: {sold_quantity}")
    
    # 2. Buscar as avaliações do produto
    reviews_url = f"https://api.mercadolibre.com/reviews/item/{product_id}"
    response_reviews = requests.get(reviews_url)
    
    if response_reviews.status_code == 200:
        reviews_data = response_reviews.json()
        
        # Extrair informações das avaliações
        rating_average = reviews_data.get("rating_average", 0)  # Pontuação média
        total_reviews = reviews_data.get("paging", {}).get("total", 0)  # Número de avaliações
        
        print(f"Pontuação média: {rating_average}")
        print(f"Número de avaliações: {total_reviews}")
    else:
        print(f"Erro ao buscar avaliações: {response_reviews.status_code}")
        print(response_reviews.text)
else:
    print(f"Erro ao buscar o produto: {response_item.status_code}")
    print(response_item.text)
