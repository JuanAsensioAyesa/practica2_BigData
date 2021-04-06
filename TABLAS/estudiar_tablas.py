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
    for i in np.arange(7):
        i = i+1
        print(i)
        f = open("./tablas/tabla_votos"+str(i)+'.pck', 'rb')
        dic = pickle.load(f)
        f.close()

        for elem in dic:

            print(dic[elem]['time'], dic_fecha[dic[elem]['time']]['dd/mm/aaaa'])
        del dic


if __name__ == "__main__":
    estudiar_fechas()
