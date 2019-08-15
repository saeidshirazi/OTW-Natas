import requests
import re


# level 1 => 2

Username = "natas2"
Password = "ZluruAthQk7Q2MqmDeTiUij2ZvWy2mBi"

url = "http://{}.natas.labs.overthewire.org/files/users.txt".format(Username) 

response = requests.get(url,auth=(Username,Password))

content = response.text

#print(content)
flag = re.findall('natas3:(.*)',content)[0]
print(flag)