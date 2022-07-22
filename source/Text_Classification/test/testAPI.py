import requests

url = 'https://localhost:44347/api/Home/GetAllBlackList'
response = requests.get(url, verify=False)
print('Status code: ', response.status_code)
print(response.json())
