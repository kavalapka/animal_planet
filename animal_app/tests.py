from django.test import TestCase
from animal_app.models import Animal


class AnimalViewTests(TestCase):
    def test_animal_list_view(self):
        response = self.client.get('/animal/')
        self.assertEqual(response.status_code, 200)


class AnimalDetailView(TestCase):
    def test_animal_detail_view(self):
        new_animal = Animal.objects.create(name='test', number='1', owner_id='1')
        response = self.client.get('/animal/{}/'.format(new_animal.id))
        self.assertEqual(response.status_code, 200)
