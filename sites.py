from bs4 import BeautifulSoup
import json
import requests

headers = {}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
domain = requests.get("http://register.start.bg")

data = domain.text

soup = BeautifulSoup(data)
result = []
for link in soup.find_all('a'):
    a = link.get('href')
    result.append(a)
with open("links.json", "w") as f:
    json.dump(result, f, indent=True)


with open('links.json') as data_file:
    data = json.load(data_file)

for element in data:
    element = str(element)
    # print(element[0])
    if element[0] == "l":
        try:
            req = requests.head("http://register.start.bg/" + element, headers=headers, allow_redirects=True, timeout=10)
            print(req.headers["Server"])
        except:
            "pass"
# print(count)
