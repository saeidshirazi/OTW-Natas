import requests
import re

Username = "natas0"
Password = Username

url = "http://{}.natas.labs.overthewire.org".format(Username) 

response = requests.get(url,auth=(Username,Password))

content = response.text
 
flag = re.findall('<!--The password for natas1 is (.*) -->',content)[0]
print(flag)