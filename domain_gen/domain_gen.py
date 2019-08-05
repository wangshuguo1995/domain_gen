#! /usr/bin/python3
from threading import Thread
from queue import Queue
from datetime import datetime
from time import sleep
from sys import exit
from utils import Subpaths, add_data
from utils import get_config, check_config, check_paths
from utils import Consumer, Producer, intro, write, print_red


def produce_consume():
    paths = Subpaths()
    real_path = paths.get_rpath()
    word_path = paths.words_path()
    config_path = paths.config_path()
    check_paths(word_path, config_path)
    config = get_config(config_path)
    try:
        error = check_config(config)
    except Exception as e:
        print(type(e).__name__, e)
        exit(1)
    else:
        if error is not None:
            print(error)
            exit(1)
    q = Queue()
    consumer = Consumer(q)
    for i in range(16):
        t = Thread(target=consumer.consume_domains)
        t.daemon = True
        t.start()
    Producer(q, config['tld'], word_path, config['max_try']).get_doms()
    q.join()
    if config['write_to_file']:
        print_red('writing to domains.json')
        add_data(real_path, consumer.get_domains())


def thread_loop():
    intro()
    while True:
        produce_consume()
        print_red('sleeping zzzzz...')
        sleep(60)


if __name__ == "__main__":
    try:
        thread = Thread(target=thread_loop)
        thread.daemon = True
        thread.start()
        thread.join()
    except KeyboardInterrupt:
        print_red('\nExiting Domain Gen')
    print_red('Finished')
