import pandas as pd


def clean_data(data:pd.DataFrame)->pd.DataFrame:
    df = data.copy()

    df = df.drop(columns=["Occupation","Blood Pressure","Heart Rate","BMI Category"])

    return df


