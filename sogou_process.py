import os
import re
import jieba
import codecs
from longconv import *

FILENAME = 'news_tensite_xml.dat'
BLOCK_SIZE = 100
PATTERN = "<content>(.*?)</content>"
CSVFILE = codecs.open("corpus.csv", "w", "utf-8")

def read_in_block(file_path):
    with open(file_path, 'rb') as f:
        while True:
            block = f.readlines(BLOCK_SIZE)
            if block:
                yield block
            else:
                return

def parseSent(sentence):
    seg_list = jieba.cut(sentence)
    output = ' '.join(list(seg_list))
    return output

def tradional2simpified(sentence):
    sentence = Converter('zh-hans').convert(sentence)
    return sentence


if __name__ == '__main__':
    # for block in read_in_block(FILENAME):
    #     text = block[0].decode('gbk', errors='ignore')
    #     m = re.match(PATTERN, text)
    #     if m:
    #         segSent = parseSent(m.group(1))
    #         CSVFILE.write("%s" % segSent)

    FILENAME = 'wiki.zh.txt'
    WIKIFILE = codecs.open("wiki.zh.sm.txt", "w", "utf-8")
    for block in read_in_block(FILENAME):
        text = block[0].decode('utf-8', errors='ignore')
        sentence = tradional2simpified(text)
        WIKIFILE.write("%s" % sentence)
        WIKIFILE.close()