@[TOC](目录)


---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 准备工具
## 硬件（自己准备）
1. 一台电脑（需要预装Windows）
2. 一块U盘
## 软件（我会在文末提供链接）
4. Phoenix OS 或 Bliss OS 有关的文件，取决于你想安装谁
5. UltraISO【可选】
# 引入
提到安卓系统，大家首先想到的应该是手机吧。市面上卖的手机，除了苹果系统就是安卓系统（虽然也会有很少很少一部分手机安装的是Linux或Windows）。但如果我希望在电脑上安装一个安卓系统呢？

# 介绍两个Android x86系统
## Phoenix OS
[Phoenix OS](www.aemow.com)是国产的安卓系统，里面做了很多的修改，包括支持各种常用的快捷键，用起来非常的爽，而且应用都是以窗口形式呈现而非全屏。可惜，最新版本基于Android 7，且对于2～3岁的笔记本，硬件适配不是非常好，所以只适用于一些比较老的笔记本，而且不开通VIP会有弹窗广告。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/02441c4ed99405b3b86ec068e323baa3.jpeg)
## Bliss OS
[Bliss OS](blissos.org)是类原生的安卓系统，最新版本的Bliss OS 15基于Android 12（可惜我的电脑引导不了QwQ）。只是用起来没Phoenix舒服，很多Windows上常用的快捷键，如Super（即Win键）+E打开文件管理器，它并不支持。但是它支持较新的硬件（但需要下载正确的镜像版本），至少对于我的电脑，触摸板是可以在Bliss OS中正常使用的，而不需要额外连接一个鼠标。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ca1c5061c7041d76bba5c2fe22ccb80c.png)

# 安装系统
## 1. BIOS 清单
安装前，需要修改BIOS中的设置，否则可能无法启动系统。
|关键词|值|
|:-|:-|
|Secure Boot|关闭|
|硬盘模式|RAID|

Secure Boot肯定是要关闭的，否则只能进入Windows（或者配置了Secure Boot的系统）。其次，硬盘模式必须不能是RST，不过可以是RAID，否则引导安卓时，会卡在"Detecting XXX OS..."，然后不停打点，但就算屏幕上打出了一百个点，都启动不了（别问我是怎么知道的，在这里我踩过坑啊）。关闭RST的步骤大家可以看看我这一篇：[关闭 Intel RST 以及导致的蓝屏修复方法](https://blog.csdn.net/jzwalliser/article/details/128344846)。

## 2. 使用安卓安装器安装
最终，我选择安装Bliss OS 11 Advanced Handware Support 到电脑中。下载完iso文件后，直接解压（或者用压缩软件将iso打开），会发现里面有一个exe文件。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/a682ac698bfb2cebf2b7bd5ec9ea432c.png)双击打开exe，然后就可以在Windows中直接安装Bliss了，不需要烧U盘之类的繁琐操作。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/70bfd239b13eb9dd99960312382b47ff.png)结束后直接重启，然后开机时按下电脑的F12键（不同电脑键位有所不同），选择Linpus Lite进入，最后选择Android就可以进入系统啦！


## 3. 使用U盘安装
但如果下载的是其它版本，如Bliss OS 12，14，15，Generic（AOSP），Sakura，那只能使用UltraISO将镜像烧到U盘上，因为里面没有自带的安装器。就算你拿Bliss OS 11 中的安装器来安装这些版本，也装不上（亲测无效啊）。这里就不再介绍，可以详细看看这篇文章：[安装Bliss OS 15（Android 12 SnowCone）](https://blog.csdn.net/jzwalliser/article/details/131742339)。

# 效果
安装好了吗？让我们一起看看效果吧！
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c5f7af5f5e759e95e4ecd9b79f278847.png)（放心没有初始密码，密码是我后来设置的）
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/330ec7ea7170a01bea9c440053e949e6.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/97b42f58fbd260c3181843d2f8225134.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/baca219abffb7198bebccbf562e1c851.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5703baeada8973931dcd3ae88504a668.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ca1c5061c7041d76bba5c2fe22ccb80c.png)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/310c1399b5fd54c350bdccaf5c093acf.png)

---


# 总结
以上就是安装Android x86的过程啦。记得需要在BIOS中修改设置在可以顺利安装哦！
给个赞好不好 O(∩_∩)O

---
# 下载链接
|Phoenix OS EXE 安装器下载|
|:--|
|文件：PhoenixOSInstaller-v3.6.1.564-x64.exe|
|[百度网盘：https://pan.baidu.com/s/1BazSw5EtMcBT-G9TVTz36g?pwd=0000 ](https://pan.baidu.com/s/1BazSw5EtMcBT-G9TVTz36g?pwd=0000)|
|也可前往[Phoenix OS官网](http://www.aemow.com/cn/biaozhunban/down/)下载|

|Phoenix OS ISO 映像下载|
|:--|
|文件：PhoenixOSInstaller_v3.6.1.564_x64.iso|
|[百度网盘：https://pan.baidu.com/s/1Y2QOcHcEUmP08O6pnqtwRA?pwd=0000](https://pan.baidu.com/s/1Y2QOcHcEUmP08O6pnqtwRA?pwd=0000)|
|也可前往[Phoenix OS官网](http://www.aemow.com/cn/biaozhunban/down/)下载|

|Bliss OS ISO 映像下载|
|:--|
|文件：Bliss-v11.14--OFFICIAL-20210507-2246_x86_64_k-google-5.10.32-lts-pledge-xanmod_m-20.1.10_pie-x86_dgc-p9.0-11.13_ld-p9.0-x86_dg-_dh-blueprint_pie-x86_w45_2020_mg-p9.0-x86.iso|
|[百度网盘：https://pan.baidu.com/s/1cSN6mlZ47rxDx_HF-eH1IA?pwd=0000](https://pan.baidu.com/s/1cSN6mlZ47rxDx_HF-eH1IA?pwd=0000)|
|其它版本也可前往[Bliss OS官网](https://blissos.org/)下载|

|UltraISO 下载（可选）|
|:--|
|文件：UltraISO9.7.6.3829.rar|
|[百度网盘：https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000](https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000)|
|其它版本也可前往[UltraISO官网](https://ultraiso.net/download.htm)下载|


---

# 花絮
前几年我从网上下载了[Phoenix OS v3.6.1](http://www.aemow.com/cn/biaozhunban/down/)（基于Android 7.1 Nougat）的是EXE安装程序，接着一顿操作安装到了E盘。但是，当时的我并不知道需要关闭Secure Boot，更不知道如何关闭。于是一开机一片蓝色，中间一行提示，按下回车键后只能重启到Windows，结果只好卸载掉Phoenix。

半年后，我总算学会了关闭Secure Boot。再次安装后开机进入，谁知系统根本无法引导，还每隔一秒就在屏幕上打出一个点......我以为是Phoenix的问题，于是又下载了Fyde OS尝试。虽然Fyde OS的Boot Manager不再在屏幕上打点了，但依然无法进入系统。

后来，在安装Linux的时候才知道，原来是Intel RST 惹的祸。RST关闭后Windows直接无法引导了，真是吓死人，一顿操作才总算修好。之后安装Phoenix OS，总算可以正常启动啦。

谁知，Phoenix OS里没有触摸板驱动......结果好，一盆冷水泼下来。我向来习惯使用触摸板而不是额外连接一个鼠标，于是只好进入Windows将Phoenix卸载掉了。

又是一年，我偶然看到了另外一个安卓系统——[Bliss OS](https://blissos.org/)。Bliss OS 11 基于Android 9.0 Pie，Bliss OS 14 基于 Android 11 R。系统界面也很好看，是原生安卓。但是要找到适合我电脑的镜像却是一件非常困难的事情，我在Bliss OS官网上下载了至少十个镜像文件，包括Bliss OS 11、Bliss OS 14、Bliss OS 15，还有AOSP版本和Sakura版本的Bliss。

Bliss OS 15可以正常开机但不能正常运行，进入系统10秒后直接崩溃重启；Bliss OS 14的标准硬件支持版本可以正常开机但不能正常关机，关机后屏幕是黑色的但电源键一直亮着，只能长按电源键强制关机；Bliss OS 14的高级硬件支持版本不能正常开机，只能通过进入Debug mode然后在命令行中输入两次exit来引导系统；Bliss OS 11的标准硬件支持版本可以正常进入，但是和Phoenix OS一样没有触摸板支持；Bliss OS generic可以正常进入系统，但无法睡眠，而且按下音量键会发出“毕”的一声巨响，应该是声卡驱动有问题；Bliss OS的社区版本（Sakura）可以开机，但和Bliss OS 15一样，刚开机系统就马上崩溃并重启……只有Bliss OS 11的高级硬件支持版本适合我的电脑啊。

不过安装成功后，体验确实不错哦。

