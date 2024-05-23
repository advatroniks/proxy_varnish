from fastapi import FastAPI

from api.router import router


app = FastAPI(
    title="Varnish SSS Proxy"
)

app.include_router(router=router)

