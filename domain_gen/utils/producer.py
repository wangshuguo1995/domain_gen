#! /usr/bin/python3
from .utils import get_pair, read


class Producer:
    def __init__(self, q, tld, words, max_=100):
        self.que = q
        self.words = read(words)
        self.max_ = max_
        self.tld = tld

    def get_doms(self):
        i = 0
        while i < self.max_:
            domain = get_pair(self.words)
            i += 1
            self.que.put(domain + self.tld)
