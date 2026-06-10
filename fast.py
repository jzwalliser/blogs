import tkinter
import re
import codecs
import os
root = tkinter.Tk()

def deal():
    url = urlentry.get()
    match = re.search(r'\d+',url)
    print(match.group(0))
    try:
        os.makedirs(f"blogs/{match.group(0)} {titleentry.get()}")
    except FileExistsError:
        pass
    original = codecs.open(f"blogs/{match.group(0)} {titleentry.get()}/blog.md","w","utf-8")
    original.write(md.get(0.0,tkinter.END))
    original.close()
    edit = codecs.open("file.md","w","utf-8")
    edit.write(md.get(0.0,tkinter.END))
    edit.close()
    os.system("python3 csdnfk.py")
    md.delete(0.0,tkinter.END)
    urlentry.delete(0,tkinter.END)
    titleentry.delete(0,tkinter.END)
    
   
    

urlframe = tkinter.Frame(root)
urllabel = tkinter.Label(urlframe,text="URL:")
urlentry = tkinter.Entry(urlframe)
urlframe.pack()
urllabel.grid(row=0,column=0)
urlentry.grid(row=0,column=1,ipadx=400)


titleframe = tkinter.Frame(root)
titlelabel = tkinter.Label(titleframe,text="标题：")
titleentry = tkinter.Entry(titleframe)
titleframe.pack()
titlelabel.grid(row=0,column=0)
titleentry.grid(row=0,column=1,ipadx=400)

md = tkinter.Text(root)
md.pack()

ok = tkinter.Button(root,text="OK",command=deal)
ok.pack()

root.mainloop()
