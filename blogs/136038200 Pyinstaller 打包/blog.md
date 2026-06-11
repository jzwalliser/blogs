@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

写好了一个Python程序，如何将其打包为可执行文件呢？国外的大神写了pyinstaller，真是太好用了。一起来看看吧！

# 安装 Pyinstaller
首先，需要安装Pyinstaller。电脑需要联网才能安装啊！（或者你提前下载安装包其实也可以）
```
pip install pyinstaller
```
速度可能会有些慢，尤其是在国内，这下载速度就真的无法接受了。可以考虑使用国内镜像，这里使用清华的镜像：
```
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller
```
等待命令执行完毕，pyinstaller就装上了。

# 原理
Pyinstaller 在收到打包指令后，会先生成一个spec文件，用于指导打包过程。之后，你的py文件就会被编译为pyc文件，然后去掉pyc文件开头的8个字节。接着，会将python解释器、依赖文件和修改后的pyc文件一起，用一种特殊的自解压格式打包起来，形成可执行文件。后面运行可执行文件时，会将所有文件自解压到一个临时目录；程序退出后会将临时目录删除。

# 用法
pyinstaller其实有许多功能，可以打造出不同的exe文件。

## 单文件打包
如果希望只生成一个文件的话，那就使用`-F`。例如，你手头上有一个叫做`game.py`的文件，需要打包为一个单独的exe。此时，运行：
```
pyinstaller -F game.py
```

稍等片刻，可执行文件就会出现在`./dist`文件夹中。如果有依赖的图片或其它文件，那么只要将依赖项按照原来的目录结构，和可执行文件放在一起。

## 多文件打包
单文件打包比较方便文件共享，但是运行速度比较慢，因为需要将大量的文件解压出来再运行。而多文件打包则运行得快的多，而且多个可执行文件可以共享依赖，（比如a.exe和b.exe打包时都依赖同样的dll，那么就可以将b.exe和a.exe置于同一个目录下，并只保留一份dll）以达到省空间的目的。但坏处在于，如果将可执行文件单独拿出来而剔去依赖文件，则会无法运行。还是`game.py`，运行：
```
pyinstaller game.py
```
此时，`./dist`文件夹下就不是单个的可执行文件了，而是一个名叫`game`的文件夹（目录名取决于py文件的名称），里面是一大堆dll（Windows系统）或so（Linux系统）文件，还有许多依赖。

## 隐藏控制台
若程序有GUI界面，或者需要程序静默运行，就可以将控制台隐藏掉，只需要在打包指令中加入`-w`参数。如：
```
pyinstaller -w game.py
```

## 添加图标
Pyinstaller 的默认打包图标是这样的：
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/2703c8364c05965e748c09a64fc28b3c.png =150x150)


Nice！不过，如果我想制作一个游戏，那么这个图标肯定气质不符。
好在pyinstaller可以使用指定的图标。图标必须是ico格式的，所以如果你手上是png或jpg之类的文件，则需要转换格式，推荐用格式工厂。或者，你也可以提取exe文件的图标。
```
pyinstaller game.py -i game.ico
pyinstaller game.py -i executable.exe
```


## 设置权限
若需要打包后的可执行文件在运行之初就向系统请求管理员权限，则可以在打包命令中添加`--uac-admin`参数。如：
```
pyinstaller --uac-admin computerfix.py
```
## 加入依赖库
如果Python脚本依赖一些以文件夹的形式存在的库，那么就需要加入依赖库，否则软件移植到其他电脑后，很可能没法运行。
假设需要打包`game.py`，依赖`pygame`、`tkinter`、`sys`、`os`、`time`四个库，那么就需要运行如下命令：
```
pyinstaller --hidden-import tkinter --hidden-import pygame game.py
```
这样pyinstaller在打包的时候，就会将`tkinter`和`pygame`库一起打包进去。但是为什么不需要申明`sys`,`os`,`time`库呢？因为这三个库在Python目录中是以py文件的形式存在的，而不是文件夹，所以pyinstaller会自动将这些文件打包进去。
不过如果你不确定依赖的库是不是文件夹，那么完全可以都申明一下依赖，像`--hidden-import time`这种写法也没问题。
## 加入其它依赖文件




如果你想将脚本打包为单文件，并将依赖项等的文件一起打包进去，那就不用担心因为依赖项丢失而导致程序无法运行，因为依赖项和可执行文件融为了一体。
网上有不少通过修改spec文件来实现的。不过，在这里我介绍`--add-data`参数，效果一样。

举个例子，假如你有一个python文件，像这样：
```py
import codecs
import os
text = codecs.open("file.txt","r","utf-8")
print(text.read())
text.close()
os.system("pause")
```
很显然，脚本依赖file.txt，若依赖项丢失，则程序无法正常运行。此时，就可以在打包的时候把依赖项一起加进去。
```
pyinstaller file.py -F --add-data ./file.txt;.
```
解释一下各参数的意义：
|参数|意义|
|:--|:--|
|pyinstaller|调用pyinstaller命令|
|file.py|打包file.py|
|-F|单文件模式|
|--add-data|需要添加依赖项|
|./file.txt|添加同目录下的file.txt（`./`代表当前目录）|
|;|分隔符|
|.|打包后，file.txt放在目标的根目录下|

这时候，python脚本中，调用操作也需要进行修改了，需要寻找文件的路径。

```py
import codecs
import sys
import os

def getpath(file): #获取当前目录
    if getattr(sys,'frozen',None): #是否打包了？
        return os.path.join(sys._MEIPASS,file) #打包了，那就返回临时的工作路径
    else: #还没打包
        return os.path.join(os.path.abspath("."),file) #返回当前路径

text = codecs.open(getpath("file.txt"),"r","utf-8")
print(text.read())
text.close()
os.system("pause")
```
`--add-data` 参数可以多次使用。如：
```
pyinstaller file.py -F --add-data ./file.txt;. --add-data ./pic.jpg;. --add-data ./data.pkl;.
```

---
# 总结
以上就是pyinstaller的一些常用参数啦。归纳一下：
|参数|意义|示例|
|:--|:--|:--|
|`-F`|打包为单文件|`pyinstaller  -F game.py`|
|`-D`|打包为一个文件夹（默认）|`pyinstaller -D game.py` <br> `pyinstaller game.py`</br>|
|`-w`|隐藏控制台窗口|`pyinstaller -w game.py`|
|`-c`|显示控制条窗口（默认）|`pyinstaller -c game.py` <br> `pyinstaller game.py`</br>|
|`-i`|添加图标|`pyinstaller -i icon.ico game.py` <br> `pyinstaller -i executable.exe game.py`</br>|
|`--uac-admin`|请求管理员权限|`pyinstaller --uac-admin fixcomputer.py`|
|`--hidden-import`|导入依赖的包|`pyinstaller --hidden-import tkinter --hidden-import pygame game.py`|
|`--add-data`|添加依赖文件|`pyinstaller file.py -F --add-data ./pic.jpg;. --add-data ./data.pkl;.`|

记得关注我哦！

