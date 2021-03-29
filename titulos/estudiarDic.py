import pickle
import numpy as np

# Saca por pantalla el diccionario


def print_regions_languages(subfield=None):
    f = open("../titulos/diccionarios/regions_languages_used.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    if subfield == None:
        print(dic)
    else:
        print(dic[subfield])
# Saca por pantalla el diccionario


def print_title_akas():
    f = open("../titulos/diccionarios/title_akas.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    print(dic)


def regions_languages():
    f = open("../titulos/diccionarios/regions_languages_used.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    return dic
# Saca por pantalla el diccionario


def title_akas():
    f = open("../titulos/diccionarios/title_akas.pck", 'rb')
    dic = pickle.load(f)
    f.close()
    return dic


if __name__ == "__main__":
    both_null = regions_languages()['both_null']
    akas = title_akas()
    not_original = 0
    not_first = 0
    for id in both_null:
        print(akas[id])
        if not 'original' in akas[id].keys():
            not_original += 1
        if not 'first' in akas[id].keys():
            not_first += 1
    print("Not original", not_original)
    print("Not first", not_first)
