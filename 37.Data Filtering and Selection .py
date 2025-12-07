# Name,Age,Score,City
# Alice,25,85.5,New York
# Bob,30,92.0,London
# Charlie,22,78.2,New York
# David,45,60.1,Paris
# Eve,35,95.5,London
# Frank,28,88.9,New York





# Import the Pandas library
import pandas as pd 

# Define the filename
filename = r"d:\FFFFF\lab\sample_data.csv"

try:
    # Load the data into a DataFrame
    df = pd.read_csv(filename) 
    print("--- Original DataFrame ---")
    print(df)
    
except FileNotFoundError:
    print(f"ERROR: The file '{filename}' was not found. Please create it.")
    exit()

# --- 1. Sorting Data ---

print("\n--- 1. Sorting by 'Score' (Descending) ---")
# Sort the DataFrame based on the 'Score' column from highest to lowest
df_sorted = df.sort_values(by='Score', ascending=False) 
print(df_sorted)

# --- 2. Filtering Data (Selection) ---

print("\n--- 2. Filtering: Only Scores >= 85 ---")
# Create a boolean mask where Score is 85 or higher
high_performers = df[df['Score'] >= 85] 
print(high_performers)

# --- 3. Adding/Modifying a Column ---

print("\n--- 3. Adding a New 'Status' Column ---")
# Use a NumPy condition (where) to assign values based on a score threshold
import numpy as np
# If the score is >= 80, the status is 'Pass'; otherwise, it's 'Fail'
df['Status'] = np.where(df['Score'] >= 80, 'Pass', 'Fail') 
print(df[['Name', 'Score', 'Status']])

# --- 4. Grouping Data (Aggregation) ---

print("\n--- 4. Grouping by 'City' and calculating Average Age ---")
# Group the DataFrame by the 'City' column
# Then calculate the mean (average) of the 'Age' for each city
city_stats = df.groupby('City')['Age'].mean() 
print(city_stats)