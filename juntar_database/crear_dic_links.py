import pandas as pd
import numpy as np
import pickle
import sys
sys.path.insert(0, "../titulos/")
import estudiarDic  # noqa


def load_movies():

    df = pd.read_csv("../data/ml-latest/movies.csv",
                     usecols=['movieId', 'title'])
    return df

# Carga el csv y devuelve un dic
# {id_Imdb:id_ML}


def load_links():
    df = pd.read_csv("../data/ml-latest/links.csv",
                     usecols=['movieId', 'imdbId'])
    dic = {}
    df = df.to_numpy()

    for row in df:
        aux = str(row[1])
        while len(aux) < 7:
            aux = "0"+aux
        dic["tt"+aux] = row[0]
    return dic


if __name__ == "__main__":
    dic_links = load_links()
   # print(dic_links)
    f = open("./diccionarios/links.pck", 'wb')
    pickle.dump(dic_links, f)
    f.close()
