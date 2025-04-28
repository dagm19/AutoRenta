from django.test import TestCase
from django.contrib.auth import get_user_model

class CustomUserTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            email="t5yKq@example.com",
            rol="Cliente",
        )
        self.assertEqual(user.username, "testuser")
        self.assertEqual(user.email, "t5yKq@example.com")
        self.assertEqual(user.rol, "Cliente")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser(self):
        User = get_user_model()
        user = User.objects.create_superuser(
            username="testsuperuser",
            password="testpassword",
            email="t5yKq@example.com",
            rol="Administrador",
        )
        self.assertEqual(user.username, "testsuperuser")
        self.assertEqual(user.email, "t5yKq@example.com")
        self.assertEqual(user.rol, "Administrador")
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)