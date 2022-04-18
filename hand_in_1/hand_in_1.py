from argparse import Action
import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re


#Download datasettet fra dette link.
#https://www.kaggle.com/sanjeetsinghnaik/top-1000-highest-grossing-movies 

file = 'data1.csv'
dst = pd.read_csv(file)

#1. Find the top 10 highest grossing Disney movies measured by world sales
disney = dst.loc[dst['Distributor'] == 'Walt Disney Studios Motion Pictures']

disney_sorted = disney.sort_values(by=['World Sales (in $)'],ascending=False)

#print(disney_sorted[:10])
#2. Create a pie chart that shows the distribution of Licenses (PG, R, M and so on)

pr_rated = dst['License'].unique()

count_license = []
labels_license = []
for rating in pr_rated:
    count_license.append(len(dst.loc[dst['License'] == rating]))
    labels_license.append(rating)


#plt.pie(count_license,labels=labels_license)
#plt.show()

#3. Get the percentage of PG rated movies between 2001 and 2015
all_PG_movies = dst.loc[dst['License'] == 'PG']

#Makes DataFrame to a list
list_of_PG_movies = all_PG_movies.values.tolist()

PG_movies_in_2001_2015 = 0
for year in range(2001,2016):
    year = str(year)
    movies_pr_year = 0
    for movies in list_of_PG_movies:
        if year in movies[4]:
            PG_movies_in_2001_2015 += 1
            movies_pr_year += 1
        procent_of_movies_pr_year = (movies_pr_year/len(all_PG_movies)) * 100
    #print(procent_of_movies_pr_year)

procent_of_movies = (PG_movies_in_2001_2015/len(all_PG_movies)) * 100
#print(procent_of_movies)

#4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)

all_movies_list = dst.values.tolist()

each_genre = []

for movie in all_movies_list:
    temp_genre = movie[8].split(',')
    for genre in temp_genre:
        clean_genre = re.sub(r"[\[\]\']", "",genre)
        clean_genre = clean_genre.strip()

        if each_genre and clean_genre in list(list(zip(*each_genre))[0]):
            index = list(list(zip(*each_genre))[0]).index(clean_genre)
            each_genre[index][1].append(movie[7])
        else:
            each_genre.append([clean_genre,[movie[7]]])

avg = []       
for total_sum in each_genre:

    Sum = sum(total_sum[1])
    avg.append(Sum/len(total_sum[1]))
    

# plt.figure(figsize=(30,15))
# plt.xticks(rotation='vertical')
# plt.bar(list(list(zip(*each_genre))[0]), avg)
# plt.show()
