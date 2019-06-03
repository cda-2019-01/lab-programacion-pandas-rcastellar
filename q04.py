##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
import pandas as pd
import numpy as np

df = pd.read_csv("tbl1.tsv", sep="\t")
aux = df['_c4'].unique()
aux = [line.upper() for line in aux]
aux.sort()
print(aux)