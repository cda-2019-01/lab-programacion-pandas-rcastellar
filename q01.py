##
## Imprima la cantidad de registros por cada letra 
## de la columna _c1 de la tabla tbl0

import pandas as pd
import numpy as np

df = pd.read_csv("tbl0.tsv", sep="\t")
aux = df.groupby('_c1').count()['_c0']
print(aux)