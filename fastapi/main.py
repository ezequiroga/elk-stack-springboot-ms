from typing import Optional

from fastapi import FastAPI

from api.routers.router import api_router
from core.config import APP_NAME, APP_VERSION, API_PREFIX

from prometheus_fastapi_instrumentator import Instrumentator

'''
app = FastAPI()
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}
'''
def get_app() -> FastAPI:
    fast_app = FastAPI(title=APP_NAME, version=APP_VERSION)
    fast_app.include_router(api_router, prefix=API_PREFIX)
    
    return fast_app


app = get_app()

Instrumentator().instrument(app).expose(app)