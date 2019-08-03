#! /usr/bin/python3
from threading import Thread
from datetime import datetime
from utils import Subpaths, get_config
from utils import Consumer, Producer
from utils import intro, write
from queue import Queue


def paths():
    return [
        Subpaths().get_rpath(),
        Subpaths().words_path(),
        Subpaths().config_path()
    ]


if __name__ == "__main__":
    real_path, word_path, config_path = paths()
    config = get_config(config_path)
    intro()
    q = Queue()
    consumer = Consumer(q)
    for i in range(8):
        t = Thread(target=consumer.consume_domains)
        t.daemon = True
        t.start()
    try:
        Producer(q, config['tld'], word_path).get_domains()
    except KeyboardInterrupt:
        print('\n\nexiting Domain Generator...\n\n')
    q.join()
    if config['write_to_file']:
        file_out = datetime.now().strftime('%Y%m%d%H%M%S_out.txt')
        write(real_path + file_out, consumer.get_domains())
