> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)


# 题目
洛谷 [P1010 [NOIP1998 普及组] 幂次方](https://www.luogu.com.cn/problem/P1010)

>## [NOIP1998 普及组] 幂次方
>
>### 题目描述
>
>任何一个正整数都可以用 $2$ 的幂次方表示。例如 $137=2^7+2^3+2^0$。
>
>同时约定次方用括号来表示，即 $a^b$ 可表示为 $a(b)$。
>
>由此可知，$137$ 可表示为 $2(7)+2(3)+2(0)$
>
>进一步：
>
>$7= 2^2+2+2^0$  ( $2^1$ 用 $2$ 表示)，并且 $3=2+2^0$。
>
>所以最后 $137$ 可表示为 $2(2(2)+2+2(0))+2(2+2(0))+2(0)$。
>
>又如 $1315=2^{10} +2^8 +2^5 +2+1$
>
>所以 $1315$ 最后可表示为 $2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2(0))+2+2(0)$。
>
>### 输入格式
>
>一行一个正整数 $n$。
>
>### 输出格式
>
>符合约定的 $n$ 的 $0, 2$ 表示（在表示中不能有空格）。
>
>### 样例 #1
>
>#### 样例输入 #1
>
>```
>1315
>```
>
>#### 样例输出 #1
>
>```
>2(2(2+2(0))+2)+2(2(2+2(0)))+2(2(2)+2(0))+2+2(0)
>```
>
>### 提示
>
>**【数据范围】**
>
>对于 $100\%$ 的数据，$1 \le n \le 2\times {10}^4$。
>
>NOIP1998 普及组 第三题
>




# 想法
虽然题目确实写得很清楚了，但是可以梳理一下这个过程。一起理解一下题目吧。以$137$为例，有以下过程：
$137=2^7+2^3+2^0=2^{2^2+2+2^0}+2^3+2^0=2^{2^2+2+2^0}+2^{2+2^0}+2^0$。
所以嘛，数字$137$最后表示为了$2(2(2)+2+2(0))+2(2+2(0))+2(0)$。
像这样的题目，一定是会想到写一个递归函数来处理这样的问题，这是最重要的。当然，本题也考察了数字转化为二进制。

# 实现
1. 将数字转化为二进制。
2. 拆分二进制，找出二进制中$1$所在的位置。
3. 递归重复以上过程，直到将数字拆分得只剩下$2$和$0$。
4. 输出。

# 题解
## C++
```cpp
#include<bits/stdc++.h>
using namespace std;
string to_bin(int n){ //将十进制转换为2进制
    string digit = "01"; //位
    if(n == 0){
        return "";
    }
    return to_bin(n / 2) + digit[n % 2];
}

vector<int> getbits(int n){ //获取二进制中1所在的位置
    string m = to_bin(n); //获取二进制
    reverse(m.begin(),m.end()); //反转，方便一会儿的遍历
    vector<int> bits; //建列表
    for(int i = 0;i < m.size();i++){ //遍历
        if(m[i] == '1'){ //找到二进制中1的位置
            bits.push_back(i); //记录下来
        }
    }
    return bits; //返回
}

string split(int x){ //递归将数字拆分为只有2和0的形式
    vector<int> bits = getbits(x); //获取1所在的位置
    reverse(bits.begin(),bits.end()); //反转，低位先遍历，高位后遍历
    string str = ""; //记录
    for(int i = 0;i < bits.size();i++){
        str += '2'; //无论如何先整一个2上去
        if(bits[i] > 2){ //如果当前的位大于2
            str += '(' + split(bits[i]) + ')'; //那么需要拆
        }
        else if(bits[i] == 2){ //如果等于2
            str += "(2)"; //那就加个2
        }
        
        else if(bits[i] == 0){ //如果等于0
                str += "(0)"; //那就加个0
        }
        str += "+"; //记得放上加号
    }
    
    return str.substr(0,str.size() - 1); //因为在前面的处理中会导致字符串末尾有一个冗余的加号，所以需要去掉
}


int main(){
    int num;
    cin >> num; //输入
    cout << split(num); //输出
    return 0;
}
```
## Python
```py
num = int(input()) #输入
def to_bin(n): #将十进制转换为2进制
    digit = "01" #获取二进制
    if n == 0:
        return ""
    return to_bin(int(n / 2)) + digit[n % 2]

def getbits(n):
    m = to_bin(n)[::-1] #反转，方便一会儿的遍历
    bits = [] #建列表
    for i in range(len(m)): #遍历
        if m[i] == "1": #找到二进制中1的位置
            bits.append(i) #记录下来
    return bits #返回

def split(x): #递归将数字拆分为只有2和0的形式
    bits = getbits(x) #获取1所在的位置
    string  = "" #记录
    for i in reversed(bits): #反转，低位先遍历，高位后遍历
        string += "2" #无论如何先整一个2上去
        if i > 2: #如果当前的位大于2
            string += "(" + split(i) + ")" #那么需要拆
        elif i == 2: #如果等于2
            string += "(2)" #那就加个2
        elif i == 0: #如果等于0
            string += "(0)" #那就加个0
        string += "+" #记得放上加号
    return string[:-1] #因为在前面的处理中会导致字符串末尾有一个冗余的加号，所以需要去掉

print(split(num)) #输出
```


# 难度
难度：★★☆☆☆
大概是没什么难度吧。主要是二进制和递归。其它迎刃而解。

# 结尾
欢迎Hack我的代码！记得评论区域留言哦！我们下期再见(˵¯͒〰¯͒˵)


