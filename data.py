import pandas as pd
import datetime

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
        df.loc[AccNo] = [Pin, Name, PhNo, 0]
        withdraw_df.loc[AccNo] = [[0 for i in range(24)]]
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
    if(getBalance(AccNo) >= amount):
        df.loc[AccNo, "Balance"] -= amount

        SaveMain()
        setWithdrawHistory(AccNo)    

        return "Success"
    elif(getBalance(AccNo) < amount):
        return "Insufficient Funds"

def deposit(AccNo, amount):
    df.loc[AccNo, "Balance"] += amount

    SaveMain()
    setDespoitHistory(AccNo)

def changePIN(AccNo, oldPIN, newPIN):
    if(oldPIN == df.loc[AccNo][0]):
        df.loc[AccNo, "Pin"] = newPIN
        SaveMain()
        return "Success"
    else:
        return "Incorrect PIN"

def getWithdrawHistory(AccNo):
    _tempList = withdraw_df.loc[AccNo, "frequency"]
    _tempList = [int(i) for i in _tempList[1:-1].split(', ')]
    return _tempList

def setWithdrawHistory(AccNo):
    _tempList = getWithdrawHistory(AccNo)
    currentHour = datetime.datetime.now().hour
    _tempList[currentHour] += 1
    withdraw_df.loc[AccNo, "frequency"] = _tempList

    SaveWithdraw()

def getDepositHistory(AccNo):
    _tempList = deposit_df.loc[AccNo, "frequency"]
    _tempList = [int(i) for i in _tempList[1:-1].split(', ')]
    return _tempList

def setDespoitHistory(AccNo):
    _tempList = getDepositHistory(AccNo)
    currentHour = datetime.datetime.now().hour
    _tempList[currentHour] += 1
    deposit_df.loc[AccNo, "frequency"] = _tempList

    SaveDeposit()
