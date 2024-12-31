from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Person
from .serializer import PersonCreateSerializer, PersonPatchSerializer, PersonSerializer


@api_view(["POST"])
def person_create(request):
    serializer = PersonCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET"])
def person_list(request):
    persons = Person.objects.all()
    serializer = PersonSerializer(persons, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def person_detail(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonSerializer(person)
    return Response(serializer.data)


@api_view(["PATCH"])
def person_update(request, pk):
    person = get_object_or_404(Person, pk=pk)
    serializer = PersonPatchSerializer(person, data=request.data, partial=True)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)


@api_view(["DELETE"])
def person_delete(request, pk):
    person = get_object_or_404(Person, pk=pk)
    person.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
