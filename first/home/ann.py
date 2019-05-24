import pandas as pd;
df=pd.read_csv('C:\\Users\\Vishnuteja_Kandalam\\deep_learning\\datasets\\P16-Artificial-Neural-Networks\\Artificial_Neural_Networks\\Churn_Modelling.csv');
xr=df.iloc[:,3:13];
x= df.iloc[:, 3:13].values;
x
y=df.iloc[:,13].values;
y
     
from sklearn.preprocessing import LabelEncoder;
le=LabelEncoder();
x[:,1]=le.fit_transform(x[:,1]);
x[:,2]=le.fit_transform(x[:,2]);
x
from sklearn.preprocessing import OneHotEncoder;
ohe=OneHotEncoder(categorical_features=[1]);
x=ohe.fit_transform(x).toarray()
x=x[:,1:]
x

from sklearn.model_selection import train_test_split;
x_tr,x_te,y_tr,y_te=train_test_split(x,y,test_size=0.2,random_state=0)

from sklearn.preprocessing import StandardScaler;
ss=StandardScaler();
x_tr=ss.fit_transform(x_tr);
x_te=ss.fit_transform(x_te);
#importing keras for building an ANN
import keras;
from keras.models import Sequential;
from keras.layers import Dense;

cls=Sequential();
cls.add(Dense(output_dim=6,input_dim=11,activation='relu',init='uniform'))

cls.add(Dense(output_dim=1,activation='sigmoid',init="uniform"))
   
cls.compile(optimizer='sgd',loss='binary_crossentropy',metrics=['accuracy']);
   
cls.fit(x_tr,y_tr,batch_size=10,epochs=100)
import numpy as np
y_pred=cls.predict(x_te);
y_pred=(y_pred>0.5);
y_pred
from sklearn.metrics import confusion_matrix;
cn=confusion_matrix(y_te,y_pred);
ary=np.array([[0,0,619,0,42,2,0,1,1,1,101348.88]]);
ary=ss.fit_transform(ary);
val=cls.predict(ary);