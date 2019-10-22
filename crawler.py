from typing import Dict
import requests
import argparse
import pprint
from bs4 import BeautifulSoup
import re
import os.path
import pprint

extension_whitelist = ['.html', '.htm', '']
href = []
updated_list = []

response = requests.get('https://en.wikipedia.org/wiki/Router_(computing)')
plain_text = response.text
soup = BeautifulSoup(plain_text, "html.parser")
rate = soup.find('body')


for link in rate.findAll('a', attrs={'href': re.compile("^/wiki/")}):
    href.append(link.get('href'))

for x in href:
    if os.path.splitext(x)[1][1:] in extension_whitelist:
        updated_list.append(x)









# class Uri():
#     """
#     Uri Class
#     """
#
#     @staticmethod
#     def new():
#         return UriBuilder()
#
#     def __init__(self, scheme: str, host: str, port: int, path: str):
#         self.scheme = scheme
#         self.host = host
#         self.port = port
#         self.path = path
#
#     def getme(self):
#         response = requests.get(self.to_string())
#         return response.text
#
#         # return requests.get(self.to_string())
#
#     def to_string(self):
#         # input = "&".join(f'{k}={v}' for k, v in self.qparam.items())
#         return f'{self.scheme}://{self.host}:{self.port}/{self.path}'
#
#
# class UriBuilder():
#     """
#     Build the web uri:  scheme, host, path and parameter
#     """
#
#     def __init__(self, scheme: str = None, host: str = None, port: int = None, path: str = None):
#         self.scheme = scheme
#         self.host = host
#         self.port = port
#         self.path = path
#
#     def with_scheme(self, scheme):
#         return UriBuilder(scheme=scheme, host=self.host, port=self.port, path=self.path)
#
#     def with_host(self, host):
#         return UriBuilder(scheme=self.scheme, host=host, port=self.port, path=self.path)
#
#     def with_port(self, port):
#         return UriBuilder(scheme=self.scheme, host=self.host, port=port, path=self.path)
#
#     def with_path(self, path):
#         return UriBuilder(scheme=self.scheme, host=self.host, port=self.port, path=path)
#
#     def to_uri(self):
#         return Uri(scheme=self.scheme, host=self.host, port=self.port, path=self.path)
#
#
# def main():
#     parser = argparse.ArgumentParser(description="Let's get some data son!")
#     parser.add_argument('--scheme', type=str, help='Please enter a scheme (ex. http)')
#     parser.add_argument('--host', type=str, help='Please enter a host (ex. demo.codingnomads.co)')
#     parser.add_argument('--port', type=int, help='Please enter a port (ex. 8080)')
#     parser.add_argument('--path', type=str, help='Please enter a host (ex. tasks_api/users)')
#     args = parser.parse_args()
#
#     u = Uri.new().with_scheme(args.scheme).with_host(args.host).with_port(args.port).with_path(args.path)
#     print(u.to_uri().to_string())
#     print(u.to_uri().getme())
#
#
# if __name__ == '__main__':
#     main()