#! /usr/bin/python3
from pprint import pprint
from .utils import print_red
from .godaddy_api_wrapper import GodaddyApiWrapper


class Consumer:
    def __init__(self, que):
        self.que = que
        self.domains = []

    def consume_domains(self):
        gd = GodaddyApiWrapper()
        while True:
            domain = self.que.get().lower()
            response = gd.call_endpoint(domain)
            if len(response) > 0:
                record = {domain: response['price']}
                self.domains.append(record)
                pprint(record)
            else:
                print_red('%-50s Not Available' % domain)
            self.que.task_done()

    def get_domains(self):
        return self.domains
