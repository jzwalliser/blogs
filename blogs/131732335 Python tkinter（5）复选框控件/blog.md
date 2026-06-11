@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 引入
最近有想看更新的，感谢各位的关注！刚刚初中升高中就感受到了万般忙碌，不过无论如何还是要抽空更新的啦。由于时间比较宝贵，等到文章完成还需要一年半载（真是无语，高中不允许携带手机，否则会拿处分，而且我还住校，于是只有周日可以拿到手机，除此之外周末还有一大堆作业要写），所以我决定先发布文章，后续再慢慢完善~

废话不多说，这一次我们来看看tkinter的复选框控件。

复选框控件就是一个小勾子，一共有两种主要状态——选中和非选中。点击一下，就会切换选中状态。

# 创建一个复选框
老样子，先制作一个窗口，然后将复选框贴到窗口上。
```py
import tkinter
root = tkinter.Tk() 
check = tkinter.Checkbutton(root) #创建一个复选框
check.pack() #把复选框贴到窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6eeddc49f0de884a68baf74196a1e187.png)



# 复选框的属性
## 颜色
复选框有各种各样的颜色。颜色包括字体颜色（`fg`或`foreground`）和背景颜色（`bg`或`background`）。颜色可以用英语单词（如`"red"`、`"blue"`）来表示，也可以用HEX格式的颜色（如`"#ff00ff"`、`"#abcd00"`）。
```python
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World",fg="red",bg="blue") #创建一个复选框，蓝底红字
check.pack() #把复选框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/729eaf39d5aefaaf45f5439a34c7831c.png)


## 字体
你可以为复选框选择喜欢的字体。比如，我喜欢宋体字，希望字体大一点（25号），并且是斜体。
```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="你好呀同学",font=("宋体",25,"italic")) #创建一个复选框，字体为宋体，字号25，斜体
#若不需要定义字体大小和字体样式，也可以直接写为：
#check = tkinter.Checkbutton(root,font="宋体")
check.pack() #把复选框放到窗口上去
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b59b7fc8263d847f2cd1ac9024fd6beb.png)

|关键词|样式|样例|
|:-|:-|:-|
|roman|正体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/843a57466bb4c9d054b6cc0dbfc52761.png)|
|italic|斜体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b59b7fc8263d847f2cd1ac9024fd6beb.png)|
|bold|粗体字|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2ceb54d58747e82e199d2c9d712a4bdf.png)|
|underline|下划线|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3616240ebea76d6a65a133d0148e1df2.png)|
|overstrike|杠掉|![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/82fcd5b39853ca704c6233cbbb2eaa33.png)|

## 光标
光标有许多种样式。内容不少，这里就稍微介绍下吧，其余的内容我找时间再专门写一篇吧。
```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="文本选择器",cursor="xterm") #光标放在复选框上后样式为文字选择器
check.pack() #把复选框粘到窗口上
root.mainloop()
```

## 状态
一般的tkinter控件都有2个常用的状态：正常（Normal）、禁用（Disabled），还有一些不常用的，如只读（Readonly）、活动（Active），这里只介绍Disabled和Normal吧，因为另外两个实在太不常见了。
```py
import tkinter
root = tkinter.Tk()
check1 = tkinter.Checkbutton(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法选中或取消选中
check1.pack()
check2 = tkinter.Checkbutton(root,text="Normal",state=tkinter.NORMAL) #可以进行操作
check2.pack()
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/31bbda57482dd2cc7670e6aa3366a02c.png)


## 边框
边框样式（`relief`）一共有这么几种：`flat`、`groove`、`raised`、`ridge`、`solid`、`sunken`，就一起来看看效果吧！
```py
import tkinter
root = tkinter.Tk()
relief = ["flat","groove","raised","ridge","solid","sunken"] #不同的样式
for i in range(len(relief)):
    check = tkinter.Checkbutton(root,text=relief[i],relief=relief[i]) #各种边框的复选框
    check.pack() #把不同样式的复选框放在窗口上
root.mainloop()
```
 ![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/943835b2aede0cfd686d31856a5c0117.png)


有了边框样式，我们还可以设置边框的厚度：`bd`或`borderwidth`。
```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello",bd=20,relief="groove") #厚厚的一层边框
check.pack() #把复选框放在窗口上
root.mainloop()
```

![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1653d435823cb5014402a862750b7eeb.png)

## 能否获取焦点
就是用户通过按<kbd>Tab</kbd>键能否将焦点切换到复选框上。若`takefocus=False`，则无法将焦点用<kbd>Tab</kbd>键切换到复选框上。默认`takefocus=True`。如：
```py
import tkinter
root = tkinter.Tk()
check1 = tkinter.Checkbutton(root,text="Hello 1") #默认可以获取焦点
check1.pack() #把复选框放在窗口上
check2 = tkinter.Checkbutton(root,text="Hello 2",takefocus=True) #可以获取焦点
check2.pack() #把复选框放在窗口上
check3 = tkinter.Checkbutton(root,text="Hello 3",takefocus=False) #无法获取焦点
check3.pack() #把复选框放在窗口上
root.mainloop()
```
可以运行一下上面的代码，试试能否用<kbd>Tab</kbd>键将焦点切换到第三个复选框上。


## 对齐
在Microsoft Office中，文字排版有三种主要的方式：靠左、居中、靠右。而在复选框中，若需要显示多行文字，也可以设置排版方式：`justify`。
```py
import tkinter
root = tkinter.Tk()
string = """水调歌头
【宋】 苏轼 
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。
明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。
转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。 
"""
check1 = tkinter.Checkbutton(root,text=string,justify=tkinter.LEFT) #靠左
check1.pack() #把复选框放在窗口上
check2 = tkinter.Checkbutton(root,text=string,justify=tkinter.RIGHT) #靠右
check2.pack() #把复选框放在窗口上
check3 = tkinter.Checkbutton(root,text=string,justify=tkinter.CENTER) #居中
check3.pack() #把复选框放在窗口上
root.mainloop()
```
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/0ee51f3a15608b560d2faf97df1d084a.png)
## 变量
复选框到底是否选中？这里，我们就需要将复选框当前状态存入一个变量中。如：
```py
import tkinter
root = tkinter.Tk()
intvar = tkinter.IntVar() #创建一个整数变量容器
check = tkinter.Checkbutton(root,text="Hello World!",variable=intvar) #关联变量
check.pack() #把复选框放在窗口上
print(intvar.get())
root.mainloop()
```
在以上例子中，我创建了一个用于存储整数的变量，然后将变量与复选框的状态绑定在一起——简单来说，如果复选框被选中，那么`intvar.get()`就会返回$1$，反之则返回$0$。
注意调用`tkinter.IntVar()`等的tkinter变量容器，必须要先创建根窗口，否则会抛出异常。

## 自定义返回值
也可以自定义返回值：比如我想要复选框在选中的状态下返回"Yes"，否则返回"No"。此时，就牵涉到`onvalue`和`offvalue`两个变量了。
```py
import tkinter
root = tkinter.Tk()
strvar = tkinter.StringVar() #创建一个字符串变量容器
check = tkinter.Checkbutton(root,text="Hello World!",variable=strvar,onvalue="Yes",offvalue="No") #选中时变量内数据为"Yes"，否则"No"
check.pack() #把复选框放在窗口上
root.mainloop()
```
Tkinter有两种变量容器：`tkinter.IntVar`和`tkinter.StringVar()`。详细内容我可能会在后期做介绍。
## 命令
在点击复选框后，可以执行一段代码。举个栗子：
```py
import tkinter
def cmd():
    print("Hello World!!!")

root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World!",command=cmd) #点击之后运行先前定义的cmd函数
check.pack() #把复选框放在窗口上
root.mainloop()
```
以上代码就是，按下复选框后输出"Hello World!!!"。

## 修改属性

```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World") #复选框
check.pack() #把复选框贴在窗口上
check.configure(font=("Consolas",50)) #将字体设置为Consolas，字体大小50，默认样式
#configure 和 config 都可以，
#check.config(font=("Consolas",50)) 效果一样
root.mainloop()
```
# 方法
## 勾选
调用`check.select()`即可勾选复选框。

```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World") #复选框
check.pack() #把复选框放在窗口上
check.select() #勾选复选框
root.mainloop()
```

## 取消勾选
和勾选相反，调用`check.deselect()`即可。
```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World") #复选框
check.pack() #把复选框放在窗口上
check.deselect() #取消勾选复选框
root.mainloop()
```

## 改变状态
调用`check.toggle()`会改变当前复选框的状态。即，如果复选框当前状态是勾选状态，那么就会被取消勾选；如果当前没有勾选，就会勾选复选框。
```py
import tkinter
root = tkinter.Tk()
check = tkinter.Checkbutton(root,text="Hello World") #创建复选框
check.pack() #把复选框放在窗口上
check.toggle() #改变当前复选框的选中状态
root.mainloop()
```

# 拓展
## 勾选/取消勾选
勾选和取消勾选的方式其实不止一种。对于设置了状态转存变量的复选框来说，还可以通过改变变量的方式来设置勾选状态。如：

```py
import tkinter
root = tkinter.Tk()
intvar = tkinter.IntVar()
check = tkinter.Checkbutton(root,text="Hello World!",variable=intvar) #创建复选框，使用intvar作为状态变量
check.pack() #把复选框放在窗口上
intvar.set(1) #设置intvar中的值为1，反映到复选框上就是将其选中
root.mainloop()
```

同理，`intvar.set(0)`也可以取消勾选。

---


# 总结
以上就是复选框的大部分内容啦。一起复习一下：
|属性|意义|
|:-|:-|
|fg或foreground|字体颜色|
|bg或background|背景颜色|
|font|字体，可以传入一个元组，也可以传入一个字符串|
|cursor|光标放置在复选框上时的样式|
|state|复选框状态，如禁用（Disabled），正常（Normal）|
|relief|边框样式|
|justify|对齐方式|
|bd或borderwidth|边框粗细|
|takefocus|是否可以获取焦点|
|variable|转存状态变量|
|onvalue|被选中时的返回值|
|offvalue|未勾选时的返回值|
|command|按下复选框后调用命令|

```py
import tkinter
root = tkinter.Tk()

check = tkinter.Checkbutton(root) #创建一个复选框

check = tkinter.Checkbutton(root,text="Hello World",fg="red",bg="blue") #创建一个复选框，蓝底红字

check = tkinter.Checkbutton(root,text="你好呀同学",font=("宋体",25,"italic")) #创建一个复选框，字体为宋体，字号25，斜体

check = tkinter.Checkbutton(root,text="文本选择器",cursor="xterm") #光标放在复选框上后样式为文字选择器

check1 = tkinter.Checkbutton(root,text="Disabled",state=tkinter.DISABLED) #禁用，无法选中或取消选中
check2 = tkinter.Checkbutton(root,text="Normal",state=tkinter.NORMAL) #可以进行操作

check = tkinter.Checkbutton(root,text="Sunken",relief="sunken") #各种边框的复选框

check = tkinter.Checkbutton(root,text="Hello",bd=20,relief="groove") #厚厚的一层边框

check1 = tkinter.Checkbutton(root,text="Hello 1") #默认可以获取焦点
check2 = tkinter.Checkbutton(root,text="Hello 2",takefocus=True) #可以获取焦点
check3 = tkinter.Checkbutton(root,text="Hello 3",takefocus=False) #无法获取焦点

string = """水调歌头
【宋】 苏轼 
丙辰中秋，欢饮达旦，大醉，作此篇，兼怀子由。
明月几时有？把酒问青天。不知天上宫阙，今夕是何年。我欲乘风归去，又恐琼楼玉宇，高处不胜寒。起舞弄清影，何似在人间。
转朱阁，低绮户，照无眠。不应有恨，何事长向别时圆？人有悲欢离合，月有阴晴圆缺，此事古难全。但愿人长久，千里共婵娟。 
"""
check1 = tkinter.Checkbutton(root,text=string,justify=tkinter.LEFT) #靠左
check2 = tkinter.Checkbutton(root,text=string,justify=tkinter.RIGHT) #靠右
check3 = tkinter.Checkbutton(root,text=string,justify=tkinter.CENTER) #居中

intvar = tkinter.IntVar() #创建一个整数变量容器
check = tkinter.Checkbutton(root,text="Hello World!",variable=intvar) #关联变量
print(intvar.get())

strvar = tkinter.StringVar() #创建一个字符串变量容器
check = tkinter.Checkbutton(root,text="Hello World!",variable=strvar,onvalue="Yes",offvalue="No") #选中时变量内数据为"Yes"，否则"No"


def cmd():
    print("Hello World!!!")
check = tkinter.Checkbutton(root,text="Hello World!",command=cmd) #点击之后运行先前定义的cmd函数

check.configure(font=("Consolas",50))

check.pack() #把复选框放在窗口上

check.select() #勾选复选框

check.deselect() #取消勾选复选框

check.toggle() #改变当前复选框的选中状态

intvar = tkinter.IntVar()
check = tkinter.Checkbutton(root,text="Hello World!",variable=intvar) #创建复选框，使用intvar作为状态变量
intvar.set(1) #设置intvar中的值为1，反映到复选框上就是将其选中
```

记得关注哦！

