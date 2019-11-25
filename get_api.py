import requests

def test_add_student():
    api_url="https://reqres.in/api/users?page=2"
    response=requests.get(api_url)
    print(response.content)
