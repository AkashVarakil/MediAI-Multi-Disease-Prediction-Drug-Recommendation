# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# Loading the dataset
df = pd.read_csv('./Heartnew.csv')

print(df)

def clean_dataset(df):
    assert isinstance(df, pd.DataFrame), "df needs to be a pd.DataFrame"
    df.dropna(inplace=True)
    indices_to_keep = ~df.isin([np.nan, np.inf, -np.inf]).any(1)
    return df[indices_to_keep].astype(np.float64)


df = clean_dataset(df)

print(df)
#import pandas as pd
import matplotlib.pyplot as plt

# read-in data
#data = pd.read_csv('./test.csv', sep='\t') #adjust sep to your needs

import seaborn as sns
sns.countplot(df['active'],label="Count")
plt.show()