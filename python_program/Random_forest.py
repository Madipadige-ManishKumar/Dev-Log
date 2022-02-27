from  sklearn.datasets import load_digits
from  sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
# ensemble is used  suppose if you use the multiple algorithms then ensemble is used to predicte the output 
import pandas as pd
# %matplotlib inline
import matplotlib.pyplot as plt
digit=load_digits()
print(dir(digit))
plt.gray()
for i  in range(4):
    print(plt.matshow(digit.images[i]))

df=pd.DataFrame(digit.data)
df.head()
print(digit.data[5])


df['target']=digit.target
print(df.head())


x_train,x_test,y_train,y_test=train_test_split(df.drop(['target'],axis='columns'),digit.target,test_size=0.2)


model=RandomForestClassifier(n_estimators=40)
model.fit(x_train,y_train)


print(model.score(x_test,y_test))
