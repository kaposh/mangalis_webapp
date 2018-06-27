from django.urls import reverse
from django.test import TestCase
from .models import Souvenir

def create_souvenir(name, description, image, available):
    """
    Create a souvenir with the given attributes
    """
    return Souvenir.objects.create(name=name, description=description, available=available )


class CatalogIndexViewTests(TestCase):
    def test_no_souvenirs(self):
        """
        If no souvenirs exist, no souvenirs are shown in the index page
        """
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['available_souvenirs'], [])

    def test_one_souvenir_no_available(self):
        """
        If a souvenir exist but is not available, no souvenirs are shown in the index page
        """
        create_souvenir("Souvenir","With Description",None, False)
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['available_souvenirs'], [])

    def test_one_souvenir_one_available(self):
        """
        If a souvenir exist but is not available, no souvenirs are shown in the index page
        """
        create_souvenir("Souvenir","With Description",None, True)
        response = self.client.get(reverse('catalog:index'))
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['available_souvenirs'], ['<Souvenir: Souvenir>'])