#!/usr/bin/env python

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
        f = open(self.filename, "r")
        self.n = int(f.readline())
        f.close()

    def now(self):
        return self.n

    def increase(self):
        return self.n + 1

    def __del__(self):
        open(self.filename, "w").write(str(self.increase()))


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
