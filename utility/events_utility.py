import json
import logging
import os

import boto3


def get_events():
    upcoming_events = []

    bucket_name = os.environ.get('bucket_name', None)

    try:
        s3 = boto3.client('s3')
        file_object = s3.get_object(Bucket=bucket_name, Key='upcoming_events.json')
        file_data = file_object['Body'].read()
        upcoming_events = json.loads(file_data.decode('utf-8'))
    except Exception as e:
        logging.error(f'an exception was encountered while reading entries: {str(e)}')
        return upcoming_events

    logging.info(f'found a total of {len(upcoming_events)} upcoming events')

    return upcoming_events
