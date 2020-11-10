import pandas as pd
import os
print(os.getcwd())
file_path = "directory.csv"
df = pd.read_csv(file_path)

grouped = df.groupby(by="Country")
# print(grouped.count())
chinese_data = df[df["Country"]=="CN"]
groupby = chinese_data.groupby(by="State/Province").count()["Brand"]
print(groupby)

