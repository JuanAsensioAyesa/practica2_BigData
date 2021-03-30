import pickle
import pandas as pd

if __name__ == "__main__":
    f = open("../juntar_database/diccionarios/links_ML_key.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    dic_generos = {}  # Diccionario que almacenara los generos
    dic_pelis_generos = {}  # Diccionario que almacenara los generos agrupados por peli
    i = 0
    for df in pd.read_csv("../data/ml-latest/movies.csv",
                          chunksize=1000000, usecols=['movieId', 'genres']):
        df = df.to_numpy()
        for row in df:
            id = row[0]
            generos = row[1]

            if id in dic_link:
                id = dic_link[id]
                if generos == '(no genres listed)':
                    generos = '\\N'  # Null
                else:
                    aux = generos.split('|')

                    generos = []
                    for genero in aux:
                        generos.append(genero)
                # print(generos)
                if not id in dic_pelis_generos:
                    dic_pelis_generos[id] = {'generos': []}
                if generos != '\\N':
                    for genero in generos:
                        dic_pelis_generos[id]['generos'].append(genero)
                        if not genero in dic_generos:
                            dic_generos[genero] = 0
                        dic_generos[genero] += 1
        i += 1
        print("Chunk ", i, "/ 1")

    f = open("./diccionarios/dic_generos.pck", 'wb')
    pickle.dump(dic_generos, f)
    f.close()

    # print(dic_generos)

    f = open("./diccionarios/dic_pelis_generos.pck", 'wb')
    pickle.dump(dic_pelis_generos, f)
    f.close()
    # print(dic_pelis_generos)
