from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from ads.models import Selection
from ads.permissions import SelectionPermission
from ads.serializers import SelectionDetailSerializer, SelectionListSerializer, \
    SelectionCreateOrUpdateSerializer


class SelectionListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionListSerializer


class SelectionDetailView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionDetailSerializer


class SelectionCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionPermission]


class SelectionUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionPermission]


class SelectionDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionCreateOrUpdateSerializer
    permission_classes = [IsAuthenticated, SelectionPermission]