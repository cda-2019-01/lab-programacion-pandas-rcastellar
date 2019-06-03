##
## Agregue el año como una columna a la tabla tbl0.tsv 
import pandas as pd
import numpy as np

df = pd.read_csv("tbl0.tsv", sep="\t")
aux = df.copy()
aux['ano'] = aux['_c3'].str.split('-').str[0]
print(aux)