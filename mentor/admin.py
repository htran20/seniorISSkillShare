from django.contrib import admin


from .models import Address, MentorProfile
# Register your models here.

admin.site.register(MentorProfile)
admin.site.register(Address)
