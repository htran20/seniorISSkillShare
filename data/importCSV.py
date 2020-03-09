import csv
import os
from mentor.models import MentorProfile, Address # imports the model

with open('data/mentorData/MentorInformationData.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        experience = row['Experience'].split(" - ")
        title = experience[1]
        employer = experience[0]
        addr = Address(street_address="", city="", state=row['Location'])
        addr.save()
        p = MentorProfile(name=row['Name'], email=row['Email'], age=21,
                          address=addr, description=row['Experience'], title="{} at {}".format(title, employer),
                          employer=employer, school=row['School'], major=row['Major'], degree=row['DegreeType'],
                          slug=row['Name'], image="/Users/htran20/Desktop/isfile/django-ecommerce/data/mentorData/IMG_5348 copy.jpg")

        p.save()