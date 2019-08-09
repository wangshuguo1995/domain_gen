#! /usr/bin/python3
from json import load, dump
from yaml import safe_load
from os.path import isfile
from random import randint
from os import environ
from sys import exit
from colorama import init
from colorama import Fore, Style
from .rpath import Subpaths


def paths():
    p = Subpaths()
    return p.get_rpath(), p.words_path(), p.config_path()


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
            m = 'Corrupt domains.json.\n'
            m += 'Creating new domains.json'
            print(m)
            write(path, new_data)
    else:
        write(path, new_data)


def get_config(path):
    with open(path) as yml_in:
        return safe_load(yml_in)


def get_1st(second, words):
    return words[randint(0, len(words) - 1)] + second


def get_2nd(first, words):
    return first + words[randint(0, len(words) - 1)]


def get_pair(words):
    return words[randint(0, len(words)-1)] + words[randint(0, len(words)-1)]


def api_keys():
    return environ['GODADDY_KEY'], environ['GODADDY_SECRET']


def check_paths(words, configs):
    if not isfile(words) or not isfile(configs):
        print('Missing conifg.yml or word_list.json')
        exit(1)


def check_config(conf):
    try:
        api_keys()
    except KeyError:
        return 'API Keys not stored as environment variables'
    e = 'ERROR in config.yml:\n'
    try:
        int(conf['max_try'])
    except Exception:
        return e + "Invalid 'max_try' value"
    try:
        float(conf['interval'])
    except Exception:
        return e + "Invalid 'time_interval'"
    if conf['tld'][0] != '.':
        return e + 'Top Level Domain name missing leading period'
    if conf['default_word']:
        try:
            int(conf['default_word']['position'])
        except Exception:
            return e + "Invalid 'position'"
        if int(conf['default_word']['position']) not in (1, 2):
            return e + "'position' may only be 1 or 2"
        if conf['default_word']['word'] is None:
            return e + "'default_word' is True but 'word' is missing"
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
