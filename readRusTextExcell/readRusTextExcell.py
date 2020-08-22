import pandas as pd
from translatorPac import google_cloud_translator as tr

df = pd.read_excel('rusTextExcell.xlsx', index_col = 0)

df["review"] = df["Review"]
df["type"] = df["review_type"]

df = df[["review", "type"]]

df_list = list(df['review'])

# print(df)
# print(df_list)


print(tr.list_translator(df_list))
