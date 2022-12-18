import pandas as pd

# Load data from "data.csv" to "df" dataframe
df = pd.read_csv("data.csv", index_col="AccNo")
# print(df.loc[12345678][0])

def login(AccNo, Pin):
    if(AccNo in df.index):
        if(Pin == df.loc[AccNo][0]):
            return "success"
    else:
        return "no data"

def register(AccNo, Pin, Name, PhNo):
    if(AccNo not in df.index):
        df.loc[AccNo] = [Pin, Name, PhNo, 0]
        return "success"
    else:
        return "already exists"

def getName(AccNo):
    return df.loc[AccNo][1]

def getPhNo(AccNo):
    return df.loc[AccNo][2]

def getBalance(AccNo):
    return df.loc[AccNo][3]

# print(register(12345678, " ", " ", " "))