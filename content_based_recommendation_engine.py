import pandas as pd
import json
import argparse

def min_max_scale(series):
    return (series - series.min()) / (series.max() - series.min())

def calculate_score(df, preferences):
    score = (
        df['Years_of_Experience'] * preferences['years_of_experience_weight'] +
        df['CPR_Certified'] * preferences['cpr_certified_weight'] -
        df['Hourly_Rate'] * preferences['hourly_rate_weight'] +
        df['Pets_Friendly'] * preferences['pets_friendly_weight'] +
        df['Has_Transportation'] * preferences['has_transportation_weight']
    )
    return score

# Parse command-line arguments
parser = argparse.ArgumentParser(description='Babysitter Recommendation Engine')
parser.add_argument('selected_parent', help='Name of the parent whose preferences to use')
args = parser.parse_args()

# Read the synthetic babysitter profiles from the CSV file
df = pd.read_csv('synthetic_babysitter_profiles.csv')

# Create a copy of the original DataFrame before normalizing the features
original_df = df.copy()

# Normalize feature values
df['Years_of_Experience'] = min_max_scale(df['Years_of_Experience'])
df['Hourly_Rate'] = min_max_scale(df['Hourly_Rate'])

# Load parent preferences from the JSON file
with open('parent_preferences.json', 'r') as f:
    parent_preferences = json.load(f)

# Get the selected parent's preferences
user_preferences = parent_preferences[args.selected_parent]

# Calculate the score for each babysitter and add it to the DataFrame
df['Score'] = calculate_score(df, user_preferences)

# Sort the DataFrame by score in descending order
sorted_df = df.sort_values(by='Score', ascending=False)

# Update the original DataFrame with the calculated scores
original_df['Score'] = sorted_df['Score']

# Print the top recommendations with original Hourly_Rate and Years_of_Experience values
top_recommendations = original_df.sort_values(by='Score', ascending=False)
print(top_recommendations.head())