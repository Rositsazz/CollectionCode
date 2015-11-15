from bs4 import BeautifulSoup
import json
import requests
# import matplotlib.pyplot as plt


class Histogram:

    def __init__(self):
        self.dictionary = {}

    def add(self, server_name):
        if server_name not in self.dictionary:
            self.dictionary[server_name] = 1
        else:
            self.dictionary[server_name] += 1

    def count(self, server_name):
        if server_name not in self.dictionary:
            return None
        return self.dictionary[server_name]

    def items(self):
        lst = []
        for key in self.dictionary:
            lst.append(key, self.dictionary[key])
        return lst

    def get_dict(self):
        return self.dictionary

    def save_links(self, domain, save_file):
        r = requests.get(domain)

        data = r.text

        soup = BeautifulSoup(data)
        result = []
        for link in soup.find_all('a'):
            a = link.get('href')
            result.append(a)
        with open(save_file, "w") as f:
            json.dump(result, f, indent=True)

    def make_requests(self, save_file, domain):
        servers = []
        headers = {}
        headers["User-Agent"] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
        r = requests.get(domain)

        data = r.text

        soup = BeautifulSoup(data)
        result = []
        for link in soup.find_all('a'):
            a = link.get('href')
            result.append(a)

        for element in result:
            element = str(element)

            if element[0] == "l":
                try:
                    req = requests.head(domain + "/" + element, headers=headers, allow_redirects=True, timeout=10)
                    request = req.headers["Server"]
                    servers.append(request)
                except:
                    "pass"

        with open(save_file, "w") as f:
            json.dump(result, f, indent=True)


def main():
    h = Histogram()
    h.make_requests("servers.json", "http://register.start.bg")
    with open('servers.json') as data_file:
        data = json.load(data_file)
    for element in data:
        h.add(element)
    hist = h.get_dict()
    # x = []
    # y = []
    # for element in hist:
    #     x.append(h.get_dict[element])
    #     y.append(h.get_dict)

    # plt.plot(x, y)
    # plt.show()
    # h.add("Apache")
    # h.add("Apache")
    # h.add("nginx")
    # h.add("IIS")
    # h.add("nginx")

    # h.count("Apache") == 2  # True
    # h.count("nginx") == 2  # True
    # h.count("IIS") == 1  # True
    # h.count("IBM Web Server") is None  # True

    # h.items()
    # h.get_dict()

if __name__ == '__main__':
    main()
