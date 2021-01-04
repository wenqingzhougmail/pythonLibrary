from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import csv


def get_time() -> object:
    """
    返回当前时间，作为最后修改时间
    """
    import time
    when_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return when_time


class TeacherLogin():
    def __init__(self, root, password, cmd, name):
        """
        生成管理员的GUI界面
        """
        self.root = root
        self.password = password
        self.cmd = cmd
        self.name = name[0]

        self.teacher = Tk()
        self.teacher.title("管理员登陆界面")
        width = 800
        height = 400
        screenwidth = self.teacher.winfo_screenwidth()
        screenheight = self.teacher.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.teacher.geometry(align_str)  # 设置窗口大小
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.teacher.resizable(width=True, height=True)
        # --------------------------------
        # 设置右上方text输出
        self.teacher_text = Text()
        self.teacher_text.place(relheight=0.20, relwidth=0.55)
        # 设置帮助信息
        Btn_help = Button(self.teacher, text="获取帮助", command=self.get_help)
        Btn_help.place(relx=0.05, rely=0.22)
        #清空文本
        btn_clear = Button(self.teacher, text="清除右侧文本", command=self.delete_text)
        btn_clear.place(relx=0.05, rely=0.85)
        # 设置退出按钮
        Btn_close = Button(self.teacher, text="关闭程序",
                           command= self.teacher.destroy)
        Btn_close.place(relx=0.25, rely=0.22)
        # 随意浏览
        Btn_random_book = Button(self.teacher, text="随机浏览", command=self.list_book)
        Btn_random_book.place(relx=0.05, rely=0.3)

        # 录入书名输入框
        self.add_enter = Entry(self.teacher)
        self.add_enter.place(relx=0.25, rely=0.4, relwidth=0.15)
        # 录入图书
        Btn_add = Button(self.teacher, text="录入图书", command=lambda: self.add_book())
        Btn_add.place(relx=0.05, rely=0.4)
        # 录入图书标签
        borrow_label = Label(self.teacher, text='输入书名:', font=('宋体', 11))
        borrow_label.place(relx=0.15, rely=0.4)
        # 录入IBSN编码输入框
        self.code_enter = Entry(self.teacher)
        self.code_enter.place(relx=0.25, rely=0.5, relwidth=0.15)
        # 录入编码标签
        code_label = Label(self.teacher, text='输入编码:', font=('宋体', 11))
        code_label.place(relx=0.15, rely=0.5)

        # 录入作者标签
        author_label = Label(self.teacher, text='输入作者:', font=('宋体', 11))
        author_label.place(relx=0.15, rely=0.6)
        # 录入作者输入框
        self.author_enter = Entry(self.teacher)
        self.author_enter.place(relx=0.25, rely=0.6, relwidth=0.15)
        # 录入类型标签
        type_label = Label(self.teacher, text='输入类型:', font=('宋体', 11))
        type_label.place(relx=0.15, rely=0.7)
        # 录入类型输入框
        self.type_enter = Entry(self.teacher)
        self.type_enter.place(relx=0.25, rely=0.7, relwidth=0.15)
        # 录入库存标签
        number_label = Label(self.teacher, text='输入库存:', font=('宋体', 11))
        number_label.place(relx=0.15, rely=0.8)
        # 录入类型输入框
        self.number_enter = Entry(self.teacher)
        self.number_enter.place(relx=0.25, rely=0.8, relwidth=0.15)

        # 右侧信息标签
        top_label = Label(self.teacher, text="管理系统",
                          bg="lightblue", fg="red", font=("宋体", 30))
        top_label.place(relx=0.6, rely=0.05, relwidth=0.4)
        # 左侧显示文本框
        self.right_text = Text()
        self.right_text.place(relx=0.45, rely=0.25, relheight=0.78)
        self.teacher.mainloop()

    def get_help(self):
        """
        点击帮助 获得帮助信息
        """
        sss = "这是一个管理图书界面，你可以在这里实现基本的一些功能，浏览图书，添加图书等."
        tkinter.messagebox.askokcancel('小提示', sss)

        s = f"你好, 欢迎 {self.root} 管理员登入该系统, 现在时间{get_time()}\n"
        self.teacher_text.insert(END, s)

    def add_book(self):
        line = [self.add_enter.get(),self.code_enter.get(),self.author_enter.get(),self.type_enter.get(),self.number_enter.get()]
        if len(self.add_enter.get()) == 0 or len(self.code_enter.get()) == 0 or len(self.author_enter.get()) == 0 or len(self.type_enter.get()) == 0 or len(self.number_enter.get()) == 0:
            self.get_tip("输入不能为空！请重新输入")
            return
        if len(self.code_enter.get())!=13:
            self.get_tip("请输入13位的ISBN编码！")
            return
        with open(r'./books.csv', mode='a', newline='', encoding='utf-8') as f:
            csv_file = csv.writer(f)
            csv_file.writerow(line)
            self.get_tip("添加成功")
        with open(r'./books1.csv', mode='a', newline='', encoding='utf-8') as f:
            csv_file = csv.writer(f)
            csv_file.writerow(line)

    def list_book(self):
        self.right_text.insert(END, '书名             ISBN码         作者     类别        库存\n')
        with open('books.csv', 'r', encoding='utf-8') as f:
            book = csv.reader(f)
            for lines in book:
                self.right_text.insert(END, lines)
                self.right_text.insert(END, '\n')
            self.right_text.insert(END, '\n\n')

    def delete_text(self):
        self.right_text.delete(1.0, END)

    def get_tip(self, string):
        """
        接受弹窗提示
        """
        is_ok = tkinter.messagebox.askokcancel("提示", string)
        if is_ok:
            return
        else:
            pass

