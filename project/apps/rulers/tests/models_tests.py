from django.test import TestCase

from project.apps.rulers.models import Ruler


class RulerTest(TestCase):
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

    def test_all_successors(self):
        successors = self.predecessor.all_successors
        self.assertEqual(len(successors), 2)
        self.assertEqual(successors[0], self. ruler)
        self.assertEqual(successors[1], self. successor)

        successors = self.ruler.all_successors
        self.assertEqual(len(successors), 1)
        self.assertEqual(successors[0], self. successor)
