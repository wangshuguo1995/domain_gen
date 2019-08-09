#! /usr/bin/python3
from multiprocessing import Process
from threading import Thread
from queue import Queue
from time import sleep
from sys import exit
from utils import get_config, check_config, check_paths, paths
from utils import Consumer, Producer
from utils import intro, add_data, print_red


def produce_consume():
    real_path, word_path, config_path = paths()
    check_paths(word_path, config_path)
    config = get_config(config_path)
    error = check_config(config)
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
    Producer(q, config, word_path).get_doms()
    q.join()
    if config['write_to_file']:
        print_red('writing to domains.json')
        p = Process(target=add_data, args=(real_path, consumer.get_domains()))
        p.start()
    print_red('sleeping zzzzz...')
    sleep(config['interval'])


def thread_loop():
    intro()
    while True:
        produce_consume()


if __name__ == "__main__":
    try:
        thread = Thread(target=thread_loop)
        thread.daemon = True
        thread.start()
        thread.join()
    except KeyboardInterrupt:
        print_red('Exiting Domain Gen')
    print_red('Finished')
