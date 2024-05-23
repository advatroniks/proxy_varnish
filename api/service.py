from fastapi import UploadFile

import aioboto3

from config import main_config


async def upload_file(
        path_param: str,
        file: UploadFile,
        bucket_name: str = "newbucket",
        s3_endpoint_url: str = "http://185.117.152.39:8333"
):
    file_as_bytes: bytes = await file.read()

    session = aioboto3.Session(
        aws_secret_access_key=main_config.ACCESS_KEY,
        aws_access_key_id=main_config.SECRET_KEY,
    )
    async with session.client(
        's3',
        endpoint_url=s3_endpoint_url,
        verify=False,
        use_ssl=False
    ) as s3_client:
        try:
            blob_s3_key = f"{bucket_name}{path_param}{file.filename}"

            await s3_client.upload_fileobj(
                file_as_bytes, bucket_name, blob_s3_key
            )

        except Exception as e:
            print(f"Unable to s3 upload {file.filename} to {blob_s3_key}: {e} ({type(e)})")
            return ""
