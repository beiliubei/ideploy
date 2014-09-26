# -*- coding: utf-8 -*-

__author__ = 'benny'
import yaml
import requests
import json
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor
from clint.textui.progress import Bar as ProgressBar
import sys
from glob import glob

infourl = 'http://fir.im/api/v2/app/info/%s?token=%s&type=%s'
uploadurl = 'http://up.qiniu.com/'


def my_callback(encoder):
    encoder_len = len(encoder)
    bar = ProgressBar(expected_size=encoder_len, filled_char='=')

    def callback(monitor):
        bar.show(monitor.bytes_read)

    return callback

if __name__ == '__main__':
    ymlfile = sys.argv[1:]
    if len(ymlfile) == 0:
        f = open('config.yml')
    else:
        f = open(ymlfile[0])

    x = yaml.load(f)
    infourl = infourl % (x['appid'], x['token'], x['type'])
    print '===== do get info from ', infourl, ' ====='
    response = requests.get(infourl)
    print json.loads(response.text)
    pkgkey = json.loads(response.text)['bundle']['pkg']['key']
    pkgtoken = json.loads(response.text)['bundle']['pkg']['token']
    print pkgkey
    print pkgtoken

    print '===== do upload file',x['filepath'], 'to', uploadurl, ' ====='
    e = MultipartEncoder(
    fields={'key': pkgkey, 'token': pkgtoken,
            'file': ('filename', open(glob(x['filepath'])[0], 'rb'), 'text/plain')}
    )
    callback = my_callback(e)
    m = MultipartEncoderMonitor(e, callback)
    uploadresponse = requests.post(uploadurl, data=m, headers={'Content-Type': m.content_type})
    print uploadresponse.text
