@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# Geogebra 是什么？
众所周知，[Geogebra](https://www.geogebra.org/)是一款数学画图软件，有着许多功能——画函数、画立体空间图像等等。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/bcc8e49d44504232b24e0f2909cf9fc3.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/be483e90ec7645739147182a283fd0da.png#pic_center)
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/c19b1b943ecb4a94b3b84c54888d7289.png#pic_center)

# 安装包？
不知道为什么，最近在官网上下架了Linux版本。在官方下载页面上，发现只有Geogebra Classic 5的Linux版，而Geogebra Classic 6的Linux版却消失了。
不信？请见官网上的[下载页面](https://geogebra.github.io/docs/reference/en/GeoGebra_Installation/#_other_geogebra_classic_6_versions)。
![在这里插入图片描述](https://i-blog.csdnimg.cn/direct/8c421f7bbbf74c64bf8fae9b27216ed4.png)
在“其他版本”中没有了Linux！没有了deb和rpm包！我在网上找来找去，最终也没有找到比6.0.666更新的安装包。

# 提取安装包
后来由于某些需要，我最终把安装包（deb格式的）从系统中重新打包提取了出来。

需要先安装`dpkg-repack`：
```bash
$ sudo apt install dpkg-repack
```
然后找到需要提取的包，这里叫做`geogebra-classic`。
最后，提取：
```bash
$ dpkg-repack geogebra-classic
```
![请添加图片描述](https://i-blog.csdnimg.cn/direct/cefbfe3b1ecc4a2593109a63878ac5ab.png)
然后安装包就有啦！这里分享给大家。当然，是否和原来官网上的一模一样，我不保证，毕竟这是重新打包的，对不？
# 下载链接
|Geogebra Linux 6.0.666 下载|
|:--|
|文件：geogebra-classic_6.0.666.0-202109211234_amd64.deb|
|[百度网盘：https://pan.baidu.com/s/1kpVCLbRKbcFUVep_xW3f2g?pwd=0000](https://pan.baidu.com/s/1kpVCLbRKbcFUVep_xW3f2g?pwd=0000)|

