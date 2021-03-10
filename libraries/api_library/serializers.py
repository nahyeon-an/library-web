from rest_framework import serializers
from .models import Library

class LibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = Library
        fields = ['name', 'sido_nm', 'gungu_nm']