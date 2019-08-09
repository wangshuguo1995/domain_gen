#! /usr/bin/python3
from .utils import get_pair, get_1st, get_2nd, read


class Producer:
    def __init__(self, q, conf, word_list_path):
        self.que = q
        self.arg = ''
        self.pos = 0
        self.words = read(word_list_path)
        if conf['default_word']['use_default']:
            self.arg = conf['default_word']['word']
            self.pos = int(conf['default_word']['position'])
        self.conf = conf

    def get_doms(self):
        i = 0
        if self.pos > 1:
            while i < self.conf['max_try']:
                domain = get_1st(self.arg, self.words)
                i += 1
                self.que.put(domain + self.conf['tld'])
        elif self.pos > 0:
            while i < self.conf['max_try']:
                domain = get_2nd(self.arg, self.words)
                i += 1
                self.que.put(domain + self.conf['tld'])
        else:
            while i < self.conf['max_try']:
                domain = get_pair(self.words)
                i += 1
                self.que.put(domain + self.conf['tld'])
