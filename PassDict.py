#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Subj: PyCharm
# @File: PassDict.py
# @Date: 2022/9/3 17:55

import os.path
import sys


def pw_convert(password_list: list[str]) -> list[str]:
    pw_out = set()
    for password in password_list:
        if password == '\n':
            continue
        pw_out.add(password)
    pw_out = sorted(pw_out)
    return pw_out


def main():
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

    pw_output = pw_convert(pw_list)

    with open('passwords_out.txt', 'w', encoding='UTF-8') as f:
        for v in pw_output:
            f.write(v)

    print('字典整理已完成，请查看 passwords_out.txt')


if __name__ == '__main__':
    main()
