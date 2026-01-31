import pandas as pd

def extract_catalog_orders(path):
    return pd.read_csv(path,sep=",", quotechar='"',parse_dates=["DATE"],dayfirst=False)
    

def extract_web_orders(path):
    return pd.read_csv(path,sep=",", quotechar='"')

def extract_products(path):
    return pd.read_csv(path,sep=",", decimal=".")
