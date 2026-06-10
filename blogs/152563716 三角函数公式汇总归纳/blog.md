@[TOC]

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 前言
笔者高中牲，之前学习三角函数有关知识时，总容易忘这忘那，所以特意整理了一下，方便复习，这里也分享给大家。

# 诱导公式
> “奇变偶不变，符号看象限”
> 
|公式一|公式二|公式三|
|:-|:-|:-|
|$\sin(\alpha+2k\pi)=\sin \alpha$ $(k\in\mathbb Z)$|$\sin(-\alpha)=-\sin \alpha$|$\sin (\pi-\alpha)=\sin \alpha$|
|$\cos(\alpha+2k\pi)=\cos \alpha$ $(k\in\mathbb Z)$|$\cos(-\alpha)=\cos \alpha$|$\cos (\pi-\alpha)=-\cos \alpha$|
|$\tan(\alpha+2k\pi)=\tan \alpha$ $(k\in\mathbb Z)$|$\tan (-\alpha)=-\tan \alpha$|$\tan (\pi-\alpha)=-\tan \alpha$|

|公式四|公式五|公式六|
|:-|:-|:-|
|$\sin (\pi+\alpha)=-\sin \alpha$|$\sin (\dfrac{\pi}{2}-\alpha)=\cos \alpha$|$\sin (\dfrac{\pi}{2}+\alpha)=\cos \alpha$|
|$\cos (\pi+\alpha)=-\cos \alpha$|$\cos (\dfrac{\pi}{2}-\alpha)=\sin \alpha$|$\cos (\dfrac{\pi}{2}+\alpha)=-\sin \alpha$|
|$\tan (\pi+\alpha)=\tan \alpha$|$\tan (\dfrac{\pi}{2}-\alpha)=\dfrac{1}{\tan \alpha}$|$\tan (\dfrac{\pi}{2}+\alpha)=-\dfrac{1}{\tan \alpha}$|

# 基本公式
## 同角三角函数关系
> $\sin^2\alpha+\cos^2\alpha=1$
> $\dfrac{\sin\alpha}{\cos\alpha}=\tan\alpha$

如图所示，取一单位圆$x^2+y^2=1$，在单位圆上任取一点$P(x,y)$

![请添加图片描述](https://i-blog.csdnimg.cn/direct/6c8dc212aea94210b5eb0e5124562e23.png)


根据正、余弦和正切函数在单位圆内的定义，可得$\sin\alpha=\dfrac{y}{r}=y$，$\cos\alpha=\dfrac{x}{r}=x$，$\tan\alpha=\dfrac{y}{x}$
$\therefore \sin^2\alpha+\cos^2\alpha=y^2+x^2=1，\dfrac{\sin\alpha}{\cos\alpha}=\dfrac{y}{x}=\tan\alpha$

## 和差公式
> $S_{(\alpha\pm\beta)}:\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$
> $C_{(\alpha\pm\beta)}:\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$
> $T_{(\alpha\pm\beta)}:\tan(\alpha\pm\beta)=\dfrac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$

如图所示，取一单位圆$x^2+y^2=1$，在单位圆上取两点$A$、$B$，记$\angle AOx=\alpha$，$\angle BOx=\beta$

![请添加图片描述](https://i-blog.csdnimg.cn/direct/1cc854a736b6480fbb82ef01530308bd.png)


根据圆的参数方程，可设$A(\cos \alpha,\sin \alpha)$，$B(\cos \beta,\sin \beta)$
$\therefore \overrightarrow{OA}=(\cos \alpha,\sin \alpha)$，$\overrightarrow{OB}=(\cos \beta,\sin \beta)$
$\because$单位圆的半径$r=1$
$\therefore |\overrightarrow{OA}|=1$，$|\overrightarrow{OB}|=1$
$\therefore \overrightarrow{OA}\cdot\overrightarrow{OB}=|\overrightarrow{OA}||\overrightarrow{OB}|\cos(\alpha-\beta)=1\times1\times\cos(\alpha-\beta)$
$\overrightarrow{OA}\cdot\overrightarrow{OB}=\cos\alpha\cos\beta+\sin\alpha\sin\beta$
$\therefore \cos(\alpha-\beta)=\cos \alpha\cos \beta+\sin \alpha\sin \beta$

用$-\beta$代替掉原来$\beta$的位置，可得$\cos(\alpha+\beta)=\cos \alpha\cos (-\beta)+\sin\alpha\sin (-\beta)=\cos \alpha\cos \beta-\sin \alpha\sin\beta$

用$\dfrac{\pi}{2}-\alpha$代替掉$\cos(\alpha-\beta)=\cos \alpha\cos \beta+\sin \alpha\sin \beta$中$\alpha$的位置，可得$\cos[(\dfrac{\pi}{2}-\alpha)-\beta]=\cos (\dfrac{\pi}{2}-\alpha)\cos \beta+\sin (\dfrac{\pi}{2}-\alpha)\sin \beta$
对等式两侧使用诱导公式，可得
$\sin (\alpha+\beta)=\sin \alpha\cos \beta+\cos \alpha\sin \beta$

用$-\beta$代替掉原来$\beta$的位置，可得$\sin(\alpha-\beta)=\sin \alpha\cos (-\beta)+\cos\alpha\sin (-\beta)=\sin\alpha\cos \beta-\cos \alpha\sin\beta$

由此得到$\sin(\alpha\pm\beta)=\sin\alpha\cos\beta\pm\cos\alpha\sin\beta$、$\cos(\alpha\pm\beta)=\cos\alpha\cos\beta\mp\sin\alpha\sin\beta$

$\therefore\tan(\alpha\pm\beta)=\dfrac{\sin(\alpha\pm\beta)}{\cos(\alpha\pm\beta)}=\dfrac{\sin\alpha\cos\beta\pm\cos\alpha\sin\beta}{\cos\alpha\cos\beta\mp\sin\alpha\sin\beta}=\dfrac{\tan\alpha\pm\tan\beta}{1\mp\tan\alpha\tan\beta}$（上下同时除以$\cos\alpha\cos\beta$）

## 二倍角公式
> $S_{2\alpha}:\sin2\alpha=2\sin\alpha\cos\alpha$
> $C_{2\alpha}:\cos2\alpha=\cos^2\alpha-\sin^2\alpha$
> $T_{2\alpha}:\tan2\alpha=\dfrac{2\tan\alpha}{1-\tan^{2}\alpha}$

$\sin2\alpha=\sin(\alpha+\alpha)=\sin\alpha\cos\alpha+\cos\alpha\sin\alpha=2\sin\alpha\cos\alpha$
$\cos2\alpha=\cos(\alpha+\alpha)=\cos\alpha\cos\alpha-\sin\alpha\sin\alpha=\cos^2\alpha-\sin^2\alpha$
$\tan2\alpha=\tan(\alpha+\alpha)=\dfrac{\tan\alpha+\tan\alpha}{1-\tan\alpha\tan\alpha}=\dfrac{2\tan\alpha}{1-\tan^2\alpha}$

## 辅助角公式
> $a \sin \alpha+ b \cos \alpha= \sqrt{a^2 + b^2} \sin(\alpha+ \varphi)$
> $a \sin \alpha+ b \cos \alpha= \sqrt{a^2 + b^2} \cos(\alpha - \theta)$
> 其中$\tan \varphi= \dfrac{b}{a}$，$\tan \theta = \dfrac{a}{b}$

$a \sin\alpha + b \cos\alpha = \sqrt{a^2+b^2} ( \dfrac{a}{\sqrt{a^2+b^2}} \sin\alpha + \dfrac{b}{\sqrt{a^2+b^2}} \cos\alpha)$

令$\dfrac{a}{\sqrt{a^2+b^2}} = \cos\varphi,\dfrac{b}{\sqrt{a^2+b^2}} = \sin\varphi$

则$a \sin\alpha + b \cos\alpha = \sqrt{a^2+b^2} ( \cos\varphi \sin\alpha + \sin\varphi \cos\alpha)= \sqrt{a^2+b^2} \sin(\alpha+\varphi)$

其中，$\tan\varphi = \dfrac{\sin\varphi}{\cos\varphi} = \dfrac{\frac{b}{\sqrt{a^2+b^2}}}{\frac{a}{\sqrt{a^2+b^2}}} = \dfrac{b}{a}$

令$\dfrac{a}{\sqrt{a^2+b^2}} = \sin\theta,\dfrac{b}{\sqrt{a^2+b^2}} = \cos\theta$

则$a \sin\alpha + b \cos\alpha = \sqrt{a^2+b^2} ( \sin\theta \sin\alpha + \cos\theta \cos\alpha)= \sqrt{a^2+b^2} \cos(\alpha-\theta)$

其中，$\tan\theta = \dfrac{\sin\theta}{\cos\theta} = \dfrac{\frac{a}{\sqrt{a^2+b^2}}}{\frac{b}{\sqrt{a^2+b^2}}} = \dfrac{a}{b}$
# 重要公式
## 升幂公式
> $1 + \cos 2\alpha= 2 \cos^2 \alpha$
> $1 - \cos 2\alpha= 2 \sin^2 \alpha$
> $1 + \sin 2\alpha= (\sin \alpha + \cos \alpha)^2$
> $1 - \sin 2\alpha= (\sin \alpha - \cos \alpha)^2$


$\because \cos2\alpha=\cos^2\alpha-\sin^2\alpha$
$\therefore \cos^2\alpha=\sin^2\alpha+\cos2\alpha$
$\cos^2\alpha+\cos^2\alpha=\sin^2\alpha+\cos^2\alpha+\cos 2\alpha$
$2\cos^2\alpha=\sin^2\alpha+\cos^2\alpha+\cos2\alpha$
$2\cos^2\alpha=1+\cos2\alpha$

$\because \cos2\alpha=\cos^2\alpha-\sin^2\alpha$
$\therefore \sin^2\alpha=\cos^2\alpha-\cos2\alpha$
$\sin^2\alpha+\sin^2\alpha=\cos^2\alpha+\sin^2\alpha-\cos 2\alpha$
$2\sin^2\alpha=\cos^2\alpha+\sin^2\alpha-\cos2\alpha$
$2\sin^2\alpha=1-\cos2\alpha$

$1+\sin 2\alpha=\sin^2\alpha+\cos^2\alpha+2\sin \alpha\cos \alpha=(\sin \alpha+\cos \alpha)^2$

$1-\sin 2\alpha=\sin^2\alpha+\cos^2\alpha-2\sin \alpha\cos \alpha=(\sin \alpha-\cos \alpha)^2$
## 降幂公式
> $\sin^2 \alpha = \dfrac{1}{2}(1 - \cos 2\alpha)$
> $\cos^2 \alpha= \dfrac{1}{2}(1 + \cos 2\alpha)$

$\because 2\sin^2\alpha=1-\cos2\alpha$
$\therefore \sin^2\alpha=\dfrac12(1-\cos2\alpha)$

$\because 2\cos^2\alpha=1+\cos2\alpha$
$\therefore \cos^2\alpha=\dfrac12(1+\cos2\alpha)$
## 逆用倍角公式
> $\sin \alpha = \dfrac{\sin 2\alpha}{2 \cos \alpha}$
> $\cos \alpha = \dfrac{\sin 2\alpha}{2 \sin \alpha}$
> $\tan \alpha = \dfrac{\tan 2\alpha(1 - \tan^2 \alpha)}{2}$
> $(\cos \alpha + \sin \alpha)(\cos \alpha - \sin \alpha)=\cos^2 \alpha - \sin^2 \alpha = \cos2\alpha$
> $2 \cos^2 \alpha - 1 = 1 - 2 \sin^2 \alpha = \cos 2\alpha$

$\because\sin 2\alpha=2\sin \alpha\cos \alpha$
$\therefore\sin \alpha = \dfrac{\sin 2\alpha}{2 \cos \alpha}$，$\cos \alpha = \dfrac{\sin 2\alpha}{2 \sin \alpha}$
$\because \tan2\alpha=\dfrac{2\tan\alpha}{1-\tan^{2}\alpha}$
$\therefore \tan \alpha = \dfrac{\tan 2\alpha(1 - \tan^2 \alpha)}{2}$

$\because\cos2\alpha=\cos^2\alpha-\sin^2\alpha$
$\therefore(\cos \alpha + \sin \alpha)(\cos \alpha - \sin \alpha)=\cos^2 \alpha - \sin^2 \alpha = \cos2\alpha$

$\because\sin^2 \alpha = \dfrac{1}{2}(1 - \cos 2\alpha)$，$\cos^2 \alpha= \dfrac{1}{2}(1 + \cos 2\alpha)$
$\therefore 2 \cos^2 \alpha - 1 = 1 - 2 \sin^2 \alpha = \cos 2\alpha$
## 积化和差
> $\cos\alpha\cos\beta=\dfrac{1}{2}[\cos(\alpha+\beta)+\cos(\alpha-\beta)]$
> $\sin\alpha\sin\beta=-\dfrac{1}{2}[\cos(\alpha+\beta)-\cos(\alpha-\beta)]$
> $\sin\alpha\cos\beta=\dfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)]$
> $\cos\alpha\sin\beta=\dfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)]$

$\dfrac{1}{2}[\cos(\alpha+\beta)+\cos(\alpha-\beta)]=\dfrac12(\cos\alpha\cos \beta-\sin \alpha\sin \beta+\cos \alpha\cos \beta+\sin \alpha\sin \beta)=\dfrac12\cdot2\cos \alpha\cos \beta=\cos \alpha\cos \beta$

$-\dfrac{1}{2}[\cos(\alpha+\beta)-\cos(\alpha-\beta)]=-\dfrac12(\cos \alpha\cos \beta-\sin \alpha\sin \beta-\cos \alpha\cos \beta-\sin \alpha\sin \beta)=-\dfrac12\cdot(-2\sin \alpha\sin \beta)=\sin \alpha\sin \beta$

$\dfrac{1}{2}[\sin(\alpha+\beta)+\sin(\alpha-\beta)]=\dfrac12(\sin \alpha\cos \beta+\sin \beta\cos \alpha+\sin \alpha\cos \beta-\sin \beta\cos \alpha)=\dfrac12\cdot2\sin \alpha\cos \beta=\sin \alpha\cos \beta$

$\dfrac{1}{2}[\sin(\alpha+\beta)-\sin(\alpha-\beta)]=\dfrac12(\sin \alpha\cos \beta+\sin \beta\cos \alpha-\sin \alpha\cos \beta+\sin \beta\cos \alpha)=\dfrac12\cdot2\sin \beta\cos \alpha=\cos \alpha\sin \beta$

## 和差化积
> $\cos\alpha+\cos\beta=2\cos\dfrac{\alpha+\beta}{2}\cos\dfrac{\alpha-\beta}{2}$
> $\cos\alpha-\cos\beta=-2\sin\dfrac{\alpha+\beta}{2}\sin\dfrac{\alpha-\beta}{2}$
> $\sin\alpha+\sin\beta=2\sin\dfrac{\alpha+\beta}{2}\cos\dfrac{\alpha-\beta}{2}$
> $\sin\alpha-\sin\beta=2\cos\dfrac{\alpha+\beta}{2}\sin\dfrac{\alpha-\beta}{2}$

令$A+B=\alpha$，$A-B=\beta$
$\therefore\left\{ \begin{aligned}&A+B=\alpha\\&A-B=\beta\end{aligned}\right.$
解得$\left\{ \begin{aligned}&A=\dfrac{\alpha+\beta}{2}\\&B=\dfrac{\alpha-\beta}{2}\end{aligned}\right.$

$\cos\alpha+\cos\beta=\cos (A+B)+\cos (A-B)=\cos A\cos B-\sin A\sin B+\cos A\cos B+\sin A\sin B=2\cos A\cos B=2\cos\dfrac{\alpha+\beta}{2}\cos\dfrac{\alpha-\beta}{2}$


$\cos\alpha-\cos\beta=\cos (A+B)-\cos (A-B)=\cos A\cos B-\sin A\sin B-\cos A\cos B-\sin A\sin B=-2\sin A\sin B=-2\sin\dfrac{\alpha+\beta}{2}\sin\dfrac{\alpha-\beta}{2}$

$\sin\alpha+\sin\beta=\sin (A+B)+\sin (A-B)=\sin A\cos B+\sin B\cos A+\sin A\cos B-\sin B\cos A=2\sin A\cos B=2\sin\dfrac{\alpha+\beta}{2}\cos\dfrac{\alpha-\beta}{2}$

$\sin\alpha-\sin\beta=\sin (A+B)-\sin (A-B)=\sin A\cos B+\sin B\cos A-\sin A\cos B+\sin B\cos A=2\sin B\cos A=2\cos\dfrac{\alpha+\beta}{2}\sin\dfrac{\alpha-\beta}{2}$

## 半角公式
> $\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$
> $\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$
> $\tan\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{1+\cos\alpha}}$
> $\tan\dfrac{\alpha}{2}=\dfrac{1-\cos\alpha}{\sin\alpha}=\dfrac{\sin\alpha}{1+\cos\alpha}$

$\because1+\cos 2\alpha=2\cos^2\alpha$
$\therefore1+\cos \alpha=2\cos^2\dfrac{\alpha}{2}$
$\therefore\cos\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1+\cos\alpha}{2}}$

$\because1-\cos 2\alpha=2\sin^2\alpha$
$\therefore1-\cos \alpha=2\sin^2\dfrac{\alpha}{2}$
$\therefore\sin\dfrac{\alpha}{2}=\pm\sqrt{\dfrac{1-\cos\alpha}{2}}$

$\therefore\tan\dfrac{\alpha}{2}=\dfrac{\sin\dfrac{\alpha}{2}}{\cos \dfrac{\alpha}{2}}=\pm\sqrt{\dfrac{1-\cos\alpha}{1+\cos\alpha}}$

$\tan \dfrac{\alpha}{2}=\dfrac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}}=\dfrac{2\sin \frac{\alpha}{2}\cos \frac{\alpha}{2}}{2\cos^2\frac{\alpha}{2}}=\dfrac{\sin \alpha}{1+\cos \alpha}$

$\tan \dfrac{\alpha}{2}=\dfrac{\sin \frac{\alpha}{2}}{\cos \frac{\alpha}{2}}=\dfrac{2\sin^2\frac{\alpha}{2}}{2\sin \frac{\alpha}{2}\cos\frac{\alpha}{2}}=\dfrac{1-\cos \alpha}{\sin \alpha}$

# 其它公式
## 三倍角公式
> $\sin 3\alpha = 3 \sin \alpha - 4 \sin^3 \alpha$
> $\cos 3\alpha = 4 \cos^3 \alpha - 3 \cos \alpha$
> $\tan 3\alpha = \dfrac{3 \tan \alpha - \tan^3 \alpha}{1 - 3 \tan^2 \alpha}$

$\sin 3\alpha=\sin (2\alpha+\alpha)=\sin 2\alpha\cos \alpha+\cos 2\alpha\sin \alpha=2\sin \alpha(1-\sin^2\alpha)+(1-2\sin^2\alpha)\sin \alpha=3\sin \alpha-4\sin^3\alpha$

$\cos 3\alpha=\cos (2\alpha+\alpha)=\cos 2\alpha\cos \alpha-\sin 2\alpha\sin \alpha=(2\cos^2\alpha-1)\cos \alpha-2(1-\cos^2\alpha)\cos \alpha=4\cos^3\alpha-3\cos \alpha$

$\tan 3\alpha=\dfrac{\sin 3\alpha}{\cos 3\alpha}=\dfrac{\sin (\alpha+2\alpha)}{\cos (\alpha+2\alpha)}=\dfrac{\sin \alpha\cos 2\alpha+\cos \alpha\sin 2\alpha}{\cos \alpha\cos 2\alpha-\sin \alpha\sin 2\alpha}=\dfrac{\sin \alpha(\cos^2\alpha-\sin ^2\alpha)+\cos \alpha\cdot2\sin \alpha\cos\alpha}{\cos \alpha(\cos ^2\alpha-\sin ^2\alpha)-\sin \alpha\cdot2\sin \alpha\cos \alpha}=\dfrac{\sin \alpha\cos^2\alpha-\sin^3\alpha+2\sin \alpha\cos^2\alpha}{\cos^3\alpha-\sin ^2\alpha\cos \alpha-2\sin^2\alpha\cos \alpha}=\dfrac{3\sin \alpha\cos^2\alpha-\sin^3\alpha}{\cos^3\alpha-3\sin^2\alpha\cos \alpha}=\dfrac{3\tan \alpha-\tan^3\alpha}{1-3\tan^2\alpha}$

## 万能公式
> $\sin \alpha=\dfrac{2\tan \dfrac{\alpha}{2}}{\tan^2\dfrac{\alpha}{2}+1}$
> $\cos \alpha=\dfrac{1-\tan^2\dfrac{\alpha}{2}}{1+\tan^2\dfrac{\alpha}{2}}$
> $\tan \alpha=\dfrac{2\tan \dfrac{\alpha}{2}}{1-\tan^2\dfrac{\alpha}{2}}$

$\sin \alpha=2\sin\dfrac{\alpha}{2}\cos \dfrac{\alpha}{2}=\dfrac{2\sin \dfrac{\alpha}{2}\cos \dfrac{\alpha}{2}}{2\sin^2\dfrac{\alpha}{2}+\cos^2\dfrac{\alpha}{2}}=\dfrac{2\tan \dfrac{\alpha}{2}}{\tan^2\dfrac{\alpha}{2}+1}$

$\cos \alpha=\cos^2\dfrac{\alpha}{2}-\sin^2\dfrac{\alpha}{2}=\dfrac{\cos^2\dfrac{\alpha}{2}-\sin^2\dfrac{\alpha}{2}}{\sin^2\dfrac{\alpha}{2}+\cos^2\dfrac{\alpha}{2}}=\dfrac{1-\tan^2\dfrac{\alpha}{2}}{1+\tan^2\dfrac{\alpha}{2}}$

$\tan \alpha=\dfrac{2\tan \dfrac{\alpha}{2}}{1-\tan^2\dfrac{\alpha}{2}}$

## 类平方差公式
> $\sin^2 \alpha - \sin^2 \beta = \sin(\alpha + \beta) \sin(\alpha - \beta)$
> $\cos^2 \alpha - \cos^2 \beta = -\sin(\alpha + \beta) \sin(\alpha - \beta)$
> $\cos^2 \alpha - \sin^2 \beta = \cos(\alpha + \beta) \cos(\alpha - \beta)$


$\sin(\alpha + \beta) \sin(\alpha - \beta)=(\sin \alpha\cos \beta+\sin \beta\cos \alpha)(\sin \alpha\cos \beta-\sin \beta\cos \alpha)=\sin^2\alpha\cos^2\beta-\sin^2\beta\cos^2\alpha=\sin^2\alpha(1-\sin^2\beta)-\sin^2\beta(1-\sin^2\alpha)=\sin^2\alpha-\sin^2\alpha\sin^2\beta-\sin^2\beta+\sin^2\alpha\sin^2\beta=\sin^2 \alpha - \sin^2 \beta$

$-\sin(\alpha+\beta)\sin (\alpha-\beta)=-(\sin \alpha\cos \beta+\sin \beta\cos \alpha)(\sin \alpha\cos \beta-\sin \beta\cos \alpha)=-(\sin^2\alpha\cos^2\beta-\sin^2\beta\cos^2\alpha)=-[(1-\cos^2\alpha)\cos^2\beta-(1-\cos^2\beta)\cos^2\alpha]=-(\cos^2\beta-\cos^2\alpha\cos^2\beta-\cos^2\alpha+\cos^2\alpha\cos^2\beta)=-(\cos^2\beta-\cos^2\alpha)=\cos^2 \alpha - \cos^2 \beta$


$\cos(\alpha + \beta) \cos(\alpha - \beta)=(\cos \alpha\cos \beta-\sin \alpha\sin \beta)(\cos \alpha\cos \beta+\sin \alpha\sin \beta)=\cos^2\alpha\cos^2\beta-\sin^2\alpha\sin^2\beta=\cos^2\alpha(1-\sin^2\beta)-(1-\cos^2\alpha)\sin^2\beta=\cos^2\alpha-\cos^2\alpha\sin^2\beta-\sin^2\beta+\sin^2\beta\cos^2\alpha=\cos^2 \alpha - \sin^2 \beta$
# 重要结论
## 常见辅助角结论
> $\sin x \pm \cos x = \sqrt{2} \sin(x \pm \dfrac{\pi}{4})$
> $\cos x \pm \sin x = \sqrt{2} \cos(\alpha \mp \dfrac{\pi}{4})$
> $\sin x \pm \sqrt{3} \cos x = 2 \sin(x \pm \dfrac{\pi}{3})$
> $\cos x \pm \sqrt{3} \sin x = 2 \cos(x \mp \dfrac{\pi}{3})$

## 特殊三角函数
|$15^\circ$|$18^\circ$|$36^\circ$|
|:-|:-|:-|
|$\sin15^{\circ}=\dfrac{\sqrt{6}-\sqrt2}{4}$|$\sin18^{\circ}=\dfrac{\sqrt{5}-1}{4}$|$\sin36^{\circ}=\dfrac{\sqrt{10-2\sqrt{5}}}{4}$|
|$\cos15^{\circ}=\dfrac{\sqrt{6}+\sqrt{2}}{4}$|$\cos18^{\circ}=\dfrac{\sqrt{10+2\sqrt{5}}}{4}$|$\cos36^{\circ}=\dfrac{\sqrt5+1}{4}$|
|$\tan15^{\circ}=2-\sqrt{3}$|$\tan18^{\circ}=\dfrac{\sqrt{5}-1}{\sqrt{10+2\sqrt{5}}}$|$\tan36^{\circ}=\dfrac{\sqrt{10-2\sqrt{5}}}{\sqrt{5}+1}$|

## 三角形内常见结论
> $\sin A+\sin B+\sin C=4\cos \dfrac{A}{2}\cos \dfrac{B}{2}\cos \dfrac{C}{2}$
> $\tan A+\tan B+\tan C=\tan A\cdot\tan B\cdot\tan C$（斜三角形）



