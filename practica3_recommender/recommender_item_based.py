import numpy as np
import pandas as pd

#Se cargan los datos
ratings_data = pd.read_csv("data/ratings.csv")
movies_data = pd.read_csv("data/movies.csv")

#Visualizacion de los datos
#print(ratings_data.head())
#print(movies_data.head())

#Merge de ratings y movies
movie_ratings = pd.merge(ratings_data, movies_data, on='movieId')
#print(movie_ratings.head())

#Matriz de usuarios, péliculas y sus puntuaciones:
matrix = movie_ratings.pivot_table(index='userId', columns='title', values='rating')
#print(matrix.head())

#Se obtiene cuanto se ha puntuado cada película
ratings_mean_count = pd.DataFrame(movie_ratings.groupby('title')['rating'].mean())
ratings_mean_count['rating_counts'] = pd.DataFrame(movie_ratings.groupby('title')['rating'].count())

#Recomendaciones ITEM - ITEM
min_rating = 25
#movie_i = 'Star Wars: Episode IV - A New Hope (1977)'
#movie_i = 'Lord of the Rings: The Fellowship of the Ring, The (2001)'
#movie_i = 'Shutter Island (2010)'
#movie_i = 'Truman Show, The (1998)'

movie_i_ratings = matrix[movie_i]
movies_like_i = matrix.corrwith(movie_i_ratings)
corr_movie_i = pd.DataFrame(movies_like_i, columns=['Correlation'])

corr_movie_i = corr_movie_i.join(ratings_mean_count['rating_counts'])

print("\nRecomendaciones a partir de: "+movie_i)
print(corr_movie_i[corr_movie_i ['rating_counts']>min_rating].sort_values('Correlation', ascending=False).head())