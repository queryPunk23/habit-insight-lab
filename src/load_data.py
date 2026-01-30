from pathlib import Path
import pandas as pd


def load_data(path_str:str) -> pd.DataFrame:

    path = Path(__file__).resolve().parent.parent
    csv_path = path / path_str

    data = pd.read_csv(csv_path)

    return data
