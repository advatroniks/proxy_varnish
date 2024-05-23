from fastapi import APIRouter, Request, UploadFile, File

from api.service import upload_file


router = APIRouter(
    tags=["Varnish_proxy"]
)


@router.post(
    path=""
)
async def upload_file_to_s3(
        request: Request,
        # path_params: Annotated[str | None, Path()],
        file: UploadFile = File(...),
):
    await upload_file(
        path_param=request.url.path,
        file=file
    )


@router.get(
    path="/"
)
async def download_file_from_s3():
    pass
