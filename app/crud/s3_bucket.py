from boto3 import client

from app.core.config import env_config
 
s3_client = client(
    service_name="s3",
    aws_access_key_id=env_config.bucket_access_key, # 본인 소유의 키를 입력
    aws_secret_access_key=env_config.bucket_secret_key, # 본인 소유의 키를 입력
    region_name=env_config.bucket_region
)

def find_rag_documents(prefix: str):
    paginator = s3_client.get_paginator('list_objects_v2')
    
    urls = []
    for page in paginator.paginate(Bucket=env_config.bucket_name, Prefix=prefix):
        for obj in page.get('Contents', []):
            key = obj['Key']
            url = s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': env_config.bucket_name, 'Key': key},
                ExpiresIn=3600
            )
            urls.append({"key": key, "url": url})
    
    return urls