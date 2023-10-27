# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:25:54 2023

@author: Radhakrishna
"""

# Transaction Trends:
'''Analyze trends in transaction volumes over time. Are there specific
 days or times when transactions are more frequent?
Investigate seasonal variations in transaction amounts. 
Do certain months or seasons see higher transaction amounts?'''


import pandas as pd
import matplotlib.pyplot as plt

# Load your data (assuming it's in a variable called 'data')
data = pd.read_csv('C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv')

# Convert TRANSACTION_DATE to datetime format
data['TRANSACTION_DATE'] = pd.to_datetime(data['TRANSACTION_DATE'], format='%d-%m-%Y')

# Group by day and calculate transaction count
daily_transactions = data.groupby(data['TRANSACTION_DATE'].dt.date)['TRANSACTION_ID'].count()
print(daily_transactions)

# Plot daily transaction trends
plt.figure(figsize=(10, 6))
daily_transactions.plot(kind='line', marker='o')
plt.title('Daily Transaction Trends')
plt.xlabel('Date')
plt.ylabel('Number of Transactions')
plt.show()

# Group by month and calculate transaction sum
monthly_transaction_amounts = data.groupby(data['TRANSACTION_DATE'].dt.to_period("M"))['AMOUNT'].sum()

# Plot monthly transaction trends
plt.figure(figsize=(10, 6))
monthly_transaction_amounts.plot(kind='bar', color='skyblue')
plt.title('Monthly Transaction Amounts')
plt.xlabel('Month')
plt.ylabel('Total Amount')
plt.savefig('monthly_transaction_amounts.png')
plt.show()
