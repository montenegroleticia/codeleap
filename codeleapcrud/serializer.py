from rest_framework import serializers
from .models import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = [
            "id",
            "username",
            "created_datetime",
            "title",
            "content",
        ]


class PersonCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["username", "title", "content"]


class PersonPatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["title", "content"]
