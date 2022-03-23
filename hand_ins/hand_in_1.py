import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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

new = all_PG_movies["Release Date"].str.split(",", n=1)


print(new.__contains__('2017'))

#4. Calculate the average of world sales for each genre and visualize the data with a bar chart. (Hint: use groupBy)

sales = dst.groupby('Genre').sum()

sorted_sales = sales.sort_values(by=['World Sales (in $)'],ascending=False)

biggest_10 = sorted_sales[:10]
#print(biggest_10)

#plt.bar(biggest_10[0], biggest_10[3])
#plt.show()