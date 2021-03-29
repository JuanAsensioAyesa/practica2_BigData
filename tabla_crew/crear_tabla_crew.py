import pandas as pd
import pickle

if __name__ == "__main__":
    f = open("../juntar_database/diccionarios/links.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    data = {}
    i = 0
    # print(dic_link)
    esta = 0
    for df in pd.read_csv("../data/title.crew.tsv",
                          chunksize=1000000, sep="\t"):
        df = df.to_numpy()
        for row in df:
            if row[0] in dic_link:
                esta += 1
                if not row[0] in data:
                    data[row[0]] = {'directors': [], 'writers': []}
                for director in row[1].split(','):
                    data[row[0]]['directors'].append(director)
                for writer in row[2].split(','):
                    data[row[0]]['writers'].append(writer)

        i += 1
        print("Chunk ", i)

    print("Hay ", esta)
    f = open("./diccionarios/tabla_crew.pck", 'wb')
    pickle.dump(data, f)
    f.close()

    """
        Diccionario de la crew de una peli
        clave: clave imdb de pelicula
            directors: ids de directores
            writers: ids de guionistas 
    """
