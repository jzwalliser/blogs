@[toc]

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

这一次，讲讲数列的特征根求通项法。

# 基本思路
当数列的递推公式内出现了连续的三项$a_n$、$a_{n+1}$、$a_{n+2}$，就可以用特征根法。方法就是：把$a_n$替换成$1$，$a_{n+1}$替换成$x$，$a_{n+2}$替换成$x^2$，然后解方程。如果有两个相同的解$x_0$，那就列$a_n=(An+B)x_0^n$；如果是两个不同的解$x_1$、$x_2$，那就列$a_n=Ax_1^n+Bx_2^n$，然后代入题目所给条件（如$a_1=n$，$a_2=m$之类的）即可。
光讲没感觉，一起来看看题目吧！

# 不同类型

## 2个解
> 已知各项都为正数的数列$\{a_n\}$满足关系$a_{n+2}=2a_{n+1}+3a_n$，$a_1=1$，$a_2=2$，求数列通项公式。

首先，把$a_n$替换成$1$，$a_{n+1}$替换成$x$，$a_{n+2}$替换成$x^2$：
$x^2=2x+3$
这就是该数列的特征方程。然后解方程：
$x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}=\dfrac{2\pm\sqrt{(-2)^2-4\times1\times(-3)}}{2\times1}$
$x_1=3,x_2=-1$
所以，解出两个不同的解，列式：$a_n=A\times3^n+B\times(-1)^n$，再代入$a_1=1$，$a_2=2$，得出方程组：
$\left\{ \begin{aligned}&1=3A-B\\&2=9A+B\end{aligned}\right.$
解得$\left\{ \begin{aligned}&A=\dfrac14\\&B=-\dfrac14\end{aligned}\right.$
得到通项公式：$a_n=\dfrac14\times3^n-\dfrac14\times(-1)^n=\dfrac{3^n-(-1)^n}{4}$

不信？不信我们敲一段Python来验证一下：
```py
for i in range(1,10):
    print(i,(3 ** i - (-1) ** i) / 4)
```

稍微整理一下结果：
|1|2|3|4|5|6|7|8|9|
|:-|:-|:-|:-|:-|:-|:-|:-|:-|
|1|2|7|20|61|182|547|1640|4921|

符合通项公式吗？太符合了！

## 1个解
> 已知各项都为正数的数列$\{a_n\}$满足关系$a_{n+2}=6a_{n+1}-9a_n$，$a_1=1$，$a_2=2$，求数列通项公式。

和上面一样，把$a_n$替换成$1$，$a_{n+1}$替换成$x$，$a_{n+2}$替换成$x^2$：
$x^2=6x-9$
得到数列的特征方程。解方程：
$x=\dfrac{-b\pm\sqrt{b^2-4ac}}{2a}=\dfrac{6\pm\sqrt{(-6)^2-4\times1\times9}}{2\times1}=3$
所以，解出两个相同的解$x_1=x_2=3$，列式：$a_n=(An+B)\cdot 3^n$，再代入$a_1=1$，$a_2=2$，得出方程组：
$\left\{ \begin{aligned}&1=3(A+B)\\&2=9(2A+B)\end{aligned}\right.$
解得$\left\{ \begin{aligned}&A=-\dfrac19\\&B=\dfrac49\end{aligned}\right.$
得到通项公式：$a_n=\dfrac{4-n}{9}\cdot3^n=3^{n-2}(4-n)$

## 无解

无解就比较麻烦了，但是**大多数情况**可以认为是周期数列（虽然不绝对），因为一般高考不太会出现其它奇奇怪怪的情况。请看题：
> 已知数列$\{a_n\}$满足关系$a_{n+2}=a_{n+1}-a_n$，$a_1=1$，$a_2=2$，求$S_{2021}$。

还是老样子，把$a_n$替换成$1$，$a_{n+1}$替换成$x$，$a_{n+2}$替换成$x^2$：
$x^2=x-1$
然后解方程，发现$\Delta =b^2-4ac=(-1)^2-4\times1\times1=-3<0$。
很好，无解！考虑是周期数列。
先来找找规律：
$a_1=1$
$a_2=2$
$a_{3}=a_{2}-a_{1}=1$
$a_{4}=a_{3}-a_{2}=-1$
$a_{5}=a_{4}-a_{3}=-2$
$a_{6}=a_{5}-a_{4}=-1$
$a_{7}=a_{6}-a_{5}=1$
$a_{8}=a_{7}-a_{6}=2$
$a_{9}=a_{8}-a_{7}=1$
$a_{10}=a_{9}-a_{8}=-1$
$\cdots$
所以发现了吧？以6个为一周期，不停地循环。而且每六个相加（$a_1\sim a_6$，$a_7\sim a_{12}$、$\cdots$）的结果都是0。
所以，$S_{2021}=336\times0+1=1$。

不信？那就自己运行程序看看吧。
```py
a = [0,1,2]
for i in range(3,2022):
    a.append(a[-1] - a[-2])
    
for i in range(1,2022):
    print("a[" + str(i) + "]=a[" + str(i - 1) + "]-a[" + str(i - 2) + "]=",a[i],sep="")
    
print("Sum:",sum(a))
```

# 小练习
好啦，上面的东西你都学会了吗？看点小练习吧！

> 已知各项都为正数的数列$\{a_n\}$满足关系$a_{n+2}=a_{n+1}+a_n$，$a_1=1$，$a_2=1$，求数列通项公式（这就是著名的斐波那契数列）。

令$a_n=1$，$a_{n+1}=x$，$a_{n+2}=x^2$，得到特征方程：
$x^2=x+1$
解得$x_1=\dfrac{1+\sqrt5}{2},x_2=\dfrac{1-\sqrt5}{2}$。
设$a_n=A\times(\dfrac{1+\sqrt5}{2})^n+B\times(\dfrac{1-\sqrt5}{2})^n$
代入$a_1=1$，$a_2=1$，得：
$\left\{ \begin{aligned}&1=A\times\dfrac{1+\sqrt5}{2}+B\times\dfrac{1-\sqrt5}{2}\\&1=A\times(\dfrac{1+\sqrt5}{2})^2+B\times(\dfrac{1-\sqrt5}{2})^2\end{aligned}\right.$
解得$\left\{ \begin{aligned}&A=\dfrac{\sqrt5} 5\\&B=-\dfrac{\sqrt5} 5\end{aligned}\right.$
$\therefore a_n=\dfrac{\sqrt5} 5[(\dfrac{1+\sqrt5}{2})^n-(\dfrac{1-\sqrt5}{2})^n]$

> 已知数列$\{a_n\}$满足关系$a_{n+2}=4a_{n+1}-4a_n$，$a_1=1$，$a_2=1$，求数列通项公式。

令$a_n=1$，$a_{n+1}=x$，$a_{n+2}=x^2$，得到特征方程：
$x^2=4x-4$
解得$x_1=x_2=2$。
设$a_n=(An+B)\cdot2^n$
代入$a_1=1$，$a_2=1$，得：
$\left\{ \begin{aligned}&1=(A+B)\times2\\&1=(2A+B)\times4\end{aligned}\right.$
解得$\left\{ \begin{aligned}&A=-\dfrac14\\&B=\dfrac34\end{aligned}\right.$
$\therefore a_n=(-\dfrac n4+\dfrac34)\times2^n=\dfrac{3-n}{4}\times2^n$

# 结尾
好啦，今天就介绍到这里啦，你学会了吗？记得点赞收藏哦！

