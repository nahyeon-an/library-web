from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LibrarySerializer
from .models import Library

class LibraryView(APIView):
    def get(self, request, **kwargs):
        if 'si' in kwargs:
            lib_queryset = Library.objects.filter(sido_nm=kwargs['si'])
        else:
            lib_queryset = Library.objects.all()
        lib_serializer = LibrarySerializer(lib_queryset, many=True)
        return Response(lib_serializer.data, status=status.HTTP_200_OK)