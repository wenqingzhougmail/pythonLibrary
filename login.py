from tkinter import *
from tkinter import ttk
import time
import csv
from StudentLogin import StudentLogin
from TeacherLogin import TeacherLogin
from Register import Register

# 获取当前时间


class Login():
    """
    登陆界面
    """
    def __init__(self):
        self.login = Tk()
        width = 800
        height = 400
        self.login.title('登入系统')
        screenwidth = self.login.winfo_screenwidth()
        screenheight = self.login.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.login.geometry(align_str)  # 设置窗口大小

        self.login.resizable(width=True, height=True)

        # 设置窗口是否可变长、宽，True：可变，False：不可变
        label_0 = Label(self.login, text="欢迎来到图书管理系统", bg="wheat", fg="black", font=("宋体", 30))
        label_0.place(relx=0.28, rely=0.15)

        # 定义账号密码标签
        label_root = Label(self.login, text="账号:", font=("宋体", 20))
        label_root.place(relx=0.20, rely=0.30)
        label_password = Label(self.login, text="密码:", font=("宋体", 20))  # 定义密码
        label_password.place(relx=0.20, rely=0.40)

        # 登入账号密码
        self.inp_root = Entry(self.login)  # 定义第一个输入框
        self.inp_root.place(relx=0.35, rely=0.31, relwidth=0.2, relheight=0.08)
        self.inp_password = Entry(self.login, show="*", )  # 定义第二个输入框  且密码隐藏
        self.inp_password.place(relx=0.35, rely=0.41, relwidth=0.2, relheight=0.08)

        label_type = Label(self.login, text='登入方式:', font=("宋体", 10))
        label_type.place(relx=0.23, rely=0.56)
        # 创建下拉框 选择登入方式
        cmb = ttk.Combobox(self.login)
        cmb.place(relx=0.35, rely=0.55, relwidth=0.2)
        cmb['value'] = ('管理员登入', '学生登入')
        # 设置默认选项
        cmb.current(0)
        # 触发事件
        btn_login = Button(self.login, text="登入",
                           command=lambda:
                           self.start(cmb.get(), self.inp_root.get(), self.inp_password.get()))
        btn_login.place(relx=0.6, rely=0.54)
        # 注册调试
        reg_type = Label(self.login, text='注册方式:', font=("宋体", 10))
        reg_type.place(relx=0.23, rely=0.66)
        # 成员注册
        reg = ttk.Combobox(self.login)
        reg.place(relx=0.35, rely=0.65, relwidth=0.2)
        reg['value'] = ('管理员注册', '学生注册')
        # 设置默认选项
        reg.current(0)
        # 触发事件
        reg_login = Button(self.login, text="注册",
                           command=lambda: self.reg_login(reg.get()))
        reg_login.place(relx=0.6, rely=0.64)

        # 关闭程序
        bt_close = Button(self.login, text="关闭程序",
                          command=self.login.destroy)
        bt_close.place(relx=0.7, rely=0.64)
        # 与我联系
        label_me = Label(self.login, text="欢迎联系作者", font=("楷体", 15))
        label_me.place(relx=0.26, rely=0.75)
        #label_me1 = Label(self.login, text="班级：自实1901", font=("楷体", 15))
        #label_me1.place(relx=0.26, rely=0.82)
        label_me2 = Label(self.login, text="作者qq：2675319752", font=("楷体", 15))
        label_me2.place(relx=0.26, rely=0.84)
        time.strftime("%H:%M:%S")
        self.label_time = Label(self.login, text=" ", fg="blue", font=("楷体", 20))
        self.label_time.place(relx=0.20, rely=0.02)
        self.gettime()
        label_timetip = Label(self.login, text="现在时间：", fg="blue", font=("楷体", 20))
        label_timetip.place(relx=0.02, rely=0.02)
        self.login.mainloop()

    def gettime(self):
        timestr = time.strftime("%H:%M:%S")
        self.label_time.configure(text=timestr)
        self.login.after(1000, self.gettime)

    #登录按钮
    def start(self, cmd, root, password):
        """
        在这里进行登入方式的判断 以及账号的判断
        """
        if "学生登入" == cmd:
            if self.test_db(root, password):
                self.login.destroy()  # 关闭
                names = self.get_name(root)
                StudentLogin(root, password, 'student', names)
        elif cmd == "管理员登入":
            if self.test_db(root, password):
                self.login.destroy()
                names = self.get_name(root)
                TeacherLogin(root, password, 'teacher', names)

    def test_db(self, root, password):
        with open('user.csv', 'r', encoding='utf-8') as f:
            users = csv.reader(f)
            if [root, password] in users:
                return TRUE

    def get_name(self, root):
        return root

    def reg_login(self, reg):
        """注册信息
        reg  表示 什么人注册
        """
        Register(reg)


Login()