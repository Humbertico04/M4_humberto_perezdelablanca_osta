#Importa pandas y usa un alias para poder utilizar sus recursos
import pandas as pd

#Cargar como dataframe de pandas el csv imdb_titulos.csv y mostrar sus 5 primeros registros
ruta = "./imdb_titulos.csv"
dft = pd.read_csv(ruta, delimiter=",")
print(dft.head(5))
print("\n")

#Cargar como dataframe de pandas el csv imdb_elenco.csv y mostrar sus 5 primeros registros
ruta = "./imdb_elenco.csv"
dfe = pd.read_csv(ruta, delimiter=",")
print(dfe.head(5))
print("\n")

#Mostrar el número de registros del dataframe de titulos
print("Número de títulos:", len(dft))
print("\n")

#Mostrar el número de registros del dataframe de elenco
print("Número de registros en elenco:", len(dfe))
print("\n")

#Mostrar las 5 peliculas más antiguas del listado de titulos
print("Las 5 películas más antiguas son:\n", dft.sort_values(by="year").head(5))
print("\n")

#Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
print("Las películas con Dracula en el nombre son:\n", dft[dft["title"].str.contains("Dracula")])
print("Número de películas con Dracula en el nombre:", len(dft[dft["title"].str.contains("Dracula")]))
print("\n")