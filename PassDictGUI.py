#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# @Subj: PyCharm
# @File: PassDictGUI.py
# @Date: 2022/9/4 15:13

import tkinter as tk
import tkinter.messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog
import os


# 定义转换函数
def pw_convert(pw_list):
    pw_out = set()
    for v in pw_list:
        if v == '\n':
            continue
        pw_out.add(v)
    pw_out = sorted(pw_out)
    return pw_out


# 定义主页面
class Application(ttk.Frame):

    def __init__(self, master, **kwargs):
        super().__init__(master, padding=10, **kwargs)
        self.var_output_name = None
        self.var_input_file = None
        self.var_input_content = []
        self.var_output_content = []
        self.pack()

        self.frame = ttk.Frame()
        self.frame.pack(side=TOP, fill=BOTH, expand=YES)

        # 定义框架
        self.frame_in = ttk.Frame(self.frame)
        self.frame_in.grid_rowconfigure(1, weight=1)
        self.frame_in.grid_columnconfigure(1, weight=1)
        self.frame_in.pack(side=LEFT, fill=BOTH, expand=YES)

        self.frame_out = ttk.Frame(self.frame)
        self.frame_out.grid_rowconfigure(1, weight=1)
        self.frame_out.grid_columnconfigure(0, weight=1)
        self.frame_out.pack(side=LEFT, fill=BOTH, expand=YES)

        # 输入区
        self.select_file_btn = ttk.Button(self.frame_in, text='选择文件', command=self.select_file,
                                          bootstyle='primary_outline')
        self.input_file_name = ttk.Entry(self.frame_in)

        self.input_txt = ttk.Text(self.frame_in)
        self.input_txt.insert(END, '请选择密码字典文件')

        # 输出区
        self.output_file_name = ttk.Entry(self.frame_out)
        self.save_file_btn = ttk.Button(self.frame_out, text='保存文件', command=self.save_file)

        self.output_txt = ttk.Text(self.frame_out)
        self.output_txt.insert(END, '整理预览区')

        # 生成页面
        self.create_widget()

    def create_widget(self):
        # 输入区
        self.select_file_btn.grid(row=0, column=0, padx=10, pady=5)
        self.input_file_name.grid(row=0, column=1, padx=10, pady=5, sticky=W + E)
        self.input_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W + N + E + S)

        # 输出区
        self.output_file_name.grid(row=0, column=0, padx=10, pady=5, sticky=W + E)
        self.save_file_btn.grid(row=0, column=1, padx=10, pady=5)
        self.output_txt.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky=W + N + E + S)

    # 输入文件按钮
    def select_file(self):
        self.var_input_file = tk.filedialog.askopenfile()
        # 更新输入输出文件路径
        self.input_file_name.delete(0, END)
        self.input_file_name.insert(END, self.var_input_file.name)
        self.output_file_name.delete(0, END)
        self.var_output_name = os.path.splitext(self.var_input_file.name)[0] + '_out.txt'
        self.output_file_name.insert(END, self.var_output_name)
        # 更新显示
        self.update_visual()

    # 更新显示
    def update_visual(self):
        # 读取文件
        with open(self.var_input_file.name, 'r', encoding='UTF-8') as f:
            self.var_input_content = f.readlines()

        # 更新输入信息
        self.input_txt.delete(1.0, END)
        for v in self.var_input_content:
            self.input_txt.insert(END, v)

        # 转换
        try:
            self.var_output_content = pw_convert(self.var_input_content)
        except ValueError as e:
            tk.messagebox.showerror('错误', str(e))

        # 更新输出信息
        self.output_txt.delete(1.0, END)
        for v in self.var_output_content:
            self.output_txt.insert(END, v)

    # 保存文件
    def save_file(self):
        self.var_output_name = self.output_file_name.get()
        if os.path.exists(self.var_output_name):
            tk.messagebox.showwarning('警告', '文件存在，将会覆盖文件：\n' + self.var_output_name)
        with open(self.var_output_name, 'w', encoding='UTF-8') as f:
            for v in self.var_output_content:
                f.write(v)
        tk.messagebox.showinfo('完成', '保存成功')


# 定义运行代码
def main():
    root = ttk.Window(
        title='PassDict',
        # size=(1200, 600)
    )
    Application(root)
    root.mainloop()


# 运行
main()
