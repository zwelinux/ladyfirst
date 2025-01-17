from django.contrib import admin
from .models import * 

admin.site.register(Product)

admin.site.site_header = 'LadyFirst.Me'