@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 引入
tkinter 的窗口其实是有很多属性的。我们可以设置它的各大属性，如窗口大小，可调整大小，透明度等等等等等等，可好玩了呢。
# 窗口的属性
## 大小
其实我在[上一期文章：Python tkinter（1）介绍&创建窗口](https://blog.csdn.net/jzwalliser/article/details/126909139#comments_23308539)里面已经提到了。叫作：`root.geometry("长x宽")`。其中，单位是“像素”。这里就复习一下吧。
```py
import tkinter
root = tkinter.Tk()
root.geometry("200x200") #创建一个200x200的窗口
root.mainloop()
```
## 位置
窗口其实还可以设置它的位置。它和窗口大小用的是同一个语句，像这样：`root.geometry("长x宽+X坐标+Y坐标")`。
我们来一段代码：
```py
import tkinter
root = tkinter.Tk()
root.geometry("200x200+50+50")
#将窗口设置为200x200的大小，并将其放在屏幕上(50,50)的位置
root.mainloop()
```
而坐标也应当是两个整数，否则会抛出错误。不过，和窗口大小不一样，坐标可以设置为负数。
而负数坐标也是有讲究的。像`root.geometry("200x200+-50+50")`，窗口将会被摆放在左边（-50，50），而`root.geometry("200x200-50+50")`，窗口将会被摆放在右边，坐标为（你的屏幕宽度-50，50）。
## 标题
设置标题也不是一个技术活。千言万语概括成这么一句代码：`root.title("一个标题")`。
```py
import tkinter
root = tkinter.Tk()
root.title("Hi!") #将窗口的标题设置为"Hi"
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3c33e3ef5a3503cb8dcd82e49b9a8ad8.png#pic_center)
效果怎么样啊？~~（就这???）~~

## 图标
其实我们还可以给窗口设置图标呢（标题栏左上角）。默认图标是一个蓝蓝的羽毛。图标有两种方式去设置：`iconbitmap()` 和 `iconphoto()`。
这两者主要区别在于，iconbitmap只能加载ico格式的图片，而iconphoto可以加载png格式的图片。而用法也不一样：
```py
import tkinter
root = tkinter.Tk()
#第一种方法：
root.iconbitmap(file="icon.ico") #这里icon.ico就是你的ico格式的图片
#第二种方法：
root.iconphoto(False,tkinter.PhotoImage(file='icon.png')) #这里icon.png就是你的的图片
```
发现了没？iconphoto其实有两个参数，第二个是图片，第一个是True或False，默认为False。如果设为True，那么图标也将应用于后面创建的所有顶级（Toplevel，后面我会讲到）窗口。
## 透明度
废话不多说，没啥好介绍的。直接上代码：`root.attributes("-alpha",透明度)`。透明度应该设置为浮点数，而不是整数，在这方面我经常搞错。如果你想设置30%的透明度，那么就是`root.attributes("-alpha",0.3)`。
```py
import tkinter
root = tkinter.Tk()
root.attributes("-alpha",0.3) #设置窗口的透明度为30%
#root.attributes("-alpha",30) 这种写法不会报错，但是透明度会被设置为100%，即不透明
root.mainloop()
```
## 最前面
就是保持窗口最前。像这样：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/f1b1f3ac21a4b7e49c48149549e10a9c.png#pic_center)来看看这是怎么实现的：
```py
import tkinter
root = tkinter.Tk()
root.attributes("-topmost",True) #将窗口保持最前
root.mainloop()
```
你也可以随时取消窗口的最前属性，只要调用`root.attributes("-topmost",False)`即可。

## 禁用
你有体验过被禁用的窗口吗？拖不动，也无法将其缩小、放大关闭等等。是不是很难受？
```py
import tkinter
root = tkinter.Tk()
root.attributes("-disabled",True) #把窗口禁用掉
root.mainloop()
```
## 工具模式
在工具模式下的窗口，将不会有最小化、最大化按钮，只有一个关闭按钮。
```py
import tkinter
root = tkinter.Tk()
root.attributes("-toolwindow",True) #工具窗口
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0099b829dd2bdfb1f095014f2b6646d9.png#pic_center)
好不好看啊？~~（有啥好看的）~~
## 全屏
设置全屏后，窗口将会撑满整个屏幕，任务栏也会被遮住。
```py
import tkinter
root = tkinter.Tk()
root.attributes("-fullscreen",True) #全屏
root.mainloop()
```
## 最大化/最小化
对于一个窗口来说，一般有三种状态：最大化、正常、最小化。
```py
import tkinter
root = tkinter.Tk()
root.state("zoomed") #最大化
root.state("normal") #正常
root.state("icon") #最小化
root.mainloop()
```
## 隐藏/显示
tkinter窗口可以消失且不出现在任务栏中，也可以恢复显示。
```py
import tkinter
root = tkinter.Tk()
root.withdraw() #隐藏窗口

#我们来搜搜词典：
#withdraw	英[wɪðˈdrɔː] 美[wɪðˈdrɔː]
#v.	撤退; (使)撤回，撤离; 停止提供; 不再给予; (使)退出; 提，取; 收回，撤回，撤销（说过的话）; 脱离（社会）;
#[例句]Tell the men to withdraw from their new position.
#告诉那些士兵从他们的新阵地上撤退。
#[其他]	第三人称单数：withdraws 现在分词：withdrawing 过去式：withdrew 过去分词：withdrawn

root.deiconify() #显示窗口
root.mainloop()
```
## 脱离标题栏
你可以设置窗口没有标题栏。但这样有一些缺点：没有标题栏的窗口需要手写窗口移动功能（如果你需要移动窗口的话），而且它不会出现在任务栏中。
```py
import tkinter
root = tkinter.Tk()
root.overrideredirect(True) #脱离标题栏
root.overrideredirect(False) #找回标题栏
root.mainloop()
```
## 可调整大小
窗口可以调整长度，也可以调整高度。不过你可以禁止这方面的调整。
```py
import tkinter
root = tkinter.Tk()
root.resizable(True,False) #只允许调整长度
root.resizable(False,True) #只允许调整高度
root.resizable(False,False) #长度和高度都不允许调整，同时最大化按钮会被禁用
root.mainloop()
```
## 窗口最大/最小可调整的大小
前面讲了禁止调整窗口大小，但如果你不想做得这么绝，那么还有下面这个法宝：
```py
import tkinter
root = tkinter.Tk()
root.maxsize(500,500) #窗口最大不能超过500×500像素
root.minsize(100,100) #窗口最小不能小于100×100像素
root.mainloop()
```
---

# 总结
上面就是tkinter窗口大部分的功能啦。一起来复习一下：
```py
import tkinter
root = tkinter.Tk()
root.geometry("300x300+50+50") #将窗口设置为300x300的大小，并将其放在屏幕上(50,50)的位置
root.title("Hello!") #将窗口的标题设置为"Hello"
root.iconbitmap(file="icon.ico") #这里icon.ico就是你的ico格式的图片
root.iconphoto(False,tkinter.PhotoImage(file='icon.png')) #这里icon.png就是你的的图片

root.attributes("-alpha",0.3) #设置窗口的透明度为30%
root.attributes("-topmost",True) #将窗口保持最前
root.attributes("-disabled",True) #把窗口禁用掉
root.attributes("-toolwindow",True) #工具窗口
root.attributes("-fullscreen",True) #全屏

root.state("zoomed") #最大化
root.state("normal") #正常
root.state("icon") #最小化

root.withdraw() #隐藏窗口
root.deiconify() #显示窗口

root.overrideredirect(True) #脱离标题栏
root.overrideredirect(False) #找回标题栏

root.resizable(True,False) #只允许调整长度
root.resizable(False,True) #只允许调整高度
root.resizable(False,False) #长度和高度都不允许调整，同时最大化按钮会被禁用

root.maxsize(500,500) #窗口最大不能超过500×500像素
root.minsize(100,100) #窗口最小不能小于100×100像素
root.mainloop()
```
而大部分的函数，如果你不给参数，那么这个函数将会返回当前状态。

我们下一期再见！
记得一键三连哦！


