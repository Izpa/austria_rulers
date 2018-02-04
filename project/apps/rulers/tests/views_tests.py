from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory

from project.apps.rulers.models import Ruler, RulerRequest
from project.apps.rulers.views import RulerWithAllSuccessorsViewSet


class RulerWithAllSuccessorsViewSetTest(APITestCase):
    def setUp(self):
        self.predecessor = Ruler.objects.create(name='predecessor',
                                                url='google.com/1',
                                                succession_order=1)
        self.ruler = Ruler.objects.create(name='ruler',
                                          url='google.com/2',
                                          predecessor=self.predecessor,
                                          succession_order=2)
        self.successor = Ruler.objects.create(name='successor',
                                              url='google.com/3',
                                              predecessor=self.ruler,
                                              succession_order=3)

    def test_ruler_request_object_create_on_each_retrieve(self):
        request = APIRequestFactory().get("")
        ruler_detail = RulerWithAllSuccessorsViewSet.as_view({'get': 'retrieve'})
        response = ruler_detail(request, pk=self.ruler.pk)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(RulerRequest.objects.count(), 1)
        self.assertEqual(RulerRequest.objects.get().ruler, self.ruler)
        self.assertEqual(RulerRequest.objects.get().ruler_successors.get(), self.successor)
