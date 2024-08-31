import pandas as pd

# Load the ratings and movies data into Pandas DataFrames
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Merge the ratings and movies dataframes on the 'movieId' column
merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# Count the number of ratings for each movie and find the movie with the most ratings
most_rated_movie = merged_df['title'].value_counts().idxmax()

print("Movie with maximum ratings:", most_rated_movie)