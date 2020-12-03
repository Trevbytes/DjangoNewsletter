from django.test import TestCase
from .models import NewsletterSignup

# Create your tests here.


class NewsletterModelTest(TestCase):

    def setUp(self):
        NewsletterSignup.objects.create(full_name="Test Full Name",
                                        email="test@g.com",
                                        postcode="16486",
                                        )

    def test_string_representation_entry(self):
        newsletter_signup = NewsletterSignup.objects.get(full_name="Test Full Name")
        self.assertEqual(str(newsletter_signup), newsletter_signup.email)

class TestViews(TestCase):

    def test_get_index(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/newsletter_form.html')
