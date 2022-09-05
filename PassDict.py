#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Subj: PyCharm
# @File: PassDict.py
# @Date: 2022/9/3 17:55

# 读取密码txt
import os.path
import sys

try:
    file_name = sys.argv[1]
except IndexError:
    print('未拖动文件打开，尝试 passwords.txt')
    if os.path.isfile('passwords.txt'):
        file_name = 'passwords.txt'
    else:
        raise FileNotFoundError('未找到 passwords.txt')

try:
    f = open(file_name, 'r', encoding='UTF-8')
except UnicodeDecodeError:
    raise UnicodeError('编码不正确，请使用 UTF-8 (without BOM) 编码的文件')
else:
    pw_list = f.readlines()
    f.close()

pw_out = set()
for v in pw_list:
    if v == '\n':
        continue
    pw_out.add(v)

pw_out = sorted(pw_out)

with open('passwords_out.txt', 'w', encoding='UTF-8') as f:
    for v in pw_out:
        f.write(v)
