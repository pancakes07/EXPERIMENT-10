"""
orignal file at:

https://colab.research.google.com/drive/1-4dudKm5njg5_qm-U8Z8NDke11Rg7sEC?usp=sharing

"""

import pandas as pd
df = pd.read_csv('/content/student-dataset.csv')
df

pip install numpy pandas matplotlib

import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Name': ['A','B','C','D','E'],
    'Marks': [85,90,None,70,60],
    'Study_Hours': [5,6,4,3,2]
}
df = pd.DataFrame(data)
print(df)

#cleaning
df['Marks']=df['Marks'].fillna(df['Marks'].mean())
print(df)

import numpy as np
df['Grade']=np.where(df['Marks'] >=75, 'Pass','Fail')
print(df)

#Visualization
plt.scatter(df['Study_Hours'],df['Marks'])
plt.title("Study hours vs Marks")
plt.show()

#Line chart Visuals
import matplotlib.pyplot as plt
plt.plot(df['Name'], df['Marks'], marker='D', linestyle='--', linewidth=3)
plt.title("Students Marks Trend")
plt.xlabel('Student')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

#Bar Plot Visuals
plt.bar(df['Name'],df['Marks'])

#Add Value labels on Bars

for i, value in enumerate(df['Marks']):
  plt.text(i, value, str(value), ha='center')
plt.title("Students Marks")
plt.xlabel('Student')
plt.ylabel('Marks')
plt.show()

#histogram
plt.hist(df['Marks'], bins=5, edgecolor='black')
plt.title("Marks Distribution")
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.grid(True)

#Mean Line
mean_value=df['Marks'].mean()
plt.axvline(mean_value, color='red', linestyle='dashed', linewidth=2)

plt.title("Marks Distribution with Mean Line")
plt.xlabel('Marks')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
