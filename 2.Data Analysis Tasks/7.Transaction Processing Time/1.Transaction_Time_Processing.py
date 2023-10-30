# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 12:27:04 2023

@author: Radhakrishna
"""

import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv'
# Read the CSV file into a DataFrame
df = pd.read_csv(file_path)

# Convert TRANSACTION_DATE and Payment_Completed to datetime
df['TRANSACTION_DATE'] = pd.to_datetime(df['TRANSACTION_DATE'])
df['Payment_Completed'] = pd.to_datetime(df['Payment_Completed'])

print(df['TRANSACTION_DATE'])
print(df['Payment_Completed'])
# Calculate the time taken for each transaction
df['TimeTaken'] = df['Payment_Completed'] - df['TRANSACTION_DATE']

# Calculate average and maximum time taken
average_time = df['TimeTaken'].mean()
max_time = df['TimeTaken'].max()

print(f"Average Time Taken: {average_time}")
print(f"Maximum Time Taken: {max_time}")

# You can also plot a histogram of time taken if you're interested in the distribution
df['TimeTaken'].astype('timedelta64[D]').plot.hist(bins=50)
plt.title('Distribution of Time Taken for Transactions')
plt.xlabel('Time Taken (days)')
plt.ylabel('Number of Transactions')
plt.show()
