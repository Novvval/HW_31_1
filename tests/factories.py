import factory
from ads.models import Ad, User, Category, Location, Selection


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    slug = factory.Faker("ean", length=8)


class LocationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Location


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Faker("name")
    email = factory.Faker("email")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    author = factory.SubFactory(UserFactory)
    category = factory.SubFactory(CategoryFactory)
    price = 100
