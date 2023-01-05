# #Question 1
# import pandas as pd
# lst=[33, 55, 65, 29,19, 23]

# ser1=pd.Series(lst)

# print(ser1)

# ser3=sum(ser1[ser1%10==3])

# print("Sum of values ending with 3:",ser3)
# ser5=sum(ser1[ser1%10==5])

# print("Sum of values ending with 5:",ser5)
# print("Final sum of values 3 and 5:",ser3+ser5)

 
# #Question 2
# import pandas as pd
# ser1=pd. Series (range (41,71,3))
# print ("Original Series:")
# print (ser1)
# for i in range(0,ser1.size):
#     if ser1[i]%2!=0:
#         ser1[i]=ser1[i]+7
#     else:
#         ser1[i]=ser1[i]-3
# print ("Updated Series:")
# print (ser1)

 
# #Question 3
# import pandas as pd
# num=[]
# for i in range(1,11):
#     val =int(input("Enter Number:"))
#     num. append (val)
#     serl=pd.Series (num)
#     #Assume if number divisible by 4
#     #then change that value = 0
# for i in range(len(serl)):
#     if serl[i]%4==0:
#         serl[i]=0
# print (serl)

# #Question 4
# import pandas as pd
# num=int (input("Enter Series Length:"))
# lst1=[]

# for i in range (num):
#     val=int (input ("Enter Value:"))
#     lst1.append (val)

# serl=pd.Series(lst1)
# print (serl)
# print (serl.head(3))

# #Question 5 
# import pandas as pd
# num=int (input ("Enter Series Length:"))
# lst1=[]

# for i in range (num):
#     val=int (input ("Enter Value:"))
#     lst1.append (val)

# serl=pd.Series(lst1)
# print (serl)
# print (serl.tail(3))


# #Question 6
# import pandas as pd
# import numpy as np
# lst1=[21, 51,71, 31,12]

# serl=pd.Series(lst1)
# print (serl)

# print (pd. Series (np.roll (serl.values,-1)))


# #Question 7
# import pandas as pd

# lst1=["Kavya", "Viswa", "Aaditya", "Thejas", "Ashi"]
# student=pd. DataFrame(lst1,columns=["Student_Name"])
# print (student)


# #Question 8
# import pandas as pd

# lstl=[["Micheal Jordan",78,86,74],["Shaquille O Neal",57,68,75],["Kevin Durant",65,75,67]]
# player=pd.DataFrame(lstl,columns=["Player Name", "Match1", "Match2", "Match3"])
# print (player)


# #Question 9
# import pandas as pd

# dict1={"Country Name": ["China", "Japan", "Russia"],
#        "capital":["Beijing", "Tokyo", "Moscow"],
#        "Population (CR) ":[140,12.57,14.34]}

# df=pd.DataFrame (dict1)
# print (df)


# #Question 10
# import pandas as pd
# lstl=[["Micheal Jordan",78,86,74],["Shaquille O Neal",57,68,75],["Kevin Durant",65,75,67]]
# player=pd.DataFrame(lstl,columns=["Player Name", "Match1","Match2","Match3"])

# print (player)

# for i,j in player.iterrows():
#     print(i,j.values)


# #Question 11 
# import pandas as pd

# lstl=[["Micheal Jordan",78,86,74],["Shaquille O Neal",57,68,75],["Kevin Durant",65,75,67]]
# player=pd.DataFrame(lstl,columns=["Player_Name", "Match1","Match2","Match3"])
# print (player)
# for i,j in player.iterrows():
#     print(i,j["Player_Name"],j["Match2"],j["Match3"])

# #Question 12
# import pandas as pd

# lstl=[["Micheal Jordan",78,86,74],["Shaquille O Neal",57,68,75],["Kevin Durant",65,75,67]]
# player=pd.DataFrame(lstl,columns=["Player_Name","Match1", "Match2","Match3"])
# print (player)

# player ["Total_Score"]=player["Match1"]+player["Match2"]+player["Match3"]
# player ["Rank"]=player["Total_Score"].rank (ascending=0)
# print (player)


# #Question 13
# import pandas as pd

# data={"Name": ["Virat","Suresh Raina","Lasith Malinga","Kapil Dev","Shikhar Dhawan"],
#       "Test":[651,458,785,724,422],
#       "T20":[786,785,574,758,678]}

# player=pd.DataFrame (data)
# print (player)
# player.index=player.index+1  #Start index with 1
# print("   Player Name")
# print(player.Name)
# print("   Test_Runs")
# print(player.Test)
# print("   T20_Runs")
# print(player.T20)


# #Question 14
# import pandas as pd
# data1={"Name":["Virat","Suresh Raina","Lasith Malinga","Kapil Dev","Shikhar Dhawan"],
#       "ODI":[563,642,751,699,582],
#       "T20":[786,785,574,758,678]}
 
# player=pd.DataFrame(data1)
# print(player)
# player.index=player.index+1 #Start index with 1
# print(player.loc[:,("Name", "ODI") ])


# #Question 15
# import pandas as pd

# datab={"Name":["Virat","Suresh Raina","Lasith Malinga","Kapil Dev","Shikhar Dhawan"],
#        "ODI":[3856,1854,1956,5378,1688],
#        "Test":[1746,6840,5893,4985,2489],
#        "T20":[3957,2849,1390,890,4783]}

# player=pd.DataFrame(datab)
# print(player)
# player.index=player.index+1 #Start index with 1

# print("\nMore Than 2000 in ODI")
# print(player.loc[player["ODI"]>2000,["Name", "ODI"]])

# print("\nLess Than 2500 in Test")
# print(player.loc[player["Test"]<2500,["Name","Test"]])

# print("\nMore Than 1500 in T20")
# print(player.loc[player["T20"]>1500,["Name","T20"]])


# #Question 16 
# import matplotlib.pyplot as plt

# day=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
# income=[510,350,475,580,600]
# #Q.a
# plt.title("The Weekly Income Report")
# #Q.b 
# plt.xlabel ("Week Days")
# plt.ylabel("Income in Rs.")
# #Q.d,e,f
# plt.plot(day, income, label="Income",
# color="red",linestyle="dashed",marker="D")
# #Q.c
# plt.legend()
# plt.show()


# #Question 17 
# import matplotlib.pyplot as plt

# month=["March", "April", "May", "June", "July", "August"]
# mask=[1500, 3500, 6500, 6700, 6000, 6800]
# sanitizer=[4400, 4500, 5500, 6000, 5600, 6300]
# hand_wash=[6500, 5000, 5800, 6300, 6200, 4500]

# plt.title("Medical Store")
# plt.xlabel("Months")
# plt.ylabel("Sale In Quantity")
# plt.plot(month,mask, label="Mask",marker="d", linewidth=3.5)
# plt.plot(month,sanitizer, label="Sanitizer",marker="o",linewidth=3.5)
# plt.plot(month,hand_wash, label="Hand Wash",marker="8",linewidth=3.5)
# plt.legend()
# plt.show()


# #Question 18
# import matplotlib.pyplot as plt

# month=["March", "April", "May", "June", "July", "August"]
# mask=[1500, 3500, 6500, 6700, 6000, 6800]
# sanitizer=[4400, 4500, 5500, 6000, 5600, 6300]
# hand_wash=[6500, 5000, 5800, 6300, 6200, 4500]
# plt.title("Medical Store")
# plt.xlabel ("Months")
# plt.ylabel ("Sale In Quantity")

# plt.subplot (2,1,1)
# plt.plot (month, sanitizer, label="Sanitizer",marker="o",
# linewidth=3.5, color="red")
# plt.legend()
# plt.subplot (2,1, 2)
# plt.plot(month,hand_wash,label="Hand Wash",marker="8",linewidth=3.5)
# plt.legend()
# plt.show()


# #Question 19
# import matplotlib.pyplot as plt
# overs=[1,2,3,4]
# runs=[6,18,10,5]
# plt.title("Bowling Records")
# plt.xlabel("Overs")
# plt.ylabel("Runs In Per Over")
# plt.bar(overs, runs, label="Bowling", width=0.7)
# plt.legend()
# plt.show()


 
