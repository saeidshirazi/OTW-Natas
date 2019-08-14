import requests
import re


# level 1 => 2

Username = "natas1"
Password = "gtVrDuiDfck831PqWsLEZy5gyDz1clto"

url = "http://{}.natas.labs.overthewire.org".format(Username) 

response = requests.get(url,auth=(Username,Password))

content = response.text

flag = re.findall('<!--The password for natas2 is (.*) -->',content)[0]
print(flag)