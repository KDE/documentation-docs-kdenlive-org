#!/usr/bin/python

# Author: Julius Künzel <jk.kdedev@smartlab.uber.space>

import sys, os, re
import subprocess

if len(sys.argv) != 2:
    sys.exit('you must specify a wikifiles.txt to parse!')
inputfile=sys.argv[1]
if not os.path.isfile(inputfile):
    sys.exit('input file %s not found' %inputfile)
text=open(inputfile,"r").read()

files = text.split('\n')

count = 1
for fn in files:
    print('File %d of %d' %(count, len(files)))
    if not fn.startswith('Icon: '):
        url = 'https://userbase.kde.org/File:%s' % fn
        result = subprocess.run(['wget', '-qO-', url], stdout=subprocess.PIPE)

        fileurl = re.search('(\/images\.userbase\/.+?\/.+?\/.+?)(?=")', str(result.stdout))
        if fileurl:
            result = subprocess.run(['wget', 'https://userbase.kde.org%s' %fileurl.group()])
            if result.returncode != 0:
                print('download error for https://userbase.kde.org%s' %fileurl.group())
        else:
            print('no result for %s' %fn)
    else:
        print('skipping %s' %fn)
    count = count + 1
