import pandas as pd

data = {
    "cust_id":[101, 102, 103],
    "Amount":[78, 98, 65]
}
data2 = {
    "cust_id":[101, 89, 90],
    "order_amount":[87, 76, 65]
}
print("Dataframe1")
df = pd.DataFrame(data)
print(df)
print("dataframe2")
df1 = pd.DataFrame(data2)
print(df1)

#concantenate two dataframe verticall
con_ver = pd.concat([df, df1], axis=0, ignore_index=True)
print(con_ver)

#concantenate horizontally

con_hor = pd.concat([df, df1], axis=1, ignore_index=True)
print(con_hor)