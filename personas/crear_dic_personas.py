import pandas as pd
import pickle

if __name__ == "__main__":
    data = {}
    i = 0
    f = open("../cast/diccionarios/tabla_cast.pck", 'rb')
    dic_cast = pickle.load(f)
    f.close()

    f = open("../crew/diccionarios/tabla_crew.pck", 'rb')
    dic_crew = pickle.load(f)
    f.close()
    lista_actores = set([])
    for key in dic_cast:
        elem = dic_cast[key]
        for key_persona in elem:
            lista_actores.add(key_persona)
    for key in dic_crew:
        elem = dic_crew[key]
        for key_persona in elem:
            lista_actores.add(key_persona)
    lista_actores = list(lista_actores)
    dic_actores = {}
    for actor in lista_actores:
        dic_actores[actor] = 0
    print("Lista construida")
    for df in pd.read_csv("../data/name.basics.tsv",
                          chunksize=1000000, sep="\t"):
        df = df.to_numpy()

        for row in df:
            if row[0] in dic_actores:
                if row[0] not in data.keys():
                    data[row[0]] = {}
                data[row[0]]['nombre'] = row[1]
                data[row[0]]['nacimiento'] = row[2]
                data[row[0]]['fallecimiento'] = row[3]
        i += 1
        print("Chunk ", i)

    print(len(data))
    f = open("./diccionarios/dict_personas.pck", 'wb')
    pickle.dump(data, f)
    f.close()
    """
        Diccionario con los datos de las personas de crew y cast
            clave:Id persona
                nombre:---
                nacimiento:---
                fallecimiento:---
    """
