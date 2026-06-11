@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 斐波那契数列
## 常规算法
```py
n = int(input()) #输入
last = 1 #上一个数
this = 1 #当前数字
if n == 1 or n == 2: #如果是第一项或第二项
    print(1) #那就是1
else:
    for i in range(n - 2): #一直算到第n项
        now = this + last #新的数字即为倒数第一个数字加倒数第二个数字
        last = this #产生了新的数字，所以倒数第一个数变成了倒数第二个
        this = now #当前数变成倒输第一个数
    print(this) #输出结果
```
## 递推法
```py
fib = [1,1] #第一、二项
n = int(input()) #输入
if n > 2:
    for i in range(n - 2): #一直算到第n项
        fib += [fib[-1] + fib[-2]] #新的数字即为倒数第一个数字加倒数第二个数字，将新的数字放到列表中
print(fib[-1]) #列表中倒数第一个数字即为结果
```
## 递归法
```py
def fib(n): #递归函数
    if n == 1 or n == 2: #第一、二项
        return 1 #那就是1
    return fib(n - 1) + fib(n - 2) #递归，新的数字即为倒数第一个数字加倒数第二个数字
print(fib(int(input()))) #输入，计算，输出
```
# 判断质数
## 常规算法
```py
result = True #预处理，当前数有可能为质数
n = int(input()) #输入
if n == 0 or n == 1: #特判0和1不是质数
    print("no") #输出
for i in range(2,int(n ** 0.5) + 1): #从2一直试到根号n，看看有没有它的因数
    if n % i == 0: #如果找到了因数
        result = False #那么不是质数
        break #不用继续找因数了
if result == True: #是质数
    print("yes") #输出
else: #不是质数
    print("no") #输出
```
## 埃氏筛法
```py
n = int(input()) #输入
l = list(range(n + 1)) #创建列表l：[1,2,3,4,...,n]
result = True #预处理，当前数有可能为质数
pointer = 2 #先处理2的所以倍数
while pointer != n: #如果指针没有指向当前数
    for i in range(pointer * 2,n + 1,pointer): #处理质数的倍数
        l[i] = 0 #质数的倍数不是质数，所以把它清掉
    if l[n] == 0: #如果当前数被清掉了
        result = False #那它就不是质数
        break #不用继续算下去了
    pointer += 1 #如果当前数没有被清掉，那它有可能就是质数，也有可能它是合数但还不是处理过的质数的倍数，所以没有被清掉，故处理下一个质数
    while l[pointer] == 0: #被清掉的数不是质数
        pointer += 1 #找到下一个质数
if result: #是质数
    print("yes") #输出
else: #不是质数
    print("No") #输出
```
# 最大公因数
## 常规算法
```py
a,b = map(int,input().split()) #输入，转换为整数，保存到变量中
n = 1 #最大公因数暂定为1
for i in range(1,min([a,b]) + 1): #一直算到a、b中较小的那个
    if a % i == 0 and b % i == 0: #找到两个数的公因数
        n = i #更新公因数
print(n) #输出
```
## 辗转相除法
```py
def gcd(a,b): #递归函数
    if b > 0:
        return gcd(b,a % b) #递归
    else:
        return a #返回a
a,b = map(int,input().split()) #输入，转换为整数，保存到变量中
print(gcd(a,b))#计算，输出
```
# 三条边求三角形面积
## 海伦公式
```py
a,b,c = map(int,input().split()) #三角形三条边长
p = (a + b + c) / 2 #三条边长的一半
print((p * (p - a) * (p - b) * (p - c)) ** 0.5) #套公式
```
# 阶乘
## 常规算法
```py
a = int(input()) #输入
result = 1 #结果
for i in range(1,a + 1): #一个个往上乘
    result *= i #乘
print(result) #输出
```
## 递归法
```py
def fact(n): #递归函数
    if n == 1: #处理的数是1
        return 1 #1! = 1
    else: #处理的数大于1
        return fact(n - 1) * n #n * (n - 1)!
print(fact(int(input()))) #输入，计算，输出
```

# 结尾
好了，分享就到这里了，记得点赞收藏哦！

