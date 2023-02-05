from functools import wraps
from typing import Optional, Type

from drf_spectacular.utils import extend_schema
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer


def custom_extend_schema(possible_error_statuses: list[int] = None, **kwargs):
    if possible_error_statuses is not None:
        responses = kwargs.get('responses', {})
        responses.update(dict.fromkeys(possible_error_statuses, ErrorResponseSerializer))
        kwargs['responses'] = responses

    def decorator(view_method):
        return extend_schema(**kwargs)(view_method)

    return decorator


def input_serializer(request_serializer_cls: Optional[Type[Serializer]] = None):

    def decorator(view_method):

        @wraps(view_method)
        def wrapper(self: APIView, request: Request, *args, **kwargs) -> Response:
            if request_serializer_cls is not None:
                request_serializer = request_serializer_cls(data=request.data)
                request_serializer.is_valid(raise_exception=True)
                kwargs['request_serializer'] = request_serializer

            return view_method(self, request, *args, **kwargs)

        return wrapper

    return decorator
