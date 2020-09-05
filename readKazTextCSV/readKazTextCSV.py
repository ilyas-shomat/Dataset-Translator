import pandas as pd
from csv_maker import csv_maker


df1 = pd.read_csv('new_kaz_dataset.csv', sep=';')
df1["number"] = df1["Num"]
df1["review"] = df1["Review"]
df1["review_type"] = df1["Review_type"]

df = df1[["number", "review", "review_type"]]
# print(df)



# data_set = csv_maker.make_list_from_data_frame(df)

# csv_maker.make_csv_from_list(data_set, 'kaz_data.csv')

print(df)