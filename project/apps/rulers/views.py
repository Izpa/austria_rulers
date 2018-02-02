from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from project.apps.rulers.models import Ruler, RulerRequest
from project.apps.rulers.serializers import RulerSerializer, RulerWithAllSuccessorsSerializer


class RulerViewSet(ListModelMixin, GenericViewSet):
    queryset = Ruler.objects.all()
    serializer_class = RulerSerializer


class RulerWithAllSuccessorsViewSet(RetrieveModelMixin, GenericViewSet):
    queryset = Ruler.objects_select_related.all()
    serializer_class = RulerWithAllSuccessorsSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        ruler_request = RulerRequest.objects.create(ruler=instance)
        ruler_request.ruler_successors.set(instance.all_successors)
        ruler_request.save()
        return Response(serializer.data)
