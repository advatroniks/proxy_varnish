from typing import Literal

import aiofiles

from fastapi import APIRouter, Response
from fastapi.responses import FileResponse

from constants import BASE_PATH

from api import utils as api_utils
from api.service import get_file_from_s3_if_not_exists_upload_to_s3


router = APIRouter(
    tags=["Varnish_proxy"]
)


@router.get(
    path="/{target_url_file:path}"
)
async def get_file_from_target_host(
        target_url_file: str
):
    file_bytes: bytes = await get_file_from_s3_if_not_exists_upload_to_s3(
        target_url_file=target_url_file,
    )

    filename = api_utils.get_filename_from_url(url=target_url_file)

    async with aiofiles.open(f"{BASE_PATH}/temporary_storage/{filename}", "wb") as file:
        await file.write(file_bytes)

    return FileResponse(
        path=f"{BASE_PATH}/temporary_storage/{filename}"
    )


