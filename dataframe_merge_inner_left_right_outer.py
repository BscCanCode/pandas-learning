import pandas as pd

data = {
    "cust_id":[101, 102, 103],
    "Amount":[78, 98, 65]
}
data2 = {
    "cust_id":[101, 89, 90],
    "order_amount":[87, 76, 65]
}

df = pd.DataFrame(data)
print(df)

df1 = pd.DataFrame(data2)
print(df1)

print("Print inner join")
#priniting inner join
merge = pd.merge(df, df1, how="inner")
print(merge)

print("Printing left join")
#left join
merge1 = pd.merge(df, df1, how="left")
print(merge1)

print("Printing right join")
#right join
merge2 = pd.merge(df, df1, how="right")
print(merge2)

print("Printing outer join")
#outer join
merge3 = pd.merge(df, df1, how="outer")
print(merge3)