from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from rest_framework.views import exception_handler

from src.common.exceptions.domain_exceptions import EntityNotFound

DOMAIN_TO_API_EXCEPTION = {
    EntityNotFound: NotFound
}


def custom_exception_handler(exc, context) -> Response | None:
    api_exc = exc
    for domain_exception, api_exception in DOMAIN_TO_API_EXCEPTION.items():
        if isinstance(exc, domain_exception):
            api_exc = api_exception()
    response = exception_handler(api_exc, context)
    return response
