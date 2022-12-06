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

#Mostrar las peliculas que en el titulo tienen la palabra "Dracula". También mostrar el número total de peliculas que coincidan con este requisito
drac=dft[dft["title"].str.contains("Dracula")].reset_index()
print("Las películas con Dracula en el nombre son: \n", drac, "\nTotal películas:", len(drac))
print("\n")

#Mostrar los 10 titulos más comunes (que más se repiten)
print("Los 10 títulos más comunes son:\n", dft["title"].value_counts().head(10))
print("\n")

#Mostrar cual fue la primer pelicula hecha titulada "Romeo and Juliet"
RyJ=dft[dft["title"].str.contains("Romeo and Juliet")].sort_values(by="year").head(1)
print(RyJ)
print("La primera película titulada {} fue estrenada en {}".format(RyJ['title'].iloc[0], RyJ['year'].iloc[0]))
print("\n")

#Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
print(dft[dft["title"].str.contains("Exorcist")].sort_values(by="year").reset_index().drop(['index'], axis=1))
print("\n")

#Mostrar cuantas peliculas fueron hechas en el año 1950
print("Películas hechas en 1950:", len(dft[dft["year"]==1950]))
print("\n")
