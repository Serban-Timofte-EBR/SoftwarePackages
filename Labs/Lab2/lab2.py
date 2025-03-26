import pandas as pd

df = pd.read_csv('date/clienti_leasing20.csv')

print(df.iloc[:,2:4])
