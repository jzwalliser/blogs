@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 前言
学校发的平板——学正宝，已经跟了我三年了，电池也用废了一块。当然，电池坏掉不是因为使用的次数很多，恰恰相反，它被我捣腾的频率其高。

这台平板电脑预装的是Android 5.1，里面仅有一个客户端应用和设置，安装的应用必须是客户端提供的，因此不能任意安装apk软件。

为了使其发挥最大的价值，我开始摸索如何让它越狱。这是三年来最轻松的几天，就让我把学正宝的越狱经验分享给大家吧。

# 精髓
中间人攻击（MitM）。
中间人攻击，就是在上网的过程中，客户端和服务器中间出现了一个中间人，这个中间人可以窃听两者之间的通信，甚至拦截通信内容并不动声色地将其修改，改完后继续发送，使双方得到的信息变为中间人希望他们获取的内容。
这就是著名的中间人攻击（Man in the Middle Attack）。
如果还不明白，那就一起来看一个历史故事：秦始皇在临终之际，写下遗诏，要让公子扶苏继位。但是赵高、李斯却把遗诏改了，使秦二世上了台。
在这里，秦王相当于服务器；赵高、李斯相当于中间人；而各位大臣相当于客户端；诏书相当于数据。
# 准备工具
## 硬件 （自己准备）
1. 一台 Windows 电脑
2. 一台学正宝
## 软件 （我会在文末提供链接）
3. Progress Telerik Fiddler（exe）
4. WPS（apk）
5. QQ浏览器（apk）

# 越狱步骤
## 1. 电脑配置 Fiddler
### 安装 Fiddler
下载 Progress Telerik Fiddler，并安装。
选择 "I Agree"。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/23fac24b2c5739e04e33120a3e7b41a6.png)

点击"Install"。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/1b5f279558fa0c0a22bf5892ebfc9ebf.png)

然后等半分钟即可。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2649cae4b08ac7c540617bbcaddcfed3.png)
### 浏览器修复
打开Fiddler。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/004972ae8728ca0fd17f9c9be7d7cd71.png)

这时，使用浏览器有可能出现这个界面。所以，我们需要设置Fiddler。由于破解学正宝，我们用不到https的加密解密，所以直接让Fiddler不要监听https协议的数据包就可以了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/9e4e181d433884fa5e5987179886e231.png)

打开 Tools > Options。
![](https://i-blog.csdnimg.cn/blog_migrate/99d50c8f175ee3598bf9011a33c1ca7e.png)

在跳出的窗口内，打开HTTPS选项卡，把"Capture HTTPS CONNECTs"选项卡取消勾选。此时，浏览器已经可以正常工作了，但是我们先别把这个窗口关掉。![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/6fb3a3ce4923bab85ff852074a6538e0.png)
### 允许远程连接
然后，再打开Connections选项卡，把"Allow remote computers to connect"项勾选上，再将端口设置为"8888"，如下图。点击“OK”以保存设置。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/8956e96affd0dbb16afa16e9c7925620.png)
### 配置断点并篡改数据包
之后，在右半边打开“Autoresponder”选项卡（绿色或灰色闪电），勾选“Enable rules”、“Accept CONNECTs”、“Unmatched requests passthrough”。将以下两项分别填入上下两个文本框，然后点击“Save”，形成一个自动响应项：
|If request matches...|then respond with...|
|:-:|:-|
|http://appdown.weikechina.com/app/app1987.apk|[你电脑中WPS的apk安装包位置]（也可以是QQ浏览器，取决于你想安装什么，但其他绝大部分应用被限制所以安装不上，我会在最后介绍解除限制的方法，也会在文末提供下载链接。）|


像这样：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c2c454e4e260946ba117dc6d4dd74fde.png)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/3d7bc45be8c8c1a8154fb7a962627f74.png)

最后，把Fiddler关掉再重新打开。
## 2. 检查学正宝应用版本
确保学正宝联网，然后打开学正宝平板桌面上的学正宝应用。如果没有提示你要下载新版本，则代表学正宝应用是最新版本。此时，需要将学正宝平板还原到出厂。**但是如果提示你要下载新版本，那么请跳过下面的内容直接看第三步。但是一定不要现在下载！** 我们需要进行一系列操作然后再下载。现在，请从最近任务中把学正宝应用划走。
### Recovery中将学正宝还原到出厂
首先，将学正宝关机。等待约10秒钟，同时按下<kbd>电源</kbd>键和<kbd>音量+</kbd>键（靠近电源键的那个），直到屏幕亮起。此时，你会在右下角注意到一行字。稍等片刻，学正宝就会进入recovery模式。

![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/884e26449203d9523151b68eada36769.jpeg)

在recovery中，是无法使用触屏的，而是用<kbd>音量+</kbd><kbd>音量-</kbd>键和<kbd>电源</kbd>键来控制。按动<kbd>音量</kbd>键，将高亮移至"wipe data/factory reset"，然后按下<kbd>电源</kbd>键进入，并选中里面的"Yes"选项。等待约30秒直到操作完成。这时候，学正宝就被重置到了出厂设置。![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c4b2200cde9d775a5e36e47bfae54508.png)

现在，将高亮移到"reboot system now"并确认，此时学正宝会重启到Android。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/0946fee93a0fdcaad31493d39debd9d7.png)

### 用最旧版本的学正宝应用登录你的账号（请严格参照下面的顺序操作，否则会登不进去）
开机后，不要连任何Wi-fi，直接打开桌面上的学正宝应用，将你的账号密码先输入到框中，但不要登录（反正也登不上，毕竟没有连接Wi-fi）。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/9cf40b1ab54c75e4a64dc5eefc9e0a1a.png)

此时，再进入设置，让学正宝连接你家Wi-fi。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/7fb7a21f00dcba72e8d2d389c6a8ee1b.png)

然后，回到学正宝应用，登录你的账号。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/fb9963603f50d6899656b5cf68acd48c.png)![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/430e35df446c3ea32d92e4139fa535dd.png)

此时，从最近任务中把学正宝应用划走。
## 3. 配置网络环境
### 将学正宝连接到代理
请确保电脑和学正宝在同一个局域网内。
首先，你需要知道电脑的IP地址。打开CMD，输入`ipconfig`，回车。此时，你就可以找到你的电脑在局域网中的ip地址了。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/4fc6aae951e79d504eae61410acf23d6.png)

打开学正宝平板的设置，进入WLAN，长按当前的网络。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/7fb7a21f00dcba72e8d2d389c6a8ee1b.png)

在跳出的窗口中选择“修改网络”。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/80527cff8ecb8f855feaec44b738217e.png)

勾选“高级选项”，将代理设置为“手动”，在“代理服务器”一栏输入你电脑的ip地址，端口输入8888。最后保存。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/ea14f7cb4e0f28efe262542ceb2fbf1d.png)
### 学正宝下载安装包

之后，打开桌面上的学正宝应用。此时，点击“确定”，下载下来的就是WPS。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/f7004c0cb9b74810ac1a5a4b041a323e.png)

静静等待下载吧！![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/bcdfc9dd24632cc347ca33ad0bd55bba.png)
### 安装应用
最后，安装。（我提供的WPS可能和截图上的WPS版本不太一样）
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/5ee84cba896c414262e51f5d1d83d1d2.png)
## 4. 安装其它软件
### 安装包解析失败
在学正宝中，如果你安装其它软件，安装器会提示“安装包解析失败”。
其实，秘密就藏在 `storage/emulated/0/weike/bmd/bmd.txt`中。你只要将软件包的包名复制到该文件中，就可以安装了。或者，在刚才抓包的过程中，顺便把这个网址的内容也改了（自己按需修改）：
```
http://app.weikechina.com/admin/index.php/Applogin/getpackage_HS
```
### 实际操作
以安装“流舟文件”为例。首先，打开WPS。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/bd78e88c3bd08e677d6550aab4e38fc2.png)

用WPS打开文件`weike/bmd/bmd.txt`。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/435d8380f376e7331a1dab3fa6bd9429.png)

将`com.liuzho.file.explorer`复制到内容的末尾，最后保存。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/f617757eeb1dd8f8b7277bbba8fe464b.png)

然后，再想方设法（比如用QQ浏览器，或者用学正宝客户端）打开流舟文件的安装包，就可以正常安装啦。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/c79c6aa50e826e5bc68f3df1ab5ebdeb.png)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   
# 漏洞分析
为什么能够顺利破解学正宝呢？
1. 学正宝客户端用的不是https协议，而是http协议。所以，传输的数据是不经过加密的，可以轻而易举地截获数据包并将其篡改掉。
2. 学正宝客户端下载完apk后，不对其进行检测，所以apk被我篡改了都不知道，傻不拉几就直接跳出安装界面了。

# 后记
## 先看看破解后的学正宝被我DIY成了什么样子
是在受不了学正宝自带的启动器Launcher3，因为来自AOSP中的大多功能都被禁用了，所以安装了Nova Launcher作为我的桌面。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/28b255a46ffd61a41029f51d4b81a6fd.png)![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/e7584cda5cfc8328d3ed91df2496375b.png)

这是多任务，壮观吧！![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/70e964bcda406a383289671cac387e61.png)
## 再看看一些神奇的应用
### 流舟文件（com.liuzho.file.explorer）
如何实现文件传输呢？因为用不了USB口了，所以干脆整个ftp服务器来传输文件吧。
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/924c9df4b427724bf3fbb4f5b7b968e7.png)电脑上：
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/d92f5d2bcc74b9756c265f64bee06d31.png)
### 隐藏的设置项（com.jami.tool.hiddensetting）
学正宝自带的设置真的太简陋了，几乎啥都没发设置，简直就是“设不了置”。![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b755a9e55dcb8c5d3b289ac8eb3e6902.png#pic_center)
因此，我特意安装了隐藏的设置项应用。这下总算方便了！
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/5e9b9cb99645253b97b81ea3d56dcac5.png#pic_center)
### Geogebra（org.geogebra.android.calculator.suite）
Geogebra上可以画各种数学函数。可惜，作为Android 5.1，学正宝只能安装旧版本的Geogebra，截图中的是 Geogebra 5.0.674.0。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/c732cd2559ceca468e6bf97aa59e69c6.png#pic_center)
### CalcES（advanced.scientific.calculator.calc991.plus）
CalcES是很高级的一款计算器，可以计算许多复杂的公式，可惜在Android 5.1 上只能安装旧版本，这里是版本5.4.4.229。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/de332b2a8d7e15c9abf0d5537feaa3e5.png#pic_center)
### Musicolet（in.krosbits.musicolet）
这是我在安卓上见过的最高级的音乐播放器，没有之一。有非常多的功能，甚至可以编辑内嵌歌词。![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2371487c1e08da89a7ff301084ad2088.jpeg#pic_center)

### Qpython3（com.hipipal.qpy3）
有想过在学正宝上打Python代码吗？可以正常运行哦～
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/b07a3da8a6a91f3aa7afbfab1e28b83d.png#pic_center)
### The Powder Toy（uk.co.powdertoy.tpt）
粉末游戏不仅可以运行在电脑上，还可以安装在安卓上哦，TPT最低支持安卓4.x JellyBean。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ca2820ec8c22823f37dbc00c00d2fe10.png#pic_center)
### QuickShortcutMaker（com.sika524.android.quickshortcut）
这款软件可以打开几乎所有的Activity。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a49424733a1f7618ae41e70b00850884.png#pic_center)
### 时钟（com.google.android.deskclock）
可以倒计时、秒表、甚至设闹钟。这是AOSP中的一部分，竟然没有预安装在学正宝上！
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/ed5297f81e6b7c934b54e1d1b569190c.png#pic_center)
### LLand（com.android.systemui.egg.LLandActivity）
安卓 5.1 自带小游戏LLand。不过这游戏难度是真的高啊，一般我只能通过两道棒棒糖关卡QAQ。![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/2d508b9adbe3681e4a85672c3bfb572c.png)
## 学正宝的配置
学正宝的配置其实并不高。一起看看下面几张截图：
### 芯片
说实在这芯片我都没见过，孤陋寡闻了啊。百度了一下，发现这个芯片真的好老，是Mediatek在2017年7月22日发布的。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/14a8a9bb120bec65124e14519d9a62cb.png#pic_center)
### 电池
容量是真的小，才1000mAh，真的用不了几个小时啊。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/18ab8ba49c4a14d6972c9c15a73cc8b4.png#pic_center)
### 系统
没想到竟然被Root过！！！
![请添加图片描述](https://i-blog.csdnimg.cn/blog_migrate/56fd3f27cb650fd3c8bc6694b3fb48ef.png)![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/2c230619d3fc985d226a081fec7982e8.png#pic_center)
## 美中不足
学正宝被破解啦！不过，仍有一些讨厌的瑕疵：
1. 无法使用USB口来传输数据。
2. 无法使用adb。USB口不能用，再加上开发者选项中没有网络adb这个选项，导致学正宝平板完全不能用adb调试。
3. 学正宝被root过，但无法访问root权限。
4. 系统版本很老。现在Android 14 UpsideDownCake都出来了，但学正宝依然处在Android 5.1.1 Lollipop，于是有很多软件装不上。
5. 芯片很老，2017年就出来了。
6. 内存很小，只有970 MB。
7. 电池容量很小，只有1000 mAh，用不了多长时间就没电了。
8. 大于100 MB的apk一定安装不上。就算是50 MB的apk都安装得很吃力，像WPS、QQ浏览器、UC浏览器只能安装旧版本，新版本安装不上。
9. 如果要截屏、录屏需要额外安装软件。而且截屏录屏会导致SystemUI当场死掉。

# 结尾
以上就是破解学正宝的全步骤啦。有不懂的可以私信我哦！一定要点赞加关注再走噢~ 

---

# 下载链接
|Telerik Progress Fiddler|
|:--|
|文件：FiddlerSetup.exe|
|[百度网盘：https://pan.baidu.com/s/1fWn0EYV5UCQ3Mnpm8mt_Uw?pwd=0000](https://pan.baidu.com/s/1fWn0EYV5UCQ3Mnpm8mt_Uw?pwd=0000)|

|WPS Office 12.5.1|
|:--|
|文件：WPS Office.apk|
|[百度网盘：https://pan.baidu.com/s/1T2ftTZUW5vg-3mJ6dWQyHA?pwd=0000](https://pan.baidu.com/s/1T2ftTZUW5vg-3mJ6dWQyHA?pwd=0000)|


|QQ浏览器 11.3.5.5512|
|:--|
|文件：QQ Browser.apk|
|[百度网盘：https://pan.baidu.com/s/1bmKLKH4ZLNqWogflpVQH2A?pwd=0000](https://pan.baidu.com/s/1bmKLKH4ZLNqWogflpVQH2A?pwd=0000)|

