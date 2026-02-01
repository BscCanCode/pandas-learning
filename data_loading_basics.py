# Goal is to read different format of files ex. csv, xlsx, json

import pandas as pd

df = pd.read_csv("iris.csv")

#print(df) #reading csv files

df2 = pd.read_excel("iris.xlsx") #before running ensure openpyxl is installed

#print(df2) #reading excel file

df3 = pd.read_json('anscombe.json')
print(df3) #reading json file