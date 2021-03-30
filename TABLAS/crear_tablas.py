import pickle
import numpy as np


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
        tabla_pelicula_out[id_pelicula]['titulo'] = info_peli['title']
        tabla_pelicula_out[id_pelicula]['esAdulta'] = info_peli['isAdult']
        tabla_pelicula_out[id_pelicula]['duracion'] = info_peli['minutes']
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
            id_persona = update_miembro_crew(
                guionista, dic_personas_in, dic_miembro_crew_out, True, False)
            tabla_crew_out[id_pelicula]['tuplas'][(id_crew, id_persona)] = 0
        for director in directores:
            id_persona = update_miembro_crew(
                director, dic_personas_in, dic_miembro_crew_out, False, True)
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


if __name__ == "__main__":
    votos_in = "dic_votos"
    dic_generos_in = load_dict("../generos/diccionarios/dic_generos.pck")
    dic_pelis_generos_in = load_dict(
        "../generos/diccionarios/dic_pelis_generos.pck")

    dic_peliculas_in = load_dict(
        "../pelicula/diccionarios/dic_peliculas.pck")
    dic_personas_in = load_dict("../personas/diccionarios/people_dict.pck")

    dic_titles_in = load_dict("../titulos/diccionarios/title_akas.pck")

    dic_crew_in = load_dict("../crew/diccionarios/tabla_crew.pck")
    dic_cast_in = load_dict("../crew/diccionarios/tabla_cast.pck")

    tabla_genero_out = {}
    tabla_pelicula_out = {}
    tabla_cast_out = {}
    tabla_miembro_cast_out = {}
    tabla_crew_out = {}
    tabla_miembro_crew_out = {}
    tabla_voto_out = {}

    for i in np.arange(7):
        i = str(i+1)
        votos_in = load_dict("../votos/diccionarios/"+votos_in+i+'.pck')
        break
