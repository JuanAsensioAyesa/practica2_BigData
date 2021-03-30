import pandas as pd
import pickle
import numpy as np


def crear_dic_pelicula():
    n = 0
    i = 0

    data = {}
    for df in pd.read_csv("../data/title.basics.tsv",
                          chunksize=1000000, usecols=['tconst', 'titleType', 'primaryTitle', 'isAdult', 'startYear', 'runtimeMinutes'], sep="\t"):

        df = df.to_numpy()
        for row in df:
            id = row[0]
            tipo = row[1]
            title = row[2]
            isAdult = row[3]
            year = row[4]
            minutes = row[5]
            if tipo == "movie" or tipo == "tvMovie":
                if not id in data.keys():
                    data[id] = {}
                data[id]['tipo'] = tipo
                data[id]['titulo'] = title
                data[id]['isAdult'] = isAdult
                data[id]['minutos'] = minutes
                data[id]['year'] = year

        i += 1
        print("Chunk", i, "/ 8 ")
    f = open("./diccionarios/dic_peliculas.pck", 'wb')
    pickle.dump(data, f)
    f.close()
    print("Numero elementos", len(data))

    """
        Diccionario de la tabla pelicula
            tipo: Tipo de peli (movie/tvMovie)
            titulo: ---
            isAdult:---
            minutos:---
            year: Anyo estreno
    """


def load_dic_peliculas():
    f = open("./diccionarios/dic_peliculas.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    return dic


if __name__ == "__main__":
    crear_dic_pelicula()
    dic = load_dic_peliculas()
    f = open("../juntar_database/diccionarios/links.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    no_esta = 0
    for key in dic_link:
        if not key in dic.keys():
            no_esta += 1
    print("Faltan ", no_esta, " de ", len(dic_link))
