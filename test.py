from pandas import pandas as pd

File = pd.read_excel('pass.xlsx', header=None)
print(File)
print(File[1][0])
print(File[0][1])
print(File[1][1])
print(File[0][2])
print(File[1][2])

