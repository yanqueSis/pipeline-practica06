import pandas as pd


def basic_exploration(df, name):
    print(f"\n Dataset: {name}")
    print("-" * 50)
    print(df.info())
    print("\n🔹 Valores nulos:")
    print(df.isnull().sum())
    print("\n🔹 Resumen estadístico:")
    print(df.describe(include="all"))


# def clean_pcode(df):
#     df["PCODE"] = df["PCODE"].str.upper()
#     df["PCODE"] = df["PCODE"].str.replace("O", "0")
#     return df


# def clean_dates(df):
#     df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce", dayfirst=True)
#     return df

CATALOG_MAP = {
    "Pet": "Pets",
    "Pest": "Pets",
    "Pets": "Pets",
    "Toy": "Toys",
    "Tosy": "Toys",
    "Tots": "Toys",
    "Toys": "Toys",
    "Sport": "Sports",
    "Sporst": "Sports",
    "Sports": "Sports",
    "Gardenings": "Gardening"
}

# def clean_catalog(df):
#     df["CATALOG"] = df["CATALOG"].str.strip()
#     df["CATALOG"] = df["CATALOG"].replace(CATALOG_MAP)
#     return df


# def create_dim_date(df):
#     dim_date = df[["DATE"]].drop_duplicates()
#     dim_date["day"] = dim_date["DATE"].dt.day
#     dim_date["month"] = dim_date["DATE"].dt.month
#     dim_date["year"] = dim_date["DATE"].dt.year
#     dim_date.rename(columns={"DATE": "full_date"}, inplace=True)
#     return dim_date

# def create_dim_catalog(df):
#     return pd.DataFrame({
#         "catalog_name": df["CATALOG"].unique()
#     })
    
#def create_dim_product(df):
#    return df[["PCODE", "PNAME", "CATALOG", "PRICE"]].drop_duplicates()

# def create_fact_orders(df, dim_date, dim_product):
#     df = df.merge(dim_date, left_on="DATE", right_on="full_date")
#     df = df.merge(dim_product, on="PCODE")
#     df["sales_amount"] = df["QTY"] * df["PRICE"]
#     return df

# ---------------------------
# 1. Limpieza del CATALOG
# ---------------------------
def clean_catalog(df):
    catalog_map = {
        "Pet": "Pets",
        "Pest": "Pets",
        "Pets": "Pets",
        "Toy": "Toys",
        "Tosy": "Toys",
        "Tots": "Toys",
        "Toys": "Toys",
        "Sport": "Sports",
        "Sporst": "Sports",
        "Sports": "Sports",
        "Gardenings": "Gardening",
        "Gardening": "Gardening"
    }

    df["CATALOG"] = (
        df["CATALOG"]
        .astype(str)
        .str.strip()
        .replace(catalog_map)
    )

    return df


# ---------------------------
# 2. Limpieza del PCODE
# ---------------------------
def clean_pcode(df):
    df["PCODE"] = (
        df["PCODE"]
        .astype(str)
        .str.upper()
        .str.replace("O", "0", regex=False)
    )

    return df


# ---------------------------
# 3. Limpieza de fechas
# ---------------------------
def clean_dates(df):
    df["DATE"] = pd.to_datetime(
        df["DATE"],
        errors="coerce",
        dayfirst=True
    )

    return df


# ---------------------------
# 4. Dimensión Fecha
# ---------------------------
def create_dim_date(df):
    dim_date = (
        df[["DATE"]]
        .dropna()
        .drop_duplicates()
        .copy()
    )

    dim_date["day"] = dim_date["DATE"].dt.day
    dim_date["month"] = dim_date["DATE"].dt.month
    dim_date["year"] = dim_date["DATE"].dt.year

    dim_date.rename(columns={"DATE": "full_date"}, inplace=True)

    return dim_date


# ---------------------------
# 5. Dimensión Catálogo
# ---------------------------
def create_dim_catalog(df):
    return (
        df[["CATALOG"]]
        .drop_duplicates()
        .rename(columns={"CATALOG": "catalog_name"})
        .reset_index(drop=True)
    )


# ---------------------------
# 6. Dimensión Producto
# ---------------------------
def create_dim_product(df):
    return (
        df[["PCODE", "DESCRIP", "TYPE", "PRICE"]]
        .drop_duplicates()
        .reset_index(drop=True)
    )


# ---------------------------
# 7. Tabla de Hechos
# ---------------------------
def create_fact_orders(df, dim_date, dim_product):
    fact = df.copy()

    fact = fact.merge(
        dim_date,
        left_on="DATE",
        right_on="full_date",
        how="left"
    )

    fact = fact.merge(
        dim_product,
        on="PCODE",
        how="left"
    )

    fact["sales_amount"] = fact["QTY"] * fact["PRICE"]

    return fact