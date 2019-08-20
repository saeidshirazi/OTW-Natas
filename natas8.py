import requests
import re

# level 7 => 8

Username = "natas8"
Password = "DBfUBfqQG69KvJvJ1iAbMoIpwSNQ9bWe"

params = {"secret":"oubWYf2kBq","submit":"submit"}

session = requests.session()
url = "http://{}.natas.labs.overthewire.org".format(Username) 

response = session.post(url,auth=(Username,Password),data=params)

content = response.text



#print(content)
flag = re.findall('Access granted. The password for natas9 is (.*)',content)[0]
print(flag)