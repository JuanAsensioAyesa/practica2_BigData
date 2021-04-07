import cx_Oracle
import config
import pickle

#Carga los valores de la tabla Peliculas
def load_peliculas(cur, con):
    print("Insertando los valores de la tabla Peliculas...")
    f = open("./tablas/tabla_pelicula.pck", 'rb')
    dic_peliculas = pickle.load(f)
    f.close()

    key_list = list(dic_peliculas.keys())
    dic_len = len(dic_peliculas)

    rows = []
    for i in range(dic_len):
        key_i = key_list[i]

        #Obtenemos datos
        ClvPelicula = dic_peliculas[key_i]["id"]
        Titulo = dic_peliculas[key_i]["titulo"]
        EsAdulta = dic_peliculas[key_i]["esAdulta"]
        Duracion = dic_peliculas[key_i]["duracion"]
        AnyoEstreno = dic_peliculas[key_i]["AnyoEstreno"]

        #Tratar datos NULL:
        if Duracion == '\\N':
            Duracion = -1
        if AnyoEstreno == '\\N':
            AnyoEstreno = -1
        rows.append((int(ClvPelicula), str(Titulo), int(EsAdulta), int(Duracion), int(AnyoEstreno)))
    
    #Insert
    cur.bindarraysize = dic_len
    cur.setinputsizes(int, 170, 1, int, int)
    cur.executemany("insert into Pelicula (ClvPelicula, Titulo, EsAdulta, Duracion, AnyoEstreno) values (:1, :2, :3, :4, :5)", rows)
    con.commit()



connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        cx_Oracle.SYSDBA)

    cur = connection.cursor()

    load_peliculas(cur, connection)

    cur.close()
    
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()
