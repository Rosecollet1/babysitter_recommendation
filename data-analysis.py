import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the synthetic babysitter profiles from the CSV file
df = pd.read_csv('synthetic_babysitter_profiles.csv')

# Display the first few rows of the dataset
print(df.head())

# Display the summary statistics of the dataset
print(df.describe())

# Visualize the distribution of years of experience
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Years_of_Experience', kde=True, bins=20)
plt.title('Distribution of Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Count')
plt.show()

# Visualize the distribution of hourly rates
plt.figure(figsize=(10, 5))
sns.histplot(data=df, x='Hourly_Rate', kde=True, bins=20)
plt.title('Distribution of Hourly Rates')
plt.xlabel('Hourly Rate ($)')
plt.ylabel('Count')
plt.show()

# Visualize the count of CPR Certified, Pets Friendly, and Has Transportation
fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(20, 5))

sns.countplot(data=df, x='CPR_Certified', ax=axes[0])
axes[0].set_title('CPR Certified')
axes[0].set_xlabel('CPR Certified')
axes[0].set_ylabel('Count')

sns.countplot(data=df, x='Pets_Friendly', ax=axes[1])
axes[1].set_title('Pets Friendly')
axes[1].set_xlabel('Pets Friendly')
axes[1].set_ylabel('Count')

sns.countplot(data=df, x='Has_Transportation', ax=axes[2])
axes[2].set_title('Has Transportation')
axes[2].set_xlabel('Has Transportation')
axes[2].set_ylabel('Count')

plt.show()
