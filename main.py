import pandas as pd

df = pd.read_csv('Lab6Data.csv')
print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))
print("Removing extra columns")
df.drop(columns=["educ_num", "education_1", "occupation_1", "workclass_1"], inplace=True)
print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))
print("Removing missing values")
df.replace(" ?", None, inplace=True)
df = df.dropna()
print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))
print("Removing duplicate rows")
df = df.drop_duplicates()
print("Features: %i Observations: %i" % (len(df.columns), len(df.index)))
df.to_csv("Lab6OutputData.csv", index=False)
print("Clean data outputted to csv")