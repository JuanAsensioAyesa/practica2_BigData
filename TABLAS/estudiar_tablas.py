import pickle
import numpy as np
import time


def estudiar_votos():
    num_votos = 0
    for i in np.arange(7):
        i = i+1
        print(i)
        f = open("./tablas/tabla_votos"+str(i)+'.pck', 'rb')
        dic = pickle.load(f)
        f.close()
        time.sleep(10)
        num_votos += len(dic)
        for elem in dic:
            print(dic[elem])
        del dic

    print("NUMERO DE VOTOS REGISTRADOS ", num_votos)


def estudiar_genero():
    f = open("./tablas/tabla_genero.pck", 'rb')
    dic = pickle.load(f)
    for elem in dic:
        print(dic[elem])


def estudiar_fechas():
    f = open("./tablas/tabla_fecha.pck", 'rb')
    dic_fecha = pickle.load(f)
    f.close()
    print(len(dic_fecha))
    for i in np.arange(7):
        i = i+1
        print(i)
        f = open("./tablas/tabla_votos"+str(i)+'.pck', 'rb')
        dic = pickle.load(f)
        f.close()

        # for elem in dic:

        #     print(dic[elem]['time'], dic_fecha[dic[elem]['time']]['dd/mm/aaaa'])
        del dic


def estudiar_peliculas():
    f = open("./tablas/tabla_pelicula.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    key = list(dic.keys())[0]
    print(dic[key].keys())


def estudiar_crew():
    f = open("./tablas/tabla_crew.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    key = list(dic.keys())[0]
    print(dic[key]['tuplas'])


def estudiar_cast():
    f = open("./tablas/tabla_cast.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    key = list(dic.keys())[10021]
    print(dic[key].keys())


def estudiar_miembro_cast():
    f = open("./tablas/tabla_miembro_cast.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    key = list(dic.keys())[0]
    print(dic[key].keys())


def estudiar_miembro_crew():
    f = open("./tablas/tabla_miembro_crew.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    key = list(dic.keys())[0]
    print(dic[key].keys())


if __name__ == "__main__":
    estudiar_miembro_crew()
