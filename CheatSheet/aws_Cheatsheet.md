## AWS Cheatsheet

### S3
- Listing S3 bucket objects:
  - Based on last modified time:
  ```
  my_objects = subprocess.check_output(["aws", "s3api", "list-objects", 
                                        "--bucket", "my_bucket", 
                                        "--prefix", "folder1/folder2/",
                                        "--query", "Contents[?LastModified>=`2018-10-23`][].{Key: Key}"])
  ```
  - More than 1000 objects (select object based on object name):
  ```
    import boto3
    
    s3_client = boto3.client('s3', 'us-east-1')
    s3_resource = boto3.resource('s3', 'us-east-1')
    
  # Create a reuseable paginator as the number of s3 objects we are listing may be over 1000.
    paginator = s3_client.get_paginator('list_objects')
    page_iterator = paginator.paginate(Bucket=BUCKET_NAME, Prefix='folder1/folder2')

    filtered_iterator = page_iterator.search("Contents[?contains(Key, `test_time_" + start_time + "`) == `true`]")
    for key_data in filtered_iterator:
      object_name = key_data.get('Key')
      if object_name:
        s3_resource.Bucket(BUCKET_NAME).download_file(object_name, '~/downloads/' + object_name)

    
    
    ```
