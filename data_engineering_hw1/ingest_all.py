#!/usr/bin/env python
# coding: utf-8
import subprocess
import sys
import click

@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db):
    """Run all ingestion scripts in sequence"""
    
    scripts = [
        {
            'name': 'Taxi Zones',
            'script': 'ingest_zones.py',
            'table': 'taxi_zone_lookup'
        },
        {
            'name': 'Green Taxi Data',
            'script': 'ingest_green_data.py',
            'table': 'green_taxi_data'
        },
        {
            'name': 'Yellow Taxi Data',
            'script': 'ingest_data.py',
            'table': 'yellow_taxi_trips'
        }
    ]
    
    for script_info in scripts:
        print(f"\n{'='*60}")
        print(f"Running: {script_info['name']}")
        print(f"{'='*60}\n")
        
        cmd = [
            'python', script_info['script'],
            '--pg-user', pg_user,
            '--pg-pass', pg_pass,
            '--pg-host', pg_host,
            '--pg-port', str(pg_port),
            '--pg-db', pg_db,
            '--target-table', script_info['table']
        ]
        
        result = subprocess.run(cmd)
        
        if result.returncode != 0:
            print(f"\n❌ Failed to run {script_info['name']}")
            sys.exit(1)
        
        print(f"\n✅ Successfully completed {script_info['name']}")
    
    print(f"\n{'='*60}")
    print("All ingestion tasks completed successfully!")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    run()
