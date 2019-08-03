#! /usr/bin/python3
from .utils import get_pair, url_maker, read, site_exists


class Producer:
    def __init__(self, que, top_level_domain, words_path):
        self.que = que
        self.tld = top_level_domain
        self.words = read(words_path)

    def get_domains(self):
        while True:
            domain = get_pair(self.words)
            exists = False
            for url in url_maker(domain, self.tld):
                if site_exists(url):
                    exists = True
                    print(domain + self.tld + ' \n\nEXISTS\n\n')
                    break
            if not exists:
                self.que.put(domain + self.tld)
