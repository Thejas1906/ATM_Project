from tools import *
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

        # Bottom
        TopFrame1 = Frame(MainFrame, bd=7, width=780, height=300, relief=RIDGE)
        TopFrame1.grid(row=1, column=0, padx=12)
        
        # Top
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

        def CurrentEntry():
            widgetSelected = str(root.focus_get()).split('.')[-1][1:]
            print(widgetSelected)

            if(widgetSelected == "entry"):
                return AccNo_entry
            if (widgetSelected == "entry2"):
                return PIN_entry

#============================Numbers============================================#

        # numpad keys function
        def insert(num):
            CurrentText = CurrentEntry().get()

            # Inserting a number based on button pressed (num)
            CurrentEntry().delete(0, END)
            CurrentEntry().insert(0, CurrentText + str(num))

        def cancel():
            cancel = tkinter.messagebox.askyesno("ATM","Do You Want To Exit ?")
            if cancel == 1:
                self.root.destroy()
                return

        # Only for txtRecipt
        def cls():
            self.txtRecipt.delete("1.0", END)

        def submit1():
            global AccNo_entry
            global PIN_entry

            AccNo_var = IntVar()
            PIN_var = IntVar()

            AccNo = AccNo_var.get()
            PIN = PIN_var.get()

            AccNo_label = Label(TopFrame2Mid, text='Enter Account Number :', font=('arial', 10, 'bold'))
            AccNo_entry = Entry(TopFrame2Mid, textvariable=AccNo_var, font=('arial', 10, 'normal'))
            PIN_label = Label(TopFrame2Mid, text='Enter PIN Number :', font=('arial', 10, 'bold'))
            PIN_entry = Entry(TopFrame2Mid, textvariable=PIN_var, font=('arial', 10, 'normal'))

            AccNo_label.place(x=20, y=30)
            AccNo_entry.place(x=20, y=60)

            PIN_label.place(x=20, y=100)
            PIN_entry.place(x=20, y=130)



#=======================CenterScreen(Widgets)===================================#

        # Main Text Widget
        self.txtRecipt = Text(TopFrame2Mid, height = 17, width = 42, bd=12, font=('arial',11,'bold'))
        self.txtRecipt.grid(row=0,column=0)

#=============================LeftArrow(Widgets)================================#

        # Left Arrow Image
        self.img_ArrowL = PhotoImage(file= "resources/images/LeftArrow.png")

        # Left Arrow Buttons
        self.btnArrowL1=Button(TopFrame2Left, width=120, height=60, state=NORMAL,command= btnltra, image=self.img_ArrowL).grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowL2 = Button(TopFrame2Left, width=120, height=60, state=NORMAL,command= btnrana, image=self.img_ArrowL).grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowL3 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, image=self.img_ArrowL).grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowL4=Button(TopFrame2Left, width=120, height=60, state=NORMAL, image=self.img_ArrowL).grid(row=3, column=0, padx=2, pady=2)

#==========================RightArrow(Widgets)==================================#

        # Right Arrow Image
        self.img_ArrowR = PhotoImage(file= "resources/images/RightArrow.png")

        # Right Arrow Buttons
        self.btnArrowR1=Button(TopFrame2Right, width=120, height=60, state=NORMAL, image=self.img_ArrowR).grid(row=0, column=0, padx=2, pady=2)
        self.btnArrowR2 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, image=self.img_ArrowR).grid(row=1, column=0, padx=2, pady=2)
        self.btnArrowR3 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, image=self.img_ArrowR).grid(row=2, column=0, padx=2, pady=2)
        self.btnArrowR4=Button(TopFrame2Right, width=120, height=60, state=NORMAL, image=self.img_ArrowR).grid(row=3, column=0, padx=2, pady=2)

#=============================Number Pad(Widgets)===============================#

        # Row 1 Images
        self.img_1 = PhotoImage(file="resources/images/NumOne.png")
        self.img_2 = PhotoImage(file="resources/images/NumTwo.png")
        self.img_3 = PhotoImage(file="resources/images/NumThree.png")
        self.img_CANCEL = PhotoImage(file="resources/images/test1.png")

        # Row 1 Buttons
        self.btn_1=Button(TopFrame1, width=160, height=60, command= lambda: insert(1), image=self.img_1).grid(row=2, column=0, padx=6, pady=4)
        self.btn_2 = Button(TopFrame1, width=160, height=60, command= lambda: insert(2), image=self.img_2).grid(row=2, column=1, padx=6, pady=4)
        self.btn_3 = Button(TopFrame1, width=160, height=60, command= lambda: insert(3), image=self.img_3).grid(row=2, column=2, padx=6, pady=4)
        self.btn_CANCEL = Button(TopFrame1, width=160, height=60, command=cancel, image=self.img_CANCEL).grid(row=2, column=3, padx=6, pady=4)



        # Row 2 Images
        self.img_4 = PhotoImage(file="resources/images/NumFour.png")
        self.img_5 = PhotoImage(file="resources/images/NumFive.png")
        self.img_6 = PhotoImage(file="resources/images/NumSix.png")
        self.img_CLEAR = PhotoImage(file="resources/images/test1.png")

        # Row 2 Buttons
        self.btn_4 = Button(TopFrame1, width=160, height=60, command= lambda: insert(4), image=self.img_4).grid(row=3, column=0, padx=6, pady=4)
        self.btn_5= Button(TopFrame1, width=160, height=60, command= lambda: insert(5), image=self.img_5).grid(row=3, column=1, padx=6, pady=4)
        self.btn_6 = Button(TopFrame1, width=160, height=60, command= lambda: insert(6), image=self.img_6).grid(row=3, column=2, padx=6, pady=4)
        self.btn_CLEAR = Button(TopFrame1, width=160, height=60, image=self.img_CLEAR).grid(row=3, column=3, padx=6, pady=4)



        # Row 3 Images
        self.img_7 = PhotoImage(file="resources/images/NumSeven.png")
        self.img_8 = PhotoImage(file="resources/images/NumEight.png")
        self.img_9 = PhotoImage(file="resources/images/NumNine.png")
        self.img_ENTER = PhotoImage(file="resources/images/test1.png")

        # Row 3 Buttons
        self.btn_7 = Button(TopFrame1, width=160, height=60, command= lambda: insert(7), image=self.img_7).grid(row=4, column=0, padx=6, pady=4)
        self.btn_8 = Button(TopFrame1, width=160, height=60, command= lambda: insert(8), image=self.img_8).grid(row=4, column=1, padx=6, pady=4)
        self.btn_9 = Button(TopFrame1, width=160, height=60, command= lambda: insert(9), image=self.img_9).grid(row=4, column=2, padx=6, pady=4)
        self.btn_ENTER = Button(TopFrame1, width=160, height=60, image=self.img_ENTER).grid(row=4, column=3, padx=6, pady=4)



        # Row 4 Images
        self.img_0 = PhotoImage(file="resources/images/NumZero.png")
        self.img_START = PhotoImage(file="resources/images/Start.png")

        # Row 4 Buttons
        self.btn_0 = Button(TopFrame1, width=160, height=60, command= lambda: insert(0), image=self.img_0).grid(row=5, column=1, padx=6, pady=4)
        self.btn_START = Button(TopFrame1, width=160, height=60, command=start, image=self.img_START).grid(row=5, column=3, padx=6, pady=4)

#=================================Number Pad End================================#

#===================================Main========================================#

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
