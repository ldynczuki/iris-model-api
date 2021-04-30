__version__ = '1.0.0'

import os
import logging.config

import time
import uuid
import urllib3
import traceback

from loguru import logger
from fastapi import FastAPI
from starlette.requests import Request
from starlette.responses import JSONResponse
from starlette.exceptions import HTTPException
from starlette.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError

from projeto.settings import PATH_LOG
from projeto.resources import resources, database

urllib3.disable_warnings()
logger.add("iris_model.log", rotation="500 MB")
logger.level("REQUEST RECEBIDA", no=38, color="<yellow>")
logger.level("REQUEST FINALIZADA", no=39, color="<green>")

app = FastAPI(
    title="Classificador Íris Dataset", description="API responsável por classificar e armazenar dados de flores", version=__version__
)

app.include_router(resources.router, prefix='/iris', tags=['Íris Predict'])
app.include_router(database.router, prefix='/database', tags=['Database'])



@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    id = uuid.uuid1()

    logger.log("REQUEST RECEBIDA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path}")

    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.log("REQUEST FINALIZADA", f"[{request.method}] ID: {id} - IP: {request.client.host}"
               + f" - ENDPOINT: {request.url.path} - TEMPO: {process_time}")
    response.headers["X-Process-Time"] = str(process_time)

    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_methods=['*'],
    allow_credentials=True,
    allow_headers=['*']
)