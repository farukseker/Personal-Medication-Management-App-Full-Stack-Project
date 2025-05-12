from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class MedicationTests(APITestCase):
    def test_create_a_new_medications_plan(self):
        """
        Ensure we can create a new medication object.
        """
        url = reverse('api:medication:create')
        data = {
            "name": "İlaç",
            "notes": "Test notu",
            "hunger_situation": "Tok",
            "start_date": "2025-05-10",
            "end_date": "2025-06-10",
            "stages": [
                {
                  "unit": 1,
                  "unit_type": "Drop",
                  "range_length": 1,
                  "range_type": "week"
                }
            ],
            "often": ["sabah", "akşam"]
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
