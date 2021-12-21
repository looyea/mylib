# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/12/22
# @file quick_parser.py
# -*- coding: utf-8 -*-
import os

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs


bookname = "F:\\图书分类\\传记\\总结：毛姆创作生涯回忆录.epub"
try:
    print('原文件名是：', bookname, '\n')
    book = epub.read_epub(bookname)

    print(book.get_metadata('DC', 'title')[0][0])
    print(book.get_metadata('DC', 'creator')[0][0])
    print(book.get_metadata('DC', 'title')[0][0])
    print(book.get_metadata('DC', 'identifier'))

    print(book.get_metadata('DC', 'publisher')[0][0])
    print(book.get_metadata('DC', 'coverage'))
    print(book.get_metadata('DC', 'contributor'))
    print(book.get_metadata('DC', 'rights'))
    print(book.get_metadata('DC', 'description'))
    print(book.get_metadata('DC', 'type'))
    print(book.get_metadata('DC', 'descributor'))
    print(book.get_metadata('DC', 'subject'))
    print(book.get_metadata('DC', 'format'))

    for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        print(x)


except Exception as err:
    print('这里出错了，怎么回事我也不知道::>_<::')
    print(err)
    # errornum += 1