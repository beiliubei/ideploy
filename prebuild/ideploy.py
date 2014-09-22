__author__ = 'benny'
import shutil
import yaml
import sys


def copyfile(ymlfile ='ci.yml'):
    print "===== do copyfile ====="
    f = open(ymlfile)
    x = yaml.load(f)
    index = 0
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
                all_the_text = all_the_text.replace(old, new)
            output = open(x['template_target_files'][index], 'w')
            output.write(all_the_text)
            output.close()
        finally:
            fsource.close()

if __name__ == '__main__':
    ymlfile = sys.argv[1:]
    if len(ymlfile) == 0:
        replace()
        copyfile()
    else:
        replace(ymlfile[0])
        copyfile(ymlfile[0])