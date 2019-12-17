"""This script downloads all the csv files from a s3 bucket, updates the content, then write to another local directory
as the same filename."""

import boto3
import csv
import os

from tempfile import NamedTemporaryFile

s3_client = boto3.client('s3', 'us-east-1')
s3_resource = boto3.resource('s3', 'us-east-1')
BUCKET_NAME = 'plant-evaluator-dashboard'
PREFIX = 'FTTA-full-stack'

# We would need to use a paginator here if the number of objects we are listing might be over 1000.
paginator = s3_client.get_paginator('list_objects')
page_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix=PREFIX + '/dashboard-data')
objs_list = []
for page in page_iterator:
    try:
        # Extend the list of objects Contents to objs_list on every page.
        objs_list.extend([obj['Key'] for obj in page['Contents'] if '.csv' in obj['Key']])
    except KeyError as e:
        if 'Contents' in str(e):
            print("s3 bucket / prefix empty.")

    for obj in objs_list:
        current_csv_name = os.path.basename(obj)
        local_csv_path = os.path.join('/home/yilanzhu/Desktop/', 'plant_eval_csvs', obj)
        output_csv_path = os.path.join('/home/yilanzhu/Desktop/', 'output', obj)

        os.makedirs(os.path.dirname(local_csv_path), exist_ok=True)  # succeeds even if directory exists.
        os.makedirs(os.path.dirname(output_csv_path), exist_ok=True)  # succeeds even if directory exists.

        s3_resource.Bucket(BUCKET_NAME).download_file(obj, local_csv_path)
        print("Downloaded: {}".format(local_csv_path))
        fieldnames = ['git_datetime', 'git_hash', 'error_type', 'rms_error', 'scenario']

        with open(local_csv_path, 'r') as read_csv_file,  open(output_csv_path, 'w+') as write_csv_file:
            reader = csv.DictReader(read_csv_file)
            writer = csv.DictWriter(write_csv_file, fieldnames=fieldnames)

            for row in reader:
                # Check for 'T's in git_datetime.
                if 'T' in row['git_datetime']:
                    row['git_datetime'] = row['git_datetime'].replace('T', ' ')
                    writer.writerow(row)

                else:
                    writer.writerow(row)
            writer.writerows(reader)
