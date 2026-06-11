@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)


# 前言
最近，想到用Python制作一个二维码扫描器，于是花了一会儿写了一个。一起看看吧！文末附下载链接哦~
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a0a664fe78a346c0728dbe61e46909f1.gif)

# 原料
## 主要的库
1. tkinter——界面
2. pyzbar——识别
3. pillow——加载图片
4. pyperclip——方便复制
## 资源
5. 图标
## 其它
6. pyinstaller——打包
# 制作
## 准备工作
由于pyzbar、pyperclip、pillow都不是python的标准库，所以需要额外安装。运行下面几行命令：
```
pip install pyzbar
pip install pyperclip
pip install pillow
```
## 界面
首先，制作一个漂亮的界面。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c57dac79790c21b36affff2470fce624.png)
```py
import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
root = tkinter.Tk() #创建窗口
root.title("二维码扫描器")
textpad = tkinter.scrolledtext.ScrolledText(root)
textpad.pack()
textpad.configure(state=tkinter.DISABLED) #用户不应该写入文本框
openqrcode = tkinter.ttk.Button(root,text="打开图片",width=80)
openqrcode.pack()
copycontent = tkinter.ttk.Button(root,text="复制内容",width=80)
copycontent.pack()
root.mainloop()
```
## 功能
接着，需要实现各种功能。

### 封装扫描二维码
由于扫描二维码的过程比较复杂，因此为了代码简洁易懂，可以将整个过程封装为一个单独的函数。
```py
def readqr(pic): #读取二维码
    content = [] #读取到的内容
    picture = PIL.Image.open(pic) #打开图片
    qrcode = pyzbar.pyzbar.decode(picture) #扫描二维码
    for qr in qrcode:
        url = qr.data.decode('utf-8') #解码
        content.append(url)
    return content
```

### 扫描
按下“打开图片”按钮，那就该扫描二维码了。这里需要考虑到一些情况：图片里没有二维码怎么办？图片打不开又该如何？
```py
def showqr():
    filename = tkinter.filedialog.askopenfilename() #打开文件对话框
    copycontent.configure(text="复制内容")
    if filename != "": #如果有打开文件
        try:
            content = readqr(filename)
        except: #如果图片无法读取
            tkinter.messagebox.showerror("错误","无法读取图片\"" + filename + "\"。")
        else: #图片正常，可以读取
            if content != []: #如果这是个二维码
                for i in content:
                    textpad.configure(state=tkinter.NORMAL) #解锁
                    textpad.insert(tkinter.INSERT,i + '\n\n') #插入内容
                    textpad.configure(state=tkinter.DISABLED) #上锁
            else:
                tkinter.messagebox.showinfo("无内容","该二维码中没有任何内容。（你确定这张图是二维码？）")
```

### 复制扫描结果
扫描完后，方便用户获取结果。
```py
def copy(): #复制
    pyperclip.copy(textpad.get("0.0",tkinter.END)) #获取文本框中的扫描结果
    copycontent.configure(text="已复制") #提示用户已复制
```

## 成果
集齐刚才几个代码碎片，即可得到一个二维码扫描器！
```py
#作者：Jzwalliser
#日期：2024/2/3

import tkinter
import tkinter.ttk
import tkinter.filedialog
import tkinter.messagebox
import tkinter.scrolledtext
import pyzbar
import pyzbar.pyzbar
import PIL
import PIL.Image
import pyperclip
import sys
import os

def getpath(file): #获取当前目录
    if getattr(sys,'frozen',None): #是否打包了？
        return os.path.join(sys._MEIPASS,file) #打包了，那就返回临时的工作路径
    else: #还没打包
        return os.path.join(os.path.abspath("."),file) #返回当前路径

def readqr(pic): #读取二维码
    content = [] #读取到的内容
    picture = PIL.Image.open(pic) #打开图片
    qrcode = pyzbar.pyzbar.decode(picture) #扫描二维码
    for qr in qrcode:
        url = qr.data.decode('utf-8') #解码
        content.append(url)
    return content

def showqr():
    filename = tkinter.filedialog.askopenfilename() #打开文件对话框
    copycontent.configure(text="复制内容")
    if filename != "": #如果有打开文件
        try:
            content = readqr(filename)
        except: #如果图片无法读取
            tkinter.messagebox.showerror("错误","无法读取图片\"" + filename + "\"。")
        else: #图片正常，可以读取
            if content != []: #如果这是个二维码
                for i in content:
                    textpad.configure(state=tkinter.NORMAL) #解锁
                    textpad.insert(tkinter.INSERT,i + '\n\n') #插入内容
                    textpad.configure(state=tkinter.DISABLED) #上锁
            else:
                tkinter.messagebox.showinfo("无内容","该二维码中没有任何内容。（你确定这张图是二维码？）")

def copy(): #复制
    pyperclip.copy(textpad.get("0.0",tkinter.END)) #获取文本框中的扫描结果
    copycontent.configure(text="已复制") #提示用户已复制

root = tkinter.Tk() #创建窗口
root.title("二维码扫描器")
root.iconbitmap(getpath("icon_clear.ico"))
textpad = tkinter.scrolledtext.ScrolledText(root)
textpad.pack()
textpad.configure(state=tkinter.DISABLED) #用户不应该写入文本框
openqrcode = tkinter.ttk.Button(root,text="打开图片",command=showqr,width=80)
openqrcode.pack()
copycontent = tkinter.ttk.Button(root,text="复制内容",command=copy,width=80)
copycontent.pack()
root.mainloop()
```

# 打包
直接打包会出问题。需要将两个dll文件添加进去才能打包成功，像这样：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7a860e849befde5f6c78292e2429ca21.png)
因此，打包命令：
```
pyinstaller -F -w --hidden-import PIL --hidden-import tkinter --hidden-import pyperclip --hidden-import pyzbar -i icon.ico --add-data=icon_clear.ico:. --add-data=libiconv.dll:./pyzbar/ --add-data=libzbar-64.dll:./pyzbar/ QRCodeReader.py
```
pyinstaller一顿输出，最后在dist文件夹下生成了我需要的exe。大功告成！

# 结尾
大家还能想到什么功能呢？欢迎评论！我们下期再见，记得点赞收藏哦~~

---

# 下载链接
|二维码扫描器 下载|
|:--|
|文件：QRCodeReader.zip|
|[百度网盘：https://pan.baidu.com/s/1FjUXIa-INvpZcOdNMfhLdA?pwd=0000](https://pan.baidu.com/s/1FjUXIa-INvpZcOdNMfhLdA?pwd=0000)|
|[CSDN：https://download.csdn.net/download/jzwalliser/88809272](https://download.csdn.net/download/jzwalliser/88809272)|

