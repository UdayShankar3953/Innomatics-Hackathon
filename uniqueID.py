import pandas as pd

# Load the CSV file into a Pandas DataFrame
ratings_df = pd.read_csv('ratings.csv')

# Count the number of unique user IDs
unique_user_ids = ratings_df['userId'].nunique()

print("Number of unique user IDs:", unique_user_ids)