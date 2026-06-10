@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 列表
列表可以看作是一大堆串在一起的变量，在python中可以像这样创建列表：
```py
>>> lst1 = []
>>> lst2 = [1,2,3]
```
像这样，就创建了一个叫`lst1`的空列表，里面什么也没有，还创建了一个叫`lst2`的，它里面有三个**元素**，元素之间用逗号分隔，分别是数字$1$、$2$、$3$。当然，列表中不仅可以存数字，还可以存字符串，甚至是列表内套列表。
```py
>>> lst1 = [1,2,"345",6,"789"]
>>> lst2 = [114,514,[1919,"810"],"恶臭"]
```
## 读取内容
若想要读取列表中的内容，则可以用`lst[n]`的方法获得，其中`n`叫下标，像这样：
```py
>>> lst = [1,2,3]
>>> lst[0]
1
>>> lst[1]
2
>>> lst[2]
3
```
解释一下：第1行（`lst = [1,2,3]`）表示创建一个列表，第2行（`lst[0]`）表示读取列表`lst`中的第0号元素，第3行表示读取第1号元素，第4行表示读取第2号元素。
那为什么是所谓“第0号”元素而不是第1号呢？因为在大部分编程语言中，数字都是从0开始数，而不是从1开始，python也不例外（`for i in range(n)`就是 从0开始的嘛）。所以想要读取列表最前面的元素， 虽然习惯上叫作“第1个元素”，但需要写作`lst[0]` ，千万别搞成`lst[1]`了。像这样推下来，习惯上 “第2个”就是`lst[1]`，“第3个”就是`lst[2]`，以此 类推。下标也可以是负的，比如`lst[-1]`表示倒数 第1个元素，`lst[-2]`表示倒数第2个。
```py
>>> lst = [1,2,3,4,5]
>>> lst[-1]
5
>>> lst[-3]
3
>>> lst[-2]
4
```
## 修改内容
要想修该列表中某个元素的值也很简单：
```py
>>> lst = [1,2]
>>> lst[0] = 3
>>> lst
[3, 2]
>>> lst[1] += 2
>>> lst
[3, 4]
```
直接把`lst[n]`当作是一个变量对待就可以了。
也可以往列表中增添元素：
```py
>>> lst = [1,2]
>>> lst.append(5)
>>> lst
[1, 2, 5]
>>> lst += [8]
>>> lst
[1, 2, 5, 8]
```
删除元素：
```py
>>> lst = [1,2,3,4,5]
>>> lst.pop()
5
>>> lst
[1, 2, 3, 4]
>>> lst.pop(1)
2
>>> lst
[1, 3, 4]
>>> lst.pop(2)
4
>>> lst
[1, 3]
```
## for 循环遍历列表
与字符串类似，列表也可以通过`len(lst)`获取长度，只不过这样得到的就是元素个数：
```py
>>> lst1 = [1,2,3,4,5,114,514]
>>> len(lst1)
7
>>> lst2 = []
>>> len(lst2)
0
>>> len([11,45,14])
3
```
因此，可以通过这种方法“过一遍”（遍历）整个列表：
```py
lst = [1,5,6,7,1,5,2]
for i in range(len(lst)):
    print(lst[i],end=" ")
```
运行结果：
```
1 5 6 7 1 5 2
```

除此之外，还有一种遍历列表的方法：
```py
lst = [1,5,6,7,1,5,2]
for i in lst:
    print(i,end=" ")
```
运行结果：
```
1 5 6 7 1 5 2
```
第一种方式代码略长，但可以知道当前是第几次循环；第二种方式更精简，适用于可忽略循环次数的情况。


## 下标越界
最后，要注意下标越界问题。看例：
```py
>>> lst = [1,2]
>>> lst[4]
Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
  File "<string>", line 10, in <module>
  File "<string>", line 1, in <module>
IndexError: list index out of range
```
于是出错了。出错是因为列表内只有2个元素，却尝试读取python列表的第5号元素是什么……那当然出错啦。

# ASCII码和字符的相互转换
在python中，有`chr()`和`ord()`两个函数，它们作用相反：`chr()`用于将ASCII码转换为字符；`ord()`用于将字符转换为ASCII码。
```py
>>> chr(48)
0
>>> chr(32) #空格

>>> chr(65)
A
>>> ord("1")
49
>>> ord(" ")
32
>>> ord("a")
97
>>> ord("A")
65
>>> ord("Z")
90
```
# 导入库
通过`import`可以导入外部的库。什么意思呢？比如说，你想用python计算正弦值，怎么办？可以直接`sin(15)`吗？
```py
>>> sin(15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sin' is not defined. Did you mean: 'bin'?
```
很明显，python并不知道`sin()`是什么东西，所以 为了计算它们，我们现要用import语句导入整个数 “套件”（`math`），再用套件（严格来说应该叫“库” ）里面的`sin()`函数（当然里面不止`sin()`函数）：
```py
>>> import math
>>> math.sin(15)
0.6502878401571168
>>> math.cos(15)
-0.7596879128588213
>>> math.tan(15)
-0.8559934009085188
```
上面这种方式是先导入库（套件），再使用里面的函数（工具）。当然，也可以只导入函数而不导入库，这就需要用到`from ... import ...`语句了：
```py
>>> from math import sin
>>> sin(15)
0.6502878401571168
>>> tan(15)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'tan' is not defined
```
由于只导入了`sin()`没导入`tan()`函数，因此胡乱使用会导致错误。解决办法是，一次性导入所需的函数，或着干脆全导进来：
```py
>>> from math import sin,cos,tan
>>> sin(15)
0.6502878401571168
>>> cos(15)
-0.7596879128588213
>>> tan(15)
-0.8559934009085188
```
```py
>>> from math import *
>>> sin(15)
0.6502878401571168
>>> cos(15)
-0.7596879128588213
>>> tan(15)
-0.8559934009085188
```

# 进制转换
在python中，可以很方便地将十进制转换为二进制、八进制和十六进制。先看一眼各个进制对应的英文及其缩写：

|进制|英文|缩写|
|:-|:-|:-|
|二进制|Binary|BIN|
|八进制|Octal|OCT|
|十进制|Decimal|DEC|
|十六进制|Hexadecimal|HEX|

如，将十进制下的数字114514转换为二进制：
```py
>>> bin(114514)
'0b11011111101010010'
```
解释一下结果是什么意思：前缀“`0b`”代表这是个二进制数，后面的“”是二进制数字。如果是八进制数则其前缀是“`0o`”，十六进制是“`0x`”。
```py
>>> bin(114514)
'0b11011111101010010'
>>> oct(114514)
'0o337522'
>>> hex(114514)
'0x1bf52'
```
若将其它进制的数转换为十进制，则可以用`int()` 函数：
```py
>>> int("1bf52",base=16)
114514
>>> int("337522",base=8)
114514
>>> int("11011111101010010",base=2)
114514
```
可见，`int(num,base=n)`是指将`n`进制数`num`转 换为十进制。

# 结尾
好啦，今天就分享到这里了，记得点赞加关注哦！

