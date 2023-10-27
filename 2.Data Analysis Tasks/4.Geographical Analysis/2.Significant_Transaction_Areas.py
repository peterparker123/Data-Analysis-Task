# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:56:22 2023

@author: Radhakrishna
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (assuming it's in a variable called 'data')
data = pd.read_csv('C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv')


# 1. Perform data analysis to identify areas with significantly more transactions than others
district_transaction_counts = data['DISTRICT'].value_counts()

# Identify areas with significantly more transactions (you can adjust the threshold as needed)
significant_areas = district_transaction_counts[district_transaction_counts > district_transaction_counts.mean()]

# Print information about areas with significantly more transactions
print("Areas with Significantly More Transactions:")
print(significant_areas)

# 2. Plot a graph with different colors to highlight areas with significantly more transactions
plt.figure(figsize=(15, 8))
sns.countplot(x='DISTRICT', data=data, palette=sns.color_palette("viridis", n_colors=len(significant_areas)))
plt.title('Distribution of Transactions Across Different Meter Districts')
plt.xlabel('Meter District')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45, ha='right')
plt.savefig('Significant Transactions Area')
plt.show()
