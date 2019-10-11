import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'practiceproject.settings')

import django
django.setup()

import random
from my_users.models import Users
from faker import Faker

fake = Faker()


def populate(N=10):

    for entry in range(N):

        fake_first = fake.first_name()
        fake_last = fake.last_name()
        fake_email = fake.email()

        Users.objects.get_or_create(first=fake_first, last=fake_last, email=fake_email)[0]

if __name__ == '__main__':
    print("populating")
    populate(20)
    print("populated")