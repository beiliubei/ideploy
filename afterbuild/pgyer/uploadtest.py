# -*- coding: utf-8 -*-
__author__ = 'liubei'

import pgupload
import sys


if __name__ == "__main__":
    ymlfile = sys.argv[1:]
    pgupload.upload(ymlfile)