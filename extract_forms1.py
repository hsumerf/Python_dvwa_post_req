# python3
#!/usr/bin/env python
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

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
    post_url = urljoin(target_url, action)
    method = form.get("method")
    input_list = form.find_all("input")
    post_data = {}
    for input in input_list:
        input_name = input.get("name")
        input_type = input.get("type")
        input_value = input.get("value")
        if input_type == "text":
            input_value = "umer"

        post_data[input_name] = input_value
    result = requests.post(post_url, data=post_data)
print(input_name)
print(input_value)
soup = BeautifulSoup(response.content, 'html.parser')
print(soup.prettify())
