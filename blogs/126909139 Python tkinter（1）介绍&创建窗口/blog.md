@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)


# tkinter是什莫东西
tkinter是Python自带的一个库，可以用来创建GUI。

# 怎么用？
## 导入
说起来也挺奇怪的，Python2.X和Python3.X的tkinter是不一样的！所以到底哪里不一样呢？

```py
#Python 2.X 首字母大写
import Tkinter
#Python 3.X 首字母小写
import tkinter
#下面我们用的是Python 3.X
```

## 创建窗口
现在到了创建窗口的时候啦！
```py
import tkinter
root = tkinter.Tk() #咱们来造一个窗口
#一般大家都喜欢用root作为窗口的变量名，后面我也一直会用root
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a69945a7770c7467e700b7349172ae00.png#pic_center)
这样窗口就出来啦！你学会了吗？~~（我学废了）~~

## 窗口主循环
什么是“主循环”呢？Actually，就是让窗口可以不停地处理事件。否则，窗口将不会显现出来（细致地说，如果不写主循环，只有在IDLE或者一些其它的编译器中会创建的窗口，而在Python的控制台中则不会）。
就是这么一行代码：
``
root.mainloop()
``
合在一起就是：
```py
import tkinter
root = tkinter.Tk()
root.mainloop() #写代码千万别漏了这一行！
```

其实，主循环还有一种写法：
```py
while True:
    root.update()
```
虽然有这种写法，但它并不是标准的，所以推荐大家使用 `root.mainloop()`。
## 调节窗口大小
创建完窗口，我们想要调节窗口大小。
``root.geometry("长度x宽度")``
注意中间的是小写字母“艾克斯”（x），而不是大写字母，更不是乘号。长度和宽度都应该是整数类型，否则会抛出大家最喜欢的错误。
举一个栗子：
```py
import tkinter
root = tkinter.Tk()
root.geometry("200x500") #创建一个200乘500大小的窗口
root.mainloop()
```
---


# 总结
上面就是tkinter的介绍和创建窗口啦。一起来复习一下：
```py
#导入
import tkinter #Python 3.X
#import Tkinter #Python 2.X
root = tkinter.Tk() #创建窗口
root.geometry("200x200") #将窗口设置为200x200
root.mainloop() #主循环
```

下一期我们再深入学习更多有关 tkinter 的知识啦！
记得一键三连哦！

