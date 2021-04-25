import numpy as np
import pandas as pd
from math import sqrt

#Se cargan los datos
ratings_data = pd.read_csv("data/ratings.csv")
movies_data = pd.read_csv("data/movies.csv")

#Se elimina la columna de géneros, no utilizada en este recomendador:
movies_data.drop(columns=['genres'], inplace=True)

#USUARIO para el que se va a recomendar películas:
user = [
            {'title':'Star Wars: Episode IV - A New Hope (1977)', 'rating':4.5},
            {'title':'Lord of the Rings: The Fellowship of the Ring, The (2001)', 'rating':4},
            {'title':'Indiana Jones and the Temple of Doom (1984)', 'rating':4},
        ] 

inputUser = pd.DataFrame(user)

#Se comprueba que existan las películas y obtenemos sus ID
IdMovies = movies_data[movies_data['title'].isin(inputUser['title'].tolist())]
#Se junta la ID con las películas del usuario
inputUser = pd.merge(IdMovies, inputUser)

#Se obtienen los usuarios que han visto las mismas películas que inputUser
users = ratings_data[ratings_data['movieId'].isin(inputUser['movieId'].tolist())]

usersId = users.groupby(['userId'])
#Prioridad a los usuarios que tienen ratings similares a inputUser
usersId = sorted(usersId,  key=lambda x: len(x[1]), reverse=True)

#Obtenemos 100 usuarios más relevantes
usersId = usersId[0:100]

#Guardamos las correlaciones entre los usuarios en un diccionario
#key: User ID
#Value: Coeficiente de correlacion
usersCorDict = {}

#Para cada usuario del subgrupo de 100 usuarios
for nameId, groupMovies in usersId:
    #Ordenamos las películas del actual grupo y el input del usuario
    groupMovies = groupMovies.sort_values(by='movieId')
    inputUser = inputUser.sort_values(by='movieId')
    #Tamaño del grupo
    n = len(groupMovies)
    #Obtenemos la puntuacion de las peliculas que tienen ambos en comun (Grupo e Input)
    temp = inputUser[inputUser['movieId'].isin(groupMovies['movieId'].tolist())]
    tempRatingList = temp['rating'].tolist()
    tempGroupList = groupMovies['rating'].tolist()
    #Calculamos la correlación entre los dos usuarios (Grupo e input)
    Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(n)
    Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(n)
    Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(n)
    
    #Si el denominador es 0, no hay correlacion
    if Sxx != 0 and Syy != 0:
        usersCorDict[nameId] = Sxy/sqrt(Sxx*Syy)
    else:
        usersCorDict[nameId] = 0
    

#Obtenemos los 50 usuarios con más correlación con input user
usersDF = pd.DataFrame.from_dict(usersCorDict, orient='index')
usersDF.columns = ['similarityIndex']
usersDF['userId'] = usersDF.index
usersDF.index = range(len(usersDF))
topUsers=usersDF.sort_values(by='similarityIndex', ascending=False)[0:50]

#Incluimos las películas que han puntuado el top 50 de usuarios
topUsersRating=topUsers.merge(ratings_data, left_on='userId', right_on='userId', how='inner')

#Para cada película que han puntuado los 50 usuarios, multiplicamos la puntuación por su correlación con input user
topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']

#Sumamos el weightedRating y similarityIndex de cada uno de las películas
tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex','weightedRating']]
tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']


recommendation_df = pd.DataFrame()
#Obtenemos la media del peso de cada película
recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
recommendation_df['movieId'] = tempTopUsersRating.index

recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)

#Mostramos las 10 películas recomendadas para input user
print(movies_data.loc[movies_data['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())])
