import requests
from pprint import pprint

# Substitua pelo seu access_token
access_token = 'APP_USR-293958870459442-022118-6355a06421b8781da12f1648623d7b2b-189502404'

# Termo de busca
# search_query = 'Kit Cadiveu Pro Nutri Glow'
search_query = 'Kit Cadiveu'

# URL da API de busca
url = f'https://api.mercadolibre.com/sites/MLB/search?q={search_query}'

# Headers com o access_token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# curl -X GET -H 'Authorization: Bearer $ACCESS_TOKEN'  https://api.mercadolibre.com/sites/$SITE_ID/search?category=$CATEGORY_ID

# Fazendo a requisição
response = requests.get(url, headers=headers)

# Verificando a resposta
if response.status_code == 200:
    data = response.json()
    produtos = data['results']

    pprint(produtos[0])

    import ipdb; ipdb.set_trace()

    for produto in produtos:
        print(f"Título: {produto['title']}")
        print(f"Preço: R${produto['price']}")
        print(f"Link: {produto['permalink']}")
        print('-' * 40)

else:
    print(f"Erro na requisição: {response.status_code}")
    print(response.text)

