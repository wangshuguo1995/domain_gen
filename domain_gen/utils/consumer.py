#! /usr/bin/python3
from .utils import url_maker, site_exists, print_red
from .godaddy_api_wrapper import GodaddyApiWrapper


class Consumer:
    def __init__(self, que):
        self.que = que
        self.domain_names = []

    def consume_domains(self):
        gd = GodaddyApiWrapper()
        while True:
            domain = self.que.get()
            exists = False
            for url in url_maker(domain):
                if site_exists(url):
                    exists = True
                    print_red('%s ALREADY EXISTS' % domain)
                    break
            if not exists:
                print('%s does not exist' % domain)
                #response = gd.call_endpoint(domain)
                #if len(response) > 0:
                #    out = 'DOMAIN: %12s\t' % response['domain']
                #    out += 'PRICE: %s' % str(response['price'])
                #    print(out)
                #    self.domain_names.append(domain)
            self.que.task_done()

    def get_domains(self):
        return self.domain_names
