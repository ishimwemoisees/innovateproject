from django.urls import reverse
from django.test import TestCase


class NomeTests(TestCase):
    def test_nome_view_status_code(self):
        url = reverse('nome')
        response = self.client.get(url)
        url.assertEquals(response.status_code, 200)
