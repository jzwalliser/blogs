@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)


集合乃高中知识，但是对于搞信息竞赛的同学们可能来不及上高中就需要透彻了解集合了。所以这一章介绍一下集合。
# 什么是集合
一般地，一定范围内某些确定的、不同的对象的全体组成一个集合。集合中的对象称为该集合的元素。
# 集合

## 表示方法
一般用大写字母代表集合，小写字母代表元素，如：$A=\{a,b,c\}$
列举法：将集合中的元素一一列举，并放在花括好内，如$\{1,2,3,4,5\}$。 
描述法：将满足一定条件的关系表示出来，如$\{x|x^2-1=0,x\in \mathbb R\}$表示方程$x^2-1=0$所有实数根的集合，即$\{1,-1\}$。
## 性质
确定性：元素是否属与某个集合，必须有明确的判断标准。
互异性：集合中的元素互不相同，即没有重复的元素。
无序性：两个集合是否相等，与其中元素的顺序无关。只要它们之中的元素一致，两个集合就相等。如：$\{a,b,c\}=\{b,c,a\}$

## 元素个数
有限集：元素个数有限的集合叫作有限集，如$\{1,2,3\}$。
无限集：元素个数无限的集合叫作无限集，如$\mathbb N$、$\{x|x<3\}$。
空集：没有任何元素在内的集合是空集，用符号$\varnothing$来表示。

## 常用数集
|符号|内容|
|:-|:-|
|$\varnothing$|空集|
|$\mathbb N$|自然数集|
|$\mathbb N_+$|正整数集|
|$\mathbb Z$|整数集|
|$\mathbb Q$|有理数集|
|$\mathbb Q_+$|正有理数集|
|$\mathbb R$|实数集|
|$\mathbb R_+$|正实数集|
|$\mathbb C$|复数集|

![请添加图片描述](https://i-blog.csdnimg.cn/direct/ab03b8f3c8c74e2ab904fdbae255a8cd.png)

# 关系
## 元素和集合之间
如果$a$是$A$的元素，则记$a\in A$，否则记为$a\notin A$或$a\overline\in A$（这种表示不太常用）。注意，$\in$和$\notin$表示的是元素与集合间的关系，而非集合之间的关系。

## 集合和集合之间
如果集合$A$的任意一个元素都是集合$B$的元素（若$a\in A$，则$a\in B$），那么集合$A$称为集合$B$的子集，记为$A\subseteq B$或$B\supseteq A$。任何一个集合都是它本身的子集，即$A\subseteq A$。空集是任何集合的子集。

如果$A\subseteq B$且$A\neq B$，那么集合$A$称为集合$B$的真子集，记为$A\subsetneqq B$或$B\supsetneqq A$。如$\{a\}\subsetneqq\{a,b\}$。对于任何$A$，$B$，$C$，若$A\subseteq B,B\subseteq C$则$A\subseteq C$。

含有$n$个元素的集合的子集有$2^n$个（包括自己和$\varnothing$），真子集有$(2^n-1)$个，非空子集$(2^n-1)$个，非空真子集$(2^n-2)$个。即：

|项目|个数|
|:-|:-|
|集合A元素个数|$n$|
|子集个数|$2^n$|
|真子集个数|$2^n-1$|
|非空子集个数|$2^n-1$|
|非空真子集个数|$2^n-2$|



## 集合之间的运算
### 补集
设$A\subseteq U$，由$U$中不属于$A$的所有元素组成的集合称为$U$的子集$A$的补集，记为$∁_UA$。$∁_UA=\{x|x\in U,x\notin A\}$。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/aa00dcbb054e4b08b45a9ad02deb8e25.png)
### 交集
同时属于集合A和集合B的元素所组成的集合，称为集合$A$和集合$B$的交集，记为$A\cap B$。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/0f1590d3fcdf43e6a9dec78f83802807.png)


### 并集
属于集合A和集合B的所有元素所组成的集合，称为集合$A$和集合$B$的并集，记为$A\cup B$。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/7eeac1802afc4a489352d4f17abe0a98.png)
### 巧记
交集（$\cap$）：两个集合所共有元素组成的集合。
并集（$\cup$）：两个集合所有的元素组成的集合。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/b75abafed1484acba5c0073a6a223aa4.png)
### 结论
#### 交集
|$A\cap A=A$|$A\cap\varnothing=\varnothing$|
|:-|:-|
|$A\cap B\subseteq A$|$A\cap B\subseteq B$|
#### 并集
|$A\cup A=A$| $A\cup\varnothing=A$|
|:-|:-|
|$A\cup B\supseteq A$|$A\cup B\supseteq B$|

#### 德·摩根公式
|$C_U(A\cap B)=(C_UA)\cup(C_UB)$|
|:-|
|$C_U(A\cup B)=(C_UA)\cap(C_UB)$|





# 区间表示集合
一些特殊的集合也可以记为区间的形式。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/5937ec4cba1c4d4788db2783013d1511.png)

---

# 总结
上面就是有关集合的知识啦。
记得一键三连哦！






