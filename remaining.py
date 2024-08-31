#all operations after Mandatory Operation
import pandas as pd

# Load the ratings and movies data into Pandas DataFrames
ratings_df = pd.read_csv('ratings.csv')
movies_df = pd.read_csv('movies.csv')

# 1. Group the user ratings based on movieId and apply aggregation operations like count and mean on ratings
grouped_ratings_df = ratings_df.groupby('movieId').agg({'rating': ['count', 'mean']})
grouped_ratings_df.columns = ['rating_count', 'rating_mean']

# 2. Apply inner join on dataframe created from movies.csv and the grouped df from step 1
merged_df = pd.merge(movies_df, grouped_ratings_df, on='movieId')

# 3. Filter only those movies which have more than 50 user ratings (i.e. > 50)
filtered_df = merged_df[merged_df['rating_count'] > 50]

# 4. Find the most popular movie based on average user ratings
most_popular_movie_avg_rating = filtered_df.sort_values(by='rating_mean', ascending=False).head(1)
print("Most popular movie based on average user ratings:")
print(most_popular_movie_avg_rating)

# 5. Find the top 5 popular movies based on the number of user ratings
top_5_popular_movies_rating_count = filtered_df.sort_values(by='rating_count', ascending=False).head(5)
print("Top 5 popular movies based on the number of user ratings:")
print(top_5_popular_movies_rating_count)

# 6. Find the third most popular Sci-Fi movie based on the number of user ratings
filtered_df['genres'] = filtered_df['genres'].str.lower()
third_most_popular_sci_fi_movie = filtered_df[filtered_df['genres'].str.contains('sci-fi')].sort_values(by='rating_count', ascending=False).iloc[2]
print("Third most popular Sci-Fi movie:")
print(third_most_popular_sci_fi_movie)


# Extract the movie ID with the highest average rating
highest_rated_movie_id = filtered_df.sort_values(by='rating_mean', ascending=False).head(1)['movieId'].values[0]

# Print the movie ID
print("Movie ID of the movie with the highest IMDB rating:", highest_rated_movie_id)



# Add a lowercase version of the 'genres' column for easier filtering
filtered_df['genres'] = filtered_df['genres'].str.lower()

# Filter Sci-Fi movies
sci_fi_movies = filtered_df[filtered_df['genres'].str.contains('sci-fi')]

# Extract the movie ID with the highest average rating among Sci-Fi movies
highest_rated_sci_fi_movie_id = sci_fi_movies.sort_values(by='rating_mean', ascending=False).head(1)['movieId'].values[0]

# Print the movie ID
print("Movie ID of the Sci-Fi movie with the highest IMDB rating:", highest_rated_sci_fi_movie_id)


