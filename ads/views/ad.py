import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import UpdateView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from ads.models import Ad
from ads.permissions import AdPermission
from ads.serializers import AdSerializer


class AdListView(ListAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer

    def get(self, request, *args, **kwargs):
        category = request.GET.getlist("cat", [])
        text = request.GET.get("text")
        location = request.GET.get("location")
        price_from = request.GET.get("price_from")
        price_to = request.GET.get("price_to")
        if category:
            self.queryset = self.queryset.filter(category_id__in=category)
        if text:
            self.queryset = self.queryset.filter(name__icontains=text)
        if location:
            self.queryset = self.queryset.filter(author__location_id__name__icontains=location)
        if price_from:
            self.queryset = self.queryset.filter(price__gte=price_from)
        if price_to:
            self.queryset = self.queryset.filter(price__lte=price_to)

        return super().get(request, *args, **kwargs)


class AdDetailView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, ]


class AdCreateView(CreateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdPermission]


class AdUpdateView(UpdateAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdPermission]


class AdDeleteView(DestroyAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    permission_classes = [IsAuthenticated, AdPermission]


@method_decorator(csrf_exempt, name='dispatch')
class AdUploadImageView(UpdateView):
    model = Ad
    fields = ("image",)
    permission_classes = [IsAuthenticated, AdPermission]

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()

        self.object.image = request.FILES.get("image", None)
        self.object.save()

        return JsonResponse({
            "id": self.object.pk,
            "name": self.object.name,
            "author": self.object.author.username,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "category_id": self.object.category_id,
            "image": self.object.image.url if self.object.image else None
        }, status=200, safe=False)
