#! /usr/bin/python3
from .utils import print_red
from .godaddy_api_wrapper import GodaddyApiWrapper


class Consumer:
    def __init__(self, que):
        self.que = que
        self.domain_names = []

    def consume_domains(self):
        gd = GodaddyApiWrapper()
        while True:
            domain = self.que.get().lower()
            response = gd.call_endpoint(domain)
            if len(response) > 0:
                record = 'DOMAIN: %-50s' % response['domain']
                record += 'PRICE: %9s' % str(response['price'])
                print(record)
                self.domain_names.append(domain)
            else:
                print_red('%s\tNot Available' % domain)
            self.que.task_done()

    def get_domains(self):
        return self.domain_names
