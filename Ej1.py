#Importa pandas y usa un alias para poder utilizar sus recursos
import pandas as pd

#Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
ruta = "./imdb_titulos.csv"
dft = pd.read_csv(ruta, delimiter=",")
print(dft.head(5))

#Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
ruta = "./imdb_elenco.csv"
dfe = pd.read_csv(ruta, delimiter=",")
print(dfe.head(5))

#Mostrar el número de registros del dataframe de titulos
print("Número de títulos:", len(dft))

#Mostrar el número de registros del dataframe de elenco
print("Número de registros en elenco:", len(dfe))