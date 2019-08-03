#! /usr/bin/python3


class Consumer:
    def __init__(self, que):
        self.que = que
        self.domain_names = []

    def consume_domains(self):
        while True:
            url = self.que.get()
            self.domain_names.append(url)
            # check go daddy here
            print(url + ' does not exist')
            self.que.task_done()

    def get_domains(self):
        return self.domain_names
