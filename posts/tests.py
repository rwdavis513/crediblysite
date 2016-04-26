
from django.test import TestCase
from django.core import serializers
from posts.serializers import PostSerializer

class PostSerializerTest (TestCase):
    def setUp(self):
        self.user = Account.objects.create_user('foo', 'foo@bar.de', 'bar')
        self.token = Token.objects.get(user=self.user).key
        self.c = Client()

    def test_serializer(self):
        # Stuff to serialize
        PostSerializer().save()
        Color(name='blue').save()
        Color(name='red').save()

        # Expected output
        expect_yaml = \
            'myapp.color:\n' \
            '  1: {name: green}\n' \
            '  2: {name: blue}\n' \
            '  3: {name: red}\n'

        # Do the serialization
        actual_yaml = serializers.serialize('yaml', Color.objects.all())

        # Did it work?
        self.assertEqual(actual_yaml, expect_yaml)