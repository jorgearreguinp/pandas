from pathlib import Path

import pandas


def write(file_type, df=pandas.DataFrame):

    filepath = Path(f"output/games.{file_type}")
    filepath.parent.mkdir(parents=True, exist_ok=True)

    if file_type == "parquet":
        df.to_parquet(filepath, engine="pyarrow")
    elif file_type == "csv":
        df.to_csv(filepath)
    else:
        print("File type not supported.")
