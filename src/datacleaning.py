def clean_data(df):
    df = df.copy()
    df["age"] = df["age"].fillna(df["age"].median())
    return df

def remove_outliers(df):
    df = df.copy()
    df = df[(df["age"] >= 18) & (df["age"] <= 65)]
    return df