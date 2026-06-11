@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# TypeError
## 拼接字符串和数字
`input()`后获得的值是`str`类型的，因此常常需要将其转化为相应的类型（如整数）再进行操作。
### 错误示范
```py
>>> "2" + 1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
```
### 正确示范
字符串和数字是无法相加的。
修改：要么把字符串转化为整数再相加，要么将整数转化为字符串后拼接。
```py
>>> int("2") + 1
3
>>> "2" + str(1)
'21'
```
## 数字、字符串当成函数
数字和字符串它不是一个函数，所以它不能被调用。
### 错误示范
```py
>>> num = 12
>>> num()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'int' object is not callable
```
```py
>>> string = "string"
>>> string()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object is not callable
```
## 给函数传入未被定义过的参数
提前搞清楚函数有哪些参数，以及参数个数，否则很容易犯这类错。
### 错误示范
```py
>>> print("Hello",set="")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' is an invalid keyword argument for print()
```
```py
>>> int('12',dec=16)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'dec' is an invalid keyword argument for int()
```
```py
>>> def hi(arg):
...     print(arg,"hi")
...
>>> hi(arg1=114)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hi() got an unexpected keyword argument 'arg1'
```
## 传入的参数个数不正确
提前搞清楚函数有哪些参数，以及参数个数，否则很容易犯这类错。
### 错误示范
```py
>>> def hello():
...     print("Hello")
...
>>> hello(1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: hello() takes 0 positional arguments but 1 was given
```
## 字符串相乘
字符串直接无法相乘。只有字符串和整数相乘，或者整数相乘。这种错误常常是因为在输入之后没有将输入的内容转化成整数导致的。
### 错误示范
```py
>>> "12" * "12"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'str'
```
### 正确示范
将需要的数据转换为整数即可。
```py
>>> 12 * 12
144
>>> 12 * "12"
'121212121212121212121212'
>>> "12" * 12
'121212121212121212121212'
```
## 量取整数的长度
整数类型无法通过`len()`函数获取其位数。
### 错误示范
```py
>>> len(123)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: object of type 'int' has no len()
```
### 正确示范
只需将需要计算位数的数字变成字符串，然后再用`len()`函数度量其长度。
```py
>>> len(str(123))
3
```
## 格式化字符串时占位符个数不正确
格式化字符串时占位符个数不正确，即可引发次错误。
### 错误示范
```py
>>> "%s" % (5,6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: not all arguments converted during string formatting
```
## 给复数比较大小
先说一下，再python中，因为某些原因，虚数单位不是i，而是j。而再数学中，我们学过虚数只能判断其是否相等，而不能判断谁大谁小。
### 错误示范
```py
>>> 1+1j > 2+3j
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '>' not supported between instances of 'complex' and 'complex'
```
### 正确示范
只能判断复数是否相等。
```py
>>> 1+1j == 2+3j
False
>>> 2+4j == 2+4j
True
```
# ValueError
## 将含有非数字的字符串转换为整数
当字符串内包含非数字时，其无法转化为整数。
### 错误示范
```py
>>> int("ab")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'ab'
```
## 拆分时数据个数和变量个数不同
当一个链表或元组中的数据个数和分配给的变量个数不同时，将会出现此错误。经常是在`a,b = input().split()`之后出现错误，因为没有搞清楚到底有几个数据。
```py
>>> a,b = (1,2,3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

```py
>>> a,b,c = (1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: not enough values to unpack (expected 3, got 2)
```
### 正确示范
使链表或元组中的数据个数和分配给的变量个数相匹配即可。
```py
>>> a,b,c = (1,2,3)
```
# NameError
## 读取未被定义过的变量
若在一个变量定义之前就去读其它，则会出现此错误。
### 错误示范
```py
>>> print(a)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
```
### 正确示范
```py
>>> a = 114514
>>> print(a)
114514
```
# AttributeError
## 拆分一个数字
只有`str`可以拆分，数字无法被split。
### 错误示范
```py
>>> num = 12
>>> num.split()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'split'
```
# ZeroDivisionError
## 除数为0
在数学上我们也学过，除数作为0是无意义的。所以在python中这种计算会导致错误。经常实在`for i in range`时候，由于没有考虑`i`的范围而导致的错误。
### 错误示范
```py
>>> 5 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```
```py
>>> for i in range(5):
...     print(5 / i)
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
ZeroDivisionError: division by zero
```
## 正确示范
注意不要出现除数为0。
```py
>>> for i in range(1,5):
...     print(5 / i)
...
5.0
2.5
1.6666666666666667
1.25
```
# ModuleNotFoundError
## 导入不存在的模块
如果导入模块时模块不存在，则可能模块名搞错了。看看有没有拼写错误，比如把“`math`”打成“`nath`”之类。
### 错误示范
```ly
>>> import unknownmodule
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'unknownmodule'
```
# SyntaxError
## 位置参数后面放了关键词参数后面
有的函数我们喜欢用关键词参数传入数据，有的则喜欢用位置参数。先看一眼这两种参数到底是什么：
```py
def func(arg1,arg2,arg3):
    print(arg1,arg2,arg3)
func(1,2,3)
func(arg1=1,arg2=2,arg3=3)
func(arg2=2,arg1=1,arg3=3)
func(1,2,arg3=3)
```
第3行就是用的位置参数传入的数据，像这样python会按照参数的位置一一对应给到各个变量（准确来说应该叫形参）：1赋值给`arg1`，2赋值给`arg2`，3赋值给`arg3`。第4、5行用的就是关键词参数，好处就是参数位置即使是乱的，依然可以把对应内容给到正确的形参（尤其是第5行）。第6行则是混合用法，前面按照位置匹配给对应的形参（1赋值给`arg1`，2赋值给`arg2`），后面按照关键词将3赋值给`arg3`。但是，位置参数必须放在前面，关键词参数必须放在后面，否则会引起混乱，python就不知道某个数据该赋值给哪个形参，就像下面的例子。
### 错误示范
```py
>>> print(1,2,3,sep="",4)
  File "<stdin>", line 1
    print(1,2,3,sep="",4)
                        ^
SyntaxError: positional argument follows keyword argument
```
### 正确示范
把关键词参数放到后面。
```py
>>> print(1,2,3,4,sep="")
1234
```
## 混用单双引号
单、双引号不能混用，否则会引起错乱。
### 错误示范
```py
>>> 'string"
  File "<stdin>", line 1
    'string"
    ^
SyntaxError: unterminated string literal (detected at line 1)
```
```py
>>> "string'
  File "<stdin>", line 1
    "string'
    ^
SyntaxError: unterminated string literal (detected at line 1)
```
### 正确示范
单双引号必须匹配。
```py
>>> "string"
'string'
>>> 'string'
'string'
```


## 缩进错误
缩进的空格个数不能乱。
### 错误示范
```py
for i in range(10):
    print(i) #前面4个空格
     print(i) #前面5个空格
```
 抛出错误：
```py
 Traceback (most recent call last):
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 31, in <module>
    start(fakepyfile,mainpyfile)
  File "/data/user/0/ru.iiec.pydroid3/files/accomp_files/iiec_run/iiec_run.py", line 30, in start
    exec(open(mainpyfile).read(),  __main__.__dict__)
  File "<string>", line 3
    print(i) #前面5个空格
IndentationError: unexpected indent
```
## 没有if直接elif或else
在没有`if`打头的情况下，一般不可以出现`else`或`elif`。
### 错误示范
```py
>>> a = 0
>>> elif a == 0:
  File "<stdin>", line 1
    elif a == 0:
    ^^^^
SyntaxError: invalid syntax
```
## 无效字符
当代码中出现一些乱七八糟的字符时，就会出现这种错误。
### 错误示范
```
>>> 5!
  File "<stdin>", line 1
    5!
     ^
SyntaxError: invalid syntax
```
## while、if、elif、else、for里面缺少内容
在`while`、`if`、`elif`、`else`、`for`里面必须要有一些语句。如果还没想好要写什么，可以先用pass留空，如正确示范那样。
### 错误示范
```py
>>> while True:
...
  File "<stdin>", line 2

    ^
IndentationError: expected an indented block after 'while' statement on line 1
```
### 正确示范
可以用pass留空。
```py
>>> while True:
...     pass
...
```
## while、if、elif、else、for语句后面没有冒号
`while`、`if`、`elif`、`else`、`for`后面需要有冒号。
### 错误示范
```py
>>> while True
  File "<stdin>", line 1
    while True
              ^
SyntaxError: expected ':'
```

# 结尾
好啦，今天就讲到这里了，记得一键三连哦！(˃ ⌑ ˂ഃ )

