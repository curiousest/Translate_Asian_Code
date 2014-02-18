#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Author: Douglas Hindson
Email: dmhindson[at]gmail.com
"""

import sys
import lib.gtranslate.gtranslate

def to_unicode_or_bust(
        obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding)
    return obj

def translateFile(filename, lin='zh_CN', lout='en'):
    """
    `filename` -- string, the text that you want to translate.
    `lin` -- string, the language of the `text`
    `lout` -- string, the language that you want the `text` translated to.
    """
    return 0


def main():
    info = """A simple python script to translate code with Google Translate by Douglas Hindson. Google Translate library credit to Galeo Tian.

Usage: python %s file_to_translate [lin] [lout]

Default Options:
     lin -- 'en'    英语
    lout -- 'zh_CN' 中文(简体)

Other Options:
    'zh-TW' -- 中文(繁体)
       'ja' -- 日语
       'de' -- 德语
       'fr' -- 法语
       'ko' -- 韩语
       'it' -- 意大利语
    ... ...
"""%(__file__)

    argv_length = len(sys.argv)
    if argv_length >= 2 and argv_length <= 4:
        result = translateFile(*sys.argv[1:])
    else:
        print info
        sys.exit()
    if not result:
        print "Sorry, error occurred, please retry."
        print info
    else:
        print '%s'%str(result)

if __name__ == '__main__':
    main()
