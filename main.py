from aioboto3.session import Session
from pathlib import Path
import asyncio

access_key = "access_key"
secret_key = "secret_key"
bucket_name = "newbucket"
file_to_upload ='PNG.png'
s3_endpoint_url = 'http://185.117.152.39:8333'


async def upload(staging_path):
    session = Session()
    async with session.client(
        's3',
        endpoint_url=s3_endpoint_url,
        aws_secret_access_key=secret_key,
        aws_access_key_id=access_key,
        use_ssl=False) as s3_client:
        try:
            blob_s3_key = bucket_name + '/' + file_to_upload
            with Path(file_to_upload).open("rb") as spfp:
                print(f"Uploading {blob_s3_key} to s3")
                await s3_client.upload_fileobj(spfp, bucket_name, blob_s3_key)
                print(f"Finished Uploading {blob_s3_key} to s3")
        except Exception as e:
            print(f"Unable to s3 upload {staging_path} to {blob_s3_key}: {e} ({type(e)})")
            return ""


async def main():
    await upload(file_to_upload)

if __name__ == '__main__':
    asyncio.run(main())