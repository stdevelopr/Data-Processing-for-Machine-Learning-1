import numpy as np
import pandas as pd
from sklearn import preprocessing

dataset = pd.read_csv('Data.csv')


def encode(dataset):
    c = int(input("Enter the index of the column to encode\n"))
    d = input("Enconde as dummy variables? (y or n)")
    
    ##Get the proper column in the proper shape
    column = dataset.iloc[:,c].values.reshape((-1,1))
    
    if d=='n':
        #Instatiate an encoder object
        oc = preprocessing.OrdinalEncoder()
        
        #Fit and transform the column into the encoding
        oc.fit(column)
        encoded_column = oc.transform(column)
        #Substitue the values into the dataset
        dataset.iloc[:,c] = encoded_column
        return dataset
    elif d=='y':
        ohe = preprocessing.OneHotEncoder()
        ohe.fit(column)
        a = ohe.transform(column).toarray()
        for index, ct in enumerate(ohe.categories_[0]):
            dataset[ct] = a[:,index]
            
        dataset = dataset.drop(dataset.columns[c], axis=1) 
        return dataset
 
process = True       
while process:
    dataset = encode(dataset)
    print("The head of the dataset looks like:\n", dataset.head())
    c = input("To stop processing enter 'x':\n")
    if c=='x':
        process=False

#create a new csv
dataset.to_csv('Data_new.csv', index=False)