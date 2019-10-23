import requests
import argparse
from bs4 import BeautifulSoup
import re
import os.path
import queue
import numpy as np
from typing import Iterable, Tuple
import matplotlib.pyplot as plt
import networkx as nx


class CrawlerItem():
    def __init__(self, url, depth):
        self.url = url
        self.depth = depth


class Crawler():
    def __init__(self, initial_url, max_depth):
        self.initial_url = initial_url
        self.max_depth = max_depth

    def crawl(self):
        result = list()

        myqueue = queue.Queue()
        myqueue.put(CrawlerItem(self.initial_url, 1))

        while not myqueue.empty():
            item = myqueue.get()
            url = item.url

            response = requests.get(url)
            plain_text = response.text
            soup = BeautifulSoup(plain_text, "html.parser")
            rate = soup.find(id='bodyContent')

            extension_whitelist = ['.html', '.htm', '']
            new_list = list()
            new_new_list = list()

            for link in rate.findAll('a', attrs={'href': re.compile("^/wiki/")}):
                new_list.append('https://en.wikipedia.org' + link.get("href"))

            for link in new_list:
                if os.path.splitext(link)[1] in extension_whitelist:
                    new_new_list.append(link)

            new_new_list = list(np.random.choice(new_list, 5, replace=False))

            for link in new_new_list:
                result.append((url, link))

                if item.depth < self.max_depth:
                    myqueue.put(CrawlerItem(link, item.depth + 1))

        return result
        # my_chart = nx.Graph
        # my_chart.add_edges_from(result)
        # nx.draw(my_chart, with_labels=True, font_weight='bold')


my_crawl = Crawler('https://en.wikipedia.org/wiki/Router_(computing)', 1)
for x in my_crawl.crawl():
    print(x)



# https://en.wikipedia.org/wiki/Router_(computing)


# my_file = []
# for x in rate:
#     my_file.append(x._json)
#
# with open('data.json', 'w') as f:
#     json.dump(my_file, f)
#
# with open('data.json', 'r') as f:
#     data = json.load(f)