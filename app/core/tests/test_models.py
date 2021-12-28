from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_succesuful(self):
        """"Test cerating a new user with email"""
        email = 'test@email.com'
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))

    def test_user_email_normalized(self):
        """Test the email normailized"""
        email = "test@EMAIL.com"
        password = 'Test123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email,email.lower())

    def test_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None,'Test123')

    def test_create_super_user(self):
        """Create super user"""
        user = get_user_model().objects.create_superuser(
            "test@EMAIL.com",
            "password"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)