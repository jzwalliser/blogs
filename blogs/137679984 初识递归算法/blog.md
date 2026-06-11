@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 介绍
递归是一种算法，即自己调用自己。可以是一个函数自己调用自己，即直接递归，也可以是两个函数相互调用，即间接递归。

递归算法主要由两个部分组成：递归操作及递归边界。递归操作是函数的主体部分，负责执行运算、实现功能；递归边界即一个条件， 满足条件后停止递归，并返回上一层，以避免程序无限递归下去而陷入死循环。

# 例
比如，计算阶乘就可以使用递归算法来实现。$n!=n\times(n-1)\times(n-2)\times\cdots\times2\times1$例如，$5!=5\times4\times3\times2\times1=120$。
假设$x$的阶乘用$f(x)$来表示$x\in\mathbb{Z_+}$，那么：

$$ f(x)=\left\{
\begin{aligned}
&1\space(x=1) \\
&x\times f(x-1)\space(x>1) \\
\end{aligned}
\right.
$$


翻译为代码如下。
## Python
```py
def f(x):
    if x > 1:
        return x * f(x - 1)
    return 1
```

## C++
```cpp
long long int f(x){
    if(x > 1){
        return x * f(x - 1);
    }
    return 1;
}
```

# 原理
可以发现，当调用$f(5)$时，程序就会递归调用$f(4)$，并计算$5\times f(4)$，然后再计算$4\times f(3)$……直到调用$f(1)$才终于撞到了边界条件，停止递归并返回$1$，接着$f(2)$返回$2$，f(3)返回6……直到$f(5)$返回$120$。
递归本质上是一种由系统自动维护的栈，数据先进后出（FILO，First in Last out）。
可见，第一个进去的$f(3)$最后一个出来，而最后进去的$f(1)$第一个出来。

# 优缺点分析
递归的写法有许多好处。首先，递归的代码简洁，可以用较少的代码表达较复杂的过程。其次，递归的效率还很高。

但递归不是万能的。能写成递归形式的算法，基本都可以写成非递归。且一个算法是否该用递归，还需要考虑数据规模。如果数据规模太过巨大，可能会导致递归几百万层，最终爆栈。

不过话说回来，递归最深深度也取决于硬件、操作系统、编程语言等因素，一般来说递归个几万层没多大问题。

递归还有一个小缺点：代码太过简洁，可能难以理解，对初学者来说可能不太友好。

# 题目
有的题目用到了递归算法：
[洛谷 P1087 [NOIP2004 普及组] FBI 树](https://blog.csdn.net/jzwalliser/article/details/135990485)
[洛谷 P1010 [NOIP1998 普及组] 幂次方](https://blog.csdn.net/jzwalliser/article/details/135980531)

# 结尾
好啦，今天的分享到此结束，记得点赞+收藏哦！

