@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 引入
tkinter 其实功能真不少，用它来制作一个漂亮的窗口一点问题都没有。这一期，我们就来看看按钮控件。
# 制作一个按钮
首先，我们需要一个按钮。创建一个窗口，然后把按钮放上去：
```py
import tkinter
root = tkinter.Tk()
button = tkinter.Button(root) #创建一个按钮
button.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5597c69c8ec8b7e81e64612a5aa27380.png)
只可惜短短的按钮上啥都没有啊。。。

# 按钮的属性
## 文本
就是显示在按钮上的文字。
```py
import tkinter
root = tkinter.Tk()
	button = tkinter.Button(root,text="Hello World") #创建一个按钮，上面写 Hello World
button.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5554252ca14a207d70bb2bf8c0d58fc5.png)
## 颜色
按钮还可以设置颜色。你可以用英语单词来表示，也可以用HEX格式的颜色。颜色一共有两个，一个是字体颜色，用`fg`或`foreground`作为属性的名称；还有一个是背景颜色，用`bg`或`background`作为属性名称。
```py
import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,text="Hi!",fg="red",bg="blue") #红色字体，蓝色背景，用英语单词代替颜色
button1.pack() #把按钮放在窗口上
button2 = tkinter.Button(root,text="Hi!",fg="#00ff00",bg="#0000ff") #绿色字体，蓝色背景，用HEX格式的颜色
button2.pack()
#其实这么写也可以：
#button2 = tkinter.Button(root,text="Hi!",foreground="#00ff00",background="#0000ff")
#但这样写有点麻烦，你觉得呢？
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/19fcba1e3cb6c62576bb6cb8a21f5ef9.png)
哈哈这配色真阴间啊！

## 字体
字体以数组的形式传入。数组的第一项是字体，第二项是字号。如果找不到这个字体，tkinter不会报错，但是会使用默认的字体来代替。
```py
import tkinter
root = tkinter.Tk()
button = tkinter.Button(root,text="Hi!",font=("Arial",50,"roman")) #字体为Arial，字号为50，正体字，也可以不指定样式，如font=("Arial",50)
#若不需要设置字体大小和字体样式，也可以直接写为：
#button = tkinter.Button(root,font="Arial")
button.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4a838e70309e3fd6a4954aa0c2f4eede.png)
而字体样式有一下几种：
|关键词|样式|
|:-|:-|
|roman|正体字|
|italic|斜体字|
|bold|粗体字|
|underline|下划线|
|overstrike|杠掉|
## 长宽
```py
import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,text="Hi!",width=5) #宽为5
button1.pack() #把按钮放在窗口上
button2 = tkinter.Button(root,text="Hi!",height=5) #长为5
button2.pack() #把按钮放在窗口上
button3 = tkinter.Button(root,text="Hi!",height=5,width=5) #长宽都为5
button3.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/548d1aafa31bf3147fb5b1c1bcb93f27.png)
哎真有点丑啊。。。
但为什么我最后一个按钮明明设置的是长宽都为5，却不是个正方形呢？这是因为tkinter Button的长和宽并不是按照像素或者固定长度来计算的（应该是其字体的长宽）。
## 对齐
按钮上的文字如果有许多行，那么可以设置居中、靠左或靠右。
```py
import tkinter
root = tkinter.Tk()
string = """水调歌头
【宋】 苏轼 
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。
明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。
转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。 
"""
button1 = tkinter.Button(root,text=string,justify=tkinter.LEFT) #靠左
button1.pack() #把按钮放在窗口上
button2 = tkinter.Button(root,text=string,justify=tkinter.RIGHT) #靠右
button2.pack() #把按钮放在窗口上
button3 = tkinter.Button(root,text=string,justify=tkinter.CENTER) #居中
button3.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/244c6988bdfc0dcb495f275abc85e666.png)

## 光标
光标有许多种样式。内容不少，这里就稍微介绍下吧，其余的内容我找时间再专门写一篇吧。
```py
import tkinter
root = tkinter.Tk()
button = tkinter.Button(root,text="Hi!",cursor="watch") #光标放在按钮上后转圈
button.pack() #把按钮粘到窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/392baa37bbce89c24f6157b0f2c65ec9.gif#pic_center)

默认鼠标样式是arrow（箭头），除此之外还有其它一些鼠标样式，如xterm等。
## 状态
一般的tkinter控件都有2个常用的状态：正常（Normal）、禁用（Disabled），还有一些不常用的，如只读（Readonly）、活动（Active），这里就略过啦。
```py
import tkinter
root = tkinter.Tk()
button1 = tkinter.Button(root,text="Normal",state=tkinter.NORMAL) #正常
button1.pack() #把按钮放在窗口上
button2 = tkinter.Button(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法点击按钮
button2.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/f37f5de47265dcc90355e083fa641e4c.png)

被禁用的按钮在默认情况下字体是灰色的，而且点不下去。但是，也可以设置禁用时的字体颜色`disabledforeground`，用法和属性`fg`类似（但似乎不能设置禁用时的背景色）。如：
```py
button = tkinter.Button(root,text="Disabled",state=tkinter.DISABLED,disabledforeground="green") #禁用时的字体是绿油油的
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4bde001a678c45be9489050cd6f75856.png)

## 命令
按下按钮后，需要有什么功能呢？这可是按钮的灵魂啊。这时候，属性`command`就派上用场了。
```py
import tkinter
def click():
    print("Hello World!")

root = tkinter.Tk()
button = tkinter.Button(root,text="Click me!",command=click) #点击之后运行先前定义的click函数
button.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9c365ced9a9aa74280e20a3573bcfe7a.png)
## 边框
边框一共有这么几种：`flat`、`groove`、`raised`、`ridge`、`solid`、`sunken`；就一起来看看效果吧！
```py
import tkinter
root = tkinter.Tk()
relief = ["flat","groove","raised","ridge","solid","sunken"] #不同的样式
for i in relief:
    button = tkinter.Button(root,text=i,relief=i) #每个样式来一个按钮
    button.pack() #把每个样式的按钮放在窗口上

root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/828937fd16bc555f88174012633bfd90.png)

有了边框样式，我们还可以设置边框的厚度：`bd`或`borderwidth`。
```py
import tkinter
root = tkinter.Tk()
button = tkinter.Button(root,text="Hi!",bd=20) #厚厚的一层边框
button.pack() #把按钮放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6455d9d3c0a0407d3bbe3fa5e1a18756.png)
## 图片
如果一个按钮上只有文字，那未免太无聊了。我们还可以在按钮上放张图片：
```py
import tkinter
root = tkinter.Tk()
photo = tkinter.PhotoImage(file="laugh.png") #加载一张图片
button = tkinter.Button(root,image=photo) #设置图片
button.pack() #把按钮贴在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e5250bc25ad03ab77b7891b91a1c152b.png)

其实，这么写应该也可以：
`button = tkinter.Button(root,image="laugh.png")`
但是，总会出现一些莫名其妙的报错，如：
```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/lib/python3.8/tkinter/__init__.py", line 2650, in __init__
    Widget.__init__(self, master, 'button', cnf, kw)
  File "/usr/lib/python3.8/tkinter/__init__.py", line 2572, in __init__
    self.tk.call(
_tkinter.TclError: image "laugh.png" doesn't exist
```
而当我使用PhotoImage加载图片时，就没有问题，所以，不建议大家这么写，最好还是提前加载图片，而不是全丢给按钮去做。
而如果希望文字和图片并存，那就不能单纯`button = tkinter.Button(root,text="Hello",image=picture)`了，否则就会发现按钮只有图片没有文字。这时候就需要另外一个属性：`compound`，它控制图片和文字的位置。


|值|意思|
|:-|:-|
|CENTER|图片中间叠加文字|
|BOTTOM|文字下方显示图片|
|LEFT|文字左边显示图片|
|RIGHT|文字右边显示图片|
|TOP|文字上面显示图片|
|NONE|木有文字|

```py
import tkinter
root = tkinter.Tk()
photo = tkinter.PhotoImage(file="laugh.png") #加载一张图片
compound = [tkinter.CENTER,tkinter.BOTTOM,tkinter.LEFT,tkinter.RIGHT,tkinter.TOP,tkinter.NONE]
for i in range(len(compound)):
    button = tkinter.Button(root,image=photo,text=compound[i],compound=compound[i]) #按钮
    button.grid(row=int(i / 2),column=i % 2) #把按钮贴在窗口上

root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/545ec7db192ba385dd60ec8f97750862.png)


# 修改属性
设置好按钮后，可以改变它的属性。可以让它变颜色，改字体。用button的configure函数即可。
```py
import tkinter
root = tkinter.Tk()
button = tkinter.Button(root,image=photo,text="Hello!") #按钮
button.pack() #把按钮贴在窗口上
button.configure(text="Hi!",font=("Consolas",50)) #将按钮上的文字改为"Hi!"，再将字体设置为Consolas，字体大小50
#configure 和 config 都可以，
#button.config(text="Hi!",font=("Consolas",50)) 效果一样
root.mainloop()
```

---


# 总结
上面就是按钮的大部分属性啦。一起来复习一下：
|属性|意义|
|:-|:-|
|text|按钮上显示文字|
|fg或foreground|字体颜色|
|bg或background|背景颜色|
|font|按钮字体，以元组或字符串的形式传入|
|justify|文字居中（Center），靠左（Left）或靠右（Right）|
|cursor|光标放置在按钮上时的样式|
|state|按钮状态，如禁用（Disabled），正常（Normal）|
|disabledforeground|禁用时的字体颜色|
|command|命令，就是按下按钮时执行的命令|
|relief|边框样式|
|bd或borderwidth|边框粗细|
|image|按钮上显示的图片，最好提前PhotoImage加载，否则可能出错|
|compound|图片和文字共存时的相对位置|

```py
import tkinter
root = tkinter.Tk()

button = tkinter.Button(root,text="Hello World") #创建一个按钮，上面写 Hello World

button = tkinter.Button(root,text="Hi!",fg="red",bg="blue") #红色字体，蓝色背景，用英语单词代替颜色
button = tkinter.Button(root,text="Hi!",fg="#00ff00",bg="#0000ff") #绿色字体，蓝色背景，用HEX格式的颜色

button = tkinter.Button(root,text="Hi!",font=("Arial",50,"roman")) #字体为Arial，字号为50，正题字
button = tkinter.Button(root,font="Arial") #字体Arial，默认字号，默认字体样式

button = tkinter.Button(root,text="Hi!",width=5) #宽为5
button = tkinter.Button(root,text="Hi!",height=5) #长为5
button = tkinter.Button(root,text="Hi!",height=5,width=5) #长宽都为5

string = """水调歌头
【宋】 苏轼 
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。
明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。
转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。 
"""
button = tkinter.Button(root,text=string,justify=tkinter.LEFT) #靠左
button = tkinter.Button(root,text=string,justify=tkinter.RIGHT) #靠右
button = tkinter.Button(root,text=string,justify=tkinter.CENTER) #居中

button = tkinter.Button(root,text="Hi!",cursor="watch") #光标放在按钮上后转圈

button = tkinter.Button(root,text="Normal",state=tkinter.NORMAL) #正常
button = tkinter.Button(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法点击按钮
button = tkinter.Button(root,text="Disabled",state=tkinter.DISABLED,disabledforeground="green") #禁用时的字体是绿油油的

def click():
    print("Hello World!")
button = tkinter.Button(root,text="Click me!",command=click) #点击之后运行先前定义的click函数

button = tkinter.Button(root,text="Groove",relief="groove") #不同边框样式的按钮
button = tkinter.Button(root,text="Hi!",bd=20) #厚厚的一层边框

photo = tkinter.PhotoImage(file="laugh.png") #加载一张图片
button = tkinter.Button(root,image=photo) #设置图片
button = tkinter.Button(root,image=photo,text="Center",compound=tkinter.CENTER) #图片位置

button.configure(text="Hi!",font=("Consolas",50,"roman"))

button.pack() #按钮放在窗口上
root.mainloop()
```

感谢您的阅读，您的点赞是我的最大动力！


