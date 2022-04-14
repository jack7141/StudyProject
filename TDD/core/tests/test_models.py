from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is successful"""
        email = 'test@londonappdev.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """Test the email for a new user is normalized"""
        email = 'test@LONDONAPPDEV.COM'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """check if invalid Email raises ValueError"""
        invaild_email = get_user_model().objects.create_user(None, 'test123')
        self.assertEqual(ValueError, type(invaild_email))

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            email='test@londonappdev.com',
            password='test123',
        )
        self.assertEqual(user.email, 'test@londonappdev.com')
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)