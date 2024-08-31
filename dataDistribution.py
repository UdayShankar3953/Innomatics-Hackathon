import pandas as pd
import matplotlib.pyplot as plt

# Load the ratings and movies data into Pandas DataFrames
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# Merge the ratings and movies dataframes on the 'movieId' column
merged_df = pd.merge(ratings_df, movies_df, on='movieId')

# Filter the merged dataframe for the movie "Fight Club (1999)" and extract the ratings
fight_club_ratings = merged_df[merged_df['title'] == 'Fight Club (1999)']['rating']

# Visualize the distribution of ratings
plt.hist(fight_club_ratings, bins=10)
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Fight Club (1999) Ratings Distribution")
plt.show()