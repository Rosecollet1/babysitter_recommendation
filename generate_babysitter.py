import pandas as pd
import random
import names

# Randomly generate a number of years of experience between 0 and 10
def generate_experience():
    return random.randint(0, 10)

# Randomly decide whether a babysitter is CPR certified (1) or not (0)
def generate_cpr_certification():
    return random.choice([0, 1])

# Randomly generate an hourly rate between 10 and 30
def generate_hourly_rate():
    return random.randint(10, 30)

# Randomly decide whether a babysitter is pet-friendly (1) or not (0)
def generate_pets_friendly():
    return random.choice([0, 1])

# Randomly decide whether a babysitter has transportation (1) or not (0)
def generate_transportation():
    return random.choice([0, 1])

# Generate a diverse set of 200 babysitter profiles
babysitter_profiles = []

for i in range(200):
    profile = {
        'Babysitter': names.get_full_name(),
        'Years_of_Experience': generate_experience(),
        'CPR_Certified': generate_cpr_certification(),
        'Hourly_Rate': generate_hourly_rate(),
        'Pets_Friendly': generate_pets_friendly(),
        'Has_Transportation': generate_transportation()
    }
    babysitter_profiles.append(profile)

# Create a pandas DataFrame from the babysitter profiles
df = pd.DataFrame(babysitter_profiles)

# Save the generated dataset to a CSV file
df.to_csv('synthetic_babysitter_profiles.csv', index=False)
