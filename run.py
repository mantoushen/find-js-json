# coding=gbk
from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from tkinter import scrolledtext
import get_js
import get_json
import get_js_text
# �������ڣ�ʵ����һ�����ڶ���
class TKK:
    def __init__(self):
        self.root = Tk()
        # ���ڴ�С
        self.root.geometry("1000x600+150+70")
        #  ���ڱ���
        self.root.title("��ͷ��<js | json>��ȡ��ƹ���")
        self.root.resizable(width=False, height=False)
        canvas = tk.Canvas(self.root, width=1000, height=600, bd=0, highlightthickness=0)
        imgpath = '2.jpg'
        img = Image.open(imgpath)
        photo = ImageTk.PhotoImage(img)
        canvas.create_image(500, 300, image=photo)
        canvas.pack()

        # url�����
        url_put = tk.StringVar()
        url_put.set('����url')
        self.entry1 = Entry(self.root,textvariable=url_put,cursor='arrow',background='gray', font=("����", 15),
                            width=30 )
        self.entry1.place(x=0,y=5)
        #��ȡԴ���밴ť
        button1 = Button(self.root, text="��ȡ", background='gray',relief=GROOVE,font=("����", 12), width=5,command=self.tk_get_js)  # command=textt////command=self.getpoem
        button1.place(x=305,y=2)
        #�õ�js_number����
        self.js_number = tk.StringVar()
        self.js_number.set('0')
        self.js_num = Label(self.root,textvariable=self.js_number,background='gray',font=("����", 15))
        self.js_num.place(x=360,y=2)

        #js�����������
        js_put = tk.StringVar()
        js_put.set('��������js·��')
        self.entry2 = Entry(self.root, textvariable=js_put,cursor='arrow', background='gray', font=("����", 15),
                            width=30,)
        self.entry2.place(x=500, y=5)
        #��ȡjs��ť
        button2 = Button(self.root, text="��ȡ", background='gray',relief=GROOVE,font=("����", 12), width=5,command=self.tk_get_js_text)  # command=textt////command=self.getpoem
        button2.place(x=805,y=2)

        #js����
        self.js_json="���Ȼ�ȡ"
        self.Text=scrolledtext.ScrolledText(self.root,background='gray',cursor='arrow',font=("����", 12),fg = 'orange')
        self.Text.place(x=0, y=50, width=300, height=550)

        #��ȡjs����
        self.url_js_text = scrolledtext.ScrolledText(self.root,background='gray',cursor='arrow',font=("����", 12),fg = '#ffffff')
        self.url_js_text.place(x=310, y=50, width=680, height=550)

        # ��ʾ����
        self.root.mainloop()
    #���get js
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
    #�Ҳ�get js text
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
