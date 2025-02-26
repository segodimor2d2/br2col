import requests
from pprint import pprint

# Substitua pelo seu access_token (se necessário)
access_token = 'APP_USR-293958870459442-022214-3e2168b9ab8b965c3e1c723afac31d86-189502404'

item_id = 'MLB5162646898'

# URL do endpoint de detalhes do item
url = f'https://api.mercadolibre.com/items/{item_id}'

# Cabeçalho de autorização
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Fazer a requisição GET
response = requests.get(url, headers=headers)

# Verificar se a requisição foi bem-sucedida
if response.status_code == 200:
    item_data = response.json()
    sold_quantity = item_data.get('sold_quantity', 0)
    print(f'Número de unidades vendidas: {sold_quantity}')
else:
    print(f'Erro ao obter detalhes do item: {response.status_code}')
