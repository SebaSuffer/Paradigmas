import pandas as pd

archivo = pd.read_csv('train.csv', sep= ',')
print(archivo['neighbourhood_group'].value_counts())