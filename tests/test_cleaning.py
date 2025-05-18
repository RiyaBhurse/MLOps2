from src.datacleaning import clean_data, remove_outliers
import pandas as pd
import pytest


def test_clean_data():
   
    data = {
        "age": [25, 30, None, 22, 28]
    }
    df = pd.DataFrame(data)

   
    cleaned_df = clean_data(df)

    assert cleaned_df["age"].isnull().sum() == 0
    assert cleaned_df["age"].median().round(1) == 26.0 or 27.0 or 25.0

#  Skipping the test for outliers for now
# @pytest.mark.skip(reason="Outlier removal is not implemented yet")
def test_remove_outliers():
    data = {
        "age": [25, 30, 17, 22, 28, 70]
    }
    df = pd.DataFrame(data)

    cleaned_df = remove_outliers(df)

    assert cleaned_df["age"].min() >= 18
    assert cleaned_df["age"].max() <= 65
    assert len(cleaned_df) == 4  