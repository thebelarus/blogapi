from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@testuser.com",
            password="password",
        )

        cls.post = Post.objects.create(
            author=cls.user,
            title="Hello",
            body="Hello world!",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "testuser"),
        self.assertEqual(self.post.title, "Hello"),
        self.assertEqual(self.post.body, "Hello world!"),
        self.assertEqual(str(self.post), "Hello"),
