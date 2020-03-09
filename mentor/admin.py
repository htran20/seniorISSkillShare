from django.contrib import admin


from .models import Address, MentorProfile, UserMentorProfile
# Register your models here.

admin.site.register(MentorProfile)
admin.site.register(Address)
admin.site.register(UserMentorProfile)
