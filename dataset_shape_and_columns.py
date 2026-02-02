import pandas as pd

df = pd.read_csv('iris.csv')

print("The shape of our dataset is: ", df.shape) #printing the size of data in row, column format
print("The column names are:\n", df.columns) #printing colmun/features