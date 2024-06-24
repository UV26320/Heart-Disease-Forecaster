# -*- coding: utf-8 -*-
"""Heart Diseases Predictions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1WIiKbq8tOVrcCWMJLhCZ6lDosqDOqQkD
"""

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

heart_data = pd.read_csv('Heart.csv')

heart_data.head()

heart_data.tail()

heart_data.shape

heart_data.info()

heart_data.describe()

#check missing value
heart_data.isnull().sum()

heart_data['target'].value_counts()

heart_data.dtypes

"""#Exploratory Data Analysis(EDA)"""

#Plotting the distribution plot.

import matplotlib.pyplot as plt
import seaborn as sns

plt.figure(figsize=(20,25))
plotnumber=1

for column in heart_data:
    if plotnumber<14:
        ax=plt.subplot(4,4,plotnumber)
        sns.distplot(heart_data[column])
        plt.xlabel(column,fontsize=20)
        plt.ylabel('Values',fontsize=20)
    plotnumber+=1
plt.show()

#Correlation matrix

plt.figure(figsize = (16, 8))

corr = heart_data.corr()
mask = np.triu(np.ones_like(corr, dtype = bool))
sns.heatmap(corr, mask = mask, annot = True, fmt = '.2g', linewidths = 1)
plt.show()

# checking the variance
heart_data.var()

"""# Normalization"""

heart_data['trestbps']=np.log(heart_data['trestbps'])
heart_data['chol']=np.log(heart_data['chol'])
heart_data['thalach']=np.log(heart_data['thalach'])

np.var(heart_data[["trestbps",'chol','thalach']])

heart_data.isnull().sum()

x=heart_data.drop('target',axis=1)
y=heart_data['target']

print(x)

print(y)

#spliting the dataset

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.30, random_state=0)

print(x.shape, x_train.shape, x_test.shape)

"""# Logistic Regression"""

model = LogisticRegression()

# training the LogisticRegression model with Training data
model.fit(x_train, y_train)

accuracies ={}

y_pred0 = model.predict(x_test)

acc0=accuracy_score(y_test,y_pred0)
accuracies['LR']=acc0*100

"""##Accuracy Score

"""

# accuracy on training data
x_train_prediction = model.predict(x_train)
training_data_accuracy = accuracy_score(x_train_prediction, y_train)

print('Accuracy on Training data : ', training_data_accuracy)

# accuracy on test data
x_test_prediction = model.predict(x_test)
test_data_accuracy = accuracy_score(x_test_prediction, y_test)

print('Accuracy on Test data : ', test_data_accuracy)

"""#Gradient Boosting"""

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
gbc = GradientBoostingClassifier()

gbc = GradientBoostingClassifier(learning_rate = 0.05, loss = 'deviance', n_estimators = 180)
gbc.fit(x_train, y_train)

y_pred = gbc.predict(x_test)

acc = accuracy_score(y_test,y_pred)
accuracies['GradientBoosting']=acc*100

print("Training accuracy score of the model is:",accuracy_score(y_train, gbc.predict(x_train))*100,"%")
print("Testing accuracy score of the model is:",accuracy_score(y_test,y_pred)*100,"%")

"""# Random Forest"""

from sklearn.ensemble import RandomForestClassifier

rfc = RandomForestClassifier(criterion = 'gini', max_depth = 7, max_features = 'sqrt', min_samples_leaf = 2, min_samples_split = 4, n_estimators = 180)
rfc.fit(x_train, y_train)

y_pred1 = rfc.predict(x_test)

acc1=accuracy_score(y_test,y_pred1)
accuracies['RF']=acc1*100

print("Training accuracy score of the model is:",accuracy_score(y_train, rfc.predict(x_train))*100,"%")
print("Testing accuracy score of the model is:",accuracy_score(y_test,y_pred1)*100,"%")

print("Confusion matrix of the model",confusion_matrix(y_test,y_pred1))

print("Classification Report",classification_report(y_test,y_pred1))

"""# XGBoost"""

from xgboost import XGBClassifier

xgb = XGBClassifier(objective = 'binary:logistic', learning_rate = 0.01, max_depth = 5, n_estimators = 180)

xgb.fit(x_train, y_train)

y_pred2 = xgb.predict(x_test)

acc2=accuracy_score(y_test,y_pred2)

accuracies['XGBoost']=acc2*100
print("Training accuracy score of the model is:",accuracy_score(y_train, xgb.predict(x_train))*100,"%")
print("Testing accuracy score of the model is:",accuracy_score(y_test,y_pred2)*100,"%")

print("Confusion matrix of the model",confusion_matrix(y_test,y_pred2))

print("Classification Report",classification_report(y_test,y_pred2))

colors = ["purple", "green", "orange", "blue"]

# sns.set_style("whitegrid")
plt.figure(figsize=(16,8))
plt.yticks(np.arange(0,1200,10))
plt.ylabel("Accuracy %")
plt.xlabel("Algorithms")
sns.barplot(x=list(accuracies.keys()), y=list(accuracies.values()), palette=colors )
plt.show()

models_df = pd.DataFrame({
    'Model': ['Logistic Regression', 'Gradient Boosting','Random Forest','XgBoost'],
    'Score': [acc0, acc, acc1, acc2]
})

models_df.sort_values(by = 'Score', ascending = False)

"""# Building a Predictive System"""

input_data = (59	,1,	1,	140,	221,	0	,1,	164,	1	,0.0	,2	,0	,2)

# change the input data to a numpy array
input_data_as_numpy_array= np.asarray(input_data)

# reshape the numpy array as we are predicting for only on instance
input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

prediction = rfc.predict(input_data_reshaped)
print(prediction)

if (prediction[0]== 0):
  print('The Person does not have a Heart Disease')
else:
  print('The Person has Heart Disease')

"""# Saving the trained model"""

import pickle

filename = 'heart_disease_model.sav'
pickle.dump(model, open(filename, 'wb'))

# loading the saved model
loaded_model = pickle.load(open('heart_disease_model.sav', 'rb'))

for column in x.columns:
  print(column)

