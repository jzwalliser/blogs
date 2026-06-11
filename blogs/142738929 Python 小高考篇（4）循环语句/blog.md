@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

循环语句可以用于重复运行一段代码。在python中，循环有两种：`for`循环和`while`循环。

# for 循环
## 一个参数
使用`for`循环可以很方便地将某一段代码重复执行一定的次数。如：
```py
for i in range(5): #循环5次
    print(i,end=" ") #打印当前循环次数
```
运行结果：
```
0 1 2 3 4
```
在以上例子中，第2行的`print(i,sep=" ")`将会被运行5次（因为`range(5)`）。而变量`i`在这里相当于是个计数器，第一次循环时它等于0，到了第二次等于1，每循环一次，`i`都会加1，直到重复五次后`i=4`。

不过，循环的“计数”变量并不一定非要是`i`，也可以是别的，像这样：
```py
for j in range(5): #循环5次
    print(j,sep=" ") #打印当前循环次数
```
此时，“计数”变量就是`j`。

## 两个参数
当然，也可以让计数器（`i`）不从0开始，如：
```py
for i in range(100,110):
    print(i,end=" ")
```
运行结果：
```
100 101 102 103 104 105 106 107 108 109
```
可见，这次`i`就是从100开始，到109结束。
归纳一下，即在`for i in range(n,m)`中，`i`的范围为$i\in [n,m),i\in\mathbb Z$

## 三个参数
前面都是在谈论`range()`中有一个参数或两个参数的情况，但在range中也可以填如3个参数。此时，这3个参数就分别为：起始、终止、步长。
```py
for i in range(1,20,3):
    print(i,end=" ")
```
运行结果：
```
1 4 7 10 13 16 19
```
像这样，`i`从1开始，且每循环一次就加3，直到`i`的值大于20后结束。
所以，对于`for i in range(n,m,l)`循环，不再是循环$m-n$次，而是$\lceil\dfrac{m-n}{l}\rceil$次。

# while 循环
`while`语句是另一种循环形式。一般情况下`for`语句是无法实现无限循环的，但while语句却可以。`while`其实和`if`挺类似的，但是对于`if`语句，它只会在条件满足的时候将语句执行一次，而`while`会一直重复执行下去，直到条件不满足为止。
```py
s = ""
while len(s) < 6:
    s += " "
    print("length",len(s))
```
运行结果：
```
length 1
length 2
length 3
length 4
length 5
length 6
```
以上这段代码表示循环增加字符串`s`的长度，而每次增加长度后就输出当前长度，并判断是否满足字符串的长度小于6，否则停止循环。

如果需要死循环（在程序正常运行的情况下永远不停止的循环），则可以利用`while`语句这么写：
```py
while True:
    print("永久循环")
```
可以复制到IDLE中，体验一下“死循环”。
# break和continue语句
# break语句
`break`语句可用于跳出循环。如：
```py
sum = 0
while True:
    sum += 1
    print(sum,end=" ")
    if sum >= 6:
        print("broken")
        break
        print("在break后面的就不被运行了，所以在结果中你看不到这句话")
```
运行结果：
```
1 2 3 4 5 6 broken
```
像这样，虽然是死循环的形式，但是执行6循环后就会进入if而碰到`break`此循环结束。

而`continue`语句则没有这么绝，在循环中一旦碰到`continue`，这下面的语句将不会被执行，而是重新从循环的第一条语句开始。
```py
for i in range(5):
    print(i,"continue之前")
    if i == 3:
        continue
    print(i,"continue之后")
```
运行结果：
```
0 continue之前
0 continue之后
1 continue之前
1 continue之后
2 continue之前
2 continue之后
3 continue之前
4 continue之前
4 continue之后
```

当`i=3`时进入第3行的if判断，碰到`continue`语句导致本次循环中第5行的`print(i,"continue之后")`被跳过，结果就没有“`3 continue之后`”这句。

# 自测
1. 阅读以下程序：
```py
for i in range(8):
    if i % 2== 0:
        print(i,end=" ")
    if i == 4:
        break
```
下列说法正确的是（      ）
A. 该程序的输出为`0 2`
B. 该程序的输出为`0 2 6 8`
C. 该程序的输出为`0 2 4`
D.以上皆不正确
【答案】C

2. 在以下程序中，若想输出`12356`，则序号处应该分别填入什么？
```py
for i in range(1,7):
    if ①________:
        ②________
```
A. ① `i == 4` ② `break`
B. ① `i == 4` ② `continue`
C. ① `i != 4` ② `print(i,end="")`
D. ① `i != 4` ② `print(i,sep="")`
【答案】C

# 总结
**for 循环**
用`for i in range(n,m,l)`可以设置起始、结束和步长。其中，起始和步长可省略，若省略起始则默认从0开始；若省略步长则默认为1。
**while 循环**
用法为`while 条件`，若条件成立则会执行循环，每执行完循环后都会检查条件是否仍然成立。若不成立则结束循环。若需要死循环，则可以写成`while True`。
**break和continue语句**
简而言之，`break`就是结束循环；`continue`就是提前结束**本次**循环。

# 结尾
好啦，就到这里了，记得点赞收藏关注哦₍˄·͈༝·͈˄*₎◞ ̑̑

