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
            {'title':'Star Wars: Episode IV - A New Hope (1977)', 'rating':5},
            {'title':'Lord of the Rings: The Fellowship of the Ring, The (2001)', 'rating':4.5},
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

#Store the Pearson Correlation in a dictionary, where the key is the user Id and the value is the coefficient
pearsonCorDict = {}

#For every user group in our subset
for name, group in usersId:
    #Let's start by sorting the input and current user group so the values aren't mixed up later on
    group = group.sort_values(by='movieId')
    inputUser = inputUser.sort_values(by='movieId')
    #Get the N for the formula
    n = len(group)
    #Get the review scores for the movies that they both have in common
    temp = inputUser[inputUser['movieId'].isin(group['movieId'].tolist())]
    #And then store them in a temporary buffer variable in a list format to facilitate future calculations
    tempRatingList = temp['rating'].tolist()
    #put the current user group reviews in a list format
    tempGroupList = group['rating'].tolist()
    #Now let's calculate the pearson correlation between two users, so called, x and y
    Sxx = sum([i**2 for i in tempRatingList]) - pow(sum(tempRatingList),2)/float(n)
    Syy = sum([i**2 for i in tempGroupList]) - pow(sum(tempGroupList),2)/float(n)
    Sxy = sum( i*j for i, j in zip(tempRatingList, tempGroupList)) - sum(tempRatingList)*sum(tempGroupList)/float(n)
    
    #If the denominator is different than zero, then divide, else, 0 correlation.
    if Sxx != 0 and Syy != 0:
        pearsonCorDict[name] = Sxy/sqrt(Sxx*Syy)
    else:
        pearsonCorDict[name] = 0
    

pearsonDF = pd.DataFrame.from_dict(pearsonCorDict, orient='index')
pearsonDF.columns = ['similarityIndex']
pearsonDF['userId'] = pearsonDF.index
pearsonDF.index = range(len(pearsonDF))

topUsers=pearsonDF.sort_values(by='similarityIndex', ascending=False)[0:50]

topUsersRating=topUsers.merge(ratings_data, left_on='userId', right_on='userId', how='inner')

topUsersRating['weightedRating'] = topUsersRating['similarityIndex']*topUsersRating['rating']

#Applies a sum to the topUsers after grouping it up by userId
tempTopUsersRating = topUsersRating.groupby('movieId').sum()[['similarityIndex','weightedRating']]
tempTopUsersRating.columns = ['sum_similarityIndex','sum_weightedRating']

#Creates an empty dataframe
recommendation_df = pd.DataFrame()
#Now we take the weighted average
recommendation_df['weighted average recommendation score'] = tempTopUsersRating['sum_weightedRating']/tempTopUsersRating['sum_similarityIndex']
recommendation_df['movieId'] = tempTopUsersRating.index

recommendation_df = recommendation_df.sort_values(by='weighted average recommendation score', ascending=False)

print(movies_data.loc[movies_data['movieId'].isin(recommendation_df.head(10)['movieId'].tolist())])
