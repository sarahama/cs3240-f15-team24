import urllib.request, json
url = "http://127.0.0.1:8000/"
response = urllib.request(url)
data = json.loads(response)
print (data)