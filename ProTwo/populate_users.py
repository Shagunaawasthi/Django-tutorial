#setting up our file. putting django default settings
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'ProTwo.settings')

#this will let us in django and let populate
import django
django.setup()

#importing models that we need to populate and Faker through which 
#we gonna populate our data
from appTwo.models import User
from faker import Faker

#instantiated an object of faker
fakegen = Faker()

def populate(N=5):

    for entry in range(N):
        fake_name = fakegen.name().split()
        fake_first_name = fake_name[0]
        fake_last_name = fake_name[1]
        fake_email = fakegen.email()

        user = User.objects.get_or_create(first_name=fake_first_name,
                                          last_name=fake_last_name,
                                          email= fake_email)[0]

#to print in cmd to let you know stuff happened
if __name__ == '__main__':
    print("populating")
    populate(20)
    print("done!")
