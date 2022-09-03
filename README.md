# PassDict

本项目为使用 python3 编写的 密码字典整理去重工具。

## 使用
本项目可以使用直接使用 PassDict.py 文件（需要安装 Python3 并添加到环境变量），或使用 Releases 的 exe 文件。

所需文件如下：

- 程序主体：PassDict.py / PassDict.exe
- 密码字典

### 密码字典要求

密码字典文件需要使用 UTF-8 Without BOM 编码。

### 使用源码

拖动密码字典文件到 PassDict.py

直接运行的情况，将会读取当前文件夹下的 passwords.txt

在当前目录运行：

```shell
python PassDict.py
```

#### 打包 exe 文件

可使用 pyinstaller 包，用如下命令将会在 `./dist/` 目录下创建 windows 可执行程序：

```shell
pyinstaller -F --icon=icon.ico PassDict.py
```

### 使用封装版

拖动密码字典文件到  PassDict.exe

直接运行的情况，将会读取当前文件夹下的 passwords.txt

## 输出

若正常运行后将会在当前文件夹生成去重整理后的 passwords_out.txt 文件。
