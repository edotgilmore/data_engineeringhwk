#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
from tqdm.auto import tqdm
import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='green_taxi_data', help='Target table name')
@click.option('--url', default='https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet', help='Parquet file URL')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, url):
    print(f"Reading data from {url}")
    
    # Read the parquet file
    df = pd.read_parquet(url)
    
    print(f"Loaded {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    
    # Create database connection
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    # Create table schema first
    df.head(0).to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )
    print("Table created")
    
    # Insert data in chunks with progress bar
    chunk_size = 100000
    total_rows = len(df)
    
    for i in tqdm(range(0, total_rows, chunk_size)):
        chunk = df.iloc[i:i+chunk_size]
        chunk.to_sql(
            name=target_table,
            con=engine,
            if_exists="append",
            index=False
        )
        print(f"Inserted {len(chunk)} rows")
    
    print(f"Successfully inserted {total_rows} rows into {target_table}")

if __name__ == "__main__":
    run()
