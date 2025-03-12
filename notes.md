



python 01mlanalitics.py co 3 orange,pi,zero

---

python -m venv myenv
python -m venv brtocol

---

organizar el df por mas vendidos después de capturar los vendidos y el seller
corregir error cuando la búsqueda no tiene resultados
tener la opción de todas las pagina
tener la opción de imprimir la lista hasta un numero de lineas para poder ver la tabla
organizar el código
construir programa que compara precios entre dos listas de productos
crear un Docker para instalar fácilmente en otras maquinas

---

https://auth.mercadolivre.com.br/authorization?response_type=code&client_id=293958870459442&redirect_uri=https://github.com/segodimor2d2/br2col


### res

https://github.com/segodimor2d2/br2col?code=TG-67b8f7c15959e700017a9008-189502404

TG-67b8f7c15959e700017a9008-189502404

https://github.com/segodimor2d2/br2col


---

# Trocando o code por um token `POSTMAN`

curl -X POST \
-H 'accept: application/json' \
-H 'content-type: application/x-www-form-urlencoded' \
'https://api.mercadolibre.com/oauth/token' \
-d 'grant_type=authorization_code' \
-d 'client_id=$APP_ID' \
-d 'client_secret=$SECRET_KEY' \
-d 'code=$SERVER_GENERATED_AUTHORIZATION_CODE' \
-d 'redirect_uri=$REDIRECT_URI' \
-d 'code_verifier=$CODE_VERIFIER' 

curl --location 'https://api.mercadolibre.com/oauth/token' \
--header 'accept: application/json' \
--header 'content-type: application/x-www-form-urlencoded' \
--data-urlencode 'grant_type=authorization_code' \
--data-urlencode 'client_id=293958870459442' \
--data-urlencode 'client_secret=1ulhZ4xSNa2xxPXuoynIYfWvuxjdV1cH' \
--data-urlencode 'code=TG-67b8f7c15959e700017a9008-189502404' \
--data-urlencode 'redirect_uri=https://github.com/segodimor2d2/br2col' \
--data-urlencode 'code_verifier=$CODE_VERIFIER'

### res
{"access_token":"APP_USR-293958870459442-022118-5631310843fa7b718a039d378e5753ce-189502404","token_type":"Bearer","expires_in":21600,"scope":"offline_access read write","user_id":189502404,"refresh_token":"TG-67b8f848152372000192b0ab-189502404"}

APP_USR-293958870459442-022118-5631310843fa7b718a039d378e5753ce-189502404
TG-67b8f848152372000192b0ab-189502404




---

curl -X POST \
-H 'accept: application/json' \
-H 'content-type: application/x-www-form-urlencoded' \
'https://api.mercadolibre.com/oauth/token' \
-d 'grant_type=refresh_token' \
-d 'client_id=293958870459442' \
-d 'client_secret=1ulhZ4xSNa2xxPXuoynIYfWvuxjdV1cH' \
-d 'refresh_token=TG-67b8f848152372000192b0ab-189502404'

### res
{"access_token":"APP_USR-293958870459442-022118-cd2f3590dd38182ef5ddc663c4948e67-189502404","token_type":"Bearer","expires_in":21600,"scope":"offline_access read write","user_id":189502404,"refresh_token":"TG-67b8fb0397a5a900019e0464-189502404"}

TG-67b8fb0397a5a900019e0464-189502404



---
### script em python para fazer os requests

```python
import requests

url = "https://api.mercadolibre.com/oauth/token"

payload = 'grant_type=refresh_token&client_id=293958870459442&client_secret=1ulhZ4xSNa2xxPXuoynIYfWvuxjdV1cH&refresh_token=TG-67b8f848152372000192b0ab-189502404'
headers = {
  'accept': 'application/json',
  'content-type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```


---


---


---
#### dados extranho
https://www.mercadolivre.com.br/nutri-glow-leave-in-professional-creme-150ml-cadiveu/p/MLB20187465#wid=MLB3899052665&sid=unknown
product_id = "MLB3899052665"

---
https://produto.mercadolivre.com.br/MLB-1583256293-kit-plastica-dos-fios-ativo-1-lt-sh-masc-300ml-original-_JM#polycard_client=search-nordic&position=55&search_layout=grid&type=item&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f


---

MLB26839777
MLB26839777
MLB5162646898
https://www.mercadolivre.com.br/cadiveu-professional-glamour-mascara-de-nutrico-200ml/p/MLB26839777#polycard_client=search-nordic&searchVariation=MLB26839777&wid=MLB5162646898&position=26&search_layout=grid&type=product&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&sid=search
Novo  |  +100 vendidos

MLB-3477406254
https://produto.mercadolivre.com.br/MLB-3477406254-cadiveu-kit-blonde-reconstructor-4-produtos-home-care-_JM#is_advertising=true&position=19&search_layout=grid&type=pad&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&is_advertising=true&ad_domain=VQCATCORE_LST&ad_position=19&ad_click_id=N2E0YTViODUtZDkyMS00YzEzLTg0ZDEtNmEyMDFjZTQ3ZWVl
Novo  |  +100 vendidos

MLB20187465
MLB20187465
MLB3899052665
https://www.mercadolivre.com.br/nutri-glow-leave-in-professional-creme-150ml-cadiveu/p/MLB20187465#polycard_client=search-nordic&searchVariation=MLB20187465&wid=MLB3899052665&position=18&search_layout=grid&type=product&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&sid=search
Novo  |  +500 vendidos

MLB-1583256293
https://produto.mercadolivre.com.br/MLB-1583256293-kit-plastica-dos-fios-ativo-1-lt-sh-masc-300ml-original-_JM#polycard_client=search-nordic&position=55&search_layout=grid&type=item&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f
Novo  |  +10mil vendidos


---

+100 vendidos.
+500 vendidos
+10mil vendidos

eu quero obter o numero de vendidos tipo +100 vendidos, +500 vendidos, +10mil vendidos, fazendo a requisição do mercado livre sem usar a API e sim usando tecnicas scraping 

minha url de exemplo é:

https://www.mercadolivre.com.br/nutri-glow-leave-in-professional-creme-150ml-cadiveu/p/MLB20187465#polycard_client=search-nordic&searchVariation=MLB20187465&wid=MLB3899052665&position=18&search_layout=grid&type=product&tracking_id=710c85fe-995b-4fbf-8809-446bb81cf81f&sid=search

---

pip install requests beautifulsoup4

---

# fluxo

chamar a função de busca e ver o máximo de produtos




# interesantes

'id': 'MLB1583256293',
'title': 'Plastica Dos Fios Cadiveu Combo 2 Unid. Passo 2',
'price': 59.85,
'vendidos': '+100 vendidos',
'rating_average' = reviews_data.get("rating_average", 0)  # Pontuação média
'total_reviews' = reviews_data.get("paging", {}).get("total", 0)  # Número de avaliações
'status': 'active',
'seller_id': 1966265164,
'permalink': 'https://produto.mercadolivre.com.br/MLB-5056957218-plastica-dos-fios-cadiveu-combo-2-unid-passo-2ima.png

---ils
'status': 'active',


'seller_id': 1966265164,


eu quero obter o resultado de uma busca de produtos no mercado livre fazendo a requisição do mercado livre sem usar a API, usando Python com as bibliotecas requests e BeautifulSoup para fazer o scraping, eu também quero os resultados das seguintes paginas que tiver na busca.

os dados que eu quero coletar são:

'id'
'title'
'price' 59.85,
'vendidos' exemplo '+100 vendidos',
'rating_average' Pontuação média se tiver
'total_reviews' Número de avaliações se tiver
'permalink'


'id'
'title'
'price'
'vendidos'
'rating_aqverage'
'total_reviews'
'permalink'

'status'
'seller_id'



search_query = 'fone%20tranya'

access_token = 'APP_USR-293958870459442-022318-f55eb1371781b897c5b2846ba9b46495-189502404'

---

## consegui capturar los seguintes atributos:

'title'
'price'
'rating_aqverage' nota
'total_reviews' numero de comentarios
'permalink' link

## baseado en el total_reviews y rating_aqverage vamos a requisitar los produtos para encontrar:

### 'vendidos' (numero de vendidos)

'status'
'seller_id'


Novo  |  +500 vendidos
Novo  |  +100 vendidos
Novo  |  +50 vendidos
Novo  |  +100 vendidos
Novo  |  +50 vendidos











