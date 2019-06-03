##
## Construya una tabla que contenga _c1 y una lista
## separada por ':' de los valores de la columna _c2
## para el archivo tbl0.tsv
## 
import pandas as pd
df = pd.read_csv("tbl0.tsv", sep="\t")
aux = df.copy()
aux = aux.groupby('_c1')['_c2'].apply(list)
aux1 = pd.DataFrame()
aux1['_c1'] = aux.keys()
aux1['lista'] = [elem for elem in aux]
aux1['lista'] = [":".join(str(v) for v in sorted(elem)) for elem in aux1['lista']]
print(aux1)
