@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 背景
红米1s很老了，小米官方只支持到Android 4.4 Kitkat，于是很多应用都安装不上去。于是，我决定将魔趣（Mokee）刷入其中。
# 准备工具
## 硬件（自己准备）
1. 一台Windows 电脑
2. 一台红米1s（Armani）
3. 一根Type B数据线
## 软件（我会在文末提供链接）
4. TWRP（img）
5. 魔趣 71.2（zip）
6. Fastboot应用（exe）
7. 小米驱动

# 刷机步骤
## 1. 重启电脑
如果你的电脑已经安装过了小米的驱动，则直接忽略第1、2步。
首先，你需要重启电脑到一个特殊的模式，用来禁用驱动程序强制签名。
打开CMD，输入`shutdown /r /o /t 0`，回车，即可重启到恢复模式。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/b424c3248349574e9c95333975454950.png)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c8f9d7d35d7f1fc85d4ad8f6ae44defa.jpeg#pic_center)
看到这个面板后，选择“疑难解答”选项。![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/72e92910386903684a72dcaca83a7336.jpeg#pic_center)
点击“启动设置”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/272304697c425743d875e8b8a1f534f6.jpeg#pic_center)
重启。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5e72e89b3919c7430bd20c2793e877dc.jpeg#pic_center)
过一会儿，电脑会显示这样一个界面。此时，按下键盘上的<kbd>7</kbd>或<kbd>F7</kbd>即可。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cfb5dc349d15d602993a732722b10e02.jpeg#pic_center)
## 2. 安装驱动
将驱动文件下载到电脑后，将其解压。
把手机关机，用USB数据线连接手机和电脑。此时，长按手机的<kbd>电源</kbd>键和<kbd>音量-</kbd>键（靠近电源键的音量键），直到屏幕亮起进入Fastboot模式。打开电脑上的设备管理器，展开其他设备，发现有Android，而且有一个感叹号。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/55c3287ae10b993a7b7d4e0f77db6e01.png#pic_center)
双击打开，会弹出这样一个窗口：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4c5c327d962719b8bc11ce0c92ce9962.png#pic_center)
我们点击“更新驱动程序(U)”，在跳出的窗口中选择“浏览我的电脑以查找驱动程序”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c6fe29240bef81e4305edf0139dd18b9.png#pic_center)
浏览存有驱动程序的文件夹，点击“下一步(N)”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d7dd04c76441334c4283a9167e849289.png#pic_center)
此时，点击“始终安装此驱动程序软件(I)”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9db6238c7918b341a586a8d6bbc970b9.png#pic_center)
稍稍等待，驱动就装上了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/d5eb0981b7e85e5315b698440244b15a.png#pic_center)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c4c2f8268d19a137a047a96f1934fcfc.png#pic_center)
安装完驱动返回，你会看到设备管理器多了一个Android Phone。这代表你成功安装了驱动。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/8c02b350e48c57367b306e6a3fdad150.png#pic_center)
但是，如果你的电脑跳出了这样一个界面，则代表你没有重启电脑。此时，返回到第一步，看看如何重启到特殊的模式。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/27ab36f2e709905558bd0d06673722e8.png#pic_center)
## 3. 刷入TWRP
此时，打开CMD，将当前的路径切换到fastboot所在的文件夹（你应该早就解压过了吧，所有需要用到的文件会在文章末尾给出链接）。此时，你的手机应仍处于fastboot模式中。运行`fastboot devices`命令以检查手机是否连接到电脑。确认无误后，输入命令`fastboot flash recovery`。等待操作完成后，将手机拔下来，撬开手机壳，把电池扣下来，过两秒再装上去。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/cfffa1f9e0bc7386c593e428fe9fa126.png)
## 4. 清空数据
此时，长按手机的<kbd>电源</kbd>键和<kbd>音量+</kbd>键（远离电源键的音量键），进入Recovery。刷机需要删除所有数据，否则是无法刷入的。所以在这个界面下，选择“Wipe”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e917833b5579fff5879510e7bab85874.png#pic_center)
进入后将下方的拉条拽到最右。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/665c027c1c6354b2e5a24eeba447b234.png#pic_center)
## 5. 刷入魔趣
完成数据清除操作后，在电脑上将刷机包复制到手机内（TWRP是支持USB文件传输的，这是它的一个特色）。回到手机，返回TWRP的主面板。此时，点击“Install”，然后找到刷机包的位置，点击刷机包。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/e917833b5579fff5879510e7bab85874.png#pic_center)
看到这个界面后，将拉条拽到最右。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6dcb8cdc2806df68d79f62709fed2c19.png#pic_center)
此时，等待大约10分钟，魔趣就会被安装到手机中。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/43a0d1a6078a2008fc1f4ff36aa5c644.png#pic_center)
等待刷机完成后，点击“Reboot System”。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/40da30cb8c1fc07e570d6d6d2766cbc4.png#pic_center)
## 6. 开机
第一次开机时间会比较长，大概10分钟。静静等待即可。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/89e1d25a6083f28ddf24d3468b386d4b.jpeg#pic_center)

# 致谢
非常感谢[魔趣团队](https://www.mokeedev.com/guide/#开发团队)，开发了红米1s刷机包！
# 结尾
这就是Redmi 1s的刷机全过程啦。点个赞再走呗~

---

# 下载链接

|TWRP 下载（Redmi 1S 专属的TWRP，其它手机请勿使用）|
|:--|
|文件：twrp-3.7.0_9-0-armani.img|
|[百度网盘：https://pan.baidu.com/s/1uhAc9fPLNd2n-l5i_Xk_VQ?pwd=0000](https://pan.baidu.com/s/1uhAc9fPLNd2n-l5i_Xk_VQ?pwd=0000)|
|也可以前往[TWRP官网](https://twrp.me/xiaomi/xiaomiredmi1s.html)下载|

|小米的驱动|
|:--|
|文件：xiaomi_usb_driver.zip|
|[百度网盘：https://pan.baidu.com/s/1WXuevgfggw0SEmeRgu7dJQ?pwd=0000](https://pan.baidu.com/s/1WXuevgfggw0SEmeRgu7dJQ?pwd=0000)|
|也可以前往[小米社区](https://web.vip.miui.com/page/info/mio/mio/detail?postId=18464849&app_version=dev.20051)下载|

|Platform Tools（里面有Fastboot）|
|:--|
|文件：platform-tools.zip|
|[百度网盘：https://pan.baidu.com/s/1CUMEmG1y4oruhHjWj0qGAQ?pwd=0000](https://pan.baidu.com/s/1CUMEmG1y4oruhHjWj0qGAQ?pwd=0000)|

|魔趣刷机包（Redmi 1S 专属的刷机包，其它手机请勿使用）|
|:--|
|文件：MK71.2-armani-190228-HISTORY.zip|
|[百度网盘：https://pan.baidu.com/s/1y6xpr11UHShbeO51AAizaA?pwd=0000](https://pan.baidu.com/s/1y6xpr11UHShbeO51AAizaA?pwd=0000)|
|也可以前往[SourceForge（马丁龙猪删库跑路后文件存放的地方）](https://sourceforge.net/projects/mokee/files/HISTORY/armani/)下载|

