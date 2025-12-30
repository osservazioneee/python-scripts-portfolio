import pandas as pd

file = input("CSV file name: ")

data = pd.read_csv(file)
data = data.drop_duplicates()
data = data.fillna("")

data.to_csv("cleaned.csv", index=False)
print("CSV cleaned")
