# Babysitter Recommendation Engine

The Babysitter Recommendation Engine is a system designed to provide personalized babysitter recommendations based on user preferences and babysitter attributes. It uses a content-based filtering approach to rank babysitters according to a point system. The system aims to help parents find the most suitable babysitter based on their specific needs and requirements.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Installation
1. Make sure you have Python 3 installed on your computer. If you don't, you can download it from the official website: https://www.python.org/downloads/.

2. Install the required libraries by running the following command in your terminal (or command prompt):
### Prerequisites

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Names
### Steps

1. Clone the repository to your local machine.

```bash
git clone https://github.com/Rosecollet1/babysitter_recommendation
```

2. Navigate to the project folder.
```bash
 cd babysitter_recommendation
```

Activate the virtual environment:
For macOS and Linux:
```bash
source venv/bin/activate
```
For Windows:

```bash
venv\Scripts\activate
```

3. Install the required libraries.
```bash
pip install pandas matplotlib seaborn names
```


## Running the Data Analysis Script

1. Open a terminal (or command prompt) and navigate to the directory containing the `data_analysis.py` and `synthetic_babysitter_profiles.csv` files.

2. Run the following command to execute the data analysis script:

```bash
python data_analysis.py
```

This will execute the data analysis code, and you should see the first few rows of the dataset, summary statistics, and visualizations displayed in the terminal (or command prompt). The histograms and bar charts will appear in separate windows, which you can close to proceed to the next visualization.

## Data Analysis Output

The data analysis script provides the following output:

- Display the first few rows of the dataset.
- Calculate summary statistics for the dataset, such as the mean, standard deviation, minimum, and maximum for each feature.
- Visualize the distribution of features using histograms.
- Visualize the relationship between categorical features and the hourly rate using bar charts.




### Recommendation Engine
To run the recommendation engine, execute the following command in the terminal:
```bash
python content_based_recommendation_engine.py <selected_parent name>
```

Replace selected_parent with the name of the parent whose preferences to use. The recommendations will be displayed in the terminal.

### Customization
You can customize the recommendation engine by modifying the input parameters in your Python script:

 - `synthetic_babysitter_profiles.csv`: A CSV file containing the babysitter profiles.
 - `parent_preferences.json`: A JSON file containing parent preferences.
