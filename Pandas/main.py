import pandas as pd
import numpy as np

exam_data={
    'name':['Anastacia','John','Ezra','David','Ethan','Jessica','Mathew','Brian','Michael','Jason'],
    'score':[30.0,56,23.9,np.nan,34,np.nan,21,60,np.nan,31.1]}
labels=['a','b','c','d','e','f','g','h','i','j']

df=pd.DataFrame(exam_data,index=labels)
print("summary about basic info of this dataframe: ")
print(df.info())