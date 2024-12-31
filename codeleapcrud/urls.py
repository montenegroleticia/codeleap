from django.urls import path
from .views import (
    person_list,
    person_create,
    person_detail,
    person_update,
    person_delete,
)

urlpatterns = [
    path("", person_list, name="person-list"),
    path("create/", person_create, name="person-create"),
    path("<int:pk>/", person_detail, name="person-detail"),
    path("<int:pk>/update/", person_update, name="person-update"),
    path("<int:pk>/delete/", person_delete, name="person-delete"),
]
