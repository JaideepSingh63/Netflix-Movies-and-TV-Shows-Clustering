#Step 1: Load the Dataset
#Download netflix_titles.csv and place it in your project folder.
import pandas as pd
# Load the dataset
df = pd.read_csv("netflix_titles.csv")
# Show top 5 rows
print(df.head())
