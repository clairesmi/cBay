from django.contrib import admin
from .models import User, Recommendation, Listing

# Register your models here.
admin.site.register(User)
admin.site.register(Recommendation)
admin.site.register(Listing)
