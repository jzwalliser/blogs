@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)


# 前言
前面为了安装Wine QQ，所以在Zorin OS（Linux发行版，基于Ubuntu 20）上开启了i386（就是32位）架构，以支持32位应用的运行。但后来，我发现软件不能正常安装及卸载了。解铃还须系铃人，既然是开启了i386架构所致，那么我们就把它给关了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5f93211ccf251727d987aa9e5af9b278.png#pic_center)

# 开启和关闭i386
## 开启i386
一行命令即可开启对i386的支持。在终端中输入：`sudo dpkg --add-architecture i386`即可。
## 关闭i386
当你想关掉i386，你会发现根本不行。输入`sudo dpkg --remove-architecture i386`后，终端提示：`dpkg: 错误: 无法移除体系结构 i386 ，当前它仍被数据库使用`。
### 卸载所有32位应用
为什么会说“仍被数据库使用”呢？因为系统中安装了32位应用，正是它们阻止了对i386的关闭。所以，需要卸载所有32位应用。输入命令：
```bash
$ sudo apt-get remove --purge `dpkg --get-selections | awk '/i386/{print $1}'`
```
这时候，如果在终端内出现大量的“正在卸载”字样后，那就恭喜！最后再输入一行命令：
```bash
$ sudo dpkg --remove-architecture i386
```
然后就大功告成啦！

### 软件包之间的循环依赖
但是，有的时候会出现一个恶心的情况：软件包之间相互依赖。软件A依赖B，B又依赖C，C又依赖A，于是，根本无法卸载软件。这时候，我们就要强制卸载软件以破坏依赖链，然后就可以按照上面的步骤正常卸载了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1e2da4e99cecb26df60cd6f081f21437.png#pic_center)
对于因依赖关系而无法卸载的软件包，我们使用dpkg卸载。这里以卸载“deepin-wine-helper”为例：
```bash
$ sudo dpkg --purge --force-all deepin-wine-helper
```
```
dpkg: deepin-wine-helper:i386：有依赖问题，但是如您所愿，将继续卸载：
 spark-dwine-helper 依赖于 deepin-wine-helper (>= 5.1).

(正在读取数据库 ... 系统当前共安装有 360652 个文件和目录。)
正在卸载 deepin-wine-helper:i386 (5.1.43-1) ...
正在清除 deepin-wine-helper:i386 (5.1.43-1) 的配置文件 ...
正在处理用于 libc-bin (2.31-0ubuntu9.9) 的触发器 ...
/sbin/ldconfig.real: File /lib/libactivation.so is empty, not checked.
```
按照这个方法，把所有因依赖关系而无法正常卸载的软件包全部强制卸载，最后再来两行命令：
```bash
$ sudo apt-get remove --purge `dpkg --get-selections | awk '/i386/{print $1}'`
$ sudo dpkg --remove-architecture i386
```
然后，就OK啦！软件更新器又可以正常使用啦。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a95f03601ea1f501924a0d1665ee768d.png#pic_center)

---
# 总结
以上就是关闭i386的步骤啦。一起来复习一下：
```bash
#如果有循环依赖，则使用dpkg --purge --force-all <软件包> 来卸载它。
$ sudo dpkg --purge --force-all deepin-wine-helper
#卸载所有32位应用
$ sudo apt-get remove --purge `dpkg --get-selections | awk '/i386/{print $1}'`
#最后关闭i386架构
$ sudo dpkg --remove-architecture i386
```
您的点赞是我最大的动力！


