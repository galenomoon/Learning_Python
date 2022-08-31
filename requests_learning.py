import requests 
response = requests.get('https://economia.awesomeapi.com.br/json/last/:moedas')
print(response.json())