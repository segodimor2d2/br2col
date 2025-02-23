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


