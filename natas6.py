import requests
import re

# level 5 => 6

Username = "natas6"
Password = "aGoY4q2Dc6MgDq4oL4YtoKtyAg9PeHa1"

params = {"secret":"FOEIUWGHFEEUHOFUOIU","submit":"submit"}
session = requests.session()
url = "http://{}.natas.labs.overthewire.org/".format(Username) 

response = session.post(url,auth=(Username,Password),data=params)

content = response.text



#print(content)
flag = re.findall('Access granted. The password for natas7 is (.*)',content)[0]
print(flag)