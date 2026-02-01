import pandas as pd

df = pd.read_csv('iris.csv')

print("Info of dataset: ")
print(df.info())

print("Description of dataset: ")
print(df.describe())

#info helps understand where are there any null values, datatypes, col names, also shape like in this dataset it is (150, 6)
#describe helps us understand statistics of the dataset like mean, median etc