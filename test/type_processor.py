# -*- coding:utf-8 -*-
# @author JourWon
# @date 2021/12/22
# @file type_processor.py
import re

type_str = '①曾…Ⅱ.①曾…②李…Ⅲ.①曾彦修（1919—2015）—访问记Ⅳ.①K825.42'
re_str = r"[A-Z.\d*]"
t = re.search(re_str, type_str)
print(t)