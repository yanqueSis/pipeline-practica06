from sqlalchemy import create_engine

def load_to_postgres(df, table_name):
    engine = create_engine(
        "postgresql+psycopg2://root:1234@localhost:5432/etl_db"
    )
    df.to_sql(table_name, engine, if_exists="append", index=False)