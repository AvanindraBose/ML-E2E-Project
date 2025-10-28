from fastapi import FastAPI
from app.api import routes_predict,routes_auth
from app.middleware.logging_middleware import LoggingMiddlware
from prometheus_fastapi_instrumentator import Instrumentator
from app.core import logging_config
from app.core.exceptions import register_exception_handlers

app = FastAPI(title='Car Prediction API')
app.add_middleware(LoggingMiddlware)

app.include_router(routes_auth.router,tags=['Auth'])
app.include_router(routes_predict.router,tags=['Prediction'])

Instrumentator().instrument(app).expose(app)

register_exception_handlers(app)

