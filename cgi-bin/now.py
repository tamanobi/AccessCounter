#!/usr/bin/env python

import os
import datetime

html_body = """
<html><body>
<p>
time:{}
</p>
<p>
count:{}
</p>
</body></html>"""


class AccessCounter:
    def __init__(self, _filename):
        self.filename = _filename
        self.n = self.read()

    def preparedFile(self):
        if os.path.exists(self.filename):
            if open(self.filename, "r").readline() == "":
                self.write(1)
        else:
            self.write(1)

    def read(self):
        self.preparedFile()
        return int(open(self.filename, "r").readline())

    def now(self):
        return self.n

    def increase(self):
        return self.n + 1

    def write(self, n):
        open(self.filename, "w").write(str(n))

    def update(self):
        self.write(self.increase())

    def __del__(self):
        self.update()


def getAccessCount(filename):
    return int(open(filename, "r").readline()) + 1


def HtmlHeader():
    return "Content-type: text/html\n"


def StrTime():
    now = datetime.datetime.now()
    return "{}/{}/{} {}:{}:{}".format(now.year, now.month, now.day, now.hour, now.minute, now.second)


def make_html():
    filename = './res/counter.log'
    ac = AccessCounter(filename)
    print HtmlHeader()
    print html_body.format(StrTime(), ac.now())


def main():
    make_html()


main()
