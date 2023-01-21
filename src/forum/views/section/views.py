from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from src.forum.views.section.serializers import SectionDetailSerializer, SectionListSerializer
from src.forum.services.section import SectionService


class SectionView(APIView):
    def get(self, request: Request, slug: str) -> Response:
        section = SectionService().get_section(slug=slug)
        serializer = SectionDetailSerializer(section)
        return Response(serializer.data, status=status.HTTP_200_OK)


class SectionListView(APIView):
    def get(self, request: Request) -> Response:
        sections_dto = SectionService().get_section_list(parent_slug=request.query_params.get('slug'))
        serializer = SectionListSerializer(sections_dto)
        return Response(serializer.data, status=status.HTTP_200_OK)
