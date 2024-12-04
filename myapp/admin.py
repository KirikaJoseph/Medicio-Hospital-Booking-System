from django.contrib import admin
from myapp.models import Member, Appointment, Contactss, User, ImageModel

# Register your models here.
admin.site.register(Member)
admin.site.register(Appointment)
admin.site.register(Contactss)
admin.site.register(User)
admin.site.register(ImageModel)