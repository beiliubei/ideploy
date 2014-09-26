# -*- coding: utf-8 -*-
__author__ = 'benny'
import shutil
import yaml
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


def copyfile(ymlfile ='ci.yml'):
    print "===== do copyfile ====="
    f = open(ymlfile)
    x = yaml.load(f)
    index = 0
    if x['replace_from_pics'] == None or x['replace_to_pics'] == None:
        return
    for filePath in x['replace_from_pics']:
        print 'source file :', filePath
        print 'target file :', x['replace_to_pics'][index]
        shutil.copy(filePath, x['replace_to_pics'][index])


def replace(ymlfile ='ci.yml'):
    print "===== do replace ====="
    f = open(ymlfile)
    x = yaml.load(f)
    print x.keys()

    index = 0
    for filePath in x['template_source_files']:
        print 'source file :', filePath
        print 'target file :', x['template_target_files'][index]
        fsource = open(filePath)
        try:
            all_the_text = fsource.read()
            for key in x.keys():
                old = "{{%s}}" % key
                new = str(x[key])
                if new == 'None':
                    new = ''
                print "replace ", old, "by ", new
                all_the_text = all_the_text.replace(old, new)
            output = open(x['template_target_files'][index], 'w')
            output.write(all_the_text)
            output.close()
        finally:
            fsource.close()
        index = index + 1

if __name__ == '__main__':
    ymlfile = sys.argv[1:]
    if len(ymlfile) == 0:
        replace()
        copyfile()
    else:
        replace(ymlfile[0])
        copyfile(ymlfile[0])