from django.test import TestCase
from users.models import User


class UserModelTest(TestCase):

    def test_create_user(self):

        user = User.objects.create_user(
            phone="+380999999999",
            password="password123"
        )

        self.assertEqual(user.phone, "+380999999999")
        self.assertTrue(user.check_password("password123"))