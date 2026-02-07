#!/usr/bin/env python
# coding: utf-8
import pandas as pd
from sqlalchemy import create_engine
import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--target-table', default='zones', help='Target table name')
@click.option('--url', default='https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv', help='CSV URL')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, target_table, url):
    print(f"Reading data from {url}")
    
    # Read the CSV file
    df = pd.read_csv(url)
    
    print(f"Loaded {len(df)} rows")
    print(f"Columns: {list(df.columns)}")
    
    # Create database connection
    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')
    
    # Insert data into database
    df.to_sql(
        name=target_table,
        con=engine,
        if_exists="replace",
        index=False
    )
    
    print(f"Successfully inserted {len(df)} rows into {target_table}")

if __name__ == "__main__":
    run()
