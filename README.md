# Fetch Rewards Task
 Fetch Rewards Application for Data Engineering Role

Exercise Link  -  https://fetch-hiring.s3.amazonaws.com/data-engineer/pii-masking.pdf

## Initial Project Setup

1. Install Docker desktop it has Docker Compose Inbuilt.
```
https://docs.docker.com/get-docker/
```
2.  Install Postgress psql
```
https://www.postgresql.org/download/
```


## To run the code
1. Clone this repo.
```bash
git clone https://github.com/ahirsarthak/fetch-project.git
```

2. Go into the cloned repo.
```bash
cd fetch-project
```

3. Install required dependencies.
For AWS CLI Subprocess Calls
```bash
pip install subprocess.run
```
For Database PSQL Connection
```bash
pip install psycopg2-binary
```
For Hashing
```bash
pip install hashlib
```
AWS-CLI
```bash
pip install awscli-local
```

4. Run this Docker code so that you container is up and running and all the data from localstack is loaded.
```bash
docker-compose up
```
and to shut it down CTRL + C or
```
docker-compose down 
```


5. Run Python code in terminal to perform ETL process.
```bash
python task.py
```



