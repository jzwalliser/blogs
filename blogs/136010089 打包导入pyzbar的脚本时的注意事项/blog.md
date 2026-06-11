@[TOC](目录)

---
> 本文由Jzwalliser原创，发布在CSDN平台上，遵循[CC 4.0 BY-SA](https://creativecommons.org/licenses/by-sa/4.0/deed.zh-hans)协议。
> 因此，若需转载/引用本文，请注明作者并附原文链接。
> 违者必究，谢谢配合。
> 个人主页：[blog.csdn.net/jzwalliser](https://blog.csdn.net/jzwalliser)
# 前言
上次用python写了个二维码扫描器（哈哈顺便推销一下：[制作二维码扫描器](https://blog.csdn.net/jzwalliser/article/details/136005354)），核心功能使用了pyzbar来实现，用于扫描二维码。但是很不幸，在打包的时候出现了一些状况。

# 问题
## 问题的出现
正常来说，如果我们要用pyinstaller以单文件模式打包一个文件，那么肯定是运行`pyinstaller -F --hidden-import <module1> --hidden-import <module2> -i <icon>` 之类的命令。这回也不例外，我运行了：
```
pyinstaller -F -w --hidden-import PIL --hidden-import tkinter --hidden-import pyperclip --hidden-import pyzbar -i icon.ico --add-data=icon_clear.ico:. QRCodeReader.py
```


可是当我双击运行打包好的exe时，却弹出了错误提示：

```
Traceback (most recent call last):
  File "PyInstaller\loader\pyimod03_ctypes.py", line 53, in __init__
  File "ctypes\__init__.py", line 374, in __init__
FileNotFoundError: Could not find module 'libiconv.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "pyzbar\zbar_library.py", line 58, in load
  File "pyzbar\zbar_library.py", line 50, in load_objects
  File "pyzbar\zbar_library.py", line 51, in <listcomp>
  File "ctypes\__init__.py", line 452, in LoadLibrary
  File "PyInstaller\loader\pyimod03_ctypes.py", line 55, in __init__
pyimod03_ctypes.install.<locals>.PyInstallerImportError: Failed to load dynlib/dll 'libiconv.dll'. Most likely this dynlib/dll was not found when the application was frozen.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "PyInstaller\loader\pyimod03_ctypes.py", line 53, in __init__
  File "ctypes\__init__.py", line 374, in __init__
FileNotFoundError: Could not find module 'C:\Users\Lenovo\AppData\Local\Temp\_MEI204842\pyzbar\libiconv.dll' (or one of its dependencies). Try using the full path with constructor syntax.

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "QRCodeReader.py", line 7, in <module>
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 419, in exec_module
  File "pyzbar\pyzbar.py", line 7, in <module>
  File "<frozen importlib._bootstrap>", line 1007, in _find_and_load
  File "<frozen importlib._bootstrap>", line 986, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 680, in _load_unlocked
  File "PyInstaller\loader\pyimod02_importers.py", line 419, in exec_module
  File "pyzbar\wrapper.py", line 151, in <module>
  File "pyzbar\wrapper.py", line 148, in zbar_function
  File "pyzbar\wrapper.py", line 127, in load_libzbar
  File "pyzbar\zbar_library.py", line 60, in load
  File "pyzbar\zbar_library.py", line 50, in load_objects
  File "pyzbar\zbar_library.py", line 51, in <listcomp>
  File "ctypes\__init__.py", line 452, in LoadLibrary
  File "PyInstaller\loader\pyimod03_ctypes.py", line 55, in __init__
pyimod03_ctypes.install.<locals>.PyInstallerImportError: Failed to load dynlib/dll 'C:\\Users\\Lenovo\\AppData\\Local\\Temp\\_MEI204842\\pyzbar\\libiconv.dll'. Most likely this dynlib/dll was not found when the application was frozen.
[3252] Failed to execute script 'QRCodeReader' due to unhandled exception!
```

大概意思是无法加载`pyzbar/libiconv.dll`。什么叫无法加载？我用`pyinstxtract.py`将刚才打包好的exe拆了开来，结果发现里面根本就没有`pyzbar`这个文件夹，更别提`libiconv.dll`了。

此时我脑残似的从网上随便找了一个`libiconv.dll`下载，然后打包进去。可依然没用。

## 解决
再仔细观察抛出的异常，里面有这么一句话：
>Could not find module 'libiconv.dll' (or one of its dependencies).

这下懂了：无法加载`libiconv.dll`可能是因为没有`libiconv.dll`，也可能是因为**缺少`libiconv.dll`的依赖项而导致的**。

此时终于恍然大悟：既然`libiconv.dll`并没有缺失（刚才不是打包进去了嘛），那很可能是因为缺少依赖导致。终于，我在`C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyzbar`下找到了另外一个dll文件：`libzbar-64.dll`。将这个dll文件也打包进去，终于没问题了！

所以，最终那个程序的打包命令是：
```
pyinstaller -F -w --hidden-import PIL --hidden-import tkinter --hidden-import pyperclip --hidden-import pyzbar -i icon.ico --add-data=icon_clear.ico:. --add-data=libiconv.dll:./pyzbar/ --add-data=libzbar-64.dll:./pyzbar/ QRCodeReader.py
```
大家也可以参考一下。

# 总结
所以如果想用pyinstaller打包和pyzbar有关的脚本，请提前将`C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\Lib\site-packages\pyzbar`文件夹下的`libiconv.dll`和 `libzbar-64.dll`复制到工作目录下，并在打包命令中添加`--add-data=libzbar-64.dll:./pyzbar/ --add-data=libiconv.dll:./pyzbar/`两个参数。



