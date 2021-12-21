# -*- coding: utf-8 -*-
import os

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs
import ebooklib.utils as util

book_path = "D:\\Download\\其他"
os.chdir(book_path)

allbooks = os.listdir(book_path)
'''
还要处理基本的一些问题
1. 处理[]
2. 加载常驻内存
'''
def process_category(category):
    idx = category.find("-")
    category = category[:idx]
    return category

for bookname in allbooks:
    # 判断是不是epub格式
    if not bookname.endswith(".epub"):
        continue
    try:
        print('原文件名是：', bookname, '\n')
        book = epub.read_epub(bookname)
        myBook = dict()
        myBook["title"] = book.get_metadata('DC', 'title')[0][0]
        myBook["author"] = book.get_metadata('DC', 'creator')[0][0]
        # print(book.get_metadata('DC', 'title')[0][0])
        # print(book.get_metadata('DC', 'identifier'))

        # print(book.get_metadata('DC', 'publisher')[0][0])
        # print(book.get_metadata('DC', 'coverage'))
        # print(book.get_metadata('DC', 'contributor'))
        # print(book.get_metadata('DC', 'rights'))
        # print(book.get_metadata('DC', 'description'))
        # print(book.get_metadata('DC', 'type'))
        # print(book.get_metadata('DC', 'descributor'))
        # print(book.get_metadata('DC', 'subject'))
        # print(book.get_metadata('DC', 'format'))

        # 获取内容解析图书类目
        found_flag = False
        for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            # print(x.get_name())
            # print(x.get_id())
            content = str(x.get_content(), "utf-8")
            if content.find("Ⅳ") >= 0:
                soup = bs(content, 'lxml')
                for p in soup.findAll("p"):
                    if p.get_text().find("Ⅳ") >= 0:
                        content_str = p.get_text()
                        idx = content_str.find("Ⅳ.①")
                        content_str = content_str[idx+3:]
                        myBook["cat"] = process_category(content_str)
                        found_flag = True
                        # idx = content_str.find("①") + 1
                        # content_str = content_str[idx:]
                        # print(content_str)
                        break
            if found_flag:
                break
        new_book_name = myBook["title"] + "-" + myBook["author"] + "-" + myBook["cat"] + ".epub"
        print("新的书名是：" + new_book_name)

    except Exception as err:
        print('这里出错了，怎么回事我也不知道::>_<::')
        print(err)
        # errornum += 1


