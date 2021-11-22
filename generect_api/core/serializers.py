from django.urls import reverse
from rest_framework import serializers

from .models import Company, Person


class PersonDetailSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Person model"""
    profile_url = serializers.HyperlinkedIdentityField(
        view_name="core:person-detail",
        lookup_field="pk",
    )

    class Meta:
        model = Person
        fields = (
            "id",
            "full_name",
            "profile_url",
            "job_title",
            "location",
            "email",
            "phone_number",
        )


class PersonListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Person model"""
    profile_url = serializers.HyperlinkedIdentityField(
        view_name="core:person-detail",
        lookup_field="pk",
    )

    class Meta:
        model = Person
        fields = (
            "id",
            "full_name",
            "profile_url",
        )


class CompanyDetailSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Company model"""
    company_url = serializers.HyperlinkedIdentityField(
        view_name="core:company-detail",
        lookup_field="pk",
    )
    persons_url = serializers.SerializerMethodField()

    def get_persons_url(self, obj):
        """Method that returns the absolute path to the list of company persons
        """
        url = f"{reverse(viewname='core:person-list')}?company_id={obj.id}"
        return self.context["request"].build_absolute_uri(url)

    class Meta:
        model = Company
        URL_FIELD_NAME = "company_url"
        fields = (
            "id",
            "name",
            "company_url",
            "location",
            "revenue",
            "persons_url",
        )


class CompanyListSerializer(serializers.HyperlinkedModelSerializer):
    """Serializer for Company model"""
    company_url = serializers.HyperlinkedIdentityField(
        view_name="core:company-detail",
        lookup_field="pk",
    )

    class Meta:
        model = Company
        fields = (
            "id",
            "name",
            "company_url",
        )
