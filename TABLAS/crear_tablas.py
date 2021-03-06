import pickle
import numpy as np
import datetime


def procesar_fichero(dic_votos):
    a = 0


def load_dict(filename):
    f = open(filename, 'rb')
    dic = pickle.load(f)
    f.close()
    return dic

# Modifica el diccionario de la tabla de genero y devuelve el id del genero


def update_genero(id_pelicula, tabla_genero, dic_generos_in, dic_pelis_generos):

    if not id_pelicula in tabla_genero:
        tabla_genero[id_pelicula] = {}
        # Id de los generos, empezando por 0
        tabla_genero[id_pelicula]['id'] = len(tabla_genero)-1
        generos = dic_pelis_generos[id_pelicula]['generos']

        tabla_genero[id_pelicula]['genero1'] = '\\N'
        tabla_genero[id_pelicula]['genero2'] = '\\N'
        tabla_genero[id_pelicula]['genero3'] = '\\N'

        i = 1
        for genero in generos:
            tabla_genero[id_pelicula]['genero'+str(i)] = genero
            i += 1
            if i == 4:
                break

    return tabla_genero[id_pelicula]['id']

# Modifica el diccionario de la tabla de peliculas y devuelve el id


def update_peliculas(id_pelicula, tabla_pelicula_out, dic_peliculas_in):
    if not id_pelicula in tabla_pelicula_out:
        tabla_pelicula_out[id_pelicula] = {}
        tabla_pelicula_out[id_pelicula]['id'] = len(tabla_pelicula_out)-1
        info_peli = dic_peliculas_in[id_pelicula]
        tabla_pelicula_out[id_pelicula]['titulo'] = info_peli['titulo']
        tabla_pelicula_out[id_pelicula]['esAdulta'] = info_peli['isAdult']
        tabla_pelicula_out[id_pelicula]['duracion'] = info_peli['minutos']
        tabla_pelicula_out[id_pelicula]['AnyoEstreno'] = info_peli['year']
    return tabla_pelicula_out[id_pelicula]['id']
# Modifica el diccionario de la tabla de crew y devuelve el id


def update_crew(id_pelicula, tabla_crew_out, dic_crew_in, dic_personas_in, dic_miembro_crew_out):

    if not id_pelicula in tabla_crew_out:
        tabla_crew_out[id_pelicula] = {}
        id_crew = len(tabla_crew_out)-1
        # Almacenamos una entrada por tupla
        tabla_crew_out[id_pelicula]['id'] = id_crew
        guionistas = dic_crew_in[id_pelicula]['writers']
        directores = dic_crew_in[id_pelicula]['directors']
        tabla_crew_out[id_pelicula]['tuplas'] = {}
        for guionista in guionistas:
            # print("guionista")
            id_persona = '\\N'
            if guionista in dic_personas_in:
                id_persona = update_miembro_crew(
                    guionista, dic_personas_in, dic_miembro_crew_out, True, False)
            # print("guionista 2")
            tabla_crew_out[id_pelicula]['tuplas'][(id_crew, id_persona)] = 0
        for director in directores:
            # print("director")
            id_persona = '\\N'
            if director in dic_personas_in:
                id_persona = update_miembro_crew(
                    director, dic_personas_in, dic_miembro_crew_out, False, True)
                # print("director 2")

            tabla_crew_out[id_pelicula]['tuplas'][(id_crew, id_persona)] = 0

    return tabla_crew_out[id_pelicula]['id']
# Modifica el diccionario de la tabla de miembro crew y devuelve el id


def update_miembro_crew(id_persona, dic_personas_in, dic_miembro_crew_out, esGuionista, esDirector):

    if not id_persona in dic_miembro_crew_out:
        dic_miembro_crew_out[id_persona] = {}
        dic_miembro_crew_out[id_persona]['id'] = len(dic_miembro_crew_out)-1
        dic_miembro_crew_out[id_persona]['nombre'] = dic_personas_in[id_persona]['nombre']
        dic_miembro_crew_out[id_persona]['nacimiento'] = dic_personas_in[id_persona]['nacimiento']
        dic_miembro_crew_out[id_persona]['fallecimiento'] = dic_personas_in[id_persona]['fallecimiento']

        dic_miembro_crew_out[id_persona]['esGuionista'] = esGuionista
        dic_miembro_crew_out[id_persona]['esDirector'] = esDirector
    else:
        if esGuionista:
            dic_miembro_crew_out[id_persona]['esGuionista'] = esGuionista
        if esDirector:
            dic_miembro_crew_out[id_persona]['esDirector'] = esDirector

    return dic_miembro_crew_out[id_persona]['id']


def update_cast(id_pelicula, tabla_cast_out, dic_cast_in, dic_personas_in, dic_miembro_cast_out):

    if not id_pelicula in tabla_cast_out:
        tabla_cast_out[id_pelicula] = {}
        id_cast = len(tabla_cast_out)-1
        # Almacenamos una entrada por tupla
        tabla_cast_out[id_pelicula]['id'] = id_cast
        tabla_cast_out[id_pelicula]['tuplas'] = {}
        for persona in dic_cast_in[id_pelicula]:

            roles = dic_cast_in[id_pelicula][persona]['roles']
            personaje = '\\N'
            if 'characters' in dic_cast_in[id_pelicula][persona]:
                personaje = dic_cast_in[id_pelicula][persona]['characters'][0]

            if ('actor' in roles or 'actress' in roles) and persona in dic_personas_in:
                id_persona = update_miembro_cast(
                    persona, dic_personas_in, dic_miembro_cast_out, personaje)
                tabla_cast_out[id_pelicula]['tuplas'][(
                    id_cast, id_persona)] = 0

    return tabla_crew_out[id_pelicula]['id']
# Modifica el diccionario de la tabla de miembro crew y devuelve el id


def update_miembro_cast(id_persona, dic_personas_in, dic_miembro_cast_out, nombrePersonaje):

    if not id_persona in dic_miembro_cast_out:
        dic_miembro_cast_out[id_persona] = {}
        dic_miembro_cast_out[id_persona]['id'] = len(dic_miembro_cast_out)-1
        dic_miembro_cast_out[id_persona]['nombre'] = dic_personas_in[id_persona]['nombre']
        dic_miembro_cast_out[id_persona]['nacimiento'] = dic_personas_in[id_persona]['nacimiento']
        dic_miembro_cast_out[id_persona]['fallecimiento'] = dic_personas_in[id_persona]['fallecimiento']

        dic_miembro_cast_out[id_persona]['personaje'] = nombrePersonaje

    return dic_miembro_cast_out[id_persona]['id']


def update_fecha(timestamp, dic_fechas_out):
    date = datetime.datetime.fromtimestamp(timestamp)

    year = date.year
    month = date.month
    day = date.day
    id_fecha = year*10000 + month * 100 + day
    if not id_fecha in dic_fechas_out:
        dic_fechas_out[id_fecha] = {}
        dic_fechas_out[id_fecha]['Dia'] = day
        dic_fechas_out[id_fecha]['Mes'] = month
        dic_fechas_out[id_fecha]['Anyo'] = year
        dic_fechas_out[id_fecha]['dd/mm/aaaa'] = str(
            day) + "/"+str(month)+"/"+str(year)
    return id_fecha


if __name__ == "__main__":
    votos_in_file = "dic_votos"
    dic_generos_in = load_dict("../generos/diccionarios/dic_generos.pck")
    dic_pelis_generos_in = load_dict(
        "../generos/diccionarios/dic_pelis_generos.pck")

    dic_peliculas_in = load_dict(
        "../pelicula/diccionarios/dic_peliculas.pck")
    dic_personas_in = load_dict("../personas/diccionarios/people_dict.pck")

    dic_titles_in = load_dict("../titulos/diccionarios/title_akas.pck")

    dic_crew_in = load_dict("../crew/diccionarios/tabla_crew.pck")
    dic_cast_in = load_dict("../cast/diccionarios/tabla_cast.pck")

    tabla_genero_out = {}
    tabla_pelicula_out = {}
    tabla_cast_out = {}
    tabla_miembro_cast_out = {}
    tabla_crew_out = {}
    tabla_miembro_crew_out = {}
    tabla_voto_out = {}
    tabla_fecha_out = {}

    id_votos = 0
    votos_out = {}
    for i in np.arange(7):
        i = str(i+1)
        print(i)
        votos_in = load_dict("../votos/diccionarios/"+votos_in_file+i+'.pck')
        # peliculas = votos_in.keys()
        no_esta = 0
        total = 0
        for pelicula in votos_in:
            total += 1
            if pelicula in dic_pelis_generos_in and pelicula in dic_peliculas_in and pelicula in dic_crew_in and pelicula in dic_cast_in:
                for voto in votos_in[pelicula]['votos']:
                    votos_out[id_votos] = {}
                    votos_out[id_votos]['clvCrew'] = update_crew(
                        pelicula, tabla_crew_out, dic_crew_in, dic_personas_in, tabla_miembro_crew_out)

                    votos_out[id_votos]['clvCast'] = update_cast(
                        pelicula, tabla_cast_out, dic_cast_in, dic_personas_in, tabla_miembro_cast_out)

                    votos_out[id_votos]['clvPelicula'] = update_peliculas(
                        pelicula, tabla_pelicula_out, dic_peliculas_in)

                    votos_out[id_votos]['clvGenero'] = update_genero(
                        pelicula, tabla_genero_out, dic_generos_in, dic_pelis_generos_in)
                    votos_out[id_votos]['user'] = voto['user']
                    votos_out[id_votos]['rate'] = voto['rate']
                    votos_out[id_votos]['clvFecha'] = update_fecha(
                        voto['time'], tabla_fecha_out)
                    # print("Generos actualizados")
                    id_votos += 1
                    # print("Liberando pelicula de RAM")
                    # del votos_in[pelicula
            else:
                no_esta += 1
        print("Faltan ", no_esta, " de ", total)
        print("Guardando votos ", i)
        f = open("./tablas/tabla_votos"+str(i)+".pck", 'wb')
        print("Guardado")
        pickle.dump(votos_out, f)
        f.close()
        del votos_out
        votos_out = {}

    print("Tabla pelicula guardada")
    f = open("./tablas/tabla_pelicula.pck", 'wb')
    pickle.dump(tabla_pelicula_out, f)
    f.close()
    del tabla_pelicula_out
    f = open("./tablas/tabla_genero.pck", 'wb')
    pickle.dump(tabla_genero_out, f)
    f.close()
    del tabla_genero_out
    print("Tabla genero guardada")
    f = open("./tablas/tabla_cast.pck", 'wb')
    pickle.dump(tabla_cast_out, f)
    f.close()
    del tabla_cast_out
    print("Tabla cast guardada")
    f = open("./tablas/tabla_crew.pck", 'wb')
    pickle.dump(tabla_crew_out, f)
    f.close()
    del tabla_crew_out
    print("Tabla crew guardada")
    f = open("./tablas/tabla_miembro_crew.pck", 'wb')
    pickle.dump(tabla_miembro_crew_out, f)
    f.close()
    del tabla_miembro_crew_out
    print("Tabla miembro crew guardada")
    f = open("./tablas/tabla_miembro_cast.pck", 'wb')
    pickle.dump(tabla_miembro_cast_out, f)
    f.close()
    del tabla_miembro_cast_out
    print("Tabla miembro cast guardada")
    f = open("./tablas/tabla_fecha.pck", 'wb')
    pickle.dump(tabla_fecha_out, f)
    f.close()
    del tabla_fecha_out
    print("Tabla fechas guardada")
