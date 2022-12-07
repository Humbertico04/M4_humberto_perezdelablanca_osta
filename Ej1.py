from ast import main

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
print("La primera película titulada {} fue estrenada en {}".format(RyJ['title'].iloc[0], RyJ['year'].iloc[0]))
print("\n")

#Listar todas las peliculas que contengan la palabra "Exorcist" ordenadas de la más vieja a la más reciente
print("Películas que contienen Exorcist en su nombre ordenadas por antigüedad:\n", 
dft[dft["title"].str.contains("Exorcist")].sort_values(by="year").reset_index().drop(['index'], axis=1))
print("\n")

#Mostrar cuantas peliculas fueron hechas en el año 1950
print("Películas hechas en 1950:", len(dft[dft["year"]==1950]))
print("\n")

#Mostrar cuantas peliculas fueron hechas de 1950 a 1959
print("Películas hechas entre 1950 y 1959:", len(dft[(dft["year"]>=1950) & (dft["year"]<=1959)]))
print("\n")

#Mostrar todos los roles o papeles que hubo en la pelicula "The Godfather". También mostrar el número total de coincidencias
gf=dfe[dfe["title"]==("The Godfather")].reset_index()
print("Los papeles en The Godfather son: \n", gf, "\nTotal papeles:", len(gf))
print("\n")

#Mostrar el elenco completo ordenado por la clasificacion "n" de la pelicula "Dracula" de 1958
drac=dfe[(dfe["title"]==("Dracula")) & (dfe["year"]==1958)].sort_values(by="n").reset_index()
print("Elenco de Dracula de 1958 ordenado por importancia: \n", drac)
print("\n")

#Mostrar cuantos papeles de "Bruce Wayne" han sido hechos en la historia de las peliculas
print("Total papeles de Bruce Wayne:", len(dfe[dfe["character"]=="Bruce Wayne"]))
print("\n")

#Mostrar cuantos papeles ha hecho "Robert De Niro" en su carrera
print("Total papeles de Robert De Niro:", len(dfe[dfe["name"]=="Robert De Niro"]))
print("\n")

#Listado de papeles como protagonista (n=1) que tuvo el actor "Charlton Heston" en la década de los 60's, ordenado por año de forma descendente
print(dfe[(dfe["n"]==1) & (dfe["name"]=="Charlton Heston") & (dfe["year"]>=1960) & (dfe["year"]<=1969)].sort_values(by="year", ascending=False).reset_index().drop(['index'], axis=1))
print("\n")

#Mostrar cuantos papeles para actores hubo en la década de los 50's
print("Total papeles para actores en la década de los 50's:", len(dfe[(dfe["type"]=="actor") & (dfe["year"]>=1950) & (dfe["year"]<=1959)]))
print("\n")

#Mostrar cuantos papeles para actrices hubo en la década de los 50's
print("Total papeles para actores en la década de los 50's:", len(dfe[(dfe["type"]=="actress") & (dfe["year"]>=1950) & (dfe["year"]<=1959)]))
print("\n")

if __name__ == "__main__":
    main()
