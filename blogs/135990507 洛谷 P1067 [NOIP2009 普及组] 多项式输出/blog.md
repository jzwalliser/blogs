> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 题目
洛谷 [P1067 [NOIP2009 普及组] 多项式输出](https://www.luogu.com.cn/problem/P1067)


># [NOIP2009 普及组] 多项式输出
>
>## 题目描述
>
>一元 $n$ 次多项式可用如下的表达式表示：
>
>$$f(x)=a_nx^n+a_{n-1}x^{n-1}+\cdots +a_1x+a_0,a_n\ne 0$$
>
>其中，$a_ix^i$ 称为 $i$ 次项，$a_i$ 称为 $i$ 次项的系数。给出一个一元多项式各项的次数和系数，请按照如下规定的格式要求输出该多项式：
>
>1. 多项式中自变量为 $x$，从左到右按照次数递减顺序给出多项式。
>
>2. 多项式中只包含系数不为 $0$ 的项。
>
>3. 如果多项式 $n$ 次项系数为正，则多项式开头不出 `+` 号，如果多项式 $n$ 次项系数为负，则多项式以 `-` 号开头。
>
>4. 对于不是最高次的项，以 `+` 号或者 `-` 号连接此项与前一项，分别表示此项系数为正或者系数为负。紧跟一个正整数，表示此项系数的绝对值（如果一个高于 $0$ 次的项，其系数的绝对值为 $1$，则无需输出 $1$）。如果 $x$ 的指数大于 $1$，则接下来紧跟的指数部分的形式为“$x^b$”，其中 $b$ 为 $x$ 的指数；如果 $x$ 的指数为 $1$，则接下来紧跟的指数部分形式为 $x$；如果 $x$ 的指数为 $0$，则仅需输出系数即可。
>
>5. 多项式中，多项式的开头、结尾不含多余的空格。
>
>## 输入格式
>
>输入共有 $2$ 行
>
>第一行 $1$ 个整数，$n$，表示一元多项式的次数。
>
>第二行有 $n+1$ 个整数，其中第 $i$ 个整数表示第 $n-i+1$ 次项的系数，每两个整数之间用空格隔开。
>
>## 输出格式
>
>输出共 $1$ 行，按题目所述格式输出多项式。
>
>## 样例 #1
>
>### 样例输入 #1
>
>```
>5 
>100 -1 1 -3 0 10
>```
>
>### 样例输出 #1
>
>```
>100x^5-x^4+x^3-3x^2+10
>```
>
>## 样例 #2
>
>### 样例输入 #2
>
>```
>3 
>-50 0 0 1
>```
>
>### 样例输出 #2
>
>```
>-50x^3+1
>```
>
>## 提示
>
>NOIP 2009 普及组 第一题
>
>对于100%数据，$0 < n < 100$，$-100 <$ 系数$< 100$
>
>---
>
>$\text{upd 2022.8.1}$：新增加一组 Hack 数据。
# 想法
先处理带有$x$的多次项，最后再单独处理一次项和常数项。对于每一项，都判断其是否是正数，如果是就加上正号，否则就是负号。特殊地，如果是$0$那就略过这一项。最后为了防止被hack，需要考虑一些特殊情况，如只有常数项。

# 实现
1. 输入时候注意多一项。
2. 处理带有$x$的项。
3. 处理字符串，删除多余内容。
4. 加上一次项和常数项。
5. 输出。

# 题解
## C++
```cpp
#include<bits/stdc++.h>
using namespace std;

string str = "";
int nums[105];
string to_str(long long int num){
	stringstream ss; //创建stringstream流
	string str;
	ss << num; //num流入stringstream
	ss >> str; //stringstream流入str
	return str;
}

int main(){
    int n;
    cin >> n; //输入
    for(int i = 0;i <= n;i++){ //注意输入的时候会多一项
        cin >> nums[i];
    }
    if(n == 0){ //如果只有常数项
    	cout << nums[0]; //输出
    	return 0; //退出
    }
	for(int i = 0;i < n;i++){
	    if(nums[i] == 1){
	    	str += "+x^" + to_str(n - i); //系数为1则不需要输出1
	    }
	    else if(nums[i] == -1){
	        str += "-x^" + to_str(n - i); //同样，系数为-1则不需要输出-1
	    }
	    else if(nums[i] == 0){
	        //如果系数为0则跳过这一项
	    }
    	else{
		    if(nums[i] > 0){ //如果是正数那就需要放个加号
		    	str += "+";
	    	}
	        str += to_str(nums[i]) + "x^" + to_str(n-i); //最后加上次数
	    }
    }

    if(str[str.size() - 1] == '1'){ //单独处理一次项，那就删掉字符串末尾的“^1”
    	str = str.substr(0,str.size() - 2);
    }
    if(str[0] == '+'){ //如果头上是加号那就删掉第一个字符（因为刚开始在处理多次项的时候所有正数都会在前面家正号）
    	str = str.substr(1,str.size() - 1);
    }
    if(nums[n] > 0){ //正常数
    	str += "+" + to_str(nums[n]);
    }
    else if(nums[n] < 0){ //负常数
    	str += to_str(nums[n]);
    }
    cout << str; //输出
    return 0;
}

```
## Python
```py
import sys
n = int(input()) #输入
string = ""
nums = input().split()
if n == 0: #如果只有常数项
	print(nums[0]) #输出
	sys.exit() #退出
	
for i in range(len(nums)):
	nums[i] = int(nums[i])

for i in range(n):
	if nums[i] == 1:
		string += "+x^" + str(n - i) #系数为1则不需要输出1
	elif nums[i] == -1:
		string += "-x^" + str(n - i) #同样，系数为-1则不需要输出-1
	elif nums[i] == 0:
		pass #如果系数为0则跳过这一项
	else:
		if nums[i] > 0: #如果是正数那就需要放个加号
			string += "+"
		string += str(nums[i]) + "x^" + str(n-i) #最后加上次数
		
if string[-1] == "1": #单独处理一次项，那就删掉字符串末尾的“^1”
	string = string[:-2]
if string[0] == "+": #如果头上是加号那就删掉第一个字符（因为刚开始在处理多次项的时候所有正数都会在前面家正号）
	string = string[1:]
if int(nums[-1]) > 0: #正常数
	string += "+" + str(nums[-1])
elif int(nums[-1]) < 0: #负常数
	string += str(nums[-1])
print(string) #输出
```

# 难度
难度：★★☆☆☆
题目还是比较容易的，只是里面的操作比较复杂，情况有许多种，需要考虑周到，并写大量的if语句。

# 结尾
你是怎么想的？欢迎分享您的想法，我们下期再见~~(˵¯͒〰¯͒˵)





