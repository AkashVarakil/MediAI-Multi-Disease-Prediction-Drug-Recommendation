# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import pickle

import warnings
warnings.filterwarnings('ignore')


df = pd.read_csv("kidney_disease.csv")

df.head()
df.shape

df.info()

df.drop('id', axis = 1, inplace = True)

df[['htn','dm','cad','pe','ane']] = df[['htn','dm','cad','pe','ane']].replace(to_replace={'yes':1,'no':0})
df[['rbc','pc']] = df[['rbc','pc']].replace(to_replace={'abnormal':1,'normal':0})
df[['pcc','ba']] = df[['pcc','ba']].replace(to_replace={'present':1,'notpresent':0})
df[['appet']] = df[['appet']].replace(to_replace={'good':1,'poor':0,'no':np.nan})
df['classification'] = df['classification'].replace(to_replace={'ckd':1.0,'ckd\t':1.0,'notckd':0.0,'no':0.0})

df['wc']=df['wc'].replace(["\t6200","\t8400","\t?"],[6200,8400, np.nan])
df['pcv']=df['pcv'].replace(["\t43","\t?"],[43,np.nan])
df['rc']=df['rc'].replace(["\t?"],[np.nan])

df = df.fillna(method='ffill')
df = df.fillna(method='backfill')

# Further cleaning
df['pe'] = df['pe'].replace(to_replace='good',value=0)
df['appet'] = df['appet'].replace(to_replace='no',value=0)
df['cad'] = df['cad'].replace(to_replace='\tno',value=0)
df['dm'] = df['dm'].replace(to_replace={'\tno':0,'\tyes':1,' yes':1, '':np.nan})

df['classification'].value_counts()

target_true_count = len(df.loc[df['classification'] == 1])
target_false_count = len(df.loc[df['classification'] == 0])
#target_true_count, target_false_count

sns.countplot(x = 'classification',data = df)
from sklearn.model_selection import train_test_split
feature_columns = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr', 'bu','sc', 'sod',
                   'pot', 'hemo', 'pcv', 'wc', 'rc', 'htn', 'dm', 'cad','appet', 'pe', 'ane']
predicted_class = ['classification']

X = df[feature_columns]
y = df[predicted_class]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.30, random_state=10)

from sklearn.svm import SVC
from sklearn.metrics import classification_report
classifier = SVC()
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))

# Creating a pickle file for the classifier
filename = 'prediction-kidney-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))