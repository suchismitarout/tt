import requests
import json
import jsonpath


url = "https://www.google.com/"
response = requests.get(url)
# assert response.status_code == 200
# print(response.headers)
# print(response.headers.get('Date'))
# print(response.headers.get('Server'))
# print(response.cookies)
# print(response.encoding)
# print(response.elapsed)
# print(response.content)
# json_rspn = response.json()
# print(response.text)
# pages = jsonpath.jsonpath(json_response, 'total_pages')
# print(pages[0])