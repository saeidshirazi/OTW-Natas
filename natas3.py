import requests
import re


# level 2 => 3

Username = "natas3"
Password = "sJIJNW6ucpu6HPZ1ZAchaDtwd7oGrD14"

url = "http://{}.natas.labs.overthewire.org/s3cr3t/users.txt".format(Username) 

response = requests.get(url,auth=(Username,Password))

content = response.text

#print(content)
flag = re.findall('natas4:(.*)',content)[0]
print(flag)