import pandas as pd

df = pd.read_excel('kazTextExcell.xlsx', index_col = 0)

df["review"] = df["Review"]
df["type"] = df["review_type"]

df = df[["review", "type"]]
print(df)

