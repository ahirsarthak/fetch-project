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
# Solution Development Decesions 
1. How will you read messages from the queue?
  I initialy tried using boto3 but it was throwing me error that I require AWS Credentials.
  So I searched online the subprocess of python where I wrote response code using AWS-CLI.
  
2. How will you mask the PII data so that duplicate values can be identified?
   I used sha256 funtion of hashlib library to do the following.
   And it also takes care of detecting the duplicate values as it produces same hash if same input is given so if the hash value is same then the value is a duplicate
   
3. What will be your strategy for connecting and writing to Postgres?
   For connection I used psycopg2.
   It has set of inbuilt python funtions to connect with psql databse '.connect' and write into it '.execute'
   
6. Where and how will your application run? 
   The application can run locally mentioned above and can be stopped using ctrl+C


