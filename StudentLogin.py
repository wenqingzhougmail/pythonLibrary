from tkinter import *
from tkinter import ttk
import tkinter.messagebox
import time
import csv


def get_time() -> object:
    """
    返回当前时间，作为最后修改时间
    """
    when_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return when_time


class StudentLogin():
    """
    学生登陆GUI界面
    """

    def __init__(self, root, password, cmd, name):
        """
        生成学生GUI界面
        """
        self.root = root
        self.password = password
        self.cmd = cmd
        self.name = name[0]
        self.student = Tk()
        self.student.title("学生登入界面")
        width = 800
        height = 400
        # 获取屏幕尺寸以计算布局参数，让窗口位于屏幕中央
        screenwidth = self.student.winfo_screenwidth()
        screenheight = self.student.winfo_screenheight()
        align_str = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)

        self.student.geometry(align_str)  # 设置窗口大小
        # 设置窗口是否可变长、宽，True：可变，False：不可变
        self.student.resizable(width=True, height=True)

        # --------------------------------
        # 设置左上方text输出
        self.student_text = Text()
        self.student_text.place(relheight=0.20, relwidth=0.55)
        # 设置帮助信息
        Btn_help = Button(self.student, text="获取帮助", command=lambda: self.get_help)
        Btn_help.place(relx=0.05, rely=0.24)
        # 设置退出按钮
        Btn_close = Button(self.student, text="关闭程序", command=self.student.destroy)
        #Btn_close = Button(self.student, text="关闭程序", command=self.login)
        Btn_close.place(relx=0.30, rely=0.24)
        # 随意浏览
        Btn_random_book = Button(self.student, text="随机浏览", command=self.list_book)
        Btn_random_book.place(relx=0.05, rely=0.35)

        # 查询图书条件框
        find = ttk.Combobox(self.student)
        find.place(relx=0.13, rely=0.46, relwidth=0.1)
        find['value'] = ('序号查询', '书名查询', '作者查询')
        # 设置默认选项
        find.current(0)
        # 查询输入框
        self.find_enter = Entry(self.student)
        self.find_enter.place(relx=0.25, rely=0.46, relwidth=0.15)
        # 查询图书
        Btn_find = Button(self.student, text="查询图书", command=lambda: self.find_book(find.get(), self.find_enter.get()))
        Btn_find.place(relx=0.05, rely=0.45)
        # 借阅图书标签
        borrow_label = Label(self.student, text='输入书名:', font=('宋体', 11))
        borrow_label.place(relx=0.15, rely=0.56)
        # 借阅图书输入框
        borrow_enter = Entry(self.student)
        borrow_enter.place(relx=0.25, rely=0.56, relwidth=0.15)
        # 借阅图书
        Btn_borrow = Button(self.student, text="借阅图书", command=lambda: self.borrow_book(borrow_enter.get()))
        Btn_borrow.place(relx=0.05, rely=0.55)
        # 归还图书标签
        back_label = Label(self.student, text='输入书名:', font=('宋体', 11))
        back_label.place(relx=0.15, rely=0.66)
        # 归还图书输入框
        back_enter = Entry(self.student)
        back_enter.place(relx=0.25, rely=0.66, relwidth=0.15)
        # 归还图书
        Btn_back = Button(self.student, text="归还图书", command=lambda: self.back_book(back_enter.get()))
        Btn_back.place(relx=0.05, rely=0.65)
        # 借阅书籍查询
        borrow_see = Button(self.student, text="已借图书", command=lambda: self.borrow_see())
        borrow_see.place(relx=0.05, rely=0.75)
        # 已还书籍查询
        return_see = Button(self.student, text="已还图书", command=lambda: self.return_see())
        return_see.place(relx=0.05, rely=0.85)
        # 清空右侧文本框
        btn_clear = Button(self.student, text="清除右侧文本", command=self.delete_text)
        btn_clear.place(relx=0.25, rely=0.85)
        # 右侧信息标签
        self.top_label = Label(self.student, text="学生系统", bg="lightgreen", fg="red", font=("宋体", 30))
        self.top_label.place(relx=0.6, rely=0.05, relwidth=0.4)
        # 右侧显示文本框
        self.right_text = Text()
        self.right_text.place(relx=0.45, rely=0.25, relheight=0.78)
        self.student.mainloop()

    def get_help(self):
        """
        点击帮助 获得帮助信息
        """
        sss = "这是一个学生图书界面，你可以在这里实现基本的一些功能，浏览图书，借阅图书，归还图书，查询图书等"
        tkinter.messagebox.askokcancel('小提示', sss)

        s = f"你好, 欢迎 {self.root} 用户登入该系统, 现在时间{get_time()}\n"
        self.student_text.insert(END, s)

    def list_book(self):
        self.right_text.insert(END, '书名             ISBN码         作者     类别        库存\n')
        with open('books.csv', 'r', encoding='utf-8') as f:
            book = csv.reader(f)
            for lines in book:
                self.right_text.insert(END, lines)
                self.right_text.insert(END, '\n')
            self.right_text.insert(END, '\n\n')

    def find_book(self, find, finder_enter):
        flag = 1
        if find == "书名查询":
            with open('books1.csv', 'r', encoding='utf-8') as f:
                self.right_text.insert(END, '书名       ISBN码    作者    类别    库存\n')
                book = csv.reader(f)
                for line in book:
                    if finder_enter == line[0]:
                        self.right_text.insert(END, line)
                        self.right_text.insert(END, '\n')
                        flag = 0
                if flag:
                    self.get_tip("很抱歉，您所查询的书籍暂时未录入本馆")
                    return
        if find == "序号查询":
            with open('books1.csv', 'r', encoding='utf-8') as f:
                self.right_text.insert(END, '书名       ISBN码    作者    类别    库存\n')
                book = csv.reader(f)
                for line in book:
                    if finder_enter == line[1]:
                        self.right_text.insert(END, line)
                        self.right_text.insert(END, '\n')
                        flag = 0
                if flag:
                    self.get_tip("很抱歉，您所查询的序号对应的书籍暂时未录入本馆")
                    return
        if find == "作者查询":
            with open('books1.csv', 'r', encoding='utf-8') as f:
                self.right_text.insert(END, '书名       ISBN码    作者    类别    库存\n')
                book = csv.reader(f)
                for line in book:
                    if finder_enter == line[2]:
                        self.right_text.insert(END, line)
                        self.right_text.insert(END, '\n')
                        flag = 0
                if flag:
                    self.get_tip("很抱歉，您所查询的作者的书籍暂时未录入本馆")
                    return

    def borrow_book(self, book_name):
        flag = 1
        with open('books1.csv', 'r', encoding='utf-8') as f:
            book = csv.reader(f)
            for line in book:
                if book_name == line[0] and line[4] != '0':
                    flag = 0
                    with open(r'./my_book.csv', mode='r+', newline='', encoding='utf-8') as f1:
                        book1 = csv.reader(f1)
                        for line1 in book1:
                            if book_name == line1[0]:
                                self.get_tip("您已经借阅该书籍，请勿重复借阅")
                                return
                        csv_file = csv.writer(f1)
                        del(line[-1])
                        csv_file.writerow(line)
                    self.get_tip("借阅成功，请您按时归还书籍")
            if flag:
                self.get_tip("抱歉，您要借阅的书籍未录入本馆或者被借完")

    def back_book(self, book_name):
        flag = 1
        with open('my_book.csv', 'r', encoding='utf-8') as f:
            book = csv.reader(f)
            for line in book:
                if book_name == line[0]:
                    flag = 0
                    with open(r'./my_book1.csv', mode='r+', newline='', encoding='utf-8') as f1:
                        book1 = csv.reader(f1)
                        for line1 in book1:
                            if book_name == line1[0]:
                                self.get_tip("您已经归还该书籍，请勿重复归还")
                                return
                        csv_file = csv.writer(f1)
                        csv_file.writerow(line)
                    self.get_tip("归还成功")
                    #with open('my_book1.csv', 'a+', encoding='utf-8') as f1:
            if flag:
                self.get_tip("您并未借阅此书")

    def borrow_see(self):
        self.right_text.insert(END, '您借阅的书籍信息如下\n')
        with open('my_book.csv', 'r', encoding='utf-8') as f:
            self.right_text.insert(END, '\n')
            book = csv.reader(f)
            for lines in book:
                self.right_text.insert(END, lines)
                self.right_text.insert(END, '\n')
            self.right_text.insert(END, '\n\n')

    def return_see(self):
        self.right_text.insert(END, '您归还的书籍信息如下\n')
        with open('my_book1.csv', 'r', encoding='utf-8') as f:
            self.right_text.insert(END, '\n')
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






