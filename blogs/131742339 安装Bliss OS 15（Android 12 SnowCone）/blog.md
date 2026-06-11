@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 引入
最近Bliss OS 15出来了。它是一个可以安装在笔记本电脑上的安卓系统，它基于Android 12 SnowCone。用起来非常爽，界面也很好看。一起来看看如何安装它吧！

# 准备工具
## 硬件（自己准备）
1. 一台电脑（需要预装Windows）
2. 一块U盘
## 软件（我会在文末提供链接）
3. UltraISO
4. Bliss OS 15 的镜像文件（iso）

# 安装


## 1. BIOS 清单
安装前，需要修改BIOS中的设置，否则可能无法启动系统。
|关键词|值|
|:-|:-|
|Secure Boot|关闭|
|硬盘模式|RAID|

Secure Boot肯定是要关闭的，否则只能进入Windows（或者配置了Secure Boot的系统）。其次，硬盘模式必须不能是RST，不过可以是RAID，否则系统无法启动。关闭RST的步骤大家可以看看我这一篇：[关闭 Intel RST 以及导致的蓝屏修复方法](https://blog.csdn.net/jzwalliser/article/details/128344846)。
## 2. 将镜像写入U盘
这里省略步骤啦，不会烧U盘的同学可以参考这里：[使用 UltraISO 将系统写入U盘](https://blog.csdn.net/jzwalliser/article/details/128381214)。

## 3. 测试
在正式安装系统前，最好先测试一下该系统是否能完美运行在你的电脑上。
首先，请确保电脑处于关机状态。
将U盘插入电脑，然后开机进入Bliss OS，选择第一项（带有“Live”字样的）来测试一下是否能开机。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/14e4b54d7adaf3387870820193f52e15.jpeg#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bb5ca9da67c3d29cd4e552cd546dd7bb.jpeg#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/bd9cbd9c2decdf347c1173775eebf5ba.jpg)
## 4. 分区
若系统能够正常开机，那就可以回到Windows系统，对本地磁盘进行分区，分出一个空白的区域用于安装Bliss OS。在这里，我分了一个32GB的空分区来存放它。

## 5. 安装
然后，将电脑关机。重启到Bliss OS，然后选择 "BlissOS-15.8.6 2023-07-03 Installation"
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/583b59a162b9de082e97c4f6b08b5c81.jpeg#pic_center)
在这个页面下，用上下键选中刚刚分出的空分区，然后确认。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6ef3d0a0c5c9236bcd50d607f3e44dec.jpeg#pic_center)此时会询问你是否需要将这个分区格式化。若先前没有安装过Bliss OS 的旧版本，则推荐选择格式化为ext4。若以前安装过Bliss OS，则不要格式化（除非你想删掉原来的数据）。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e5255178e55a6f66bf9cb079e734fadb.jpeg#pic_center)
稍稍等待进入该页面，选择 "Yes"。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d1e3440a0bd1f098874985babef56afc.jpeg#pic_center)
（注：不一定会出现这个界面）如果你以前安装过Bliss OS 的旧版本，那么会看到这个界面。此处选择“Yes”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/42b5d824644afc5e1df2a9e0d025ed63.jpeg#pic_center)
（注：不一定会出现这个界面） 如果你以前安装过Bliss OS 的旧版本，那么会看到这个界面。此处还是选择“Yes”，这样原来的老版本Bliss OS会被更新。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/728b2ebbdd69c62f44cddbefa185fa44.jpeg#pic_center)之后，等待其安装完毕即可。

## 6. 调整启动顺序
（注：不是每台电脑都需要这个操作，取决于你的习惯）
安装Bliss OS后，每次开机会默认进入Bliss OS的EFI Boot Manager。如果你想要使用原来的Boot Manager（比如我习惯使用 rEFInd），那就需要进入UEFI设置来调整启动顺序。
首先，在Bliss OS中选中“Advanced options”。
![](https://i-blog.csdnimg.cn/blog_migrate/f0b9130d706bc341e465f0af5285524e.jpg)

选择 “UEFI OS”。
![](https://i-blog.csdnimg.cn/blog_migrate/47b64eb4fc9c03d112a02078fce673ba.jpg)进入后，切换到“Boot”选项卡，选中你喜欢的Boot Manager，将其提高到第一位。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/7ad327e96be1694cf0075a256ef7c579.jpeg#pic_center)切换到“Exit”选项卡，选中“Exit Saving Changes”，然后“Yes”，退出。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/44d47b3e969567d09150a4856ce956aa.jpeg#pic_center)
# 效果
安装完啦！一起来看看效果吧~
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/712f538e671fe9df41892b5e241e01e4.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/520965d614ccfebf0aa9747a35675533.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/254389af4fd524a726a20381980d7783.png#pic_center)
这副图你注意到了下面的Error code了吗？有没有感觉是在骂人......
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/79b51be902ce8a508d2d152232ec8ee3.png#pic_center)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cedd69733ed21e7d5e5eeceb07cece90.png#pic_center)
# 美中不足
Bliss OS确实不错，但是仍有一些小缺陷。
1. 有的时候屏幕会竖起来，不得不用ScreenOrientation把屏幕锁起来。
2. 有些软件不能开小窗。
3. 和Bliss OS 11不同，Bliss OS 15 的x86版不支持Arm应用，因为里面没有Houdini或Libndk。
# 结尾
创作不易，给个赞再走呗~

---

|UltraISO 下载|
|:--|
|文件：UltraISO9.7.6.3829.rar|
|[百度网盘：https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000](https://pan.baidu.com/s/1MgIe1htg9asqU-Eo7J9MBA?pwd=0000)|
|其它版本也可前往[UltraISO官网](https://ultraiso.net/download.htm)下载|

|Bliss OS 15 下载|
|:--|
|文件：Bliss-v15.8.6-x86_64-OFFICIAL-gapps-20230703.iso|
|[百度网盘：https://pan.baidu.com/s/1EkALttL6a5YxhreyXNWTDg?pwd=0000](https://pan.baidu.com/s/1EkALttL6a5YxhreyXNWTDg?pwd=0000)|
|其它版本也可前往[SorceForge](https://sourceforge.net/projects/blissos-x86/files/Official/BlissOS15/)下载|

---
# 后记
看了文章下面的评论，发现也有不少人在安装Bliss OS的过程中遇到了这样那样的困难。
首先，我个人觉得Bliss OS在驱动方面确实做得不咋地，我自己在安装过程中就遇到不少的问题。这是我在另一篇文章[安装Android x86](https://blog.csdn.net/jzwalliser/article/details/128345043)里面写的，在花絮那一节：
> 又是一年，我偶然看到了另外一个安卓系统——Bliss OS。Bliss OS 11 基于Android 9.0 Pie，Bliss OS 14 基于 Android 11 R。系统界面也很好看，是原生安卓。但是要找到适合我电脑的镜像却是一件非常困难的事情，我在Bliss OS官网上下载了至少十个镜像文件，包括Bliss OS 11、Bliss OS 14、Bliss OS 15，还有AOSP版本和Sakura版本的Bliss。
> 
> Bliss OS 15可以正常开机但不能正常运行，进入系统10秒后直接崩溃重启；Bliss OS 14的标准硬件支持版本可以正常开机但不能正常关机，关机后屏幕是黑色的但电源键一直亮着，只能长按电源键强制关机；Bliss OS 14的高级硬件支持版本不能正常开机，只能通过进入Debug mode然后在命令行中输入两次exit来引导系统；Bliss OS 11的标准硬件支持版本可以正常进入，但是和Phoenix OS一样没有触摸板支持；Bliss OS generic可以正常进入系统，但无法睡眠，而且按下音量键会发出“毕”的一声巨响，应该是声卡驱动有问题；Bliss OS的社区版本（Sakura）可以开机，但和Bliss OS 15一样，刚开机系统就马上崩溃并重启……只有Bliss OS 11的高级硬件支持版本适合我的电脑啊。

我也是在挑选了大量不同版本的镜像之后才找到了合适的那个。我用的电脑是Lenovo 小新 Air 14，所以如果你的电脑型号和我的一样，可以放心参照本教程；但如果不一样，那么本教程只能作为参考，如果遇到问题解决不了，也可以去试试不同的镜像，或者网上发文求助。

私信我大概没啥用，因为你遇到的问题我可能没有遇到，所以我也不知道如何处理。不过安慰一下你，为你提供点情绪价值还是可以的～

最后，祝大家安装顺利，玩得愉快～

