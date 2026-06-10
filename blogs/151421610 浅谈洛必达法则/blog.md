@[TOC]

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

洛必达法则本来是高数中的内容，然而这东西在高中却出奇地好用，尤其是对于某些需要用端点效应才能解决的题目，洛必达法则一下就能解决。
所以这一次，主要介绍一下洛必达法则吧。这里我只介绍用法，至于严格证明嘛，请自己买书看吧！
# L’Hôpital’s Rule
洛必达法则之核心就两条：
$x\rightarrow a$时，若$f(x)\rightarrow0$，$g(x)\rightarrow 0$，则$\lim\limits_{x\rightarrow a}\dfrac{f(x)}{g(x)}=\dfrac{f'(x)}{g'(x)}$
$x\rightarrow a$时，若$f(x)\rightarrow\infty$，$g(x)\rightarrow \infty$，则$\lim\limits_{x\rightarrow a}\dfrac{f(x)}{g(x)}=\dfrac{f'(x)}{g'(x)}$

说人话：如果一个参数带入一个含参分数，导致分子和分母同时为$0$或$\infty$，那么直接对分子和分母分别求导，然后再代。

为了便于理解，这里再提供几道例题，一起看看吧！

# 几种未定型
## $\dfrac{0}{0}$型

> 当$x\rightarrow0$时，求$\dfrac{\sin x}{2x}$的值。

发现当$x=0$时，$\sin x=0$，$2x=0$，分子分母都为$0$，无法直接求。此时，可以使用洛必达法则。
首先，对分子和分母求导。
分子求导：$(\sin x)'=\cos x$
分母求导：$(2x)'=2$
所以$\lim\limits_{x\rightarrow0}\dfrac{\sin x}{2x}=\lim\limits_{x\rightarrow0}\dfrac{\cos x}{2}$
现在，可以把$x=0$代入到处理完的分数中了：$\lim\limits_{x\rightarrow0}\dfrac{\cos x}{2}=\dfrac12$。
综上，$\lim\limits_{x\rightarrow0}\dfrac{\sin x}{2x}=\dfrac12$。

## $\dfrac\infty\infty$型

> 当$x\rightarrow+\infty$时，求$\dfrac{2x^2}{3x}$的值。

发现当$x\rightarrow +\infty$时，$2x^2\rightarrow +\infty$，$3x \rightarrow +\infty$，分子分母都为$\infty$，无法直接求。此时，依然可以使用洛必达法则。
首先，对分子和分母求导。
分子求导：$(2x^2)'=4x$
分母求导：$(3x)'=3$
所以$\lim\limits_{x\rightarrow +\infty}\dfrac{2x^2}{3x}=\lim\limits_{x\rightarrow+\infty}\dfrac{4x}{3}$
现在，又可以把$x\rightarrow+\infty$代到处理完的分数中了：$\lim\limits_{x\rightarrow +\infty}\dfrac{4x}{3}=\dfrac{4\cdot+\infty}{3}=+\infty$。
综上，$\lim\limits_{x\rightarrow +\infty}\dfrac{2x^2}{3x}=+\infty$。（我过程写的可能不是很规范，但意思是这个意思）

## $0\cdot \infty$型
> 当$x=0$时，求$x\ln x$的值。

发现当$x=0$时，$x=0$，$\ln x \rightarrow -\infty$，无法直接求。此时，还是可以使用洛必达法则。但是，需要对原来的式子进行一些变形。像这样：
$x\ln x=\ln x\cdot\dfrac{1}{\frac{1}{x}}= \dfrac{\ln x}{\frac{1}{x}}$
然后，就变成了之前介绍的$\dfrac\infty\infty$型了。所以直接按照之前的流程来就行，求导，代入：
分子求导：$(\ln x)'=\dfrac1x$
分母求导：$(\dfrac{1}{x})'=-\dfrac{1}{x^2}$
所以$\lim\limits_{x\rightarrow 0}x \ln x=\lim\limits_{x\rightarrow 0} \dfrac{\ln x}{\frac{1}{x}}=\lim\limits_{x\rightarrow 0} \dfrac{\frac1x}{-\frac{1}{x^2}}= \lim\limits_{x\rightarrow 0} -\dfrac{x^2}{x} =\lim\limits_{x\rightarrow 0} -x=0$。

还有，大家可以试试把$\ln x$变成分母部分，会发现出问题了：$\lim\limits_{x\rightarrow 0}x \ln x=\lim\limits_{x\rightarrow 0} \dfrac{x}{\frac{1}{\ln x}}=\lim\limits_{x\rightarrow 0}-x(\ln x)^2$，函数变复杂了！说明不可以把$\ln x$变到分母上，只能把$x$变成$\dfrac1x$，不然很难求解。

## 非洛必达情况
某些东西可能看起来很像洛必达法则能处理的，实则并不是。看这个：
> 求$\lim\limits_{x\rightarrow +\infty}\dfrac{x+\sin x}{x}$。

如果按照洛必达法则的思路，那么$\lim\limits_{x\rightarrow +\infty}\dfrac{x+\sin x}{x}= \lim\limits_{x\rightarrow +\infty}\dfrac{1+\cos x}{1}$。
然后发现：诶，$\cos x$不是个周期函数吗，当$x\rightarrow+\infty$时它并不收敛（即无限趋近于某一个值，可以是无穷），这怎么求啊？
实际上，只需要分析一下原函数$\dfrac{x+\sin x}{x}$就行了：观察分子分母，发现$x\in \mathbb R$时，$\sin x\in[-1,1]$。所以$x\rightarrow +\infty$时，分子和分母其实是相等的，因为分子中的$\sin x$相对于$x$实在是太小了，直接忽略不计了。
举几个例子：当$x=10000$时，$\dfrac{x+\sin x}{x}=\dfrac{10000-0.984}{10000}\approx 1$；当$x=114514$时，$\dfrac{x+\sin x}{x}=\dfrac{114514+0.559}{114514}\approx 1$。
所以，$\lim\limits_{x\rightarrow +\infty}\dfrac{x+\sin x}{x}=1$，整个过程实际上用不到洛必达法则，而且还比用了还要简单。

# 注意
使用洛必达法则需要注意几点：
1. 分子、分母必须分别可导！
2. 检查函数形式经过转化后是否符合以上介绍的几种未定型（$\dfrac00$/$\dfrac\infty\infty$），若不是，不能用洛必达法则。
3. 处理完函数之后，发现函数变复杂了，那么换个思路，看看有没有其它方法。
4. 洛必达法则不是只能用一次，如果用完后还是解决不了问题，那就继续用，直到解决问题为止。
5. 在高考中，小题随便用，大题慎用，可能会扣分。
6. 不要和导数里面的“上导下不导，下导上不导”搞混了，洛必达法则时“上下分别导”。

# 小练习

> 求$\lim\limits_{x\rightarrow0^+}\dfrac{e^x-e^{-x}}{x^2}$。

$\lim\limits_{x\rightarrow0^+}\dfrac{e^x-e^{-x}}{x^2}=\lim\limits_{x\rightarrow0^+}\dfrac{e^x+e^{-x}}{2x}=\dfrac{2}{0^+}=+\infty$

> 求$\lim\limits_{x\rightarrow0}\dfrac{e^x-x-1}{x^2}$。

$\lim\limits_{x\rightarrow0}\dfrac{e^x-x-1}{x^2}= \lim\limits_{x\rightarrow0}\dfrac{e^x-1}{2x}= \lim\limits_{x\rightarrow0}\dfrac{e^x}{2}=\dfrac12$

# 结尾
好啦，今天就介绍到这里啦，你学会了吗！记得点赞关注+收藏哦！

