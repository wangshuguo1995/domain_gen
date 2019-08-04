#! /usr/bin/python3
from threading import Thread
from queue import Queue
from datetime import datetime
from sys import exit
from utils import Subpaths
from utils import get_config, check_config, check_paths
from utils import Consumer, Producer, intro, write, print_red


def main():
    real_path = Subpaths().get_rpath()
    word_path = Subpaths().words_path()
    config_path = Subpaths().config_path()
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
    intro()
    q = Queue()
    consumer = Consumer(q)
    for i in range(8):
        t = Thread(target=consumer.consume_domains)
        t.daemon = True
        t.start()
    try:
        Producer(q, config['tld'], word_path, config['max_try']).get_doms()
    except KeyboardInterrupt:
        print_red('\n\nexiting DomainGen early...\n')
    q.join()
    if config['write_to_file']:
        file_out = datetime.now().strftime('%Y%m%d%H%M%S_out.txt')
        write(real_path + file_out, consumer.get_domains())
    print_red('finished')
