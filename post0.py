#!/usr/bin/env python

import requests
from  bs4 import BeautifulSoup

target_url = "http://192.168.184.128/dvwa/login.php"

data_dict = {"username":"admin","password":"password","Login":"submit"}
print(data_dict)
response = requests.post("http://192.168.184.133/dvwa/login.php", data=data_dict)
print(response.url)
print(response)
response = str(response.content)
if "Damn Vulnerable Web App" in response:
    print("True")
soup = BeautifulSoup(response, 'html.parser')
print(soup.prettify())

