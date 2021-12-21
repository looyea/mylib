# -*- coding: utf-8 -*-
import os

import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup as bs
import re

book_path = "F:\\图书分类\\传记"
os.chdir(book_path)

allbooks = os.listdir(book_path)
'''
还要处理基本的一些问题
1. 处理[]
2. 加载常驻内存
'''
def get_book_type(content):
    idx = content[content.find("Ⅳ"):].find("①")
    type = content[idx:].replace(" ", "")
    print(type)
    return type

def name_processor(book_name):
    re_to_del = [r"\[.*\]", r"\【.*\】", r"\(.*\)", r"\（.*\）"]
    for re_item in re_to_del:
        book_name = re.sub(re_item, "", book_name)

    book_name = book_name.replace("——", ":").replace("：", ":").replace(" ", "")

    return book_name

for bookname in allbooks:
    # 判断是不是epub格式
    if not bookname.endswith(".epub"):
        continue
    try:
        print('原文件名是：', bookname)
        book = epub.read_epub(bookname)
        myBook = dict()
        myBook["title"] = book.get_metadata('DC', 'title')[0][0]
        myBook["author"] = book.get_metadata('DC', 'creator')[0][0]

        # 获取内容解析图书类目
        found_flag = False
        for x in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
            content = str(x.get_content(), "utf-8")
            if content.find("Ⅳ") >= 0:
                soup = bs(content, 'lxml')
                for p in soup.findAll("p"):
                    if p.get_text().find("Ⅳ") >= 0:
                        content_str = p.get_text()
                        get_book_type(content_str)
                        #myBook["cat"] = content_str #process_category(content_str)
                        found_flag = False
                        # idx = content_str.find("①") + 1
                        # content_str = content_str[idx:]
                        # print(content_str)
                        break
            if found_flag:
                break
        new_book_name = myBook["title"] + "-" + myBook["author"]
        if found_flag:
            new_book_name = new_book_name + "-" + myBook["cat"] + ".epub"
        else:
            new_book_name += ".epub"

        print("新的书名是：", name_processor(new_book_name), '\n')

    except Exception as err:
        print('这里出错了，怎么回事我也不知道::>_<::')
        print(err)
        # errornum += 1


# ----------------------------
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

# print(x.get_name())
# print(x.get_id())