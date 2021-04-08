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

def load_generos(cur, con):
    print("Insertando los valores de la tabla Genero...")
    f = open("./tablas/tabla_genero.pck", 'rb')
    dic_generos = pickle.load(f)
    f.close()

    key_list = list(dic_generos.keys())
    dic_len = len(dic_generos)

    rows = []
    for i in range(dic_len):
        key_i = key_list[i]
        #Obtenemos datos
        ClvGenero = dic_generos[key_i]["id"]
        Genero1 = dic_generos[key_i]["genero1"]
        Genero2 = dic_generos[key_i]["genero2"]
        Genero3 = dic_generos[key_i]["genero3"]

        #Tratar datos NULL:
        sinGenero = "Sin genero"
        if Genero1 == '\\N':
            Genero1 = sinGenero
        if Genero2 == '\\N':
            Genero2 = sinGenero
        if Genero3 == '\\N':
            Genero3 = sinGenero

        rows.append((int(ClvGenero), str(Genero1), str(Genero2), str(Genero3)))
    
    #Insert
    cur.bindarraysize = dic_len
    cur.setinputsizes(int, 64, 64, 64)
    cur.executemany("insert into Genero (ClvGenero, Genero1, Genero2, Genero3) values (:1, :2, :3, :4)", rows)
    con.commit()

def load_MiembroCrew(cur, con):
    print("Insertando los valores de la tabla MiembroCrew...")
    f = open("./tablas/tabla_miembro_crew.pck", 'rb')
    dic_miembro = pickle.load(f)
    f.close()

    key_list = list(dic_miembro.keys())
    dic_len = len(dic_miembro)

    rows = []
    for i in range(dic_len):
        key_i = key_list[i]

        #Obtenemos datos
        ClvMiembroCrew = dic_miembro[key_i]["id"]
        EsGuionista = dic_miembro[key_i]["esGuionista"]
        EsDirector = dic_miembro[key_i]["esDirector"]
        Nombre = dic_miembro[key_i]["nombre"]
        AnyoNacimiento = dic_miembro[key_i]["nacimiento"]
        AnyoFallecimiento = dic_miembro[key_i]["fallecimiento"]

        #Tratar datos NULL:
        if AnyoFallecimiento == '\\N':
            AnyoFallecimiento = -1
        if AnyoNacimiento == '\\N':
            AnyoNacimiento = -1

        rows.append((int(ClvMiembroCrew), int(EsGuionista), int(EsDirector), str(Nombre), int(AnyoNacimiento), int(AnyoFallecimiento)))
    
    #Insert
    cur.bindarraysize = dic_len
    cur.setinputsizes(int, int, int, 64, int, int)
    cur.executemany("insert into MiembroCrew (ClvMiembroCrew, EsGuionista, EsDirector, Nombre, AnyoNacimiento, AnyoFallecimiento) values (:1, :2, :3, :4, :5, :6)", rows)
    con.commit()

def load_MiembroCast(cur, con):
    print("Insertando los valores de la tabla MiembroCast...")
    f = open("./tablas/tabla_miembro_cast.pck", 'rb')
    dic_miembro = pickle.load(f)
    f.close()

    key_list = list(dic_miembro.keys())
    dic_len = len(dic_miembro)

    rows = []
    for i in range(dic_len):
        key_i = key_list[i]
        #Obtenemos datos
        ClvMiembroCast = dic_miembro[key_i]["id"]
        NombrePersonaje = dic_miembro[key_i]["personaje"]
        Nombre = dic_miembro[key_i]["nombre"]
        AnyoNacimiento = dic_miembro[key_i]["nacimiento"]
        AnyoFallecimiento = dic_miembro[key_i]["fallecimiento"]

        #Tratar datos NULL:
        if AnyoFallecimiento == '\\N':
            AnyoFallecimiento = -1
        if AnyoNacimiento == '\\N':
            AnyoNacimiento = -1

        rows.append((int(ClvMiembroCast), str(NombrePersonaje), str(Nombre), int(AnyoNacimiento), int(AnyoFallecimiento)))
    
    #Insert
    cur.bindarraysize = dic_len
    cur.setinputsizes(int, 80, 64, int, int)
    cur.executemany("insert into MiembroCast (ClvMiembroCast, NombrePersonaje, Nombre, AnyoNacimiento, AnyoFallecimiento) values (:1, :2, :3, :4, :5)", rows)
    con.commit()

def load_fecha(cur, con):
    print("Insertando los valores de la tabla Fecha...")
    f = open("./tablas/tabla_fecha.pck", 'rb')
    dic_fecha = pickle.load(f)
    f.close()

    key_list = list(dic_fecha.keys())
    dic_len = len(dic_fecha)

    rows = []
    for i in range(dic_len):
        key_i = key_list[i]

        #Obtenemos datos
        ClvFecha = key_i
        Anyo = dic_fecha[key_i]["Anyo"]
        Mes = dic_fecha[key_i]["Mes"]
        Dia = dic_fecha[key_i]["Dia"]
        DiaMesAnyo = dic_fecha[key_i]["dd/mm/aaaa"]
        rows.append((int(ClvFecha), int(Anyo), int(Mes), int(Dia), str(DiaMesAnyo)))
    
    #Insert
    cur.bindarraysize = dic_len
    cur.setinputsizes(int, int, int, int, 64)
    cur.executemany("insert into Fecha (ClvFecha, Anyo, Mes, Dia, DiaMesAnyo) values (:1, :2, :3, :4, to_date(:5, 'dd/mm/yyyy'))", rows)
    con.commit()

def load_crew(cur, con):
    print("Insertando los valores de la tabla Crew...")
    f = open("./tablas/tabla_crew.pck", 'rb')
    dic_miembro = pickle.load(f)
    f.close()

    key_list = list(dic_miembro.keys())
    dic_len = len(dic_miembro)

    rows = []
    tam = 0
    for i in range(dic_len):
        key_i = key_list[i]
        tuplas_list = list(dic_miembro[key_i]["tuplas"])
        for j in range (len(tuplas_list)):
            #Obtenemos datos
            ClvCrew = tuplas_list[j][0]
            ClvMiembroCrew = tuplas_list[j][1]
            if ClvMiembroCrew != '\\N':
                rows.append((int(ClvCrew), int(ClvMiembroCrew)))
                tam += 1
    
    #Insert
    cur.bindarraysize = tam
    cur.setinputsizes(int, int)
    cur.executemany("insert into Crew (ClvCrew, ClvMiembroCrew) values (:1, :2)", rows)
    con.commit()

def load_cast(cur, con):
    print("Insertando los valores de la tabla Cast...")
    f = open("./tablas/tabla_cast.pck", 'rb')
    dic_miembro = pickle.load(f)
    f.close()

    key_list = list(dic_miembro.keys())
    dic_len = len(dic_miembro)

    rows = []
    tam = 0
    for i in range(dic_len):
        key_i = key_list[i]
        tuplas_list = list(dic_miembro[key_i]["tuplas"])
        for j in range (len(tuplas_list)):
            #Obtenemos datos
            ClvCast = tuplas_list[j][0]
            ClvMiembroCast = tuplas_list[j][1]
            if ClvMiembroCast != '\\N':
                rows.append((int(ClvCast), int(ClvMiembroCast)))
                tam += 1
    
    #Insert
    cur.bindarraysize = tam
    cur.setinputsizes(int, int)
    cur.executemany("insert into Cast (ClvCast, ClvMiembroCast) values (:1, :2)", rows)
    con.commit()

def load_voto(cur, con):
    for voto_i in range(7):
        voto_i +=1
        print("Insertando los valores de la tabla Voto ("+str(voto_i)+")...")
        f = open("./tablas/tabla_votos"+str(voto_i)+".pck", 'rb')
        dic_voto = pickle.load(f)
        f.close()

        key_list = list(dic_voto.keys())
        dic_len = len(dic_voto)

        rows = []
        tam = 0
        for i in range(dic_len):
            key_i = key_list[i]

            #Obtenemos datos
            ClvVoto = key_i
            ClvCrew = dic_voto[key_i]["clvCrew"]
            ClvCast = dic_voto[key_i]["clvCast"]
            ClvPelicula = dic_voto[key_i]["clvPelicula"]
            ClvGenero = dic_voto[key_i]["clvGenero"]
            ClvFecha = dic_voto[key_i]["clvFecha"]
            UserName = dic_voto[key_i]["user"]
            Puntuacion = dic_voto[key_i]["rate"]

            rows.append((int(ClvVoto), int(ClvCrew), int(ClvCast), int(ClvPelicula), int(ClvGenero), int(ClvFecha), int(UserName), float(Puntuacion)))
            tam +=1

            if tam == 10240:
                #Insert
                cur.bindarraysize = tam
                cur.setinputsizes(int, int, int, int, int, int, int, float)
                cur.executemany("insert into Voto (ClvVoto, ClvCrew, ClvCast, ClvPelicula, ClvGenero, ClvFecha, UserName, Puntuacion) values (:1, :2, :3, :4, :5, :6, :7, :8)", rows)
                con.commit()
                tam = 0
                rows = []

        if tam != 10240:
            #Insert
            cur.bindarraysize = tam
            cur.setinputsizes(int, int, int, int, int, int, int, float)
            cur.executemany("insert into Voto (ClvVoto, ClvCrew, ClvCast, ClvPelicula, ClvGenero, ClvFecha, UserName, Puntuacion) values (:1, :2, :3, :4, :5, :6, :7, :8)", rows)
            con.commit()
            tam = 0
            rows = []

############################################
################### MAIN ###################

connection = None
try:
    connection = cx_Oracle.connect(
        config.username,
        config.password,
        config.dsn,
        cx_Oracle.SYSDBA)

    cur = connection.cursor()

    load_peliculas(cur, connection)
    load_generos(cur, connection)
    load_MiembroCrew(cur, connection)
    load_MiembroCast(cur, connection)
    load_fecha(cur, connection)
    load_crew(cur, connection)
    load_cast(cur, connection)
    load_voto(cur, connection)

    cur.close()
    
except cx_Oracle.Error as error:
    print(error)
finally:
    # release the connection
    if connection:
        connection.close()
