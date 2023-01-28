from drf_spectacular.utils import extend_schema, OpenApiParameter
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.common.exceptions.error_serializer import ErrorResponseSerializer
from src.forum.views.section.serializers import SectionDetailSerializer, SectionListSerializer
from src.forum.services.section import SectionService


class SectionView(APIView):
    @extend_schema(operation_id='get-section',
                   parameters=[
                       OpenApiParameter(name='slug', location=OpenApiParameter.PATH, required=True, type=str)
                   ],
                   responses={200: SectionDetailSerializer,
                              404: ErrorResponseSerializer},
                   description='Get data of a section, its parent, its children, and related topics.')
    def get(self, request: Request, slug: str) -> Response:
        section = SectionService().get_section(slug=slug)
        serializer = SectionDetailSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionListView(APIView):
    @extend_schema(operation_id='get-section-list',
                   parameters=[
                       OpenApiParameter(name='slug', location=OpenApiParameter.QUERY, required=False, type=str)
                   ],
                   responses={200: SectionListSerializer,
                              404: ErrorResponseSerializer},
                   description='Get a list of all children of section. '
                               'If query parameter is not specified, gets all root sections.')
    def get(self, request: Request) -> Response:
        sections_dto = SectionService().get_section_list(parent_slug=request.query_params.get('slug'))
        serializer = SectionListSerializer(sections_dto)
        return Response(serializer.data, status=status.HTTP_200_OK)
