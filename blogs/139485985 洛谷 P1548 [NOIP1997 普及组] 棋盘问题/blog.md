> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 题目

洛谷 [P1548 [NOIP1997 普及组] 棋盘问题](https://www.luogu.com.cn/problem/P1548)
> ## [NOIP1997 普及组] 棋盘问题
>
> ### 题目背景
>
> NOIP1997 普及组第一题
>
> ### 题目描述
>
> 设有一个 $N \times M$ 方格的棋盘 $(1≤N≤100,1≤M≤100)$
>
> 求出该棋盘中包含有多少个正方形、多少个长方形（不包括正方形）。
>
> 例如：当 $N=2, M=3$ 时：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/1b0781e56f18d2df8051093021c497a5.png)
>
>
> 正方形的个数有 $8$ 个：即边长为 $1$ 的正方形有 $6$ 个；边长为 $2$ 的正方形有 $2$ 个。
>
> 长方形的个数有 $10$ 个：
>
> 即
>
> - $2 \times 1$ 的长方形有 $4$ 个：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/572486a32a876600b834ffc31c600dd0.png)
>
> - $1 \times 2$ 的长方形有 $3$ 个：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/038104f04b4d2f22f8f102946ec73271.png)
>
> - $3 \times 1$ 的长方形有 $2$ 个：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/53a27698e21eeadad186cf42e2a0a641.png)
>
> - $3 \times 2$ 的长方形有 $1$ 个：
>
> ![](https://i-blog.csdnimg.cn/blog_migrate/eee4e05bb8f83a20b9389aadd22c7b48.png)
>
> ### 输入格式
>
> 一行两个整数 $N,M$。
>
> ### 输出格式
>
> 一行两个整数，表示正方形的个数与长方形的个数。
>
> ### 样例 #1
>
> #### 样例输入 #1
>
> ```
> 2 3
> ```
>
> #### 样例输出 #1
>
> ```
> 8 10
> ```
# 想法

这道题，可以先数正方形和长方形一共有多少个，再单独数正方形有多少个，最后相减即可算出长方形个数。
第一步：数正方形、长方形总数。我们以$3\times4$棋盘为例：
先看左上角，即第一行第一个点（图片中用圆圈标出），它连接右下方任意格点（用叉标出）即可形成一个正方形或长方形。一共$3\times4=12$个选择。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/5b88821810d6458c9e8a8290a408f524.png)

再处理第二个点，一共$2\times4=8$个选择。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/c74e0c91c6444a1196e96342887af5d2.png)



第3个点，一共$1\times4=4$个选择。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/8fed9a0991ae4ac49982cbf156fec9dc.png)
对于第一行第四个点来说，有$0\times4=0$个选择。
到了第二行第一个点，共$3\times3=9$个选择。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/7f9a189040f64a4983226fca11b8c3f9.png)

第二个点，$3\times2=6$个选择。
![请添加图片描述](https://i-blog.csdnimg.cn/direct/ff821dcdb96c4a52a5076b3aa1be683e.png)

后面就不一一列举了。


所以，有$3\times4+2\times4+1\times4+3\times3+2\times3+1\times3+3\times2+2\times2+1\times2+3\times1+2\times1+1\times1=60$个正方形和长方形。
由特殊到一般，对于大小为$x\times y$的棋盘，正方形与长方形共有：

$$
\begin{aligned}
&t=xy+x(y-1)+x(y-2)+\cdots+x\times1+(x-1)y+(x-1)(y-1)+\cdots+(x-1)\times1+\cdots+1\times1
\\&=[x+(x-1)+(x-2)+\cdots+1][y+(y-1)+(y-2)+\cdots+1]
\\&=\frac{x(x+1)}{2}\times\frac{y(y+1)}{2}
\\&=\frac{xy(x+1)(y+1)}{4}
\end{aligned}
$$

OK，现在只数正方形。还是以$3\times4$棋盘为例：
先是最小的$1\times1$正方形：共$3\times4$个。
再是$2\times2$正方形，共$2\times3=6$个。
$3\times3$正方形：$1\times2=2$
由于的棋盘最短边为$3$，所以不可能再有$4\times4$正方形。因此最大正方形的边长取决于棋盘最短边。
综上，共$3\times4+2\times3+1\times2=20$个正方形。再由特殊推广到一般，对于大小为$x\times y$的棋盘：令$k=min\{x,y\}$，其中$min\{x,y\}$代表取$x,y$中的最小值。
正方形的个数为：
$$
\begin{aligned}
&s=xy+(x-1)(y-1)+(x-2)(y-2)+\cdots+(x-k)(y-k)\\
&=xy+xy-x-y+1^2+xy-2x-2y+2^2+\cdots+xy-kx-ky+k^2\\
&=(k+1)xy-(1+2+\cdots+k)(x+y)+(1^2+2^2+3^2+\cdots+k^2)\\
&=(k+1)xy-\frac{k(k+1)}{2}(x+y)+\sum^k_{i=1}i^2\\
&=(k+1)xy-\frac{k(k+1)(x+y)}{2}+\frac{k(k+1)(2k+1)}{6}
\end{aligned}
$$

# 实现
1. 输入。
2. 根据刚才的公式直接代数据。
3. 输出。

# 题解
## C++

```cpp
#include<iostream>
using namespace std;
int main(){
	int x,y;
	cin >> x >> y; //输入
	int k = min(x,y); //套公式
	int s = (k + 1) * x * y - k * (k + 1) * (x + y) / 2 + k * (k + 1) * (2 * k + 1) / 6; //正方形
	int t = (x + 1) * (y + 1) * x * y / 4; //正方形与长方形总数
	cout << s << ' ' << t - s; //输出
	return 0;
}
```

## Python
```py
x,y = input().split()
x = int(x)
y = int(y)
k = min(x,y)
s = (k + 1) * x * y - k * (k + 1) * (x + y) / 2 + k * (k + 1) * (2 * k + 1) / 6 #正方形
t = (x + 1) * (y + 1) * x * y / 4 #正方形与长方形总数
print(int(s),int(t - s)) #输出
```

# 难度

难度：★★☆☆☆
这道题还是有点难的，虽然放在第一题，但要想写出一个完美的程序还是需要推出公式，说白了这就是道数学题。等到公式推出来了，甚至连判断、循环语句都不需要了，代码简洁得很啊。
# 结尾

这道题你是怎么AC的？欢迎讨论哦！我们下期再见~

