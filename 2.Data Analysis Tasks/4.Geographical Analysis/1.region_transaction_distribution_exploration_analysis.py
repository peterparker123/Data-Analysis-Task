# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:53:19 2023

@author: Radhakrishna
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (assuming it's in a variable called 'data')
data = pd.read_csv('C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv')

# 1. Explore the distribution of transactions across different meter districts and regions
district_region_counts = data.groupby(['DISTRICT', 'REGION']).size().reset_index(name='Transaction Count')

# Print information about the distribution
print("Distribution of Transactions Across Different Meter Districts and Regions:")
print(district_region_counts)

# 2. Plot a graph displaying the distribution of transactions across different meter districts and regions
plt.figure(figsize=(15, 8))
sns.barplot(x='DISTRICT', y='Transaction Count', hue='REGION', data=district_region_counts, palette='viridis')
plt.title('Distribution of Transactions Across Different Meter Districts and Regions')
plt.xlabel('Meter District')
plt.ylabel('Number of Transactions')
plt.xticks(rotation=45, ha='right')
plt.legend(title='Region')
plt.savefig('Distribution of Transactions Across Different Meter districts and regions')
plt.show()


