import pandas as pd
from src.clean_data import clean_data
from src.load_data import load_data
from pathlib import Path
import matplotlib.pyplot as plt


pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

path = Path(__file__).resolve().parent.parent

str_path = path / "data" / "raw" / "Sleep_health_and_lifestyle_dataset.csv"

data = load_data(str_path)

cleaned_data = clean_data(data)

#Plotting a Scatter plot to visualize the relationship between Sleep Duration and Quality of Sleep
plt.scatter(data=cleaned_data,
            x="Sleep Duration",
            y="Quality of Sleep")
plt.title("Sleep Duration vs Quality of Sleep")
plt.xlabel("Sleep duration")
plt.ylabel("Quality of Sleep")

plt.show()

#Plotting a Scatter plot to visualize the relationship between Sleep Duration and Stress Level
plt.scatter(data=cleaned_data,
            x="Sleep Duration",
            y="Stress Level")
plt.title("Sleep Duration vs Stress Level")
plt.xlabel("Sleep duration")
plt.ylabel("Stress level")
plt.show()

### Viewing Sleep Duration in Box Plot for Gender

male_sleep = data[data['Gender']=='Male']['Sleep Duration']
female_sleep = data[data['Gender']=='Female']['Sleep Duration']

plt.boxplot([male_sleep, female_sleep],labels=['Male','Female'])
plt.title("Sleep Duration vs Gender")
plt.xlabel("Sleep duration")
plt.ylabel("Gender")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
