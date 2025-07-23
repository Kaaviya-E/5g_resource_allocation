import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle

df = pd.read_csv("D:/5G/5g_project/Quality of Service 5G.csv")
df2=df.copy()
print(df.head())
print(df['Signal_Strength'].dtype)
df['Signal_Strength']=df['Signal_Strength'].str.replace('dBm','').astype(int)
print(df.head())
df['Latency']=df['Latency'].str.replace('ms','').astype(int)
print(df.head())
df['Required_Bandwidth'] = df['Required_Bandwidth'].str.replace(' Kbps', 'e-3').str.replace(' Mbps', '').astype(float)
df['Allocated_Bandwidth'] = df['Allocated_Bandwidth'].str.replace(' Kbps', 'e-3').str.replace(' Mbps', '').astype(float)
df['Resource_Allocation'] = df['Resource_Allocation'].str.replace('%', '').astype(float)
print(df.head())
plt.figure(figsize=(10, 6))
sns.barplot(x='Application_Type', y='Required_Bandwidth', data=df, ci=None)
plt.title('Required Bandwidth by Application Type')
plt.xlabel('Application Type')
plt.ylabel('Required Bandwidth (Mbps)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
sns.barplot(x='Application_Type', y='Allocated_Bandwidth', data=df, ci=None)
plt.title('Allocated Bandwidth by Application Type')
plt.xlabel('Application Type')
plt.ylabel('Allocated Bandwidth (Mbps)')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
plt.figure(figsize=(10, 6))
sns.barplot(x='Application_Type',y='Resource_Allocation',data=df)
plt.xticks(rotation=90)
plt.xlabel('Application Type')
plt.ylabel('Resource Allocation')
plt.title('Resource Allocation by Application Type')
plt.show()
df.drop(columns=['Timestamp','User_ID'],inplace=True,axis=1)
df.head()
df1=pd.get_dummies(df,columns=['Application_Type'],drop_first=True)

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split


# Use the one-hot encoded DataFrame df1 for X and y
X = df1.drop("Resource_Allocation", axis=1)
y = df1["Resource_Allocation"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("R² Score:", r2_score(y_test, y_pred))
print("MAE:", mean_absolute_error(y_test, y_pred))


with open("randomforest.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as xgb_model.pkl")

