# installing nessecarry libraries

import pandas as pd 
import numpy as np 

#  loading the dataset
df = pd.read_csv("C:/Users/Admin/OneDrive/Desktop/Numpy/numpy/project/numpy_practice_employees.csv")

print(df.head())

# checking for the missing value
print("Missing value is ")
print(df.isnull().sum())

df ['Salary'].fillna(df['Salary'].mean(),inplace = True)


df.replace([np.inf, -np.inf], np.nan, inplace=True)


# Fill NaN for numeric columns only
df.fillna(df.select_dtypes(include=['number']).mean(), inplace=True)


# removing dublicate record's

df.drop_duplicates(inplace= True)

# removing negative salary 

df['Salary'] = np.where(df['Salary'] < 0, df['Salary'].mean(), df['Salary'])


salary_mean = df['Salary'].mean()
salary_std = df['Salary'].std()

lower_bond = salary_mean - (3 * salary_std)
upper_bond = salary_mean + (3 * salary_std)

# Removing where salary is low or high

df = df [(df['Salary'] >= lower_bond) & (df['Salary']<= upper_bond)]

df.to_csv('Cleaned employe data.csv', index = False)

print("Data cleaned succesfully , File Saved as Cleaned employe data.csv")
