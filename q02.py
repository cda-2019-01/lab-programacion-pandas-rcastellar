##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
import pandas as pd
import numpy as np

df = pd.read_csv("tbl0.tsv", sep="\t")
aux = df.groupby('_c1').mean()['_c2']
print(aux)