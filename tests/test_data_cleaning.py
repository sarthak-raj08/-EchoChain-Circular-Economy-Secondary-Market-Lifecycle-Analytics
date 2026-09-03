import pandas as pd
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def test_cleaned_dataset_exists():
    file = BASE_DIR / "data" / "cleaned" / "EchoChain_Data_Cleaned.csv"
    assert file.exists()


def test_cleaned_dataset_shape():
    file = BASE_DIR / "data" / "cleaned" / "EchoChain_Data_Cleaned.csv"
    df = pd.read_csv(file)

    assert len(df) == 10000
    assert len(df.columns) == 33


def test_cleaned_dataset_has_no_duplicate_rows():
    file = BASE_DIR / "data" / "cleaned" / "EchoChain_Data_Cleaned.csv"
    df = pd.read_csv(file)

    assert df.duplicated().sum() == 0


def test_transaction_ids_are_unique():
    file = BASE_DIR / "data" / "cleaned" / "EchoChain_Data_Cleaned.csv"
    df = pd.read_csv(file)

    assert df["Transaction_ID"].notna().all()
    assert df["Transaction_ID"].is_unique


def test_product_ids_are_not_empty():
    file = BASE_DIR / "data" / "cleaned" / "EchoChain_Data_Cleaned.csv"
    df = pd.read_csv(file)

    assert df["Product_ID"].notna().all()
