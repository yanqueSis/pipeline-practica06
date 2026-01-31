import pandas as pd

def extract_catalog_orders(path):
    return pd.read_csv(
        path,
        sep=",",
        engine="python"
    )

def extract_web_orders(path):
    return pd.read_csv(
        path,
        sep=";",
        engine="python"
    )

def extract_products(path):
    return pd.read_csv(
        path,
        sep=",",
        engine="python"
    )
