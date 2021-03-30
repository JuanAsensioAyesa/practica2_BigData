import pandas as pd
import numpy as np
import pickle

if __name__ == "__main__":
    regions = {}
    i = 1
    f = open("../juntar_database/diccionarios/links.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    for df in pd.read_csv("../data/title.akas.tsv",
                          chunksize=1000000, usecols=["titleId", "ordering", "isOriginalTitle", "region", "language", "title"], sep="\t"):

        # for col in df.columns:
        #     print(col)
        df = df.to_numpy()
        # print(df.shape)
        for row in df:
            if row[0] in dic_link:
                titleId = row[0]
                ordering = row[1]
                title = row[2]
                region = row[3]
                language = row[4]
                isOriginal = row[5]

                if not titleId in regions.keys():
                    regions[titleId] = {}

                if(ordering == 1):
                    # Guardamos el primero, para que haya siempre uno
                    regions[titleId]['first'] = title
                if(isOriginal == 1):
                    # Guardamos el titulo original
                    regions[titleId]['original'] = title
                if(region == 'US'):
                    # Nos guardamos el titulo de EEUU
                    regions[titleId]['US'] = title
                if not 'regions' in regions[titleId].keys():

                    # Nos guardamos la region para despues estudiar cuantos null
                    regions[titleId]['regions'] = [region]
                else:
                    if region == '\\N' and not region in regions[titleId]['regions']:
                        regions[titleId]['regions'].append(region)
                    elif region != '\\N':
                        regions[titleId]['regions'].append(region)

                # Nos guardamos los titulos en ingles o en espanyol
                if(language == "es" or language == 'en'):
                    regions[titleId][language] = title

                # Nos guardamos los lenguajes para estudiarlos despues
                if not 'languages' in regions[titleId].keys():

                    # Nos guardamos la region para despues estudiar cuantos null
                    regions[titleId]['languages'] = [language]
                else:
                    if language == '\\N' and not language in regions[titleId]['languages']:
                        regions[titleId]['languages'].append(language)
                    elif region != '\\N':
                        regions[titleId]['languages'].append(language)

                """
                    Se van a guardar los siguientes datos por cada entrada (titleId)
                        1: first: Es el primer titulo que aparezca,para tener siempre uno de cada seguro
                        2: original:Titulo original (Con este creo que el first deja de hacer falta)
                        3: US:Titulo de EEUU, supongo que asi nos aseguramos de tenerlo en ingles
                        4: en/es: Titulos en espanyol o ingles, aunque muchos tienen como lenguaje null
                        5: regions:Lista de regiones registradas por titulo (Eliminado por ocupar mucho)
                        6: languages:Lista de lenguajes registrados por titulo (Eliminado por ocupar mucho)

                        Los elementos 5 y 6 los meto para estudiar cuantos datos tenemos de lenguajes/regiones para
                        poder estudiar que almacenar

                        Si es necesario se podría utilizar la API de google translate para ver el idioma de un titulo
                """
        print("Chunk", i, "/ 26")
        i += 1
    regions_used = {'null': 0}

    languages_used = {'null': 0}
    both_null = []

    i = 0
    BN = 0
    ES = 0
    for id in regions:
        data = regions[id]
        regions_data = list(set(data['regions']))
        languages_data = list(set(data['languages']))

        # Almacenamos los que son solo null
        regions_null = False
        languages_null = False
        if(len(regions_data) == 1 and regions_data[0] == '\\N'):
            regions_used['null'] += 1
            regions_null = True
        if(len(languages_data) == 1 and languages_data[0] == '\\N'):
            languages_used['null'] += 1
            languages_null = True
        if regions_null and languages_null:
            both_null.append(id)
            BN += 1
        for region in regions_data:
            if region != '\\N':
                if not region in regions_used.keys():
                    regions_used[region] = 0
                regions_used[region] += 1
        for language in languages_data:
            if language == 'es':
                ES += 1
            if language != '\\N':
                if not language in languages_used.keys():
                    languages_used[language] = 0
                languages_used[language] += 1
        # Vaciamos para almacenar
        del regions[id]['regions']   # (Vaciamos para poder guardar)
        del regions[id]['languages']   # (Vaciamos para poder guardar)
        i += 1
        print("id ", i, "/", len(regions))
    data_used = {'regions': regions_used,
                 'languages': languages_used, 'both_null': both_null}
    """
        Se van a guardar los siguientes datos:
            regions: Datos de regiones que aparecen en las entradas de los titulos
                null: Numero de titulos que solo tienen null como region
                region: Numero de entradas por region
            languages: Datos de los idiomas que aparecen en las entradas
                null: Numero de titulos que su lenguaje es null
                language: Numero de titulos por lenguaje
            both_null: Numero de datos que su region y lenguaje es null
    """

    # print(regions)
    print("BOTH NULL", BN)
    print("ESPAÑOL", ES)
    f = open("./diccionarios/regions_languages_used.pck", 'wb')
    pickle.dump(data_used, f)
    f.close()
    print("Regions languages used saved")

    f = open("./diccionarios/title_akas.pck", 'wb')
    pickle.dump(regions, f)
    f.close()
    print("Title akas saved")
