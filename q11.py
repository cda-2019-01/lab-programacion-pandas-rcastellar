##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd

df = pd.read_csv("tbl2.tsv", sep="\t")
aux = df.copy()
aux['_c5'] = aux['_c5a'] + ":" + aux['_c5b'].astype('str')
aux = aux.groupby('_c0')['_c5'].apply(list)
aux1 = pd.DataFrame()
aux1['_c0'] = aux.keys()
aux1['lista'] = [elem for elem in aux]
aux1['lista'] = [",".join(str(v) for v in sorted(elem)) for elem in aux1['lista']]
print(aux1)