@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 前言
最近无聊，准备安装一个Linux系统。于是，我选中了一个使用已久的系统——[Zorin OS](https://zorin.com/os/)。安装过程并非一帆风顺，甚至有惊有险啊！想安装Ubuntu的同学也可以参考一下，过程大同小异。


# Zorin OS 介绍
这次我安装的是Zorin OS 16。这个OS很好看，是Linux 的一个发行版，基于Ubuntu 20.04.3 LTS。有兴趣的同学可以上网百度一下哈。这里有它的官网：[Zorin OS](https://zorin.com/os/)，文章结尾我也会提供下载链接。![](https://i-blog.csdnimg.cn/blog_migrate/152d71079b5c5ea78b6612239dbab8f9.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/093e53945b5ec7e24f6a830f1f06a35d.png#pic_center)
# 准备工具
## 硬件（自己准备）
1. 一台电脑（需要预装Windows）
2. 一块U盘
## 软件（我会在文末提供链接）
3. UltraISO
4. Zorin OS 镜像（iso）
# 安装

## 1. 磁盘分区
安装前一定要记得给磁盘做分区，而不是在安装系统的过程中让安装器自动分区，否则很可能会丢失数据啊！还有，一定要备份重要文件！谁知道在安装过程中会出现什么意外呢。
## 2. 关闭Secure Boot（可选）
大部分电脑，默认是打开Secure Boot的。但是Secure Boot 只允许进入Windows或者配置了Secure boot 的 OS，所以有可能无法进入Zorin OS。怎么办呢？那就把它关了吧。管理员权限运行cmd，输入`shutdown /r /fw /t 0`，电脑重启到BIOS设置页面。选中secure boot，将enabled改为disabled。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/aca3cae8ac898c1fd35632906d5781c5.png)


## 3. 关闭RST
RST是Intel开发的一个功能，全名叫做“Rapid Storage Technology”，它可以使系统运行得更快，但是除Windows外的大部分系统不支持。所以，需要关闭它才能正常引导Zorin OS。详细操作可以看看这里：[关闭 Intel RST 以及导致的蓝屏修复方法](https://blog.csdn.net/jzwalliser/article/details/128344846)。

## 4. 下载&写U盘
在官网上下载 ISO 镜像文件，并将其写入U盘。需要准备一个至少4GB的U盘。此处步骤省略，可以看看这篇文章：[使用 UltraISO 将系统写入U盘](https://blog.csdn.net/jzwalliser/article/details/128381214)。

## 5. U盘加载系统
接着，将电脑关机。我的笔记本电脑是Lenovo XiaoXin Air 14 2019。U盘插入电脑，然后开机，疯狂地摁<kbd>F12</kbd>键（每个电脑的键位是不一样的，我的电脑是F12），选择Linpus Lite（就是我的U盘），回车键进入后，选中“Try or install Zorin OS”（第一个选项），即可进入系统。

## 6. 正式安装
现在可以安装系统啦！只要按照安装器上的指导，一步步走下去即可。这里就不再赘述。但一定要安装到先前配置好的分区中，而不是让安装器自动分区！否则很可能丢失数据。

安装过程中最好是联网，（虽然不联网也不至于安装不了），否则一些重要的内容就没法下载，需要之后再通过软件更新器来安装。

## 7. 重启
安装好后就可以重启啦！好好体验一番吧！


---

# 总结
以上就是安装的全过程啦。记得最好备份文件啊！数据无价，谨慎操作。
创作不易，点个赞好不好(˃ ⌑ ˂ഃ )

---
# 下载链接

|Zorin OS 下载|
|:--|
|文件：Zorin-OS-16-Core-64-bit-r1.iso|
|[百度网盘：https://pan.baidu.com/s/1N4POSQBgCuEttk2WZpUoCg?pwd=0000](https://pan.baidu.com/s/1N4POSQBgCuEttk2WZpUoCg?pwd=0000)|
|也可以前往[Zorin OS官网](https://zorin.com/os/download/)下载|

|UltraISO 下载|
|:--|
|文件：UltraISO9.7.6.3829.rar|
|[百度网盘：https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000](https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000)|
|其它版本也可前往[UltraISO官网](https://ultraiso.net/download.htm)下载|


---
# 花絮
我的安装过程其实并非一帆风顺。安装还没开始，安装器就提示我，要关闭一个叫作“RST”的功能才能顺利安装Zorin OS（Ubuntu 和该功能冲突，所以基于Ubuntu的Zorin OS 也和该功能冲突）。

之后，安装器给了我一个网址：[Intel RST](https://help.ubuntu.com/rst/)（这个网站看看就好，别去按照它操作！亲测失败啊。下面介绍我踩的坑历程哈哈哈）。这个页面上有关于关闭RST的一些教程。看了一下，关闭 RST 后会导致 Windows 无法引导。按照教程修改注册表后，再次管理员运行`shutdown /r /fw /t 0`，进入bios。选中storage，将RST改为RAID模式。

这时候，跳出了一个对话框，大致意思是，会删除所有数据（其实是假的，或者说我理解错了对话框的意思）。于是我心一狠，选择了“yes”，重启。

结果，真的无法进入Windows了！开机后引导半天，然后蓝屏，代码是“INACCESSIBLE_BOOT_DEVICE”。

于是我去网上搜索如何补救，却发现根本没有教程。我把raid模式改回rst模式，还是无济于事，每次开机只能进入Windows RE（Windows Recovery）。我在这个模式下运行各种命令，什么diskpart、bcdedit之类的，但一点用都没有。正当我接近崩溃的时候，一个关键词——安全模式，映入眼帘。我尝试着，电脑竟然成功引导进入了安全模式！

智能的Windows在安全模式中修复了引导，于是总算可以正常进入系统啦，真是有惊无险呢。这时候将rst模式改为raid模式，windows仍能正常开机。

可惜，在安装Zorin OS时，因为没提前给磁盘分区，而是随便把这个工作交给了安装器，结果磁盘坏了一个重要的分区。虽然将坏掉的区域格式化后又可以用了，但里面的50GB的数据灰飞烟灭——包括一堆代码，PPT文档，网课之类的。唉，福兮祸所伏啊。不过还好坏掉的不是C盘D盘，因为里面的数据可重要多了啊。

好吧，后来谁知文件恢复软件竟然给我恢复出了80~90GB的数据，多了整整30GB呢——包括我一个月前删掉的图片、视频、垃圾文件之类的，但是对我来说最重要的Python、C++代码，一个都没有恢复出来呜呜呜……

所以，记得备份！备份！备份！

还是这句话：数据无价，谨慎操作啊。

