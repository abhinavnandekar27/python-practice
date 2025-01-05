import requests as req
url = "https://webhook.site/82183cb5-9ffe-4d71-b043-0bd99c6162b9"
h = {"User-Agent":"Abhinav"}
data = req.get(url,timeout=10, headers=h)
print(data.status_code)
print(data.text)