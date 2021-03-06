from google.colab import drive
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
%matplotlib inline
drive.mount('/content/drive')
k='drive/My Drive/mnist_new.csv'
data=pd.read_csv(k)
data.head()
a=data.iloc[3,1:].values
a=a.reshape(28,28).astype('uint8')
plt.imshow(a)
df_x=data.iloc[:,1:]
df_y=data.iloc[:,0]
x_train,x_test,y_train,y_test=train_test_split(df_x,df_y,test_size=0.2,random_state=4)
y_train.head()
rf=RandomForestClassifier(n_estimators=100)
rf.fit(x_train,y_train)
pred=rf.predict(x_test)
s=y_test.values
count=0
for i in range(len(pred)):
  if(pred[i]==s[i]):
    count+=1
print(count)
print(len(pred))
print("accuracy:",(11610/12000)*100)
