import pandas as pd
from ydata_profiling import ProfileReport

df = pd.read_csv("csv's\\titanic.csv")
print(df.head())

prof = ProfileReport(df)
prof.to_file(output_file = 'output.html')

# DO NOT TRY TO OPEN THE FILE USING LIVE SERVER, OPEN IT FROM FILE EXPLORER