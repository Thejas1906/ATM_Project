import pandas as pd
import tkinter.messagebox
from tkinter import *
from tkinter import ttk

class atm:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "ATM System")
        self.root.geometry('790x760+280+0')
        self.root.configure(background ='yellow')

#=================================Frame=========================================#
        MainFrame = Frame(self.root, bd=20, width=780, height=700, relief=RIDGE)
        MainFrame.grid()

        TopFrame1 = Frame(MainFrame, bd=7, width=780, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        TopFrame2 = Frame(MainFrame, bd=7, width=780, height=300, relief=RIDGE)
        TopFrame2.grid(row=0, column=0, padx=8)

        TopFrame2Left = Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Left.grid(row=0, column=0, padx=3)

        TopFrame2Mid = Frame(TopFrame2, bd=5, width=500, height=300, relief=RIDGE)
        TopFrame2Mid.grid(row=0, column=1, padx=3)

        TopFrame2Right= Frame(TopFrame2, bd=5, width=190, height=300, relief=RIDGE)
        TopFrame2Right.grid(row=0, column=2, padx=3)

#============================Functions==========================================#

        def start():
            self.txtRecipt.insert(END, '\n\nLogin To Registered account :-' + "\n\n\n\n")
            self.txtRecipt.insert(END, 'Register A New Account:- ' + "\n\n\n\n")

        def btnltra():
            cls()
            submit1()

        def btnrana():
            cls()
            self.txtRecipt.insert(END, '\nEnter Your Name :')
            self.txtRecipt.insert(END, '\nEnter Your Account Number:')
            self.txtRecipt.insert(END, '\nSet Your PIN Number:')
            self.txtRecipt.insert(END, '\nEnter Your Phone Number:')
            self.txtRecipt.insert(END, '\nEnter Your Frist Deposit Amount :')


#============================Numbers============================================#

        def insert0():
            value0=0
            self.txtRecipt.insert(END,value0)

        def insert1():
            value1=1
            self.txtRecipt.insert(END,value1)

        def insert2():
            value2=2
            self.txtRecipt.insert(END, value2)

        def insert3():
            value3=3
            self.txtRecipt.insert(END, value3)

        def insert4():
            value4=4
            self.txtRecipt.insert(END, value4)

        def insert5():
            value5=5
            self.txtRecipt.insert(END, value5)

        def insert6():
            value6=6
            self.txtRecipt.insert(END, value6)

        def insert7():
            value7=7
            self.txtRecipt.insert(END, value7)

        def insert8():
            value8=8
            self.txtRecipt.insert(END, value8)

        def insert9():
            value9=9
            self.txtRecipt.insert(END, value9)

        def cancel():
            cancel = tkinter.messagebox.askyesno("ATM","Do You Want To Exit ?")
            if cancel == 1:
                self.root.destroy()
                return

        def cls():
            self.txtRecipt.delete("1.0", END)

        def submit1():
            AccNo_var = StringVar()
            PIN_var = IntVar()

            AccNo = AccNo_var.get()
            PIN = PIN_var.get()

            AccNo_var.set("")
            PIN_var.set("")

            AccNo_label = Label(root, text='Enter Your Account Number :', font=('arial', 10, 'bold'))
            AccNo_entry = Entry(root, textvariable=AccNo_var, font=('arial', 10, 'normal'))
            PIN_label = Label(root, text='Enter Your PIN Number :', font=('arial', 10, 'bold'))
            PIN_entry = Entry(root, textvariable=PIN_var, font=('arial', 10, 'normal'), show='*')

            AccNo_label.grid(row=0, column=0)
            AccNo_entry.grid(row=0, column=1)
            PIN_label.grid(row=1, column=0)
            PIN_entry.grid(row=1, column=1)


#=======================CenterScreen(Widgets)===================================#
        self.txtRecipt = Text(TopFrame2Mid, height = 17, width = 42, bd=12, font=('arial',11,'bold'))
        self.txtRecipt.grid(row=0,column=0)

#=============================LeftArrow(Widgets)================================#
        self.img_arrow_Left = PhotoImage(file= "C:\IP PICS\lArrow.png")
        self.root.btnArrowL1=Button(TopFrame2Left, width=120, height=60, state=NORMAL,command= btnltra,
        image=self.img_arrow_Left).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowL2 = Button(TopFrame2Left, width=120, height=60, state=NORMAL,command= btnrana,
        image=self.img_arrow_Left).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowL3 = Button(TopFrame2Left, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Left).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowL4=Button(TopFrame2Left, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Left).grid(row=3, column=0, padx=2, pady=2)

#==========================RightArrow(Widgets)==================================#
        self.img_arrow_Right = PhotoImage(file= "C:\IP PICS\dArrow.png")
        self.btnArrowR1=Button(TopFrame2Right, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Right).grid(row=0, column=0, padx=2, pady=2)

        self.btnArrowR2 = Button(TopFrame2Right, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Right).grid(row=1, column=0, padx=2, pady=2)

        self.btnArrowR3 = Button(TopFrame2Right, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Right).grid(row=2, column=0, padx=2, pady=2)

        self.btnArrowR4=Button(TopFrame2Right, width=120, height=60, state=NORMAL,
        image=self.img_arrow_Right).grid(row=3, column=0, padx=2, pady=2)

#=============================Number Pad(Widgets)===============================#
#=============================ROW ONE===========================================#
        self.img1 = PhotoImage(file= "C:\IP PICS\one.png")
        self.btn1=Button(TopFrame1, width=160, height=60,command= insert1,
        image=self.img1).grid(row=2, column=0, padx=6, pady=4)

        self.img2 = PhotoImage(file="C:\IP PICS\dtwo.png")
        self.btn2 = Button(TopFrame1, width=160, height=60,command= insert2,
        image=self.img2).grid(row=2, column=1, padx=6, pady=4)

        self.img3 = PhotoImage(file="C:\IP PICS\dthree.png")
        self.btn3 = Button(TopFrame1, width=160, height=60,command= insert3,
        image=self.img3).grid(row=2, column=2, padx=6, pady=4)

        self.imgCL = PhotoImage(file="C:\IP PICS\cancel.png")
        self.btnCL = Button(TopFrame1, width=160, height=60,command= cancel,
        image=self.imgCL).grid(row=2, column=3, padx=6, pady=4)

#================================ROW TWO========================================#
        self.img4 = PhotoImage(file="C:\IP PICS\dfour.png")
        self.btn4 = Button(TopFrame1, width=160, height=60,command= insert4,
        image=self.img4).grid(row=3, column=0, padx=6, pady=4)

        self.img5 = PhotoImage(file="C:\IP PICS\dfive.png")
        self.btn5= Button(TopFrame1, width=160, height=60,command= insert5,
        image=self.img5).grid(row=3, column=1, padx=6, pady=4)

        self.img6 = PhotoImage(file="C:\IP PICS\dsix.png")
        self.btn6 = Button(TopFrame1, width=160, height=60,command= insert6,
        image=self.img6).grid(row=3, column=2, padx=6, pady=4)

        self.imgCLR = PhotoImage(file="C:\IP PICS\clear.png")
        self.btnCLR = Button(TopFrame1, width=160, height=60,
        image=self.imgCLR).grid(row=3, column=3, padx=6, pady=4)

#=========================ROW THREE=============================================#
        self.img7 = PhotoImage(file="C:\IP PICS\dseven.png")
        self.btn7 = Button(TopFrame1, width=160, height=60,command= insert7,
        image=self.img7).grid(row=4, column=0, padx=6, pady=4)

        self.img8 = PhotoImage(file="C:\IP PICS\deight.png")
        self.btn8 = Button(TopFrame1, width=160, height=60,command= insert8,
        image=self.img8).grid(row=4, column=1, padx=6, pady=4)

        self.img9 = PhotoImage(file="C:\IP PICS\dnine.png")
        self.btn9 = Button(TopFrame1, width=160, height=60,command= insert9,
        image=self.img9).grid(row=4, column=2, padx=6, pady=4)

        self.imgETR = PhotoImage(file="C:\IP PICS\enter.png")
        self.btnETR = Button(TopFrame1, width=160, height=60,
        image=self.imgETR).grid(row=4, column=3, padx=6, pady=4)

#================================ROW FOUR======================================#

        self.img0 = PhotoImage(file="C:\IP PICS\zero.png")
        self.btnETR = Button(TopFrame1, width=160, height=60,command= insert0,
        image=self.img0).grid(row=5, column=1, padx=6, pady=4)


        self.imgSTR = PhotoImage(file="C:\IP PICS\start.png")
        self.btnMT = Button(TopFrame1, width=160, height=60,command= start,
        image=self.imgSTR).grid(row=5, column=3, padx=6, pady=4)

#=================================Number Pad End================================#
#===================================Main========================================#

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()

#self.txtRecipt.insert(END, '\nWithdraw :-' + "\n\n\n\n\n")
#self.txtRecipt.insert(END, 'Check Balance :-' + "\n\n\n\n\n")
#self.txtRecipt.insert(END, 'Deposit :-' + "\n\n\n\n\n")
#self.txtRecipt.insert(END, 'Set New PIN Number :-')
