import requests

response = requests.get("https://localhost:44347/api/Home/GetAllBlackList", verify=False)
print(response.status_code)
print(response.json())