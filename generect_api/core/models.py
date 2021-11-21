from django.db import models
from django.utils.translation import gettext_lazy as _


class Person(models.Model):
    """Person model."""
    full_name = models.CharField(_("person.full_name"), max_length=100)
    job_title = models.CharField(_("person.job_title"), max_length=50)
    location = models.CharField(_("person.location"), max_length=50)
    email = models.EmailField(_("person.email"), max_length=50)
    phone_number = models.CharField(_("person.phone_number"), max_length=50)
    company = models.ForeignKey(
        "Company", on_delete=models.SET_NULL, null=True,
        related_name="persons")

    def __str__(self):
        """Return person name."""
        return self.full_name

    class Meta:
        verbose_name = _("Person")
        verbose_name_plural = _("Persons")


class Company(models.Model):
    """Company model."""
    name = models.CharField(_("company.name"), max_length=50)
    location = models.CharField(_("company.location"), max_length=50)
    revenue = models.PositiveIntegerField(_("company.revenue"))

    def __str__(self):
        """Return company name."""
        return self.name

    class Meta:
        verbose_name = _("Company")
        verbose_name_plural = _("Companies")
