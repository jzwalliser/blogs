
@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 引入
高中生活好忙碌，回头一看，已经有个把月没有写文章了，总算是腾出来点时间，浅浅更新一下吧。

废话不多说，这一次我们来看看tkinter的单选框控件。

单选框控件看起来像两个同心圆，旁边有文字描述。一般来说，单选框适用于两个及以上的选项，单独的一个单选框是没有意义的。在一组单选框中，用户可以选中其中一项。

# 创建一个单选框
创建窗口，然后将单选框放到窗口上。
```py
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root) #创建一个单选框
radio.pack() #把单选框放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c24517498c9137b88c5a06a71391790b.png)
# 单选框的属性
## 颜色
单选框有各种各样的颜色。在这里，颜色包括字体颜色（`fg`或`foreground`）和背景颜色（`bg`或`background`）。颜色可以用英语单词（如`"red"`、`"blue"`）来表示，也可以用HEX格式的颜色（如`"#ff00ff"`、`"#abcd00"`）。
```python
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="Hello World",fg="green",bg="red") #创建一个单选框，红底绿字
radio.pack() #把单选框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/104d1b5d803b262f3d8b9c3756c3ce91.png)


## 字体
单选框可以设置为不同的字体。比如，我喜欢宋体字，希望字体大一点（25号），并且是斜体。
```py
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="你好呀同学",font=("宋体",25,"italic")) #创建一个单选框，字体为宋体，字号25，斜体
#若不需要定义字体大小和字体样式，也可以直接写为：
#radio = tkinter.Radiobutton(root,font="宋体")
radio.pack() #把单选框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/63899064f9cf2a7410a142cd46a04d51.png)


|关键词|样式|样例|
|:-|:-|:-|
|roman|正体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bf845efdecb27f8b9b2c89dceaacabdd.png)|
|italic|斜体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/63899064f9cf2a7410a142cd46a04d51.png)|
|bold|粗体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4053ad60cba2698ce274109ffcab9390.png)|
|underline|下划线|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/76e577f866efe73578fa261cb661bfb5.png)|
|overstrike|杠掉|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b94397885544e428fd34796a9f2f3a82.png)|

## 光标
光标有许多种样式。内容不少，这里就稍微介绍下吧，其余的内容我找时间再专门写一篇吧。
```py
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="文本选择器",cursor="xterm") #光标放在单选框上后样式为文字选择器
radio.pack() #把单选框粘到窗口上
root.mainloop()
```

## 状态
一般的tkinter控件都有2个常用的状态：正常（Normal）、禁用（Disabled），还有一些不常用的，如只读（Readonly）、活动（Active），这里只介绍Disabled和Normal吧，因为另外两个确实不太常见啊。
```py
import tkinter
root = tkinter.Tk()
radio1 = tkinter.Radiobutton(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法选中或取消选中
radio1.pack() #放置单选框
radio2 = tkinter.Radiobutton(root,text="Normal",state=tkinter.NORMAL) #可以进行操作
radio2.pack() #放置单选框
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cf69c5bd574eb437868a0a775ba0557d.png)


## 边框
边框样式（`relief`）一共有这么几种：`flat`、`groove`、`raised`、`ridge`、`solid`、`sunken`。将其排在一起，欣赏一下不同的效果吧！
```py
import tkinter
root = tkinter.Tk()
relief = ["flat","groove","raised","ridge","solid","sunken"] #不同的样式
var = tkinter.StringVar() #创建字符串变量容器
for i in range(len(relief)):
    radio = tkinter.Radiobutton(root,text=relief[i],relief=relief[i],variable=var,value=i) #各种边框的单选框
    radio.pack() #把不同样式的单选框放在窗口上
root.mainloop()
```
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/857460619127313e4f6abce52eb59293.png)


除了边框样式，我们还可以设置边框的厚度：`bd`或`borderwidth`。
```py
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="Hello",bd=20,relief="groove") #厚厚的一层边框
radio.pack() #把单选框放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c0097d4271f4f29a09a4a0e834f28c11.png)


## 能否获取焦点
就是用户通过按<kbd>Tab</kbd>键能否将焦点切换到单选框上。若`takefocus=False`，则无法将焦点用<kbd>Tab</kbd>键切换到单选框上。默认`takefocus=True`。如：
```py
import tkinter
root = tkinter.Tk()
radio1 = tkinter.Radiobutton(root,text="Hello 1") #默认可以获取焦点
radio1.pack() #把单选框放在窗口上
radio2 = tkinter.Radiobutton(root,text="Hello 2",takefocus=True) #可以获取焦点
radio2.pack() #把单选框放在窗口上
radio3 = tkinter.Radiobutton(root,text="Hello 3",takefocus=False) #无法获取焦点
radio3.pack() #把单选框放在窗口上
root.mainloop()
```
可以运行一下上面的代码，试试能否用<kbd>Tab</kbd>键将焦点切换到第三个单选框上。


## 对齐
在Microsoft Office中，文字排版有三种主要的方式：靠左、居中、靠右。而在单选框中，若需要显示多行文字，也可以设置排版方式：`justify`。
```py
import tkinter
root = tkinter.Tk()
string = """虞美人·春花秋月何时了
【五代十国】李煜
春花秋月何时了？往事知多少。小楼昨夜又东风，故国不堪回首月明中。
雕栏玉砌应犹在，只是朱颜改。问君能有几多愁？恰似一江春水向东流。
"""
radio1 = tkinter.Radiobutton(root,text=string,justify=tkinter.LEFT) #靠左
radio1.pack() #把单选框放在窗口上
radio2 = tkinter.Radiobutton(root,text=string,justify=tkinter.RIGHT) #靠右
radio2.pack() #把单选框放在窗口上
radio3 = tkinter.Radiobutton(root,text=string,justify=tkinter.CENTER) #居中
radio3.pack() #把单选框放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/010a99a9e27a4bb6797944375fbb7e7a.png)
## 变量
一组单选框中，到底选中的是哪一个？这时，我们就需要将一组单选框的状态绑定到同一个变量。听起来可能会有些抽象，那么就一起看看下面的例子，以方便理解。如：
```py
import tkinter
root = tkinter.Tk()
intvar = tkinter.IntVar() #创建一个整数变量容器
radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #选中1时，intvar内的值被设置为1
radio1.pack() #放置单选框
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #选中2时，intvar内的值被设置为2
radio2.pack() #放置单选框
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #选中3时，intvar内的值被设置为3
radio3.pack() #放置单选框
root.mainloop()
```
在以上例子中，我们创建了一个用于存储整数的变量，然后将变量与3个单选框的状态绑定在一起——简单来说，单选框被选中后，`intvar`中的值就会被设置为对应单选框的`value`。例如，我选中了名为“Choice 1”的单选框，那么$1$将会被存入`intvar`。接着我又反悔了，改选“Choice 3”，那么$3$将会被存入`intvar`，替换掉原来的内容。
注意调用`tkinter.IntVar()`等tkinter变量容器，必须要先创建根窗口，否则会抛出异常。


## 命令
在点击单选框后，可以执行一段代码。举个栗子：
```py
import tkinter
def cmd():
    print("Hello World!!!")

root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="Hello World!",command=cmd) #点击之后运行先前定义的cmd函数
radio.pack() #把单选框放在窗口上
root.mainloop()
```
以上代码就是，按下单选框后输出"Hello World!!!"。

## 修改属性
```py
import tkinter
root = tkinter.Tk()
radio = tkinter.Radiobutton(root,text="Hello World") #单选框
radio.pack() #把单选框贴在窗口上
radio.configure(font=("Consolas",50)) #将字体设置为Consolas，字体大小50，默认样式
#configure 和 config 都可以，
#radio.config(font=("Consolas",50)) 效果一样
root.mainloop()
```

# 方法
和单选框不同，在这里我只介绍一个方法（即如何勾选特定的选项），因为其它方法都比较反逻辑，而且容易导致出错。
## 勾选
调用`radio.select()`即可勾选单选框。

```py
import tkinter
root = tkinter.Tk()
intvar = tkinter.IntVar()
radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #单选框1
radio1.pack() #放置单选框
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #单选框2
radio2.pack() #放置单选框
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #单选框3
radio3.pack() #放置单选框
radio2.select() #勾选单选框2
root.mainloop()
```





# 拓展
## 勾选
勾选某个单选框的方式其实不止一种。由于在编程中，一般都会为不同的单选选项设置不同的值，因此还可以通过改变变量的方式来设置勾选状态。如：

```py
import tkinter
root = tkinter.Tk()
intvar = tkinter.IntVar()
radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #单选框1
radio1.pack() #放置单选框
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #单选框2
radio2.pack() #放置单选框
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #单选框3
radio3.pack() #放置单选框
intvar.set(2) #设置intvar中的值为2，反映到复选框上就是将第二个选中
root.mainloop()
```
在上述例子中，同样可以选中值为2的单选框。


# 总结
上面便是单选框的主要内容啦。一起来复习一下：
|属性|意义|
|:-|:-|
|fg或foreground|字体颜色|
|bg或background|背景颜色|
|font|字体，可以传入一个元组，也可以传入一个字符串|
|cursor|光标放置在单选框上时的样式|
|state|单选框状态，如禁用（Disabled），正常（Normal）|
|relief|边框样式|
|justify|对齐方式|
|bd或borderwidth|边框粗细|
|takefocus|是否可以获取焦点|
|variable|转存状态变量|
|onvalue|被选中时的返回值|
|offvalue|未勾选时的返回值|
|command|按下单选框后调用命令|

```py
root = tkinter.Tk()

radio = tkinter.Radiobutton(root) #创建一个单选框

radio = tkinter.Radiobutton(root,text="Hello World",fg="green",bg="red") #创建一个单选框，红底绿字

radio = tkinter.Radiobutton(root,text="你好呀同学",font=("宋体",25,"italic")) #创建一个单选框，字体为宋体，字号25，斜体

radio = tkinter.Radiobutton(root,text="文本选择器",cursor="xterm") #光标放在单选框上后样式为文字选择器

radio1 = tkinter.Radiobutton(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法选中或取消选中
radio2 = tkinter.Radiobutton(root,text="Normal",state=tkinter.NORMAL) #可以进行操作

radio = tkinter.Radiobutton(root,text="Ridge",relief="ridge") #各种边框的复选框

radio = tkinter.Radiobutton(root,text="Hello",bd=20,relief="groove") #厚厚的一层边框

radio1 = tkinter.Radiobutton(root,text="Hello 1") #默认可以获取焦点
radio2 = tkinter.Radiobutton(root,text="Hello 2",takefocus=True) #可以获取焦点
radio3 = tkinter.Radiobutton(root,text="Hello 3",takefocus=False) #无法获取焦点

string = """虞美人·春花秋月何时了
【五代十国】李煜
春花秋月何时了？往事知多少。小楼昨夜又东风，故国不堪回首月明中。
雕栏玉砌应犹在，只是朱颜改。问君能有几多愁？恰似一江春水向东流。
"""
radio1 = tkinter.Radiobutton(root,text=string,justify=tkinter.LEFT) #靠左
radio2 = tkinter.Radiobutton(root,text=string,justify=tkinter.RIGHT) #靠右
radio3 = tkinter.Radiobutton(root,text=string,justify=tkinter.CENTER) #居中

intvar = tkinter.IntVar() #创建一个整数变量容器
radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #选中1时，intvar内的值被设置为1
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #选中2时，intvar内的值被设置为2
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #选中3时，intvar内的值被设置为3

def cmd():
    print("Hello World!!!")
radio = tkinter.Radiobutton(root,text="Hello World!",command=cmd) #点击之后运行先前定义的cmd函数

radio.configure(font=("Consolas",50))

radio.pack() #把复选框放在窗口上

radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #单选框1
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #单选框2
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #单选框3
radio2.select() #勾选单选框2

intvar = tkinter.IntVar()
radio1 = tkinter.Radiobutton(root,text="Choice 1",variable=intvar,value=1) #单选框1
radio2 = tkinter.Radiobutton(root,text="Choice 2",variable=intvar,value=2) #单选框2
radio3 = tkinter.Radiobutton(root,text="Choice 3",variable=intvar,value=3) #单选框3
intvar.set(2) #设置intvar中的值为2，反映到复选框上就是将第二个选中
```

感谢您的阅读！我们下期再见～


