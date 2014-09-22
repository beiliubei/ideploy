__author__ = 'benny'
import yaml

infourl = 'http://fir.im/api/v2/app/info/%s?token=%s'
uploadurl = 'http://up.qiniu.com/'


if __name__ == '__main__':
    f = open('config.yml')
    x = yaml.load(f)
    infourl = infourl % (x['appid'], x['token'])
    print infourl