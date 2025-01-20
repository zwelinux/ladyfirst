from django.contrib import admin
from .models import * 

admin.site.register(Product)

admin.site.register(User)
admin.site.register(Transaction)
admin.site.register(SharedLink)
admin.site.register(Favorite)
admin.site.register(Admin)

admin.site.site_header = 'LadyFirst.Me'