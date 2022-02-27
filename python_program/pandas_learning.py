import pandas  as pd
import numpy as np
dict1={
    "name":['harry','rohan','skillf'],
    "marks":[92,34,17]
}
df=pd.DataFrame(dict1)
# DataFrame Will convert  the data into excel sheet 
df.to_csv('friends.csv')#,index=False
# to_csv Converts The DataFrame in excel sheet
df.head(2)  # Show the First n rows 
df.tail(2) # Shows The n rows From last
# df.describe()  It Will do Static Analsys
friends=pd.read_csv('friends.csv')
# print(friends['marks'][0])
# friends.index=['first','secind','Third']