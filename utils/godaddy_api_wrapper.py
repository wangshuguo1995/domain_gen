#! /usr/bin/python3
from json import loads
from urllib.request import Request, urlopen
from .utils import api_keys


class GodaddyApiWrapper:
    def __init__(self):
        self.url = "https://api.godaddy.com/v1/domains/available?"
        self.url += "domain=%s&checkType=FULL&forTransfer=false"
        key, secret = api_keys()
        self.header = {
            "Authorization": "sso-key %s:%s" % (key, secret)
        }

    @staticmethod
    def convert_price(price):
        return price / (10 ** 6)

    def call_endpoint(self, domain_name):
        godaddy = self.url % domain_name
        try:
            r = Request(godaddy, headers=self.header)
            resp = loads(urlopen(r).read().decode())
        except Exception:
            return {}
        else:
            if resp['available'] and 'price' in resp:
                return {
                    "price": self.convert_price(resp['price']),
                    "domain": resp['domain']
                }
            return {}
