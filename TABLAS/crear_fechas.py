import pickle
import numpy as np
import datetime
if __name__ == "__main__":
    dic_fechas = {}
    i_fecha = 1
    for i in np.arange(7):
        i = i+1
        print(i)
        f = open("./tablas/tabla_votos"+str(i)+'.pck', 'rb')
        dic = pickle.load(f)
        f.close()

        for elem in dic:
            date = datetime.datetime.fromtimestamp(dic[elem]['time'])
            date = date.split('-')
            year = date[0]
            print(date)
        del dic
