import pandas as pd
import pickle

if __name__ == "__main__":
    f = open("../juntar_database/diccionarios/links.pck", 'rb')
    dic_link = pickle.load(f)
    f.close()
    data = {}
    i = 0
    # print(dic_link)
    data = {}
    esta = 0
    jobs = {}
    for df in pd.read_csv("../data/title.principals.tsv",
                          chunksize=1000000, sep="\t"):
        # for col in df.columns:
        #     print(col)
        # break
        df = df.to_numpy()
        for row in df:
            id = row[0]
            id_persona = row[2]
            role = row[3]
            characters = row[5]

            #print(id, id_persona, role, characters)

            if id in dic_link:
                # if not role in jobs:
                #     jobs[role] = 0
                # jobs[role] += 1
                esta += 1
                if not id in data:
                    data[id] = {}
                if not id_persona in data[id]:
                    data[id][id_persona] = {'roles': []}

                data[id][id_persona]['roles'].append(role)
                if characters != '\\N':
                    characters = characters.replace('[', '')
                    characters = characters.replace(']', '')
                    characters = characters.replace('"', '')
                    if not 'characters' in data[id][id_persona]:
                        data[id][id_persona]['characters'] = []

                        for aux in characters.split(','):
                            data[id][id_persona]['characters'].append(aux)

                    else:
                        for character in characters.split(','):
                            data[id][id_persona]['characters'].append(
                                character)
        i += 1
        print("Chunk ", i, "/ 44")
    # print(data)
    #print("Hay ", esta, "de ", len(dic_link))
    f = open("./diccionarios/tabla_cast.pck", 'wb')
    pickle.dump(data, f)
    f.close()
    """
        Diccionario tabla cast
        clave id imdb pelicula:
            clave id Persona:
                roles: los roles de la persona
                characters: personajes que interpreta ( si procede con su rol)
    """
