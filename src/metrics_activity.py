import pandas as pd


def analyze_activity_and_sleep(file_path):
    try:

        df = pd.read_csv("../data/raw/Sleep_health_and_lifestyle_dataset.csv")


        filtered_df = df[df['Physical Activity Level'] > 60]

        # THE CALCULATION:
        df.groupby('Physical Activity Level')['Quality of Sleep'].mean()
        result = filtered_df.groupby('Physical Activity Level')['Quality of Sleep'].mean()

        return result

    except FileNotFoundError:
      print("File Not Found, please check the path")
      return none
