from tkinter import *
import tkinter.messagebox
import data
import tools_GUI
import matplotlib.pyplot as plt

class atm:
    def __init__(self,root):
        self.root = root
        blank_space = " "
        self.root.title(110 * blank_space + "ATM System")
        self.root.geometry('790x654+580+140')
        self.root.configure(background ='yellow')
        
        # list of entry widgets
        self.entryList = []

        # "welcome", "login or register", "login", "user", "register", "withdraw", "deposit", "history", "changePin"
        self.screen = ""

#=================================Frames========================================#

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

#=======================Misc Functions==========================================#

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
            elif(self.screen == "register"):
                self.AccNo_label.destroy()
                self.AccNo_entry.destroy()
                self.PIN_label.destroy()
                self.PIN_entry.destroy()
                self.AccName_label.destroy()
                self.AccName_entry.destroy()
                self.PhNo_label.destroy()
                self.PhNo_entry.destroy()
            elif(self.screen == "user"):
                self.withdraw_label.destroy()
                self.deposit_label.destroy()
                self.history_label.destroy()
                self.changePin_label.destroy()
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
            elif(self.screen == "changePin"):
                self.cpo_label.destroy()
                self.cpo_entry.destroy()
                self.cpn_label.destroy()
                self.cpn_entry.destroy()
            elif(self.screen == "history"):
                self.wd_label.destroy()
                self.deposit_label.destroy()

        def CurrentEntry():
            # get the selected entry on screen
            widgetSelected = root.focus_get()

            # return the entry which is selected
            for entry in self.entryList:
                if(widgetSelected == entry):
                    return entry
        
        def UpdateArrows():
            if(self.screen == "welcome"):
                try:
                    self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                    self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                    self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                    self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                    self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                    self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                    self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                    self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
                except:
                    pass
            elif(self.screen == "login or register"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Enabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Enabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "login"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "register"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "user"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Enabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Enabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Enabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Enabled)
            elif(self.screen == "withdraw"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "deposit"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "changePin"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            elif(self.screen == "history"):
                self.btnArrow1.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow2.config(image=self.img_ArrowLeft_Disabled)
                self.btnArrow3.config(image=self.img_ArrowLeft_Enabled)
                self.btnArrow4.config(image=self.img_ArrowLeft_Enabled)
                self.btnArrow5.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow6.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow7.config(image=self.img_ArrowRight_Disabled)
                self.btnArrow8.config(image=self.img_ArrowRight_Disabled)
            
#=================================Screens=======================================#

        def WelcomeScreen():
            DestroyWidgets()
            self.screen = "welcome"
            UpdateArrows()

            self.WelcomeMSG_Main = Label(TopFrame2Mid, text="WELCOME TO ATM", font=('arial', 20, 'bold'))
            self.WelcomeMSG_Main.place(x=70, y=20)

            self.WelcomeMSG_Sub = Label(TopFrame2Mid, text="Press start to continue", font=('arial', 10, 'normal'))
            self.WelcomeMSG_Sub.place(x=130, y=60)

        def start():
            DestroyWidgets()
            self.screen = "login or register"
            UpdateArrows()

            self.login_label = Label(TopFrame2Mid, text="Login", font=('arial', 20, 'bold'))
            self.register_label = Label(TopFrame2Mid, text="Register", font=('arial', 20, 'bold'))
            
            self.login_label.place(x=15, y=15)
            self.register_label.place(x=15, y=85)

        def LoginScreen():
            DestroyWidgets()
            self.screen = "login"
            UpdateArrows()

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

        def RegisterScreen():
            DestroyWidgets()
            self.screen = "register"
            UpdateArrows()

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

        def UserPanel(AccNo):
            DestroyWidgets()
            self.screen = "user"
            UpdateArrows()

            self.user_label = Label(TopFrame2Mid, text=f"{data.getName(self.AccNo)}'s User Panel")
            self.balance_label = Label(TopFrame2Mid, text=f"Balance: ${data.getBalance(self.AccNo)}", font=('arial', 10))

            self.withdraw_label = Label(TopFrame2Mid, text="Withdraw", font=('arial', 20, 'bold'))
            self.deposit_label = Label(TopFrame2Mid, text="Deposit", font=('arial', 20, 'bold'))
            self.history_label = Label(TopFrame2Mid, text="Transaction History", font=('arial', 20, 'bold'))
            self.changePin_label = Label(TopFrame2Mid, text="Change PIN", font=('arial', 20, 'bold'))

            self.user_label.place(x=5, y=5)
            self.balance_label.place(x=5, y=28)
                
            self.withdraw_label.place(x=258, y=15)
            self.deposit_label.place(x=280, y=85)
            self.history_label.place(x=120, y=155)
            self.changePin_label.place(x=225, y=225)

        def WithdrawScreen():
            DestroyWidgets()
            self.screen = "withdraw"
            UpdateArrows()

            self.balance_label = Label(TopFrame2Mid, text=f"Balance: ${data.getBalance(self.AccNo)}", font=('arial', 10))
            self.balance_label.place(x=5, y=5)

            self.withdraw_label = Label(TopFrame2Mid, text='Enter Amount :', font=('arial', 10, 'bold'))
            self.withdraw_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

            self.withdraw_label.place(x=15, y=85)
            self.withdraw_entry.place(x=15, y=110)

            self.entryList.append(self.withdraw_entry)

        def DepositScreen():
            DestroyWidgets()
            self.screen = "deposit"
            UpdateArrows()
                        
            self.balance_label = Label(TopFrame2Mid, text=f"Balance: ${data.getBalance(self.AccNo)}", font=('arial', 10))
            self.balance_label.place(x=5, y=5)

            self.dep_label = Label(TopFrame2Mid, text='Enter Amount :', font=('arial', 10, 'bold'))
            self.dep_entry = Entry(TopFrame2Mid, font=('arial', 10, 'normal'))

            self.dep_label.place(x=15, y=85)
            self.dep_entry.place(x=15, y=110)

            self.entryList.append(self.dep_entry)

        def HistoryScreen():
            DestroyWidgets()
            self.screen = "history"
            UpdateArrows()

            self.balance_label = Label(TopFrame2Mid, text=f"Balance:$ {data.getBalance(self.AccNo)}", font=('arial', 10))
                        
            self.wd_label = Label(TopFrame2Mid, text="Withdraw", font=('arial', 20, 'bold'))
            self.deposit_label = Label(TopFrame2Mid, text="Deposit", font=('arial', 20, 'bold'))
            
            self.wd_label.place(x=15, y=155)
            self.deposit_label.place(x=15, y=225)

        def ChangePinScreen():
            DestroyWidgets()
            self.screen = "changePin"
            UpdateArrows()

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

        def PlotWithdrawHistory():
            history = data.getWithdrawHistory(self.AccNo)
            time = history[0]
            amount = history[1]
            tools_GUI.Plot(time, amount)

        def PlotDepositHistory():
            history = data.getDepositHistory(self.AccNo)
            time = history[0]
            amount = history[1]
            tools_GUI.Plot(time, amount)

#=======================Button Functions========================================#

        def arrow(num):
            match(num):
                case 1:
                    # Arrow 1 : "login or register" => "login"
                    if(self.screen == "login or register"):
                        LoginScreen()

                case 2:
                    # Arrow 2 : "login or register" => "register"
                    if(self.screen == "login or register"):
                        RegisterScreen()

                case 3:
                    # Arrow 3 : "history" => Plot Withdraw History
                    if(self.screen == "history"):
                        PlotWithdrawHistory()

                case 4:
                    # Arrow 4 : "history" => Plot Deposit History
                    if(self.screen == "history"):
                        PlotDepositHistory()

                case 5:
                    # Arrow 5 : "user" => "withdraw"
                    if(self.screen == "user"):
                        WithdrawScreen()

                case 6:
                    # Arrow 6 : "user" => "deposit"
                    if(self.screen == "user"):
                        DepositScreen()

                case 7:
                    # Arrow 7 : "user" => "history"
                    if(self.screen == "user"):
                        HistoryScreen()

                case 8:
                    # Arrow 8 : "user" => "changePin"
                    if(self.screen == "user"):
                        ChangePinScreen()

        # Num Key Function
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

        def clear():
            try:
                CurrentEntry().delete(0, END)
            except:
                print("No entry selected")

        def enter():
            if(self.screen == "login"):
                # Store Info globally for this session
                self.AccNo = int(str(self.AccNo_entry.get()).strip())
                self.Pin = int(str(self.PIN_entry.get()).strip())

                # Check for "Int", "Digit Error", "Non Int"
                AccNo_check = tools_GUI.CheckInt(self.AccNo, digit=8)
                Pin_check = tools_GUI.CheckInt(self.Pin, digit=4)

                # Proceed if checks are passed
                if(AccNo_check == "Int" and Pin_check == "Int"):
                    if(data.login(self.AccNo,self.Pin) == "Success"):
                        UserPanel(self.AccNo)
                    elif(data.login(self.AccNo,self.Pin) == "No Data"):
                        tkinter.messagebox.showwarning("Not Found", "No such account exists")
                elif(AccNo_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 8 digit account number")
                elif(Pin_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 4 digit pin number")

            elif(self.screen == "register"):
                # Store Info globally for this session
                self.AccNo = int(str(self.AccNo_entry.get()).strip())
                self.Pin = int(str(self.PIN_entry.get()).strip())
                self.Name = str(self.AccName_entry.get()).strip()
                self.PhNo = int(str(self.PhNo_entry.get()).strip())

                # Check for "Int", "Digit Error", "Non Int" and "STR", "Non STR"
                AccNo_check = tools_GUI.CheckInt(self.AccNo, digit=8)
                Pin_check = tools_GUI.CheckInt(self.Pin, digit=4)
                AccName_check = tools_GUI.CheckSTR(self.Name)
                PhNo_check = tools_GUI.CheckInt(self.PhNo, digit=10)
                    
                # Proceed if checks are passed
                if(AccNo_check == "Int" and Pin_check == "Int" and AccName_check == "STR" and PhNo_check == "Int"):
                    if(data.register(self.AccNo, self.Pin, self.Name, self.PhNo) == "Success"):
                        UserPanel(self.AccNo)
                        tkinter.messagebox.showinfo("Success", "Successfully Created New Account !")
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


            elif(self.screen == "changePin"):
                self.cpo = int(self.cpo_entry.get())
                self.cpn = int(self.cpn_entry.get())

                # Check for "Int", "Digit Error", "Non Int"
                oldP_check = tools_GUI.CheckInt(self.cpo, digit=4)
                newP_check = tools_GUI.CheckInt(self.cpn, digit=4)

                # Proceed if checks are passed
                if(oldP_check == "Int" and newP_check == "Int"):
                    if(data.changePin(self.AccNo, self.cpo, self.cpn)) == "Success":
                        UserPanel(self.AccNo)
                        tkinter.messagebox.showinfo("Alert", "Successfully changed your PIN!")
                    elif(data.changePin(self.AccNo,self.cpo) == "Incorrect PIN"):
                        tkinter.messagebox.showwarning("Incorrect PIN", "Please Check entered PIN")
                elif(oldP_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 4 digit pin number")
                elif(newP_check == "Digit Error"):
                    tkinter.messagebox.showwarning("Digit Error", "Enter an 4 digit pin number")

            elif(self.screen == "withdraw"):
                amount = int(self.withdraw_entry.get())

                # Check for "Success", "Insufficient Funds"
                withdraw_check = data.withdraw(self.AccNo, amount)
                
                # Proceed if checks are passed
                if(withdraw_check == "Success"):
                    tkinter.messagebox.showinfo("Alert", f"Successfully withdrawed ${amount}")
                    UserPanel(self.AccNo)
                elif(withdraw_check == "Min 2000"):
                    tkinter.messagebox.showerror("Alert", "A min of $2000 is required to keep your account running.")
                elif(withdraw_check == "Insufficient Funds"):
                    tkinter.messagebox.showinfo("Alert", "Insufficient Funds")

            elif(self.screen == "deposit"):
                amount = int(self.dep_entry.get())
                data.deposit(self.AccNo, amount)
                tkinter.messagebox.showinfo("Alert", f"Successfully deposited ${amount}")
                UserPanel(self.AccNo)

        def back():
            if(self.screen == "login or register"):
                WelcomeScreen()
            elif(self.screen == "login" or self.screen == "register"):
                start()
            elif(self.screen == "user"):
                # how to know which screen we are coming from "login" or register ??
                start()
            elif(self.screen == "withdraw" or self.screen == "deposit" or self.screen == "history" or self.screen == "changePin"):
                UserPanel(self.AccNo)

#=======================CenterScreen(Widgets)===================================#

        # 400 x 275
        self.img_atm_background = PhotoImage(file="resources/images/background3.png")
        self.atm_background = Label(TopFrame2Mid, image=self.img_atm_background)
        self.atm_background.grid(row=0, column=0)

        WelcomeScreen()

#=============================LeftArrow(Widgets)================================#

        # Left Arrow Image
        self.img_ArrowLeft_Enabled = PhotoImage(file= "resources/images/LeftArrowEnabled.png")
        self.img_ArrowLeft_Disabled = PhotoImage(file= "resources/images/LeftArrowDisabled.png")

        # Left Arrow Buttons
        self.btnArrow1 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(1), image=self.img_ArrowLeft_Disabled)
        self.btnArrow2 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(2), image=self.img_ArrowLeft_Disabled)
        self.btnArrow3 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(3), image=self.img_ArrowLeft_Disabled)
        self.btnArrow4 = Button(TopFrame2Left, width=120, height=60, state=NORMAL, command= lambda: arrow(4), image=self.img_ArrowLeft_Disabled)

        
        self.btnArrow1.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrow2.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrow3.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrow4.grid(row=3, column=0, padx=2, pady=2)

#==========================RightArrow(Widgets)==================================#

        # Right Arrow Image
        self.img_ArrowRight_Enabled = PhotoImage(file= "resources/images/RightArrowEnabled.png")
        self.img_ArrowRight_Disabled = PhotoImage(file= "resources/images/RightArrowDisabled.png")

        # Right Arrow Buttons
        self.btnArrow5 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(5), image=self.img_ArrowRight_Disabled)
        self.btnArrow6 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(6), image=self.img_ArrowRight_Disabled)
        self.btnArrow7 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(7), image=self.img_ArrowRight_Disabled)
        self.btnArrow8 = Button(TopFrame2Right, width=120, height=60, state=NORMAL, command= lambda: arrow(8), image=self.img_ArrowRight_Disabled)

        self.btnArrow5.grid(row=0, column=0, padx=2, pady=2)
        self.btnArrow6.grid(row=1, column=0, padx=2, pady=2)
        self.btnArrow7.grid(row=2, column=0, padx=2, pady=2)
        self.btnArrow8.grid(row=3, column=0, padx=2, pady=2)

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
        self.img_BACK = PhotoImage(file="resources/images/Back.png")
        self.img_START = PhotoImage(file="resources/images/Start.png")

        # Row 4 Buttons
        self.btn_0 = Button(TopFrame1, width=160, height=60, command= lambda: [CurrentEntry(),insert(0)], image=self.img_0).grid(row=5, column=1, padx=6, pady=4)
        self.btn_BACK = Button(TopFrame1, width=160, height=60, command=back, image=self.img_BACK).grid(row=5, column=2, padx=6, pady=4)
        self.btn_START = Button(TopFrame1, width=160, height=60, command=start, image=self.img_START).grid(row=5, column=3, padx=6, pady=4)

#=================================Number Pad End================================#

#===================================Main========================================#

if __name__=='__main__':
    root = Tk()
    application = atm(root)
    root.mainloop()
