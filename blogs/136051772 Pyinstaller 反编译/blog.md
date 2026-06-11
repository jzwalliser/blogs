@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 前言
以前用Python写过很多小程序，为了方便用pyinstaller打包成了各种exe，然后保存到了电脑的各个角落。但有一次因为磁盘分区出了问题，导致我的源码库全部丢失（太悲伤了），只有那些遍布磁盘不同角落的exe文件幸免于难。不得已，为了恢复一部分源码，只得将先前编译好的exe反编译成py文件。

# 原理
要想反编译pyinstaller生成的exe，需要先了解pyinstaller是如何打包py脚本生成exe的。
Pyinstaller 在收到打包指令后，会先生成一个spec文件，用于指导打包过程。之后，py文件会被先编译为pyc文件，然后pyc文件又会被去掉开头的8个字节。接着，pyinstaller会将python解释器、依赖文件和修改后的pyc文件一起，用一种特殊的自解压格式打包在一起，形成可执行文件。后面运行可执行文件时，会将所有文件自解压到一个临时目录，然后运行；程序结束后又会将临时目录删除。
其它有关Pyinstaller的内容可以参考这篇文章：[Pyinstaller 打包](https://blog.csdn.net/jzwalliser/article/details/136038200)

# 准备工具
## 软件（我会在文末提供链接）
1. Pyinstaller Extractor（py）
2. Sublime Text（exe）
3. Uncompyle 6（whl）

## 反编译步骤
在这里我有一个`hello.py`文件，里面的内容是：
```py
print("Hello World!!!")
```
之后，将其打包为exe：
```
pyinstaller -F hello.py
```
最后，pyinstaller一顿输出，打包完成。
本章，就以刚刚打包好的`hello.exe`为例，一起看看如何反编译它。（到时候记得将`hello.exe`替换为你需要反编译的文件）

### 1. 解压
将`pyinstxtractor.py`（请关注文末的下载链接）复制到`hello.exe`文件所在的目录，然后运行命令：
```
pyinstxtractor.py hello.exe
```
输出一堆：
```
D:\studio\pyin\dist\pyinstxtractor.py:86: DeprecationWarning: the imp module is deprecated in favour of importlib; see the module's documentation for alternative uses
  import imp
[*] Processing hello.exe
[*] Pyinstaller version: 2.1+
[*] Python version: 38
[*] Length of package: 7275745 bytes
[*] Found 69 files in CArchive
[*] Beginning extraction...please standby
[+] Possible entry point: pyiboot01_bootstrap
[+] Possible entry point: pyi_rth_multiprocessing
[+] Possible entry point: hello
[*] Found 206 files in PYZ archive
[*] Successfully extracted pyinstaller archive: hello.exe

You can now use a python decompiler on the pyc files within the extracted director
```

看到``[*] Successfully extracted pyinstaller archive: hello.exe``即代表解压成功。此时，会出现一个文件夹：`hello.exe_extracted`，进入后，找到`hello`（没有后缀名）。
### 2. 添加文件头
Pyinstaller在打包py脚本的时候，会先生成`pyc`文件，再从文件头删掉16个字节，其中包括时间戳、Magic Number，所以文件是不完整的，直接反编译会导致出错。因此，我们需要人为地将文件头加回去。

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d3e6d283ad01a791808132b9c9129039.png)
此时，找到文件（前面我打包的是`hello.py`，所以解压出来的叫`hello`），在后面添加后缀`.pyc`，然后用Sublime Text打开，此时是以16进制的方式打开的。

再打开文件夹`PYZ-00.pyz_extracted`，还是用Sublime Text随便打开其中一个pyc文件。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9bb690f3e1b58e0bff01c00f9c91926d.png)

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0f249df41cde0f5c69ff2d46da78c960.png)
打开后，应该是这个样子的（左边是需要修改的文件，右边是随便打开的pyc文件）：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1b11752c22958b065e0336e7364622ba.png)

将pyc文件的第一行复制下来，然后添加到缺失16个字节的文件的第一行，保存：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/8058898bd17cd67862491d7909c291b1.png)
### 3. Pyc文件反编译
最后，使用uncompyle6进行反编译。若还没有安装，则可以去文末下载whl文件，也可以运行：
```
pip install uncompyle6
```

安装好后，运行：
```py
uncompyle6 hello.pyc
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/44060edd8a57f7067b98ce8c9ad58b57.png)
最后就会显示源码了，虽然与初始的版本略有不同，但基本不影响。如果需要保存到文件，可以运行：
```
uncompyle6 hello.pyc>hello.py
```
然后就大功告成啦！

# 注意事项
由于某些原因（因为xdis还没有开始支持Python 3.9及以上），Uncompyle 6暂时无法反编译Python 3.9及更高版本产生的pyc文件（只能等待xdis更新啦）。
有的时候，pyc会反编译失败，此时可以尝试一些其它的反编译器，如Decompyle 3或在线反编译器（自己上网搜）。
还有，定时备份源代码文件！

---
# 下载链接

|Pyinstaller Extractor 下载|
|:--|
|文件：pyinstxtractor.py|
|[百度网盘：https://pan.baidu.com/s/1sDEmpPPT5bn_XWZlKuDjCA?pwd=0000](https://pan.baidu.com/s/1sDEmpPPT5bn_XWZlKuDjCA?pwd=0000)|
|也可以可前往[SourceForge](https://sourceforge.net/projects/pyinstallerextractor/)下载|

|Uncompyle 6 下载|
|:--|
|文件：Uncompyle Python 3.3-3.8.zip|
|[百度网盘：https://pan.baidu.com/s/14iHGfR202y6tSdOcHuPAyA?pwd=0000](https://pan.baidu.com/s/14iHGfR202y6tSdOcHuPAyA?pwd=0000)|
|也可以前往[PyPI](https://pypi.org/project/uncompyle6/)下载|

|Sublime Text 下载|
|:--|
|文件：Sublime Text Setup.exe|
|[百度网盘：https://pan.baidu.com/s/1jGUZKsvDkiTLqvu_JymUZA?pwd=0000](https://pan.baidu.com/s/1jGUZKsvDkiTLqvu_JymUZA?pwd=0000)|
|其它版本也可以前往[Sublime Text 官网](http://www.sublimetext.com/)下载|


