# from tools import *
import matplotlib.pyplot as plt
import pandas as pd
import tkinter.messagebox
from tkinter import *
import data
import tools_GUI

class atm:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "ATM System")
        self.root.geometry('790x654+580+140')
        self.root.configure(background ='yellow')

        self.entryList = []

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

        def DestroyWidgets():
            if(self.screen == "welcome"):
                self.WelcomeMSG_Main.destroy()
                self.WelcomeMSG_Sub.destroy()
            elif(self.screen == "login or register"):
                self.login_label.destroy()
                self.register_label.destroy()
            elif(self.screen == "login"):
                self.AccNo_label.destroy()
                self.AccNo_entry.destroy()
                self.PIN_label.destroy()
                self.PIN_entry.destroy()
                try:
                    self.PopUpLabel.destroy()
                except:
                    pass
            elif(self.screen == "register"):
                self.AccNo_label.destroy()
                self.AccNo_entry.destroy()
                self.PIN_label.destroy()
                self.PIN_entry.destroy()
                self.AccName_label.destroy()
                self.AccName_entry.destroy()
                self.PhNo_label.destroy()
                self.PhNo_entry.destroy()
                try:
                    self.PopUpLabel.destroy()
                except:
                    pass
            elif(self.screen == "user"):
                self.withdraw_label.destroy()
                self.deposit_label.destroy()
                self.History_label.destroy()
                self.changePIN_label.destroy()
                self.user_label.destroy()
                self.balance_label.destroy()
            elif(self.screen == "withdraw"):
                self.withdraw_label.destroy()
                self.withdraw_entry.destroy()
                self.balance_label.destroy()
            elif(self.screen == "deposit"):
                self.dep_label.destroy()
                self.dep_entry.destroy()
                self.balance_label.destroy()
            elif(self.screen == "changePIN"):
                self.cpo_label.destroy()
                self.cpo_entry.destroy()
                self.cpn_label.destroy()
                self.cpn_entry.destroy()
            elif(self.screen == "History"):
                self.wd_label.destroy()
                self.deposit_label.destroy()

                
                
        def start():
            DestroyWidgets()
            self.screen = "login or register"

            self.login_label = Label(TopFrame2Mid, text="Login", font=('arial', 20, 'bold'))
            self.register_label = Label(TopFrame2Mid, text="Register", font=('arial', 20, 'bold'))
            
            self.login_label.place(x=15, y=15)
            self.register_label.place(x=15, y=85)

        def CurrentEntry():
            widgetSelected = root.focus_get()


            for entry in self.entryList:
                if(widgetSelected == entry):
                    return entry

           
            
#============================Numbers============================================#

        # numpad keys function

        def clear():
            try:
                CurrentEntry().delete(0, END)
            except:
                print("No entry selected")
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

        def UserPanel(AccNo):
            DestroyWidgets()
            self.screen = "user"

            self.user_label = Label(TopFrame2Mid, text=f"{data.getName(self.AccNo)}'s User Panel")
            self.balance_label = Label(TopFrame2Mid, text=f"Balance: {data.getBalance(self.AccNo)}", font=('arial', 10))

            self.withdraw_label = Label(TopFrame2Mid, text="Withdraw", font=('arial', 20, 'bold'))
            self.deposit_label = Label(TopFrame2Mid, text="Deposit", font=('arial', 20, 'bold'))
            self.History_label = Label(TopFrame2Mid, text="Transaction History", font=('arial', 20, 'bold'))
            self.changePIN_label = Label(TopFrame2Mid, text="Change PIN", font=('arial', 20, 'bold'))

            self.user_label.place(x=5, y=5)
            self.balance_label.place(x=5, y=28)
                
            self.withdraw_label.place(x=258, y=15)
            self.deposit_label.place(x=280, y=85)
            self.History_label.place(x=120, y=155)
            self.changePIN_label.place(x=225, y=225)

        def enter():
            if(self.screen == "login"):
                self.AccNo = int(str(self.AccNo_entry.get()).strip())
                self.Pin = int(str(self.PIN_entry.get()).strip())
                
                if(data.login(AccNo=self.AccNo, Pin=self.Pin) == "Success"):
                    UserPanel(self.AccNo)
                elif(data.login(AccNo=self.AccNo, Pin=self.Pin) == "No Data"):
                    tkinter.messagebox.showwarning("Not Found", "No such account exists")
            elif(self.screen == "register"):
                self.AccNo = int(str(self.AccNo_entry.get()).strip())
                self.Pin = int(str(self.PIN_entry.get()).strip())
                self.Name = str(self.AccName_entry.get()).strip()
                self.PhNo = int(str(self.PhNo_entry.get()).strip())

                AccNo_check = tools_GUI.CheckInt(self.AccNo, digit=8)
                Pin_check = tools_GUI.CheckInt(self.Pin, digit=4)
                AccName_check = tools_GUI.CheckSTR(self.Name)
                PhNo_check = tools_GUI.CheckInt(self.PhNo, digit=10)
                
                if(AccNo_check == "Int" and Pin_check == "Int" and AccName_check == "STR" and PhNo_check == "Int"):
                    if(data.register(self.AccNo, self.Pin, self.Name, self.PhNo) == "Success"):
                        UserPanel(self.AccNo)
                    elif(data.register(self.AccNo, self.Pin, self.Name, self.PhNo) == "Already Exists"):
                        tkinter.messagebox.showwarning("Already Exists", "An account with this account number already exists")
                elif(AccNo_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 8 digit account number")
                elif(Pin_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 4 digit pin number")
                elif(PhNo_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 10 digit phone number")
                elif(AccName_check == "Non STR"):
                    tkinter.messagebox.showwarning("Text Error", "Enter an alphabetical value")


            elif(self.screen == "changePIN"):
                self.cpo = int(self.cpo_entry.get())
                self.cpn = int(self.cpn_entry.get())
                data.changePIN(self.AccNo, self.cpo, self.cpn)
                tkinter.messagebox.showinfo("Alert", "Successfully changed your PIN!")
                UserPanel(self.AccNo)

            elif(self.screen == "withdraw"):
                data.withdraw(self.AccNo, int(self.withdraw_entry.get()))
                tkinter.messagebox.showinfo("Alert", f"Successfully withdrawed ${self.withdraw_entry.get()}")
                UserPanel(self.AccNo)
            elif(self.screen == "deposit"):
                data.deposit(self.AccNo, int(self.dep_entry.get()))
                tkinter.messagebox.showinfo("Alert", f"Successfully deposited ${self.dep_entry.get()}")
                UserPanel(self.AccNo)

        
        def arrow(num):
            match(num):
                case 1:      
                    if(self.screen == "login or register"):
                        DestroyWidgets()
                        self.screen = "login"

                        self.AccNo_label = Label(TopFrame2Mid, text='Enter Account Number :', font=('arial', 10, 'bold'))
                        self.AccNo_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))
                        self.PIN_label = Label(TopFrame2Mid, text='Enter PIN Number :', font=('arial', 10, 'bold'))
                        self.PIN_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.AccNo_label.place(x=15, y=15)
                        self.AccNo_entry.place(x=15, y=40)

                        self.PIN_label.place(x=15, y=85)
                        self.PIN_entry.place(x=15, y=110)

                        self.entryList.append(self.AccNo_entry)
                        self.entryList.append(self.PIN_entry)
                    if(self.screen == "user"):
                        pass

                case 2:
                    if(self.screen == "login or register"):
                        DestroyWidgets()
                        self.screen = "register"

                        self.AccNo_label = Label(TopFrame2Mid, text='Set Account Number :', font=('arial', 10, 'bold'))
                        self.AccNo_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))
                        self.PIN_label = Label(TopFrame2Mid, text='Set PIN Number :', font=('arial', 10, 'bold'))
                        self.PIN_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))
                        self.AccName_label = Label(TopFrame2Mid, text="Enter Your Name :", font=('arial', 10, 'bold'))
                        self.AccName_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))
                        self.PhNo_label = Label(TopFrame2Mid, text="Enter Phone Number :", font=('arial', 10, 'bold'))
                        self.PhNo_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.AccNo_label.place(x=15, y=15)
                        self.AccNo_entry.place(x=15, y=40)
                        self.PIN_label.place(x=15, y=80)
                        self.PIN_entry.place(x=15, y=105)
                        self.AccName_label.place(x=15, y=150)
                        self.AccName_entry.place(x=15, y=175)
                        self.PhNo_label.place(x=15, y=220)
                        self.PhNo_entry.place(x=15, y=245)
                        
                        self.entryList.append(self.AccNo_entry)
                        self.entryList.append(self.PIN_entry)
                        self.entryList.append(self.AccName_entry)
                        self.entryList.append(self.PhNo_entry)
                    if(self.screen == "user"):
                        pass

                case 3:
                    if(self.screen == "History"):
                        date1 = ["25/12","26/12","27/12"]
                        withdrawed = [3,4,6]
                        plt.plot(date1,withdrawed, color = "r")
                        plt.yticks(withdrawed)
                        plt.show()


                case 4:
                    pass

                case 5:
                    if(self.screen == "user"):
                        DestroyWidgets()
                        self.screen = "withdraw"

                        self.balance_label = Label(TopFrame2Mid, text=f"Balance: {data.getBalance(self.AccNo)}", font=('arial', 10))

                        self.withdraw_label = Label(TopFrame2Mid, text='Enter Amount :', font=('arial', 10, 'bold'))
                        self.withdraw_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.balance_label.place(x=5, y=5)

                        self.withdraw_label.place(x=15, y=85)
                        self.withdraw_entry.place(x=15, y=110)

                        self.entryList.append(self.withdraw_entry)
                    if(self.screen == "withdraw"):
                        pass

                case 6:
                    if(self.screen == "user"):
                        DestroyWidgets()
                        self.screen = "deposit"
                        
                        self.balance_label = Label(TopFrame2Mid, text=f"Balance: {data.getBalance(self.AccNo)}", font=('arial', 10))

                        self.dep_label = Label(TopFrame2Mid, text='Enter Amount :', font=('arial', 10, 'bold'))
                        self.dep_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.balance_label.place(x=5, y=5)

                        self.dep_label.place(x=15, y=85)
                        self.dep_entry.place(x=15, y=110)

                        self.entryList.append(self.dep_entry)
                    if(self.screen == "deposit"):
                        pass

                case 7:
                    if(self.screen == "user"):
                        DestroyWidgets()
                        self.screen = "History"

                        self.balance_label = Label(TopFrame2Mid, text=f"Balance: {data.getBalance(self.AccNo)}", font=('arial', 10))
                        
                        self.wd_label = Label(TopFrame2Mid, text="Withdraw", font=('arial', 20, 'bold'))
                        self.deposit_label = Label(TopFrame2Mid, text="Deposit", font=('arial', 20, 'bold'))
                        
                        self.wd_label.place(x=15, y=155)
                        self.deposit_label.place(x=15, y=225)


                case 8:
                    if(self.screen == "user"):
                        DestroyWidgets()
                        self.screen = "changePIN"

                        self.cpo_label = Label(TopFrame2Mid, text='Enter old PIN :', font=('arial', 10, 'bold'))
                        self.cpo_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.cpn_label = Label(TopFrame2Mid, text='Enter new PIN :', font=('arial', 10, 'bold'))
                        self.cpn_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

                        self.cpo_label.place(x=15, y=15)
                        self.cpo_entry.place(x=15, y=40)

                        self.cpn_label.place(x=15, y=85)
                        self.cpn_entry.place(x=15, y=110)

                        self.entryList.append(self.cpo_entry)
                        self.entryList.append(self.cpn_entry)
                    if(self.screen == "changePIN"):
                        pass
                    


#===============================================================================#

        # "welcome", "login or register", "login", "user", "register", "Withdraw"
        self.screen = "welcome"

#=======================CenterScreen(Widgets)===================================#

        # 400 x 275
        self.img_atm_background = PhotoImage(file="resources/images/background2.png")
        self.atm_background = Label(TopFrame2Mid, image=self.img_atm_background)
        self.atm_background.grid(row=0, column=0)

        self.WelcomeMSG_Main = Label(TopFrame2Mid, text="WELCOME TO ATM", font=('arial', 20, 'bold'))
        self.WelcomeMSG_Main.place(x=70, y=20)

        self.WelcomeMSG_Sub = Label(TopFrame2Mid, text="Press start to continue", font=('arial', 10, 'normal'))
        self.WelcomeMSG_Sub.place(x=130, y=60)

#=============================LeftArrow(Widgets)================================#

        # Left Arrow Image
        self.img_ArrowL = PhotoImage(file= "resources/images/LeftArrow.png")

        # Left Arrow Buttons
        self.btnArrow1 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(1), image=self.img_ArrowL).grid(row=0, column=0, padx=2, pady=2)
        self.btnArrow2 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(2), image=self.img_ArrowL).grid(row=1, column=0, padx=2, pady=2)
        self.btnArrow3 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(3), image=self.img_ArrowL).grid(row=2, column=0, padx=2, pady=2)
        self.btnArrow4 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(4), image=self.img_ArrowL).grid(row=3, column=0, padx=2, pady=2)

#==========================RightArrow(Widgets)==================================#

        # Right Arrow Image
        self.img_ArrowR = PhotoImage(file= "resources/images/RightArrow.png")

        # Right Arrow Buttons
        self.btnArrow5 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(5), image=self.img_ArrowR).grid(row=0, column=0, padx=2, pady=2)
        self.btnArrow6 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(6), image=self.img_ArrowR).grid(row=1, column=0, padx=2, pady=2)
        self.btnArrow7 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(7), image=self.img_ArrowR).grid(row=2, column=0, padx=2, pady=2)
        self.btnArrow8 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(8), image=self.img_ArrowR).grid(row=3, column=0, padx=2, pady=2)

#=============================Number Pad(Widgets)===============================#

        # Row 1 Images
        self.img_1 = PhotoImage(file="resources/images/NumOne.png")
        self.img_2 = PhotoImage(file="resources/images/NumTwo.png")
        self.img_3 = PhotoImage(file="resources/images/NumThree.png")
        self.img_CANCEL = PhotoImage(file="resources/images/Cancel.png")

        # Row 1 Buttons
        self.btn_1 = Button(TopFrame1, width=160, height=60, command= lambda: insert(1), image=self.img_1).grid(row=2, column=0, padx=6, pady=4)
        self.btn_2 = Button(TopFrame1, width=160, height=60, command= lambda: insert(2), image=self.img_2).grid(row=2, column=1, padx=6, pady=4)
        self.btn_3 = Button(TopFrame1, width=160, height=60, command= lambda: insert(3), image=self.img_3).grid(row=2, column=2, padx=6, pady=4)
        self.btn_CANCEL = Button(TopFrame1, width=160, height=60, command=cancel, image=self.img_CANCEL).grid(row=2, column=3, padx=6, pady=4)



        # Row 2 Images
        self.img_4 = PhotoImage(file="resources/images/NumFour.png")
        self.img_5 = PhotoImage(file="resources/images/NumFive.png")
        self.img_6 = PhotoImage(file="resources/images/NumSix.png")
        self.img_CLEAR = PhotoImage(file="resources/images/Clear.png")

        # Row 2 Buttons
        self.btn_4 = Button(TopFrame1, width=160, height=60, command= lambda: insert(4), image=self.img_4).grid(row=3, column=0, padx=6, pady=4)
        self.btn_5= Button(TopFrame1, width=160, height=60, command= lambda: insert(5), image=self.img_5).grid(row=3, column=1, padx=6, pady=4)
        self.btn_6 = Button(TopFrame1, width=160, height=60, command= lambda: insert(6), image=self.img_6).grid(row=3, column=2, padx=6, pady=4)
        self.btn_CLEAR = Button(TopFrame1, width=160, height=60, command=clear, image=self.img_CLEAR).grid(row=3, column=3, padx=6, pady=4)



        # Row 3 Images
        self.img_7 = PhotoImage(file="resources/images/NumSeven.png")
        self.img_8 = PhotoImage(file="resources/images/NumEight.png")
        self.img_9 = PhotoImage(file="resources/images/NumNine.png")
        self.img_ENTER = PhotoImage(file="resources/images/Enter.png")

        # Row 3 Buttons
        self.btn_7 = Button(TopFrame1, width=160, height=60, command= lambda: insert(7), image=self.img_7).grid(row=4, column=0, padx=6, pady=4)
        self.btn_8 = Button(TopFrame1, width=160, height=60, command= lambda: insert(8), image=self.img_8).grid(row=4, column=1, padx=6, pady=4)
        self.btn_9 = Button(TopFrame1, width=160, height=60, command= lambda: insert(9), image=self.img_9).grid(row=4, column=2, padx=6, pady=4)
        self.btn_ENTER = Button(TopFrame1, width=160, height=60, command=enter, image=self.img_ENTER).grid(row=4, column=3, padx=6, pady=4)

                                                                  
        # Row 4 Images
        self.img_0 = PhotoImage(file="resources/images/NumZero.png")
        self.img_START = PhotoImage(file="resources/images/Start.png")

        # Row 4 Buttons
        self.btn_0 = Button(TopFrame1, width=160, height=60, command= lambda: [CurrentEntry(),insert(0)] ,image=self.img_0).grid(row=5, column=1, padx=6, pady=4)
        self.btn_START = Button(TopFrame1, width=160, height=60, command=start, image=self.img_START).grid(row=5, column=3, padx=6, pady=4)

#=================================Number Pad End================================#

#===================================Main========================================#

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
