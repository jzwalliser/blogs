@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 引入
优秀的tkinter库还有那些控件呢？这期我们就来看看输入框吧！

# 创建一个输入框
先制作一个窗口，然后把输入框黏上去。
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root) #创建一个输入框
entry.pack() #把输入框放到窗口上去
root.mainloop()
```
![==放一个图片！==](https://i-blog.csdnimg.cn/blog_migrate/d905bd22c82e630414c6f7747d104014.png)
# 输入框的属性
## 颜色
输入框可以改变它的颜色。颜色包括字体颜色（`fg`或`foreground`）、背景颜色（`bg`或`background`）、选中时的高亮颜色（`selectbackground`）和选中时的字体颜色（ `selectforeground`）。

颜色可以用英语单词（如`"red"`、`"blue"`）来表示，也可以用HEX格式的颜色（如`"#ff00ff"`、`"#abcd00"`）。

```python
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,fg="red",bg="blue",selectbackground="black",selectforeground="white")
#创建一个输入框，正常时蓝底红字，被选中的内容黑底白字
entry.pack() #把输入框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/804cf338b5e81850f9d5404ed5d3a80f.png)
## 字体
还可以设置输入框的字体。比如，我喜欢宋体字，希望字体大一点，并且是斜体。
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,font=("宋体",25,"italic"))
#创建一个输入框，字体为宋体，字号25，斜体
#若不需要设置字体大小和字体样式，也可以直接写为：
#entry = tkinter.Entry(root,font="宋体")
entry.pack() #把输入框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/30bcaa0bc59857e08c879db81ff5a140.png)而字体的样式除了有斜体之外，还有以下几种：
|关键词|样式|样例|
|:-|:-|:-|
|roman|正体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3da571f9d5c6bca399aa0eefca458c8e.png)|
|italic|斜体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5628582da0ea325d562d2c1bc9ce4f14.png)|
|bold|粗体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c2da8be93d89ef72f0fda071c1c9091a.png)|
|underline|下划线|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6b0aec0021e02a4975df49a4b9e681f3.png)|
|overstrike|杠掉|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/dfe48c98b4b30564ec74bb12eaf2dc0d.png)|

## 长度
输入框只能设置其长度而不能设置其宽度。因此，如果你像这样：`entry1 = tkinter.Entry(root,width=50,height=20)`，那么会报错。而长度并不是像素个数，而是一次性可现实的英文字母个数。也就是说，如果长度为50，那么在不左右滑动的情况下可以一下子显示约50个英文字母。
```py
import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,width=50) #长度约为50个英文字母
entry1.pack()
entry2 = tkinter.Entry(root,width=20) #长度约为20个英文字母
entry2.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/50c705bd138359929e515685608161bd.png)
## 光标
光标有许多种样式。内容不少，这里就稍微介绍下吧，其余的内容我找时间再专门写一篇吧。

```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,cursor="crosshair") #光标放在输入框上后样式为十字准心
entry.pack() #把输入框粘到窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/8620993ea30bce497e3b9c2f49ea941c.png)
默认鼠标样式是xterm（文本编辑，工字形），除此之外还有其它一些鼠标样式，如arrow等。
## 状态
一般的tkinter控件都有2个常用的状态：正常（Normal）、禁用（Disabled），还有一些不常用的，如只读（Readonly）、活动（Active），这里只介绍Disabled和Normal吧，因为另外两个实在太不常见了。
```py
import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,state=tkinter.DISABLED)
#禁用，无法点击也无法往里面输入内容，也无法从中复制内容
entry1.pack() 
entry2 = tkinter.Entry(root,state=tkinter.NORMAL)
#可以进行操作
entry2.pack() 
entry3 = tkinter.Entry(root,state="readonly")
#只能复制内容，而不可以输入内容。
#tkinter模块中，没有tkinter.READONLY 这个变量，所有就用字符串代替吧
entry3.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/95686f2896b55082f4e0157b4b4e5f48.png)
## 边框
边框样式（`relief`）一共有这么几种：`flat`、`groove`、`raised`、`ridge`、`solid`、`sunken`，就一起来看看效果吧！

```py
import tkinter
root = tkinter.Tk()
relief = ["flat","groove","raised","ridge","solid","sunken"] #不同的样式
for i in range(len(relief)):
    entry = tkinter.Entry(root,relief=relief[i]) #每个样式来一个输入框
    entry.place(x=5,y=i * 30) #把每个样式的输入框放在窗口上

root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1606011489281b7e46a7c53ec033af6e.png)
有了边框样式，我们还可以设置边框的厚度：`bd`或`borderwidth`。

```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,bd=20) #厚厚的一层边框
entry.pack() #把输入框放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/11268c2caf27da73a06a131a320f2e40.png)
结果就成这样了，这边框真感人！

## 显示的字符
如果你想创建一个密码输入框，那么你肯定希望输入的密码被显示为星星或圆点。关键就在于`show`属性，你想让它显示星星，就`show="*"`，之后你又想让它显示原来的内容，就`show=""`。
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,show="*") #将输入的内容显示为"*"
#当然，你也可以将星星替换成你喜欢的字符
#如果想让输入框显示原来的内容，则可以：
#entry.configure(show="")
entry.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/36c46624b3bc3ae6d9cff9ce4e24d9bb.png)
## 对齐方式
在WPS中，文字排版有三种主要的方式：靠左、居中、靠右。其实Entry也有这三种，如示例：
```py
import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,justify=tkinter.RIGHT) #靠右
entry1.pack()
entry2 = tkinter.Entry(root,justify=tkinter.LEFT) #靠左
entry2.pack()
entry3 = tkinter.Entry(root,justify=tkinter.CENTER) #居中
entry3.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6f687537f6fe27636d1a0199be4590bf.png)
## 光标闪烁和粗细
光标的闪烁速度可以被改变，使用属性`insertontime`，即光标显示的时间，和`insertofftime`，即光标隐藏的时间。
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root,insertofftime=100,insertontime=1000)
#输入的时候，每次光标闪烁，都显示1000毫秒（即1秒），隐藏100毫秒
entry.pack()
root.mainloop()
```
同时，还可以改变光标的粗细，那就是`insertwidth`属性。
```py
import tkinter
root = tkinter.Tk()
entry1 = tkinter.Entry(root,insertwidth=1) #细细的光标，粗细为1
entry1.pack()
entry2 = tkinter.Entry(root,insertwidth=10) #粗细为10
entry2.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ebcea490b504f9a6721aa9da03de75c1.png)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cd338f7fcac644815ef9860860b3aa43.png)
# 修改属性
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root) #输入框
entry.pack() #把输入框贴在窗口上
entry.configure(font=("Consolas",50)) #将字体设置为Consolas，字体大小50，默认样式
#configure 和 config 都可以，
#entry.config(font=("Consolas",50)) 效果一样
root.mainloop()
```
# 方法
我们除了要给输入框各种属性，还需要对其进行操作。

## 插入内容
如果我们希望在输入框内插入内容，则可以使用`insert()`方法。具体如下：
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry()
entry.pack()
entry.insert(tkinter.END,"Hello World!!!")
#在输入框中文字的末尾添加字符串"Hello World!!!"
root.mainloop()
```
而除了`tkinter.END`，还可以是`tkinter.INSERT`。两者的区别在于，`tkinter.END`代表在文末添加字符串，而`tkinter.INSERT`代表在当前的光标位置添加字符串。
## 获取内容
当我们需要获取输入框中的内容，可以调用`get()`方法。
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry()
entry.pack()
entry.insert(tkinter.END,"Hello World!!!") #插入文本
get_something = entry.get() #获取输入框中的内容
print(get_something)
root.mainloop()
```
以上的程序会输出输入框中的内容，这里当然就是"Hello World!!!"啦。
## 删除内容
在这几种操作中，怎么能少了删除呢！要删除输入框中的内容，就调用`delete()`方法。
```python
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.pack()
entry.insert(tkinter.END,"Hello World!!!") #插入文本
entry.delete(0,tkinter.END) #删除全部内容
root.mainloop()
```
而`delete()`用法稍稍复杂，我们看看下面这个表：
|示例|意思|
|:-|:-|
|entry.delete(0)|删除第1个字符|
|entry.delete(1)|删除第2个字符|
|entry.delete(0,2)|删除第1-2个字符|
|entry.delete(0,tkinter.END)|删除所有字符|
|entry.delete(0,tkinter.INSERT)|从第1个开始一直删到光标所在位置的前面一个字符|

## 移动光标
将光标移到指定的位置，不多说直接看下面的栗子：
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.pack()
entry.icursor(0) #将光标移动到第一个字符之前
root.mainloop()
```
## 选中内容
我们可以让输入框选中某一部分内容，分别为`entry.select_from()`和`entry.select_to()`方法，如：
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.insert(tkinter.END,'Hello World!!!!')
entry.select_from(0) #从第1个字符开始
entry.select_to(7) #一直选择到第8个字符
entry.pack()
```
但也可以取消选中：
```py
import tkinter
root = tkinter.Tk()
entry = tkinter.Entry(root)
entry.insert(tkinter.END,'Hello World!!!!')
entry.select_clear() #取消选中
entry.pack()
```

# 总结
上面就是输入框的主要内容啦。一起来复习一下：
|属性|意义|
|:-|:-|
|fg或foreground|字体颜色|
|bg或background|背景颜色|
|selectforeground|被选中时候的字体颜色|
|selectbackground|被选中时候的背景颜色|
|font|字体，可以传入一个元组，也可以传入一个字符串|
|width|长度|
|cursor|光标放置在输入框上时的样式|
|state|输入框状态，如禁用（Disabled），正常（Normal）|
|relief|边框样式|
|bd或borderwidth|边框粗细|
|show|如何展示输入的内容|
|insertontime|光标显示的时间|
|insertofftime|光标被隐藏的时间|
|insertwidth|光标粗细|

```python
import tkinter
root = tkinter.Tk()

entry = tkinter.Entry(root) #创建一个输入框

entry = tkinter.Entry(root,fg="red",bg="blue",selectbackground="black",selectforeground="white") #正常时蓝底红字，被选中的内容黑底白字
entry = tkinter.Entry(root,font=("宋体",25,"italic")) #字体为宋体，字号25，斜体
entry = tkinter.Entry(root,font="宋体") #字体为宋体，默认字体大小，默认样式

entry1 = tkinter.Entry(root,width=50) #长度约为50个英文字母
entry2 = tkinter.Entry(root,width=20) #长度约为20个英文字母

entry = tkinter.Entry(root,cursor="crosshair") #光标放在输入框上后样式为十字准心

entry1 = tkinter.Entry(root,state=tkinter.DISABLED) #禁用，无法点击也无法往里面输入内容，也无法从中复制内容
entry2 = tkinter.Entry(root,state=tkinter.NORMAL) #可以进行操作
entry3 = tkinter.Entry(root,state="readonly") #只能复制内容，而不可以输入内容。tkinter模块中，没有tkinter.READONLY 这个变量，所有就用字符串代替吧

entry = tkinter.Entry(root,relief="groove") #不同边框样式的输入框
entry = tkinter.Entry(root,bd=20) #厚厚的一层边框

entry = tkinter.Entry(root,show="*") #将输入的内容显示为"*"
entry = tkinter.Entry(root,show="") #显示原来的内容

entry1 = tkinter.Entry(root,justify=tkinter.RIGHT) #靠右
entry2 = tkinter.Entry(root,justify=tkinter.LEFT) #靠左
entry3 = tkinter.Entry(root,justify=tkinter.CENTER) #居中

entry = tkinter.Entry(root,insertofftime=100,insertontime=1000) #输入的时候，每次光标闪烁，都显示1000毫秒（即1秒），隐藏100毫秒

entry1 = tkinter.Entry(root,insertwidth=1) #细细的光标，粗细为1
entry2 = tkinter.Entry(root,insertwidth=10) #粗细为10

entry.configure(font=("Consolas",50)) #将字体更换为Consolas，字号50，默认样式

entry.insert(tkinter.END,"Hello World!!!") #在输入框中文字的末尾添加字符串"Hello World!!!"
entry.delete(0,tkinter.END) #删除全部内容
entry.get() #获取输入框中的内容

entry.icursor(0) #将光标移动到第一个字符之前

entry.pack() #把输入框放到窗口上去

entry.select_from(0) #从第1个字符开始选择
entry.select_to(7) #一直选择到第8个字符

entry.select_clear() #取消选中

root.mainloop()
```
哈哈，谢谢您的阅读！点个赞，关注一下呗！我们下期再见～

