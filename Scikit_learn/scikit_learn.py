import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
from sklearn.model_selection import train_test_split

df = pd.read_csv("C:\\Users\\002CL0744\\Documents\\NLP-NaturalLanguageProcessing\\Scikit_learn\\smsspamcollection.tsv", sep='\t')

print(df.head()) #first 5 rows
print(df.isnull().sum()) #sum of null values in the file
print(len(df)) #length of file
print(df['label'].unique()) #unique values in label column
print(df['label'].value_counts()) #count of each unique value

#visualization with length
plt.xscale('log')
bins = 1.15**(np.arange(0,50))
plt.hist(df[df['label'] == 'ham']['length'], bins=bins, alpha = 0.8)
plt.hist(df[df['label'] == 'spam']['length'], bins=bins, alpha = 0.8)
plt.legend('ham','spam')
plt.show()

#visualization with punct 
plt.xscale('log')
bins = 1.5**(np.arange(0,15))
plt.hist(df[df['label'] == 'ham']['punct'], bins=bins, alpha = 0.8)
plt.hist(df[df['label'] == 'spam']['punct'], bins=bins, alpha = 0.8)
plt.legend('ham','spam')
plt.show()

