@[TOC](目录)

---

> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)

# 用户选择界面无法登录
正常情况下，若想在GNOME的用户登录界面切换用户，并以root身份登录，那一定是会失败的。所以，需要改变方式。

# 解决
## 1. 切换tty
绝大多数Linux发行版都支持通过快捷键切换tty。所以，按下<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F3</kbd>或者结合其它Function键，可以从<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F1</kbd>试到<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>F6</kbd>，直到找到没有任何图形界面的终端。此时，用root身份登录。（因为是实体机上运行的linux所以没法在控制台中截屏，拍得比较糊）
![](https://i-blog.csdnimg.cn/direct/27eeebf538434822a362c9085f824df8.jpeg)
若不知道root密码，也可以登录普通账户，然后输入`sudo -i`即可进入root身份。

## 2. 启动GNOME桌面
登录root后，输入命令`startx`即可启动GNOME图形化界面。

```bash
$ startx
```

![请添加图片描述](https://i-blog.csdnimg.cn/direct/0984912e27ad48bca774f63762d8a1d0.png)

# 注意事项
登录root之后，注意不要锁屏，锁屏后无法重新解锁屏幕。同样，如果需要切换用户，用<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Fn</kbd>切换。

