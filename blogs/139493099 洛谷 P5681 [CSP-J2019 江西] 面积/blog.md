> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 题目
洛谷 [P5681 [CSP-J2019 江西] 面积](https://www.luogu.com.cn/problem/P5681)
> ## [CSP-J2019 江西] 面积
>
> ### 题目描述
>
> Alice 有一个边长为 $a$ 的正方形，Bob 有一个 长宽分别为 $b,c$ 的矩形，请你告诉他们俩谁的图 形面积更大。
>
> ### 输入格式
>
> 仅一行三个正整数 $a,b,c$
>
> ### 输出格式
>
> 输出仅一行一个字符串，若正方形面积大则输出 `Alice`，否则输出 `Bob`。
>
> ### 样例 #1
>
> #### 样例输入 #1
>
> ```
> 5 4 6
> ```
>
> #### 样例输出 #1
>
> ```
> Alice
> ```
>
> ### 样例 #2
>
> #### 样例输入 #2
>
> ```
> 7 5 10
> ```
>
> #### 样例输出 #2
>
> ```
> Bob
> ```
>
> ### 提示
>
> 【数据范围】
> 对于 $30\%$ 的数据，$1 \le a,b,c \le 100$，$b=c$；
> 对于 $80\%$ 的数据，$1\le a,b,c \le 10^4$； 
> 对于 $100\%$ 的数据，$1\le a,b,c \le 10^9$。
>
> 【样例 $1$ 解释】
> 正方形面积为  $25$，矩形面积为 $24$。
>
> 【样例 $2$ 解释】
> 正方形面积为  $49$，矩形面积为 $50$。

# 想法
这道题很容易，直接输入然后计算面积，输出即可。但是注意数据范围，所以最好用`long long int`，以防数据溢出。

# 实现
1. 输入$a,b,c$
2. 比较$a\times a$和$b\times c$。
3. 输出。

# 题解
## C++
```cpp
#include<bits/stdc++.h>
using namespace std;
int main(){
	long long int a,b,c;
	cin >> a >> b >> c; //输入
	if(a * a > b * c){ //比较面积
		cout << "Alice";
	}
	else{
		cout << "Bob";
	}
	return 0;
}
```

## Python
```py
a,b,c = input().split() //输入
a = int(a)
b = int(b)
c = int(c)
if a * a > b * c: //比较面积
	print("Alice")
else:
	print("Bob")
```

# 难度

难度：★☆☆☆☆
这道题其实不是很难，不过注意数字太大了可能会溢出。
# 结尾

这道题你是怎么AC的？欢迎评论区讨论！

