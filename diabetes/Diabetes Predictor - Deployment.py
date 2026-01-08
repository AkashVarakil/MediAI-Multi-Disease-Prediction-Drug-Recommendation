# Importing essential libraries
import numpy as np
import pandas as pd
import pickle

# Loading the dataset
df = pd.read_csv('./diabetes.csv')

# Renaming DiabetesPedigreeFunction as DPF
df = df.rename(columns={'DiabetesPedigreeFunction':'DPF'})

#import pandas as pd
import matplotlib.pyplot as plt

# read-in data
#data = pd.read_csv('./test.csv', sep='\t') #adjust sep to your needs

import seaborn as sns
sns.countplot(df['Outcome'],label="Count")
plt.show()

# count occurences
#occurrences = df.loc[:, 'Outcome'].value_counts()

# plot histogram
#plt.bar(occurrences.keys(), occurrences)
#plt.show()


# Replacing the 0 values from ['Glucose','BloodPressure','SkinThickness','Insulin','BMI'] by NaN
df_copy = df.copy(deep=True)
df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = df_copy[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0,np.NaN)

# Replacing NaN value by mean, median depending upon distribution
df_copy['Glucose'].fillna(df_copy['Glucose'].mean(), inplace=True)
df_copy['BloodPressure'].fillna(df_copy['BloodPressure'].mean(), inplace=True)
df_copy['SkinThickness'].fillna(df_copy['SkinThickness'].median(), inplace=True)
df_copy['Insulin'].fillna(df_copy['Insulin'].median(), inplace=True)
df_copy['BMI'].fillna(df_copy['BMI'].median(), inplace=True)

# Model Building
from sklearn.model_selection import train_test_split
X = df.drop(columns='Outcome')
y = df['Outcome']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=0)

from sklearn.neural_network  import MLPClassifier
#from sklearn.ensemble  import GradientBoostingClassifier
from sklearn.metrics import classification_report
classifier = MLPClassifier(max_iter=500)
classifier.fit(X_train, y_train)
print("Accuracy on training set: {:.3f}".format(classifier.score(X_train, y_train)))
y_pred = classifier.predict(X_test)
print(classification_report(y_test, y_pred))




# Creating a pickle file for the classifier
filename = 'diabetes-prediction-rfc-model.pkl'
pickle.dump(classifier, open(filename, 'wb'))


data = np.array([[0,137,40,35,168,43.1,2.288,33]])
my_prediction = classifier.predict(data)
print(my_prediction)

if my_prediction == 1:
    Answer = 'Diabetic'


    msg = 'Hello:According to our Calculations, You have DIABETES'
    print('Hello:According to our Calculations, You have DIABETES')

else:
    Answer = 'No-Diabetic'
    msg = 'Congratulations!!  You DON T have diabetes'
    print('Congratulations!! You DON T have diabetes')
    Prescription = 'Nill'