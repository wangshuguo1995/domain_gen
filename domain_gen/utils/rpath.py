#! /usr/bin/python3
from os.path import realpath


class Rpath:
    def __init__(self):
        p = realpath(__file__)
        self.rpath = '/' + '/'.join([i for i in p.split("/")[:-2] if i])
        self.rpath += '/'

    def get_rpath(self):
        return self.rpath


class Subpaths(Rpath):
    def __init__(self):
        super(Subpaths, self).__init__()

    def get_rpath(self):
        return self.rpath

    def words_path(self):
        return self.rpath + 'resources/word_list.json'

    def config_path(self):
        return self.rpath + 'resources/config.yml'
