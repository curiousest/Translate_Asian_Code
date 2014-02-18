# Translate Asian Code

A python script to translate strings of Asian characters in code without messing up the code. Uses Google Translate.

## Requirement 
[gtranslate](https://github.com/galeo/gtranslate) - A simple python script for using Google Translate for free.

[BeautifulSoup 3](http://www.crummy.com/software/BeautifulSoup/) - a Python library designed for quick turnaround projects like screen-scraping.

## Usage

    python translateFile.py source_file_to_translate destination_file  [lin] [lout] [record_translations]

    Default Options:
        lin -- 'zh_CN'    英语
        lout -- 'en' 中文(简体)
        record_translations -- False
    
    Other Options:
        'zh-TW' -- 中文(繁体)
           'ja' -- 日语
           'de' -- 德语
           'fr' -- 法语
           'ko' -- 韩语
           'it' -- 意大利语
        ... ...

## License

This simple script is licensed under [GPLv3](http://www.gnu.org/licenses/quick-guide-gplv3.html).
