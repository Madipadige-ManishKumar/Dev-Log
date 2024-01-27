import pandas as pd 
import numpy as np 

# dict = {
#     "name":['Manish',"Harry","rohan"],
#     "marks":[87,89,9],
#     "city":["hyd",'rampur',"kolkta"]
# }
# df=pd.DataFrame(dict)
# df.to_csv("friends.csv",index=False)
# data=pd.read_csv('friends.csv',index_col=False)
# print(data)
# print(df.describe())
# data['name'][0]="Mansih Kumar"
# data.to_csv()
# print(data)
arr1=pd.DataFrame(np.array(np.random.rand(10,6)))
print(arr1)
arr=arr1
arr1.iloc[0,0]=100
print(arr)
arr=arr.drop(0,axis=0)
print(arr)
print(arr.info())