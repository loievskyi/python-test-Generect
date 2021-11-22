from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.viewsets import ModelViewSet

from .models import Company, Person
from .serializers import (
    PersonListSerializer, PersonDetailSerializer,
    CompanyDetailSerializer, CompanyListSerializer,
)


class PersonViewSet(ModelViewSet):
    """ModelViewSet for Person model."""

    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ("full_name", "jod_title", "location", "email",
                     "phone_number", "company", "company_name")
    filterset_fields = ("company_id",)
    queryset = Person.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return PersonListSerializer
        else:
            return PersonDetailSerializer


class CompanyViewSet(ModelViewSet):
    """ModelViewSet for Company model"""

    filter_backends = (filters.SearchFilter, DjangoFilterBackend)
    search_fields = ("name", "location", "revenue")
    queryset = Company.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return CompanyListSerializer
        else:
            return CompanyDetailSerializer
