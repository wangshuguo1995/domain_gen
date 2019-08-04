#! /usr/bin/python3
from .utils import get_pair, url_maker, read, site_exists


class Producer:
    def __init__(self, q, tld, words, max_records=100):
        self.que = q
        self.tld = tld
        self.words = read(words)
        self.max_records = max_records

    def get_doms(self):
        i = 0
        while i < self.max_records:
            domain = get_pair(self.words)
            exists = False
            for url in url_maker(domain, self.tld):
                if site_exists(url):
                    exists = True
                    print(domain + self.tld + ' \n\nEXISTS\n\n')
                    break
            if not exists:
                i += 1
                self.que.put(domain + self.tld)
