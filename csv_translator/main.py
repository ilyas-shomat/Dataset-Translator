from csv_translator import csv_convert
import pandas as pd


data_frame = pd.read_csv('rusText.csv', sep=';')
data_frame["number"] = data_frame["Num"]
data_frame["review"] = data_frame["Review"]
data_frame["review_type"] = data_frame["review_type"]

df = data_frame[["number", "review", "review_type"]]

list = csv_convert.make_list_from_data_frame(df)

print(list)