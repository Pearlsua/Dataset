# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1h9cECtnxt-eTri9FByzVaju2my1hws5R
"""

# 필요한 라이브러리들 임포트
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import os

# CSV 파일을 읽어 데이터프레임 (df)에 저장
# 데이터프레임의 첫 5개 행을 확인
df=pd.read_csv('/content/user_behavior_dataset.csv')
df.head()

#데이터프레임의 컬럼명을 확인
df.columns

# 데이터프래임의 통계적 요약 정보를 확인
df.describe

# 데이터프레임에서 결측치(null) 값을 컬럽별로 합산하여 확인
df.isnull().sum()

# 데이터프레임의 구조와 데이터 타입 정보를 확인
df.info()

df['Device Model'].value_counts()
df['Device Model']=df['Device Model'].replace('Xiaomi Mi 11',0)
df['Device Model']=df['Device Model'].replace('iPhone 12',1)
df['Device Model']=df['Device Model'].replace('Google Pixel 5',2)
df['Device Model']=df['Device Model'].replace('OnePlus 9',3)
df['Device Model']=df['Device Model'].replace('Samsung Galaxy S21',4)

# 'Operating System' 컬럼의 값을 OS 이름에서 숫자로 변환하여 매핑
df['Operating System'].value_counts()
df['Operating System']=df['Operating System'].replace('Android',1)
df['Operating System']=df['Operating System'].replace('iOS',0)

df['Gender'].value_counts()
df['Gender']=df['Gender'].replace('Male',1)
df['Gender']=df['Gender'].replace('Female',0)

# 하루 데이터 사용량의 분포를 시각화
sns.histplot(df['Data Usage (MB/day)'])

sns.pairplot(df, vars=['App Usage Time (min/day)',
'Screen On Time (hours/day)', 'Battery Drain (mAh/day)',
'Data Usage (MB/day)', 'Age'], hue='User Behavior Class',
                                      palette='bright')
plt.suptitle('Pair Plot of Numerical Features', y=1.02)
plt.show()

plt.figure(figsize=(12, 10))
corr_matrix = df.select_dtypes(include=['int64', 'float64']).corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
plt.title('Correlation Matrix of Numerical Features')
plt.show()

plt.figure(figsize=(6, 6))
df['Operating System'].value_counts().plot.pie
(autopct='%1.1f%%', colors=['skyblue', 'red'], startangle=140, explode=[0.05, 0.05])
plt.title('Operating System Distribution')
plt.ylabel('')
plt.show()

g = sns.FacetGrid(df, col='Operating System', row='Gender', margin_titles=True, palette='Set2')
g.map(sns.histplot, 'App Usage Time (min/day)', bins=20, kde=False, color='blue')
g.fig.subplots_adjust(top=0.9)
g.fig.suptitle('App Usage Time by OS and Gender')
plt.show()

plt.figure(figsize=(10, 6))
age_usage = df.groupby('Age')['App Usage Time (min/day)'].mean().reset_index()
sns.lineplot(x='Age', y='App Usage Time (min/day)', data=age_usage, marker='o', color='green')
plt.title('Age vs. Average App Usage Time')
plt.xlabel('Age')
plt.ylabel('Average App Usage Time (min/day)')
plt.show()

df.columns

plt.figure(figsize=(10, 5))
plt.scatter(df['Number of Apps Installed'],df['Battery Drain (mAh/day)'])
plt.ylabel('Battery Drain (mAh/day)')
plt.xlabel('Number of Apps downloaded')
plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 4000, 200))
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
plt.scatter(df['Number of Apps Installed'],df['Data Usage (MB/day)'])
plt.ylabel('Data Usage (MB/day)')
plt.xlabel('Number of Apps downloaded')
plt.xticks(np.arange(0, 100, 5))
plt.yticks(np.arange(0, 3000, 200))
plt.grid()
plt.show()

df.columns

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Device Model', kde=True, hue='Operating System')
plt.grid()
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Screen On Time (hours/day)', kde=True)
plt.grid()
plt.show()

X=df.drop(columns=['User Behavior Class'],axis=1)
y=df['User Behavior Class']

from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Model
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Predictions
y_pred = log_reg.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

from sklearn.ensemble import RandomForestClassifier

# Model
rf_model = RandomForestClassifier(n_estimators=10, random_state=42)
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

from sklearn.svm import SVC

# Model
svm_model = SVC(kernel='linear', probability=True)
svm_model.fit(X_train, y_train)

# Predictions
y_pred = svm_model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

from sklearn.neighbors import KNeighborsClassifier

# Model
knn_model = KNeighborsClassifier(n_neighbors=5)
knn_model.fit(X_train, y_train)

# Predictions
y_pred = knn_model.predict(X_test)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

