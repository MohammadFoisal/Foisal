import requests

#POST

a=("Author:- Mohammad Foisal")
c=("_______________")
d=(" ")
b=("Facebook:- /mohammadfoisal.ARC")
print(a)
print(c)
print(d)
print(b)


Nickname = input("Enter your Banglalink  ID : ")

headers = {
    "x-app-key":"0skgg0ksg4880840w8w4gco0k4wckw0cg0w0w88s",
    "x-api-key":"e2394d344c00d5f872d874b045988059"
    }

url = "https://circle.happycell.mobi/mylife/appapi/appcall.php?op=getUserInfobyNickname&nickname=" + Nickname

req = requests.post(url, headers=headers,verify=False)
print(req.text)
