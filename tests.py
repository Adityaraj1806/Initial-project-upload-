from django.test import TestCase
from django.contrib.auth.models import User
from .models import Faculty, Publication

class ModelTest(TestCase):

    def setUp(self):
        # Create user
        self.user = User.objects.create(username="testuser")

        # Create faculty
        self.faculty = Faculty.objects.create(
            user=self.user,
            department="CSE",
            designation="Professor"
        )

        # Create publication
        self.publication = Publication.objects.create(
            faculty=self.faculty,
            title="AI Research",
            journal="IEEE",
            year=2025
        )

    def test_publication(self):
        self.assertEqual(self.publication.title, "AI Research")
        self.assertEqual(self.publication.journal, "IEEE")
        self.assertEqual(self.publication.year, 2025)