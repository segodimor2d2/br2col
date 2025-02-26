import requests
from bs4 import BeautifulSoup

# URL do produto
url = "https://www.mercadolivre.com.br/nutri-glow-leave-in-professional-creme-150ml-cadiveu/p/MLB20187465#polycard_client=search-nordic&searchVariation=MLB20187465&wid=MLB3899052665&position=18&search_layout=grid&type=product&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&sid=search"

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

    if vendidos_element:
        vendidos_text = vendidos_element.text.strip()
        print(f"Número de vendidos: {vendidos_text}")
    else:
        print("Elemento de vendidos não encontrado.")
else:
    print(f"Erro ao acessar a página: {response.status_code}")
