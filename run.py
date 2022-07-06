# coding=gbk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import scrolledtext
import get_js
import get_json
import get_js_text
# 创建窗口：实例化一个窗口对象。
class TKK:
    def __init__(self):
        self.root = Tk()
        # 窗口大小
        self.root.geometry("1000x600+150+70")
        #  窗口标题
        self.root.title("馒头的<js | json>爬取审计工具")
        self.root.resizable(width=False, height=False)
        canvas = tk.Canvas(self.root, width=1000, height=600, bd=0, highlightthickness=0)
        imgpath = '2.jpg'
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(500, 300, image=photo)
        canvas.pack()

        # url输入框
        url_put = tk.StringVar()
        url_put.set('输入url')
        self.entry1 = Entry(self.root,textvariable=url_put,cursor='arrow',background='gray', font=("宋体", 15),
                            width=30 )
        self.entry1.place(x=0,y=5)
        #获取源代码按钮
        button1 = Button(self.root, text="获取", background='gray',relief=GROOVE,font=("宋体", 12), width=5,command=self.tk_get_js)  # command=textt////command=self.getpoem
        button1.place(x=305,y=2)
        #得到js_number数量
        self.js_number = tk.StringVar()
        self.js_number.set('0')
        self.js_num = Label(self.root,textvariable=self.js_number,background='gray',font=("宋体", 15))
        self.js_num.place(x=360,y=2)

        #js等链接输入框
        js_put = tk.StringVar()
        js_put.set('输入左侧的js路径')
        self.entry2 = Entry(self.root, textvariable=js_put,cursor='arrow', background='gray', font=("宋体", 15),
                            width=30,)
        self.entry2.place(x=500, y=5)
        #爬取js按钮
        button2 = Button(self.root, text="爬取", background='gray',relief=GROOVE,font=("宋体", 12), width=5,command=self.tk_get_js_text)  # command=textt////command=self.getpoem
        button2.place(x=805,y=2)

        #js呈现
        self.js_json="请先获取"
        self.Text=scrolledtext.ScrolledText(self.root,background='gray',cursor='arrow',font=("宋体", 12),fg = 'orange')
        self.Text.place(x=0, y=50, width=300, height=550)

        #爬取js内容
        self.url_js_text = scrolledtext.ScrolledText(self.root,background='gray',cursor='arrow',font=("宋体", 12),fg = '#ffffff')
        self.url_js_text.place(x=310, y=50, width=680, height=550)

        # 显示窗口
        self.root.mainloop()
    #左侧get js
    def tk_get_js(self,):
        url=self.entry1.get()
        name,js,js_num=get_js.get_js(url)
        js_name, json, json_num = get_json.get_json(url)
        self.js_number.set(js_num)
        self.Text.delete('1.0','end')
        for i in range(len(json)):
            self.Text.insert(INSERT,"--"+json[i]+"\n"+"\n")
        for i in range(len(js)):
            self.Text.insert(INSERT,"--"+js[i]+"\n"+"\n")
    #右侧get js text
    def tk_get_js_text(self):
        url = self.entry1.get()
        js_name, js, js_num = get_js.get_js(url)
        if 'http' not in self.entry2.get():
            js_url = "http://"+js_name[0]+"/"+self.entry2.get()
        else:
            js_url = self.entry2.get()
        self.url_js_text.delete('1.0', 'end')
        js_data=get_js_text.get_js_text(js_url)
        self.url_js_text.insert(INSERT,js_data)


if __name__ == '__main__':
    tkk = TKK
    tkk()
