import io

import httpx

import aioboto3

from api import utils as api_utils

from config import main_config


async def upload_file_to_s3(
        target_url_file: str,
        file_as_bytes: bytes,
        bucket_name: str,
        s3_endpoint_url: str,
):
    print(bucket_name)
    print(s3_endpoint_url)
    session = aioboto3.Session(
        aws_secret_access_key=main_config.SECRET_KEY,
        aws_access_key_id=main_config.ACCESS_KEY,
    )
    async with session.client(
        's3',
        endpoint_url=s3_endpoint_url,
        verify=False,
        use_ssl=False
    ) as s3_client:
        file_as_bytes = io.BytesIO(file_as_bytes)
        blob_s3_key = f"{bucket_name}/{target_url_file}"
        print(blob_s3_key)
        await s3_client.upload_fileobj(
            file_as_bytes, bucket_name, blob_s3_key
        )


async def get_file_from_s3_if_not_exists_upload_to_s3(
        target_url_file: str,
) -> bytes:

    #TODO
    bucket_name = "newbucket"


    session = aioboto3.Session(
        aws_secret_access_key=main_config.SECRET_KEY,
        aws_access_key_id=main_config.ACCESS_KEY,
    )
    async with session.client(
        's3',
        endpoint_url=main_config.S3_ENDPOINT_NAME,
        verify=False,
        use_ssl=False
    ) as s3_client:
        try:
            blob_s3_key = f"{bucket_name}/{target_url_file}"

            s3_obj = await s3_client.get_object(
                Bucket=bucket_name,
                Key=blob_s3_key
            )

            return await s3_obj['Body'].read()

        except Exception as e:
            print(f"Unable to get {target_url_file} in {blob_s3_key}: {e} ({type(e)})")

            async with httpx.AsyncClient() as httpx_client:
                response = await httpx_client.get(
                    url=f"http://{target_url_file}"
                )
                file_as_bytes = response.content

            await upload_file_to_s3(
                target_url_file=target_url_file,
                file_as_bytes=file_as_bytes,
                bucket_name=bucket_name,
                s3_endpoint_url=main_config.S3_ENDPOINT_NAME
            )

            recent_uploaded_s3_obj = await s3_client.get_object(
                Bucket=bucket_name,
                Key=blob_s3_key
            )
            return await recent_uploaded_s3_obj['Body'].read()

