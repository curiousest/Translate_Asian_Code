#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

"""
Author: Douglas Hindson
Email: dmhindson[at]gmail.com
"""

import sys, codecs
import lib.gtranslate.gtranslate as GT

# 0×3000 is ideographic space (i.e. double-byte space)
IDEOGRAPHIC_SPACE = 0x3000

#these characters will be used as part of blocks of text to translate if they aren't separated from Asian characters by non-Asian characters or another of these characters in front 
#ex: in "text 好 !语", the "好 !语" would be translated
#ex: in "text 好 !text 语", "好 !" would be translated, then "语" would be translated
PART_OF_ASIAN_TEXT = {' ', '\t', '!', '?', '"', ',', '.', '：', '？', '，', '【', '【', '。'}

def to_unicode_or_bust(
        obj, encoding='utf-8'):
    if isinstance(obj, basestring):
        if not isinstance(obj, unicode):
            obj = unicode(obj, encoding, "ignore")
    return obj

def isAsianCharacter(char):
    """Is the character Asian?"""
    if char:
        # Anything over is an Asian character
        return ord(char) > IDEOGRAPHIC_SPACE
    return 0

def translateFile(sourceFileName, destFileName, lin='zh_CN', lout='en', record_translations=False):
    """
    `sourceFileName` -- string, the name of the file that you want to translate.
    `destFileName` -- string, the name of the file that you want to translate.
    `lin` -- string, the language of the `text`
    `lout` -- string, the language that you want the `text` translated to.
    `recordTranslations` -- boolean, if you want the command line to print out each translation before/after.
    """
    sourceFile = 0
    destFile = 0
    try:
        sourceFile = codecs.open(sourceFileName, "r", "utf-8")
        destFile = codecs.open(destFileName, "w", "utf-8")
    except IOError, e:
        print e    

    asianTextFlag = False

    for line in sourceFile:
        bufferText = u''
        for char in line:
            unicode_char = to_unicode_or_bust(char)
            if asianTextFlag and char in PART_OF_ASIAN_TEXT:
                bufferText = bufferText + unicode_char
            elif isAsianCharacter(unicode_char):
                bufferText = bufferText + unicode_char
                asianTextFlag = True
            else:
                if asianTextFlag:
                    translatedText = GT.translate(bufferText.encode('utf8'), lin, lout)
                    if record_translations:
                        print bufferText
                        print translatedText
                    destFile.write(translatedText)
                    bufferText = u''
                    asianTextFlag = False
                destFile.write(char)
    
    sourceFile.close()
    destFile.close()
            
    return 

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
    if argv_length >= 3 and argv_length <= 6:
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
