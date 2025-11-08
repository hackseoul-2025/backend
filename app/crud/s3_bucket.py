from boto3 import client
from fastapi.responses import StreamingResponse


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

def find_yolo_model(model_name: str):
    generator = iter_s3_file(env_config.bucket_name, f"{model_name}.mlpackage.zip")

    return StreamingResponse(
        generator,
        media_type="application/zip",
        headers={
            "Content-Disposition": f"attachment; filename={model_name}.mlpackage.zip"
        }
    )

def iter_s3_file(bucket: str, key: str, chunk_size: int = 1024*1024):
    obj = s3_client.get_object(Bucket=bucket, Key=key)
    body = obj["Body"]
    
    while True:
        chunk = body.read(chunk_size)
        if not chunk:
            break
        yield chunk