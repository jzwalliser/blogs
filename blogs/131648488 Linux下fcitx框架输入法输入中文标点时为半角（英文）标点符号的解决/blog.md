@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 引入
有的时候，发现在Linux下使用fcitx框架输入中文的时候，标点符号却一直是半角标点符号，像这样：
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/fc7c3e68f99477d689952e4d5cbcdb33.gif#pic_center)

# 解决
其实，问题就藏在fcitx输入法中。出乎意料的是，这不是一个bug，而是一项功能...
## 1.打开fcitx设置
不管用什么方法，反正先打开fcitx的输入法配置。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/a2ddd463384da909dcb55eab249395e9.png)
## 2.打开全局配置
切换到全局配置选项卡后，勾选底部的“显示高级选项”，并下滑，找到“切换全角标点”一栏。看到旁边的快捷键了吗？我这里是<kbd>Ctrl</kbd>+<kbd>.</kbd>。
![在这里插入图片描述](https://i-blog.csdnimg.cn/blog_migrate/14fb11ab97ea8fae132fabb963cdb8d6.png)
## 3. 随便找个可以输入地方敲下快捷键
此时，随便打开一个可以输入东西的窗口，并切换到中文输入法。此时，敲下刚才的快捷键，然后就可以输入全角标点啦！快试试吧！

# 总结
以上就是没法输入全角标点的解决方法啦。记得点个赞加关注再走噢！

