# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:39:57 2023

@author: Radhakrishna
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (assuming it's in a variable called 'data')
data = pd.read_csv('C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv')

# 1. Analyze which payment providers are frequently used for these transactions
telco_counts = data['TELCO'].value_counts()

# 2. Check if there are multiple providers
multiple_providers = len(telco_counts) > 1

# 3. Calculate the percentage share
telco_percentage = telco_counts / telco_counts.sum() * 100

# Plot the distribution of transactions among payment providers
plt.figure(figsize=(15, 8))
sns.barplot(x=telco_counts.index, y=telco_counts.values, palette='viridis')
plt.title('Distribution of Transactions Among Payment Providers')
plt.xlabel('Payment Provider')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45, ha='right')
plt.savefig('telco analysis.png')
plt.show()

# Print information about the payment providers and their percentage share
print("Information about Payment Providers:")
print(telco_counts)

if multiple_providers:
    print("\nThere are multiple payment providers.")
else:
    print("\nThere is only one payment provider.")

print("\nPercentage Share of Transactions Among Payment Providers:")
print(telco_percentage)

