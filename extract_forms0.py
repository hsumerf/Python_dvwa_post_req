# python3
#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup

def request(url):
    try:
        get_response = requests.get(url)
        return get_response
    except Exception:
        pass

target_url = "http://192.168.184.128/mutillidae/index.php?page=dns-lookup.php"
response = request(target_url)

print(response)
soup = BeautifulSoup(response.content, 'html.parser')
forms_list = soup.find_all("form")

for form in forms_list:
    action = form.get("action")
    method = form.get("method")

    input_list = form.find_all("input")
    for input in input_list:
        input_name = input.get("name")
print(action)
print(method)
print(input_name)
