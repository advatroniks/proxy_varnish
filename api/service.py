from fastapi import UploadFile

from aioboto3 import Session

from config import main_config


async def upload_file(
        path_param: str,
        file: UploadFile,
        bucket_name: str = "newbucket",
        s3_endpoint_url: str = "http://185.117.152.39:8333"
):
    file_as_bytes: bytes = await file.read()

    session = Session()
    async with session.client(
        's3',
        endpoint_url=s3_endpoint_url,
        aws_secret_access_key=main_config.ACCESS_KEY,
        aws_access_key_id=main_config.SECRET_KEY,
        use_ssl=False
    ) as s3_client:
        try:
            blob_s3_key = f"{bucket_name}/{path_param}/{file.filename}"

            await s3_client.upload_fileobj(
                file_as_bytes, bucket_name, blob_s3_key
            )

        except Exception as e:
            print(f"Unable to s3 upload {file.filename} to {blob_s3_key}: {e} ({type(e)})")
            return ""
