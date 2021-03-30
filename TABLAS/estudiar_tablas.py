import pickle
import numpy as np

if __name__ == "__main__":
    num_votos = 0
    for i in np.arange(7):
        i = i+1
        print(i)
        f = open("./tablas/tabla_votos"+str(i)+'.pck', 'rb')
        dic = pickle.load(f)
        f.close()

        num_votos += len(dic)
        del dic

    print("NUMERO DE VOTOS REGISTRADOS ", num_votos)
