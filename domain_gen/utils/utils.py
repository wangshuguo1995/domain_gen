#! /usr/bin/python3
from yaml import safe_load
from json import load, dump
from random import randint
from urllib.request import urlopen
from os import environ
from colorama import init
from colorama import Fore, Style


def write(path, json_data):
    with open(path, 'w') as json_out:
        dump(json_data, json_out)


def read(path):
    with open(path) as json_in:
        return load(json_in)


def get_config(path):
    with open(path) as yml_in:
        return safe_load(yml_in)


def get_pair(words):
    return words[randint(0, len(words)-1)] + words[randint(0, len(words)-1)]


def url_maker(phrase, tld):
    return [
        'http://%s%s' % (phrase, tld),
        'https://%s%s' % (phrase, tld),
        'http://www.%s.%s' % (phrase, tld),
        'https://www.%s.%s' % (phrase, tld)
    ]


def site_exists(url):
    try:
        urlopen(url, timeout=4)
    except Exception:
        return False
    return True


def api_keys():
    return environ['GODADDY_KEY'], environ['GODADDY_SECRET']


def check_config(conf):
    if len(conf) != 3:
        return 'Invalid config.yml values'
    try:
        api_keys()
    except KeyError:
        return 'API Keys not stored as environment variables'
    try:
        int(conf['max_records'])
    except Exception:
        return 'Invalid max_records value in config.yml'
    if conf['tld'][0] != '.':
        return 'Top Level Domain name missing leading period'


def intro():
    init()
    print(
        Fore.LIGHTRED_EX +
        """
----------     --------     ********      ------    --------  ----    ----
************  **********   ----------    ********   ********  *****   ****
--        -- ----    ---- ************  ----------    ----    ------  ----
**        ** ***      *** ---  --  --- ****    ****   ****    ************
--        -- ---      --- ***  **  *** ------------   ----    ------------
**        ** ****    **** ---  --  --- ************   ****    ****  ******
------------  ----------  ***  **  *** ----    ---- --------  ----   -----
**********     ********   ---      --- ****    **** ********  ****    ****
------------ ------------ ----    ---- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
************ ************ *****   **** * * * * * * * * * * * * * * * * * *
----         ----         ------  ---- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
****  ****** ************ ************ * * * * * * * * * * * * * * * * * *
----  ------ ------------ ------------ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
****    **** ****         ****  ****** * * * * * * * * * * * * * * * * * *
------------ ------------ ----   ----- ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
************ ************ ****    **** * * * * * * * * * * * * * * * * * *
        """
    )
    print(Fore.CYAN + 'by rootVIII')
    print(Style.RESET_ALL)
