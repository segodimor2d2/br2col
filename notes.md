
https://github.com/segodimor2d2/br2col
https://github.com/segodimor2d2/br2col?code=TG-67b276bb45f9fb00015cb527-189502404

---

293958870459442

1ulhZ4xSNa2xxPXuoynIYfWvuxjdV1cH


---

# GERAR CODE
- logado no ML

https://auth.mercadolivre.com.br/authorization?response_type=code&client_id=$1735423776486220&redirect_uri=$https://github.com/segodimor2d2/br2col&code_challenge=$CODE_CHALLENGE&code_challenge_method=$CODE_METHOD

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










