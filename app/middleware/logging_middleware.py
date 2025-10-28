import logging
from starlette.middleware.base import BaseHTTPMiddleware

class LoggingMiddlware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        logging.info(f"Request Method is:{request.method} and the endpoint is:{request.url}")
        response = await call_next(request)
        logging.info(f"The Status Code of the response is:{response.status_code}")
        return response

