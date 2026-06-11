> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 题目
洛谷 [P1093 [NOIP2007 普及组] 奖学金](https://www.luogu.com.cn/problem/P1093)
> ## [NOIP2007 普及组] 奖学金
>
> ### 题目背景
>
> NOIP2007 普及组 T1
>
> ### 题目描述
>
> 某小学最近得到了一笔赞助，打算拿出其中一部分为学习成绩优秀的前 $5$ 名学生发奖学金。期末， 每个学生都有 $3$ 门课的成绩：语文、数学、英语 。先按总分从高到低排序，如果两个同学总分相同，再按语文成绩从高到低排序，如果两个同学总分和语文成绩都相同，那么规定学号小的同学排在前面，这样，每个学生的排序是唯一确定的。
>
> 任务：先根据输入的 $3$ 门课的成绩计算总分， 然后按上述规则排序，最后按排名顺序输出前五名名学生的学号和总分。
>
> 注意，在前 $5$ 名同学中，每个人的奖学金都不 相同，因此，你必须严格按上述规则排序。例如，在某个正确答案中，如果前两行的输出数据（每行输出两个数：学号、总分) 是：
>
> ```plain
> 7 279
> 5 279
> ```
>
> 这两行数据的含义是：总分最高的两个同学的学号依次是 $7$ 号、$5$ 号。这两名同学的总分都是 $279$ (总分等于输入的语文、数学、英语三科成绩之 和) ，但学号为 $7$ 的学生语文成绩更高一些。
>
> 如果你的前两名的输出数据是：
>
> ```plain
> 5 279
> 7 279
> ```
>
> 则按输出错误处理，不能得分。
>
> ### 输入格式
>
> 共 $n+1$ 行。
>
> 第 $1$ 行为一个正整数 $n \le 300$，表示该校 参加评选的学生人数。
>
> 第 $2$ 到 $n+1$ 行，每行有 $3$ 个用空格隔开 的数字，每个数字都在 $0$ 到 $100$ 之间。第 $j$ 行的 $3$ 个数字依次表示学号为 $j-1$ 的学生的 语文、数学、英语的成绩。每个学生的学号按照输入顺序编号为 $1\sim n$（恰好是输入数据的行号减 $1$）。
>
> 保证所给的数据都是正确的，不必检验。
>
> ### 输出格式
>
> 共 $5$ 行，每行是两个用空格隔开的正整数，依 次表示前 $5$ 名学生的学号和总分。
>
> ### 样例 #1
>
> #### 样例输入 #1
>
> ```
> 6
> 90 67 80
> 87 66 91
> 78 89 91
> 88 99 77
> 67 89 64
> 78 89 98
> ```
>
> #### 样例输出 #1
>
> ```
> 6 265
> 4 264
> 3 258
> 2 244
> 1 237
> ```
>
> ### 样例 #2
>
> #### 样例输入 #2
>
> ```
> 8
> 80 89 89
> 88 98 78
> 90 67 80
> 87 66 91
> 78 89 91
> 88 99 77
> 67 89 64
> 78 89 98
> ```
>
> #### 样例输出 #2
>
> ```
> 8 265
> 2 264
> 6 264
> 1 258
> 5 258
> ```

# 想法

这道题吧，其实很简单，但是写起代码来挺复杂的。我的想法是，直接制作一个结构体，包含学号以及三科成绩，之后用`sort`对其进行排序。至于排序，我个人不太喜欢用`cmp`函数，而是更习惯重载运算符。

# 实现
1. 输入，将语数英三科成绩及学号写入结构体。
2. 排序。
3. 输出前5项。

# 题解
## C++
```cpp
#include<bits/stdc++.h>
using namespace std;
struct stu{ //结构体
	int score; //分数，第一关键字
	int chn; //语文分数，第二关键字
	int index; //学号，第三关键字
}; 
stu students[305];
bool operator < (stu a,stu b){ //重载运算符
	if(a.score != b.score){ //先看总分
		return a.score > b.score;
	}
	else if(a.chn != b.chn){ //再看语文
		return a.chn > b.chn;
	}
	return a.index < b.index; //最后看学号
}
int main(){
	int n;
	cin >> n;
	for(int i = 0;i < n;i++){
		int chn,math,eng;
		cin >> chn >> math >> eng;
		students[i].score = chn + math + eng; 总分
		students[i].chn = chn; //语文
		students[i].index = i + 1; //学号从1开始，i从0开始，所以+1
	}
	sort(students,students + n); //排序
	for(int i = 0;i < 5;i++){ //输出前5
		cout << students[i].index << ' ' << students[i].score << "\n";
	}
	return 0;
}
```

## Python
```py
class stu: #结构体
    score = 0 #分数，第一关键字
    chn = 0 #语文分数，第二关键字
    index = 0 #学号，第三关键字
    def __gt__(self,other): #重载运算符
        if self.score != other.score: #先看总分
            return self.score < other.score
        elif self.chn != other.chn: #再看语文
            return self.chn < other.chn
        return self.index > other.index #最后看学号

n = int(input())

students = []
for i in range(n):
    chn,math,eng = input().split()
    chn = int(chn)
    math = int(math)
    eng = int(eng)
    student = stu()
    student.score = chn + math + eng #总分
    student.chn = chn #语文
    student.index = i + 1 #学号从1开始，i从0开始，所以+1
    students.append(student)
students.sort() #排序
    
for i in range(5): #输出前5
    print(students[i].index,students[i].score)
```

# 难度
难度：★☆☆☆☆
这道题难度较低，就是写起来比较繁琐。这种题推荐用结构体，因为它可以捆绑几个数据在一起，还可以重载运算符，方便的很啊。

# 结尾
这道题你是怎么AC的？欢迎在评论区讨论！

