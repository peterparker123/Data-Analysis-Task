# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 11:29:55 2023

@author: Radhakrishna
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from sample_data.csv
file_path = 'C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv'
df = pd.read_csv(file_path)

# Examine the distribution of payment amounts
plt.figure(figsize=(10, 6))
sns.histplot(df['AMOUNT'], bins=20, kde=True)
plt.title('Distribution of Payment Amounts')
plt.xlabel('Payment Amount')
plt.ylabel('Frequency')
plt.savefig('Payment_Amount_distribution.png')
plt.show()

# Check for common payment amounts
# Group by region, meter type, and payment amount, then count occurrences
common_payment_amounts = df.groupby(['REGION', 'METRE_TYPE', 'AMOUNT']).size().reset_index(name='COUNT')

# Find the most common payment amount for each region and meter type
most_common_payments = common_payment_amounts.loc[common_payment_amounts.groupby(['REGION', 'METRE_TYPE'])['COUNT'].idxmax()]

print("Most Common Payment Amounts Grouped by Region and Meter Type:")
print(most_common_payments)

# Measure the variability of transactions in terms of value
payment_amount_variance = df['AMOUNT'].var()
payment_amount_std_dev = df['AMOUNT'].std()

print("Variance of Payment Amounts:", payment_amount_variance)
print("Standard Deviation of Payment Amounts:", payment_amount_std_dev)
