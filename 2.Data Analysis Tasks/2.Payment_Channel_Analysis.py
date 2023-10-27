# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 15:34:59 2023

@author: Radhakrishna
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load your data (assuming it's in a variable called 'data')
data = pd.read_csv('C:\\programming\\python_programs\\Day8\\2.Data Analysis Tasks\\sample_data.csv')

# Group by payment channels and calculate the count of transactions
payment_channel_counts = data['PAYMENT_CHANNEL'].value_counts()

# Find the most dominant payment channel
most_dominant_channel = payment_channel_counts.idxmax()

# Plot the payment channel distribution
plt.figure(figsize=(10, 6))
bar_plot = payment_channel_counts.plot(kind='bar', color=['red' if channel == most_dominant_channel else 'skyblue' for channel in payment_channel_counts.index])
plt.title('Distribution of Payment Channels for Prepaid Meter Recharges')
plt.xlabel('Payment Channel')
plt.ylabel('Number of Transactions')
plt.savefig('payment_channel_distribution.png')  # Save the bar plot
plt.show()

# Convert TRANSACTION_DATE to datetime format
data['TRANSACTION_DATE'] = pd.to_datetime(data['TRANSACTION_DATE'], format='%d-%m-%Y')

# Create a pivot table with Payment Channels and Transaction Dates
heatmap_data = data.pivot_table(index='PAYMENT_CHANNEL', columns=data['TRANSACTION_DATE'].dt.to_period("M"), aggfunc='size', fill_value=0)

# Plot heatmap
plt.figure(figsize=(12, 8))
heatmap_plot = sns.heatmap(heatmap_data, cmap='viridis', annot=True, fmt='d', cbar_kws={'label': 'Number of Transactions'})
plt.title('Heatmap of Payment Channels Over Time')
plt.xlabel('Month')
plt.ylabel('Payment Channel')
plt.savefig('payment_channel_heatmap.png')  # Save the heatmap
plt.show()
