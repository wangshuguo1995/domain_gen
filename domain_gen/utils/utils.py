#! /usr/bin/python3
from yaml import safe_load
from json import load, dump
from random import randint
from sys import exit
from os import environ
from os.path import isfile
from colorama import init
from colorama import Fore, Style


def write(path, json_data):
    with open(path, 'w') as json_out:
        dump(json_data, json_out)


def read(path):
    with open(path) as json_in:
        return load(json_in)


def add_data(path, new_data):
    path += 'domains.json'
    if isfile(path):
        try:
            existing = read(path)
            write(path, existing + new_data)
        except Exception:
            write(path, new_data)
    else:
        write(path, new_data)


def get_config(path):
    with open(path) as yml_in:
        return safe_load(yml_in)


def get_pair(words):
    return words[randint(0, len(words)-1)] + words[randint(0, len(words)-1)]


def api_keys():
    return environ['GODADDY_KEY'], environ['GODADDY_SECRET']


def check_paths(words, configs):
    if not isfile(words) or not isfile(configs):
        print('Missing conifg.yml or word_list.json')
        exit(1)


def check_config(conf):
    if len(conf) != 4:
        return 'Invalid config.yml values'
    try:
        api_keys()
    except KeyError:
        return 'API Keys not stored as environment variables'
    try:
        int(conf['max_try'])
    except Exception:
        return 'Invalid max_try value in config.yml'
    try:
        float(conf['interval'])
    except Exception:
        return 'Invalid time interval in config.yml'
    if conf['tld'][0] != '.':
        return 'Top Level Domain name missing leading period'
    return None


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
    print(Fore.CYAN + 'Author:  rootVIII')
    print(Style.RESET_ALL)


def print_red(red_str):
    print(Fore.LIGHTRED_EX + red_str)
    print(Style.RESET_ALL)
