
python 00mlanalitics.py co 4 esp32
python 00mlanalitics.py co 3 orange,pi,5

python 01mlanalitics.py co 3 orange,pi,5
python 01mlanalitics.py co 3 esp32,cam
python 01mlanalitics.py co 20 raspberry
python 01mlanalitics.py co 20 carro,control,remoto

python 02mlanalitics.py co 20 esp32,cam
python 02mlanalitics.py co 20 esp32


```python
soup.find_all('a', class_='andes-pagination__link')

Paginación

soup.find('ul', class_='andes-pagination')
soup.find_all('a', class_='andes-pagination__button')
andes-pagination


next_button =
soup.find('li', class_='andes-pagination__button andes-pagination__button--next')


soup.find('li', class_='andes-pagination__button andes-pagination__button--next')


ui-search-layout__item shops__layout-item


products = soup.find_all('li', class_='ui-search-layout__item')


andes-pagination__button andes-pagination__button--current


soup.find_all('li', class_='andes-pagination__button')

'https://listado.mercadolibre.com.co/esp32'

'https://listado.mercadolibre.com.co/esp32'

---

python 00mlanalitics.py co 4 esp32

soup.find('li', class_='andes-pagination__button andes-pagination__button--next')

soup.find_all('li', class_='andes-pagination__button')


python 02mlanalitics.py co 4 esp32

url
'https://listado.mercadolibre.com.co/esp32'

ipdb> link
'https://listado.mercadolibre.com.co/esp32'

python 02mlanalitics.py co 4 esp32

tst_scrape_mercado_livre(search_query, until=1, country='co')
tst_scrape_mercado_livre(search_query)

python 02mlanalitics.py co 4 esp32
tst_scrape_mercado_livre(search_query, all_products, pags_list, 1)

pagslinlk(soup)

asoup = BeautifulSoup(response.text, 'html.parser')
abtnlinks = {a.get_text(strip=True): a['href'] for a in asoup.find_all('a', class_='andes-pagination__link') if 'href' in a.attrs}
apglinks  = {int(k): v for k, v in abtnlinks.items() if k.isdigit()}



```python
---







```python


porque o primeiro codigo gera sim resultados, mas o seguindo não??

este é o primeiro codigo:

def tst_scrape_mercado_livre(search_query, all_products, pags_list, pagnum):
    country='co'
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

    print(f"\nColetando dados da página {page}...")

    url = link
    if link == '': url = f"{base_url}/{search_query}"

    verlink = pags_list[pagnum]

    # import ipdb; ipdb.set_trace()
    response = requests.get(verlink, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a página {page}. Status code: {response.status_code}")

    soup = BeautifulSoup(response.text, 'html.parser')
    btnlinks = {a.get_text(strip=True): a['href'] for a in soup.find_all('a', class_='andes-pagination__link') if 'href' in a.attrs}
    pglinks  = {int(k): v for k, v in btnlinks.items() if k.isdigit()}

    print(pglinks)



este é o segundo codigo:

def pagslinlk(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    btnlinks = {a.get_text(strip=True): a['href'] for a in soup.find_all('a', class_='andes-pagination__link') if 'href' in a.attrs}
    pglinks  = {int(k): v for k, v in btnlinks.items() if k.isdigit()}
    return pglinks

def tst_scrape_mercado_livre(search_query, all_products, pags_list, pagnum):
    country='co'
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

    print(f"\nColetando dados da página {page}...")

    url = link
    if link == '': url = f"{base_url}/{search_query}"

    verlink = pags_list[pagnum]

    # import ipdb; ipdb.set_trace()
    response = requests.get(verlink, headers=headers)
    if response.status_code != 200:
        print(f"Erro ao acessar a página {page}. Status code: {response.status_code}")


    pglinks = pagslinlk(response)
    print(pglinks)







```#python
