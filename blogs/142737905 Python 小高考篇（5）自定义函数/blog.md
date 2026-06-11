@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

在python中，如果有一个代码片段需要频繁使用，则可以考虑将其写为一个自定义函数。
# def 定义函数
通过def关键词，可以自定义一个函数，之后再在代码内调用它。如：
```py
def hello():
    print("Hello World!")
    print("Hello!")
hello()
```
运行结果：
```
Hello World!
Hello!
```
第一行代表定义一个函数，函数名字叫`hello`；第2行到第3行代表该函数需要执行的东西，第4行代表执行该函数。

## 传入参数
就像数学公式内，我们可能会这么写：$f(x)=x+1$。可以注意到，其实它有一个参数$x$。
python内定义函数也可以有参数，像这样：
```py
def sayhello(who):
    print("Hello",who + "!")
sayhello("Jzwalliser")
```
运行结果：
```
Hello Jzwalliser!
```
对比一下，发现第一个例子中，在定义函数名时，后面的括号中没有任何内容（`def hello():`），而在第二个例子中，括号中有个“`who`”（`def sayhello(who):`）。其中，这里的“`who`”就是一个参数，可以理解为一个变量。再看最后一行（`sayhello("Jzwalliser")`），其实在这里就把`who`的值设置为了"Jzwalliser"，所以第二行在输出有关内容时，读取到的`who`的值即为"Jzwalliser"。

## 返回值
返回值，就是一个函数运行完后还给外界的数值。如：
```py
def plus(a,b):
    print(a + b)
def plus2(a,b):
    return a + b
result1 = plus(114000,514)
result2 = plus2(114000,514)
print("result1",result1)
print("result2",result2)
```
运行结果：
```
114514
result1 None
result2 114514
```
同样是加法计算，`plus`函数只是直接输出结果，但`plus2`函数更为（高明），它可以将计算结果保存到指定的变量中。
这就是返回值，在函数最后面添加一行`return sth`就可以将数据返回给外界，就像是函数内部和外部的桥梁一样。
不过注意，`return`后面的代码是不执行的，像这样：
```py
def test():
    print("return 之前")
    return 114514
    print("return 之后")
test()
```
运行结果：
```
return 之前
```
# lambda 定义函数
`lambda`是一种很简洁（偷懒）的函数定义方法，它的代码量比`def`定义的函数少很多，但是正因如此它所能实现的功能也远没有`def`多。
先看个例子，将$f(x)=2x$分别用`lambda`和`def`变成函数：
```py
f = lambda x:2 * x
print(f(5))
```
```py
def f(x):
    return x * 2
print(f(5))
```
以上两段代码其实是基本等价的，可以看出第一段代码量要少很多，甚至连个`return`都没有，但实际上它依然有个返回值。
解释一下第一段代码什么意思：
1. `f`为函数名
2. `lambda`表示需要定义一个函数
3. `x`是一个参数
4. `2 * x`是一个表达式，同时也是这个函数的返回值


# 递归
递归，就是一个函数自己调用自己。递归主要由两个部分组成：递归操作及递归边界。递归操作是函数的主体部分，负责执行运算、实现功能；递归边界即一个条件， 满足条件后停止递归，并返回上一层，以避免程序无限递归下去而陷入死循环。
比如，计算斐波那契数列就可以使用递归算法来实现。假设第$x$项用$f(x)$来表示（$x\in\mathbb{Z_+}$），那么：

$$ f(x)=\left\{
\begin{aligned}
&1\space(x=1) \\
&1\ (x=2)\\
&f(x-1)+f(x-2)\space(x\geq 3) \\
\end{aligned}
\right.
$$


翻译为python如下。

```py
def f(x):
    if x == 1 or x == 2:
        return 1
    else:
        return f(x - 1) + f(x - 2)
```

由于之前就写过一篇关于递归的文章，这里就不在赘述了，欲知详情，请移步到这里：[初识递归算法](https://blog.csdn.net/jzwalliser/article/details/137679984)。


# 自测
1. 阅读以下代码：
```py
def f(x):
    if x > 1:
        return x * f(x - 1)
    return 1
print(f(10))
```
该程序输出为（      ）
A. `362880`
B. `3628800`
C. `39916800`
D. `10`
【答案】B

2. 阅读一下代码：
```py
def f(x):
    if x == 0:
        return 1
    return f(x - 1) * 2
```
这段代码表达的等价数学公式是（      ）
A. $f(x) = 2^x(x\in\mathbb Z)$
B. $f(x) = 2x(x\in\mathbb Z)$
C. $f(x) = 2x-2(x\in\mathbb Z)$
D. $f(x) =2^{x-1}(x\in\mathbb Z)$
【答案】A


# 总结
**def 定义函数**
使用`def`定义函数的模板：
```py
def function(arg1,arg2,arg3): #定义函数
   returnvalue = do_sth(arg1,arg2,arg3) #操作和运算
   return returnvalue #返回值
```
**lambda 定义函数**
模板：
```py
func = lambda arg1,arg2,arg3:do_sth(arg1,arg2,arg3)
```
**递归**
递归，即函数自己调用自己。层层深入进行计算，之后再回溯，将计算结果返回到上一层参与运算。
# 结尾
好啦，今天就分享到这里了，记得一键三连哦(˵¯͒〰¯͒˵)

