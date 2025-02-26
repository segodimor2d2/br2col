import requests

refresh_token = "TG-67b8fe5b76d1e3000107166f-189502404"

url = "https://api.mercadolibre.com/oauth/token"

payload = f'grant_type=refresh_token&client_id=293958870459442&client_secret=1ulhZ4xSNa2xxPXuoynIYfWvuxjdV1cH&refresh_token={refresh_token}'
headers = {
  'accept': 'application/json',
  'content-type': 'application/x-www-form-urlencoded'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
