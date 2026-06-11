@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 前言
学完Python后再学C++，会有一种神奇的感觉，因为许多Python的内置函数用的很方便，但C++都没有，需要自己写，如整数和字符串的转换。这篇文章中，就一起看看常用函数的写法吧！

# 类型转换
## string 转 int
网上有许多int和string互转的方法，但在我看来都挺繁琐。使用stringstream其实最方便。
```cpp
#include<sstream> //必须导入sstream或bits/stdc++库
int to_int(string str){
	stringstream ss; //创建stringstream流
	int num;
	ss << str; //str流入stringstream
	ss >> num; //stringstream流入num
	return num;
}
```
## int 转 string
```cpp
#include<sstream> //必须导入sstream或bits/stdc++库
string to_str(long long int num){
	stringstream ss; //创建stringstream流
	string str;
	ss << num; //num流入stringstream
	ss >> str; //stringstream流入str
	return str;
}
```
# 进制转换
## 10进制转n进制（$2\leq n\leq 16,n\in \mathbb Z$）
用于将10进制的数转换位n进制。
```cpp
string dec_to_m(int n,int m){ //十进制数n转m进制
	string digit = "0123456789ABCDEF"; //位数
	if(n == 0){ //如果除完了
		return "";
	}
	
	return dec_to_m(n / m,m) + digit[n % m]; //依次相除并添加位数
}
```
## n进制转10进制（$2\leq n\leq 16,n\in \mathbb Z$）
用于将n进制的数转换为10进制。
```cpp
long long int n_to_dec(string m,int base){ //base进制的数字m
	reverse(m.begin(),m.end()); //将数字反转过来，方便遍历
	long long int ans = 0; //十进制的数
	for(int i = 0;i < m.size();i++){ //遍历每一位
		int digit; //当前位
		if('0' <= m[i] and m[i] <= '9'){ //将字符转换为整数
			digit = m[i] - '0';
		}
		else if('A' <= m[i] and m[i] <= 'Z'){ //如果是16进制则需要处理字母
			digit = m[i] - 'A' + 10;
		}
		else if('a' <= m[i] and m[i] <= 'z'){ //如果是16进制则需要处理字母
			digit = m[i] - 'a' + 10;
		}
		ans += pow(base,i) * digit; //依次累加
	}
	return ans;
}
```

# 数学
## lowbit
利用二进制的特性，可以将数字的二进制表示法最末尾的$1$取出来。
```cpp
int lowbit(int num){
	return num & (-num);
}
```

## Miller-Rabin 判断素数
```cpp
bool prime(long long int n){
	if(n <= 1){ //如果是1或0则不是素数
		return false;
	}
	
	for(long long int i = 2;i <= sqrt(n);i++){ //从2开始枚举到sqrt(n)
		if(n % i == 0){ //如果里面有n的因数则n不是素数
			return false; //可以结束函数的运行了
		}
	}
	return true; //是素数
}
```

## 快速幂
```cpp
long long int fastpow(int a,int n){
	long long int ans = 1;
	while(n){
		if(n & 1){ //当前位需要乘
			ans *= a;
		}
		a *= a; //平方
		n = n >> 1; //将n右移一位
	}
	return ans;
}
```

## 最大公约数
```cpp
int gcd(int a,int b){
	if(b){
		return gcd(b,a % b);
	}
	return a;
}
```

## 最小公倍数
```cpp
int gcd(int a,int b){
	if(b){
		return gcd(b,a % b);
	}
	return a;
}

int lcm(int a,int b){
	return a * b / gcd(a,b);
}
```

# 其它算法
## 并查集
```cpp
const int N = 10005;
int s[N];
void init(){ //初始化
	for(int i = 1;i <= N;i++){
		s[i] = i;
	}
}
int find(int x){ //查找
	if(x != s[x]){
		s[x] = find(s[x]); //路径压缩
	}
	return s[x];
}

void merge(int x,int y){
	x = find(x);
	y = find(y);
	if(x != y){
		s[x] = s[y];
	}
}
```

# 结尾
以上就是几个常用的C++模板了，也许在哪里会用到呢。
大家还想要什么模板呢？评论区见~
给个赞再走哦~

