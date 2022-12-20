import pandas as pd
from datetime import datetime

def SaveMain():
    global df
    df.to_csv("data.csv")
    df = pd.read_csv("data.csv", index_col=0)

def SaveWithdraw():
    global withdraw_df
    withdraw_df.to_csv("withdrawdata.csv")
    withdraw_df = pd.read_csv("withdrawdata.csv", index_col=0)

def SaveDeposit():
    global deposit_df
    deposit_df.to_csv("depositdata.csv")
    deposit_df = pd.read_csv("depositdata.csv", index_col=0)

# # Load data from "data.csv" to "df" dataframe
df = pd.read_csv("data.csv", index_col=0)
withdraw_df = pd.read_csv("withdrawdata.csv", index_col=0)
deposit_df = pd.read_csv("depositdata.csv", index_col=0)

def login(AccNo, Pin):
    if(AccNo in df.index):
        if(Pin == df.loc[AccNo][0]):
            return "Success"
    else:
        return "No Data"

def register(AccNo, Pin, Name, PhNo):
    if(AccNo not in df.index):
        df.loc[AccNo] = [Pin, Name, PhNo, 2000]
        withdraw_df.loc[AccNo] = [[0, 1], [0, 0]]
        deposit_df.loc[AccNo] = [[0 for i in range(24)]]
        
        SaveMain()
        SaveWithdraw()
        SaveDeposit()
        return "Success"
    else:
        return "Already Exists"

def getName(AccNo):
    return df.loc[AccNo, "Name"]

def getPhNo(AccNo):
    return df.loc[AccNo, "PhNo"]

def getBalance(AccNo):
    return df.loc[AccNo, "Balance"]

def withdraw(AccNo, amount):
    if(getBalance(AccNo) < amount):
        return "Insufficient Funds"
    elif(getBalance(AccNo) - 2000 < amount):
        return "Min 2000"
    elif(getBalance(AccNo) >= amount):
        df.loc[AccNo, "Balance"] -= amount

        SaveMain()
        setWithdrawHistory(AccNo, amount)    

        return "Success"

def deposit(AccNo, amount):
    df.loc[AccNo, "Balance"] += amount

    SaveMain()
    setDespoitHistory(AccNo)

def changePin(AccNo, oldPIN, newPIN):
    if(oldPIN == df.loc[AccNo][0]):
        df.loc[AccNo, "Pin"] = newPIN
        SaveMain()
        return "Success"
    else:
        return "Incorrect PIN"

def getWithdrawHistory(AccNo):
    time = withdraw_df.loc[AccNo, "time"]
    amount = withdraw_df.loc[AccNo, "amount"]

    time = [int(i) for i in time[1:-1].split(', ')]
    amount = [int(i) for i in amount[1:-1].split(', ')]
    print("time", time)
    print("amount", amount)

    return [time, amount]

def setWithdrawHistory(AccNo, amount):
    data = getWithdrawHistory(AccNo)
    currentTime = datetime.now().hour*60 + datetime.now().minute

    data[0].append(currentTime)
    data[1].append(amount)

    withdraw_df.loc[AccNo] = data

    SaveWithdraw()

def getDepositHistory(AccNo):
    time = deposit_df.loc[AccNo, "time"]
    amount = deposit_df.loc[AccNo, "amount"]

    time = [int(i) for i in time[1:-1].split(', ')]
    amount = [int(i) for i in amount[1:-1].split(', ')]
    print("time", time)
    print("amount", amount)

    return [time, amount]

def setDespoitHistory(AccNo, amount):
    data = getDepositHistory(AccNo)
    currentTime = datetime.now().hour*60 + datetime.now().minute

    data[0].append(currentTime)
    data[1].append(amount)

    withdraw_df.loc[AccNo] = data

    SaveDeposit()
