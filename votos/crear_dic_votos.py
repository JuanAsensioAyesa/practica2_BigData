import pandas as pd
import pickle

if __name__ == "__main__":
    f = open("../juntar_database/diccionarios/links_ML_key.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    i = 0

    dic_votos = {}
    ficheros_guardados = 0
    contador = 0
    for df in pd.read_csv("../data/ml-latest/ratings.csv",
                          chunksize=1000000,):
        # for col in df.columns:
        #     print(col)
        # break
        df = df.to_numpy()
        if contador == 4:
            contador = 0
            ficheros_guardados += 1
            print("Reseteamos dic para liberar RAM")
            filename = "dic_votos"
            filename += str(ficheros_guardados) + '.pck'
            f = open("./diccionarios/"+filename, 'wb')
            pickle.dump(dic_votos, f)
            f.close()
            del dic_votos
            dic_votos = {}
        for row in df:
            id_peli = dic_link[row[1]]  # Usamos id de imdb
            id_user = row[0]
            rate = row[2]
            timestamp = row[3]
            if not id_peli in dic_votos:
                dic_votos[id_peli] = {'votos': []}
            voto = {'user': id_user, 'rate': rate, 'time': timestamp}
            dic_votos[id_peli]['votos'].append(voto)

        i += 1
        contador += 1
        print("Chunk ", i, "/ 28")
    ficheros_guardados += 1
    print("Reseteamos dic")
    filename = "dic_votos"
    filename += str(ficheros_guardados) + '.pck'
    f = open("./diccionarios/"+filename, 'wb')
    pickle.dump(dic_votos, f)
    f.close()
    del dic_votos
    """
        Dic votos
        id: id imdb
            votos:[{user,rate,time}]
    """
