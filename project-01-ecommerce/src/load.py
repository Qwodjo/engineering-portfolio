import pandas as pd
from sqlalchemy import create_engine, text
from transform import transform

# TODO: move this to env later
DB_URL = "postgresql+psycopg2://postgres:password@localhost:5432/olist"

def get_engine():
    engine = create_engine(DB_URL)
    return engine

def load_to_db(df):
    engine = get_engine()

    print("connecting to postgres...")

    print("loading orders_enriched table...")
    df.to_sql('orders_enriched', engine, if_exists='replace', index=False, chunksize=1000)
    print(f"loaded {len(df)} rows")

    # quick sanity check
    with engine.connect() as conn:
        result = conn.execute(text("SELECT COUNT(*) FROM orders_enriched"))
        print("rows in db:", result.fetchone()[0])


if __name__ == "__main__":
    df = transform()
    load_to_db(df)
