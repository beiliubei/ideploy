# -*- coding: utf-8 -*-

__author__ = 'liubei'
import yaml
import requests
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from clint.textui.progress import Bar as ProgressBar
import sys
from glob import glob


def my_callback(encoder):
    encoder_len = len(encoder)
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    return callback


def upload(ymlfile):
    uploadurl = 'http://www.pgyer.com/apiv1/app/upload'
    if len(ymlfile) == 0:
        f = open('pgconfig.yml')
    else:
        f = open(ymlfile[0])

    x = yaml.load(f)

    print '===== do upload file',x['file'], 'to', uploadurl, ' ====='
    e = MultipartEncoder(
    fields={'uKey': x['uKey'], '_api_key': x['_api_key'], 'publishRange': x['publishRange'], 'isPublishToPublic': x['isPublishToPublic'], 'password':x['password'],
            'file': ('filename', open(glob(x['file'])[0], 'rb'), 'text/plain')}
    )
    callback = my_callback(e)
    m = MultipartEncoderMonitor(e, callback)
    uploadresponse = requests.post(uploadurl, data=m, headers={'Content-Type': m.content_type})
    print uploadresponse.text


if __name__ == '__main__':
    ymlfile = sys.argv[1:]
    upload(ymlfile)