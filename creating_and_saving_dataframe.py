# goal create a simple data and save it in various format ex. csv, xlsx, json

import pandas as pd

data = {
    "Name":['A', 'B', 'C', 'D', 'E'],
    "Age":[34, 78, 65, 54, 98],
    "City":['Mumbai', 'Nagpur', 'Nashik', 'Pune', 'Kolhapur']
}

df = pd.DataFrame(data)

print(df)

#file saving

df.to_csv("csvfile.csv", index=False)
df.to_excel("excelfile.xlsx", index=False)
df.to_json("jsonfile.json")

print("File created successfully!")