import requests
from pprint import pprint

# https://produto.mercadolivre.com.br/MLB-3477406254-cadiveu-kit-blonde-reconstructor-4-produtos-home-care-_JM#is_advertising=true&position=19&search_layout=grid&type=pad&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=19&ad_click_id=N2E0YTViODUtZDkyMS00YzEzLTg0ZDEtNmEyMDFjZTQ3ZWVl
# Defina o ID do produto

# product_id = "MLB3899052665"
# product_id = "MLB5162646898"

# product_id = "MLB3477406254"
product_id = "MLB1583256293"

# https://www.mercadolivre.com.br/nutri-glow-leave-in-professional-creme-150ml-cadiveu/p/MLB20187465#polycard_client=search-nordic&searchVariation=MLB20187465&wid=MLB3899052665&position=18&search_layout=grid&type=product&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&sid=search

# Substitua pelo seu access_token
access_token = 'APP_USR-293958870459442-022310-834286236bedb7c89c635857476eb812-189502404'

# Headers com o token de autenticação
headers = {
    "Authorization": f"Bearer {access_token}"
}

# curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN' https://api.mercadolibre.com/items/MLA0000000

# 1. Buscar os dados do produto
item_url = f"https://api.mercadolibre.com/items/{product_id}"

response_item = requests.get(item_url, headers=headers)

if response_item.status_code == 200:
    product_data = response_item.json()

    pprint(product_data)
    # import ipdb; ipdb.set_trace()
    
    # Extrair informações básicas
    sold_quantity = product_data.get("sold_quantity", 0)  # Número de vendidos
    title = product_data.get("title", "Produto sem título")
    
    print(f"Produto: {title}")
    print(f"Número de vendidos: {sold_quantity}")
    
    # 2. Buscar as avaliações do produto
    reviews_url = f"https://api.mercadolibre.com/reviews/item/{product_id}"
    response_reviews = requests.get(reviews_url, headers=headers)
    
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
