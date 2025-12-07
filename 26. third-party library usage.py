import pandas as pd
#print(pd.__version__)
# create a data frame
df=pd.read_csv("Housing.csv")
#operation 
#print(df.head())

#print(df.describe())
print(df.info())


