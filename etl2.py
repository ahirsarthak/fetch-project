import subprocess
import json
import boto3
import psycopg2
from datetime import datetime
from hashlib import sha256

sqs = boto3.client('sqs', region_name=None,
                   endpoint_url='http://localhost:4566')
queue_url = 'http://localhost:4566/000000000000/login-queue'


def mask_pii(data):
    # Hash device_id and ip using sha256
    data['masked_device_id'] = sha256(data['device_id'].encode()).hexdigest()
    data['masked_ip'] = sha256(data['ip'].encode()).hexdigest()
    return data


conn = psycopg2.connect(
    host="localhost",
    port=5432,
    user="postgres",
    password="postgres",
)


def current_time():
    return str(datetime.now().strftime('%Y-%m-%d'))


def write_to_db(data):
    cur = conn.cursor()
    # insert data into user_logins table
    cur.execute("INSERT INTO user_logins(user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date) VALUES(%s, %s, %s, %s, %s, %s, %s)",
                (data['user_id'], data['device_type'], data['masked_ip'], data['masked_device_id'], data['locale'], data['app_version'], current_time()))
    conn.commit()


# while True:
    # response = subprocess.run(['awslocal', 'sqs', 'receive-message', '--queue-url',
    #                         queue_url, '--wait-time-seconds', '5'], capture_output=True)

    # if response.returncode == 0:
    # Extract the message body
    #   message_body = json.loads(response.stdout)
    # Extract the user_id field
    #  data = json.loads(message_body['Messages'][0]['Body'])
    # data = mask_pii(data)
    #data["app_version"] = str(data["app_version"])
    # write_to_db(data)
    # print(data)
    # else:
    # print(response.stderr)
while True:
    # Receive messages from SQS
    messages = sqs.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=10)
    if 'Messages' in messages:
        for message in messages['Messages']:
            # parse json data
            data = json.loads(message['Body'])
            # mask pii data
            data = mask_pii(data)
            # write to postgres
            write_to_db(data)
            # delete message from queue
            sqs.delete_message(QueueUrl=queue_url,
                               ReceiptHandle=message['ReceiptHandle'])
    # else:
        # wait for new messages
        # time.sleep(5)
