from datetime import timedelta, date
from django.core.exceptions import ValidationError


def check_if_true(value):
    if value:
        raise ValidationError("Status cannot be true when creating ad")


def check_age(value):
    if value > date.today() - timedelta(days=3285):
        raise ValidationError("Must be older than 9")


def check_email(value):
    if "rambler.ru" in value:
        raise ValidationError("Cannot have an email in this domain")

