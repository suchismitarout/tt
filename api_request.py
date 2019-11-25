import requests

response = requests.get('http://127.0.0.1:5000/info')
print(response.content)
print(response.text)
print(response.status_code)