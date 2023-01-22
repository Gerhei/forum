from rest_framework.exceptions import NotFound, PermissionDenied
from rest_framework.response import Response
from rest_framework.views import exception_handler

from src.common.exceptions.domain_exceptions import EntityNotFound, AccessError

DOMAIN_TO_API_EXCEPTION = {
    EntityNotFound: NotFound,
    AccessError: PermissionDenied
}


def custom_exception_handler(exc, context) -> Response | None:
    api_exc = exc
    for domain_exception, api_exception in DOMAIN_TO_API_EXCEPTION.items():
        if isinstance(exc, domain_exception):
            detail = exc.message if exc.message else api_exception.default_detail
            api_exc = api_exception(detail=detail)
    response = exception_handler(api_exc, context)
    return response
