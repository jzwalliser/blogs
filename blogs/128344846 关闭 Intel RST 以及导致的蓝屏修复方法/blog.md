@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 前言
上次，为了在电脑中安装一个Linux系统，于是在BIOS中关闭了Intel RST。结果，Windows 11无法引导了！我在手机上各种搜索，电脑上各种操作，总算是修好了Windows。就让我分享一下经验吧！
# Intel RST
## RST 是什么？
RST 的全名叫作“Rapid Storage Technology”。大部分电脑在默认情况下都是开启的，它可以加快电脑的运行速度。但是，除了Windows以外的大部分系统都不支持RST，所以必须将其关闭才可以安装Linux。
## 关闭 RST
### 1. 开启安全模式
在关闭RST前，一定要记得提前将Windows的引导设置为“安全模式”！否则关闭RST后再引导Windows，你将会收获“INACCESIBLE_BOOT_DEVICE”蓝屏。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/96e99a86625223535510ff2c911dc85c.png#pic_center)
首先，打开msconfig。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/34b2243c015cfb76b5626bdc616c476d.png#pic_center)
打开后，切换到“引导”选项卡。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3dddecebc20d6e0dde97e355d6753314.png#pic_center)
选中“安全引导”后，确定。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/17c48a3374513a4ed3e6f02f61b91531.png#pic_center)

### 2. 进入BIOS
每台电脑进入BIOS的方式不太一样。不过，有一种通用的方法：以管理员权限运行CMD，输入`shutdown /r /fw /t 0`，然后电脑就会自动重启进入BIOS。每个型号的电脑BIOS略有差异，我的电脑是Lenovo小新14-2019，下面的步骤仅作参考。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/e7f2eef37e805e5f428c9e9df10bab58.jpeg)
### 3. 关闭RST
左右键切换选项卡为“Configuration”，然后选中“Storage”，进入。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/b094bb739654714bde221b40c3df4c63.jpeg)

选中“Controller Mode”，跳出的弹窗中选择“AHCI mode”，回车。这时候，有可能会跳出一个红色的警告弹窗，提示“所有信息将被删除”。其实都是吓人的，直接“Yes”就可以了，并不会删除你什么数据。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/40dc2aa334dc7441210f11b06b932ad6.jpeg)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ae1a2e9df518cd99f1a7a0d663d2b065.png)![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/87c89cd46104029e27d0d4cd7fe9f41e.jpeg)

操作完后，回到最初的面板，左右键切换到“Exit”选项卡，选中“Exit Saving Changes”，然后“Yes”即可保存设置并退出BIOS。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/d33e18ab9c29437440b2d62bc2f6a400.jpeg)
### 4. 关闭安全模式
这时候，重启进入Windows。若你提前打开了安全模式，那么电脑可以正常引导，进入后再将安全模式关掉就可以了，方法和先前的打开安全模式类似，打开msconfig后将安全引导取消勾选，重启后就恢复正常了，这里不再赘述。但是，你如果像我一样没有提前打开，那么就准备收获蓝屏吧！
## 操作不当后蓝屏了怎么办
若你的电脑一开机就蓝屏，那就是因为在关闭RST前没有提前按照上面的步骤开启安全模式。这时候，你就需要按照下面的步骤来修复了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ec0676d7b474cfaab7ada0d6b67309df.png#pic_center)
### 1. 进入Windows RE
Windows 多次引导失败后，会自动进入Windows Recovery Environment。进入Windows RE后，点击“疑难解答”。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/74bcc5559a667877185d2ba019f2ba62.jpeg)

然后选择“高级选项”。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/378c5638acd6c8abaf1b04c801eff7a0.jpeg)

点击“启动设置”。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/99d0cf32dc9d06537a16eda1824bf53b.jpeg)
### 2. 手动进入安全模式
点击重启。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/2b67fdd385c29097c9bf2f080b145d8f.jpeg)

重启后，电脑将会显示该界面。按下键盘上的数字“4”，等待Windows进入安全模式。在安全模式下，Windows会自动修复引导。然后Windows就可以正常开机啦！
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/667128db25c460eb4208679e713d2ffc.jpeg)

---

# 结尾
上面就是关闭Intel RST和修复蓝屏的全过程啦。
给个赞好不好\~\\(\^o\^)/~


