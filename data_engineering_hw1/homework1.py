# Question 1. Understanding Docker images

# Run docker with the python:3.13 image. Use an entrypoint bash to interact with the container.

# What's the version of pip in the image?

# 25.3 This is the correct answer.
# 24.3.1
# 24.2.1
# 23.3.1

# Question 2. Understanding Docker networking and docker-compose

# Given the following docker-compose.yaml, what is the hostname and port that pgadmin should use to connect to the postgres database?

# services:
#   db:
#     container_name: postgres
#     image: postgres:17-alpine
#     environment:
#       POSTGRES_USER: 'postgres'
#       POSTGRES_PASSWORD: 'postgres'
#       POSTGRES_DB: 'ny_taxi'
#     ports:
#       - '5433:5432'
#     volumes:
#       - vol-pgdata:/var/lib/postgresql/data

#   pgadmin:
#     container_name: pgadmin
#     image: dpage/pgadmin4:latest
#     environment:
#       PGADMIN_DEFAULT_EMAIL: "pgadmin@pgadmin.com"
#       PGADMIN_DEFAULT_PASSWORD: "pgadmin"
#     ports:
#       - "8080:80"
#     volumes:
#       - vol-pgadmin_data:/var/lib/pgadmin

# volumes:
#   vol-pgdata:
#     name: vol-pgdata
#   vol-pgadmin_data:
#     name: vol-pgadmin_data

# postgres:5433
# localhost:5432 
# db:5433
# postgres:5432 <== This is the correct answer.
# db:5432 <== This also correct.

