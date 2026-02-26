# How do you merge two data frames in Pandas?

# ---->In Pandas, you merge DataFrames using pd.merge()
import pandas as pd

df1 = pd.DataFrame({
    "id": [1, 2, 3],
    "name": ["Allan", "Sita", "Ram"]
})

df2 = pd.DataFrame({
    "id": [1, 2, 4],
    "marks": [85, 90, 75]
})

merged_df = pd.merge(df1, df2, on="id")  #two dataframe ko id matching matra merge huncha 

print(merged_df)