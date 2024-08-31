import pandas as pd

# Load the ratings and movies data into Pandas DataFrames
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Merge the ratings and movies dataframes on the 'movieId' column
merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# Filter the merged dataframe for the movie "Terminator 2: Judgment Day (1991)" and calculate the average rating
terminator_rating = merged_df[merged_df['title'] == 'Terminator 2: Judgment Day (1991)']['rating'].mean()

print("Average rating for Terminator 2: Judgment Day (1991):", terminator_rating)