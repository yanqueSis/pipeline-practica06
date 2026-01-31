def basic_exploration(df, name):
    print(f"\n📌 Dataset: {name}")
    print("-" * 50)
    print(df.info())
    print("\n🔹 Valores nulos:")
    print(df.isnull().sum())
    print("\n🔹 Resumen estadístico:")
    print(df.describe(include="all"))


def clean_pcode(df):
    df["PCODE"] = df["PCODE"].str.upper()
    df["PCODE"] = df["PCODE"].str.replace("O", "0")
    return df


def clean_dates(df):
    df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce", dayfirst=True)
    return df

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

def clean_catalog(df):
    df["CATALOG"] = df["CATALOG"].str.strip()
    df["CATALOG"] = df["CATALOG"].replace(CATALOG_MAP)
    return df
