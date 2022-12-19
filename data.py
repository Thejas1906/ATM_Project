import pandas as pd


# print(df.loc[12345678][0])

def Save():
    global df
    df.to_csv("data.csv")
    df = pd.read_csv("data.csv", index_col=0)

# Load data from "data.csv" to "df" dataframe
df = pd.read_csv("data.csv", index_col=0)

def login(AccNo, Pin):
    if(AccNo in df.index):
        if(Pin == df.loc[AccNo][0]):
            return "Success"
    else:
        return "No Data"

def register(AccNo, Pin, Name, PhNo):
    if(AccNo not in df.index):
        df.loc[AccNo] = [Pin, Name, PhNo, 0]
        Save()
        return "Success"
    else:
        return "Already Exists"

def getName(AccNo):
    return df.loc[AccNo][1]

def getPhNo(AccNo):
    return df.loc[AccNo][2]

def getBalance(AccNo):
    return df.loc[AccNo][3]

def withdraw(AccNo, amount):
    df.iloc[list(df.index).index(AccNo), 3] -= amount
    Save()

def deposit(AccNo, amount):
    df.iloc[list(df.index).index(AccNo), 3] += amount
    Save()

def changePIN(AccNo, oldPIN, newPIN):
    if(oldPIN == df.loc[AccNo][0]):
        df.iloc[list(df.index).index(AccNo), 0] = newPIN
        Save()
        return "Success"
    else:
        return "Incorrect PIN"

# def Whistory(AccNo, ):




# print(register(12345678, " ", " ", " "))