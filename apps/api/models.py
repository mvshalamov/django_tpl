import json
from django.db import models


class SomeUser(models.Model):
    username = models.CharField(max_length=100, unique=True, db_index=True)
    email = models.EmailField(max_length=150, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def to_json(self):
        return json.dumps(
            {
                'pk': self.pk,
                'username': self.username,
                'email': self.email
            }
        )

    def __str__(self):
        return self.username

    @classmethod
    def create_user(cls, username, email):
        user = cls()
        user.username = username
        user.email = email
        user.save()
        return user
