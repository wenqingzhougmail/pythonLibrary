from tkinter import *
import csv
import tkinter.messagebox
#import pandas as pd
class Register():
    """
    注册人员信息
    生成一个注册GUI窗口
    """

    def __init__(self, db_people):
        # db_people 表示什么人注册
        self.db_people = db_people
        print(self.db_people)
        # 下面开始搭建一个注册GUI界面
        self.reg = Tk()
        self.reg.title("注册界面")
        width = 800
        height = 400
        # 获取屏幕尺寸以计算布局参数，让窗口位于屏幕中央
        screenwidth = self.reg.winfo_screenwidth()
        screenheight = self.reg.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.reg.geometry(align_str)  # 设置窗口大小
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.reg.resizable(width=True, height=True)
        # 注册标签
        reg_label = Label(self.reg, text
        =self.db_people, font=("宋体", 30))
        reg_label.place(relx=0.4, rely=0.1)
        # 生成常用控件
        self.root = Label(self.reg, text="账号:",
                          font=("宋体", 12))
        self.root.place(relx=0.4, rely=0.3)

        self.password1 = Label(self.reg, text="密码:", font=("宋体", 12))
        self.password1.place(relx=0.4, rely=0.4)

        # 生成对应输入框
        self.root_enter = Entry(self.reg)
        self.root_enter.place(relx=0.45, rely=0.3)
        self.password_enter = Entry(self.reg)
        self.password_enter.place(relx=0.45, rely=0.4)

        # 生成注册按钮
        reg_btn = Button(self.reg, text="注册", command=self.start_reg)
        reg_btn.place(relx=0.5, rely=0.6)
        # 生成返回按钮
        return_btn = Button(self.reg, text="返回", command=self.reg.destroy)
        return_btn.place(relx=0.6, rely=0.6)
        self.reg.mainloop()

    def start_reg(self):
        row = [self.root_enter.get(), self.password_enter.get()]
        with open('user.csv', 'r', encoding='utf-8') as f:
            a = csv.reader(f)
            b = [i[0] for i in a]
            if self.root_enter.get() in b:
                self.get_tip("该账户已被注册")
                return FALSE
        with open(r'./user.csv', mode='a', newline='', encoding='utf-8') as f:
            csv_file = csv.writer(f)
            csv_file.writerow(row)
        self.get_tip("注册成功")

    def get_tip(self, string):
        """
        接受弹窗提示
        """
        is_ok = tkinter.messagebox.askokcancel("提示", string)
        if is_ok:
            self.root_enter.delete(0, END)
            self.password_enter.delete(0, END)
        else:
            pass