# main.py
from config.config import DATA_PATH, DROP_COLUMNS
from preprocessing import (
    Check_data_type,
    Drop_unnecessary_features,
    Read_data_file,
)


def main():
    print("=== 1. Loading Dataset ===")
    df = Read_data_file(DATA_PATH)

    if df is not None:
        print(f"Data Loaded Successfully. Shape: {df.shape}\n")

        print("=== 2. Data Quality & Type Report ===")
        report = Check_data_type(df)
        print(report.to_string())
        print("-" * 60)

        print("=== 3. Dropping Unnecessary Features ===")
        df_cleaned = Drop_unnecessary_features(df, DROP_COLUMNS)
        print(f"Features after drop: {list(df_cleaned.columns)}")
        print(f"New Shape: {df_cleaned.shape}")


if __name__ == "__main__":
    main()