###### This is a modules that read csv from url.

import pandas as pd

###### This is a function that creates a dataframe from a URL that points to a CSV file
def create_dataframe(url):
    data = pd.read_csv(url)
    return data

###### This is a test function that takes as input: (a) a pandas DataFrame and (b) a list of column names. The function returns True if the following conditions hold:
###### 1. The DataFrame contains only the columns that you specified as the second argument.
###### 2. The values in each column have the same python type
###### 3. There are at least 10 rows in the DataFrame.


def test_create_dataframe(df,column_names):
    ### condition 1
    if list(df) != column_names:
        raise ColumnError("Column name does not match")
        
    ### condition 2
    ### to count how many unique types in each column 
    ### return a list of intergers
    dtypeCount =[df.iloc[:,i].apply(type).nunique() for i in range(df.shape[1])]
    if dtypeCount != [1] * len(df.columns):
        raise TypeError("Values in one or more column do not have the same python type")
        
    ### condition 3
    if len(df.index) < 10:
        raise LengthError("There are less than 10 rows in dataframe")
        
    return True

