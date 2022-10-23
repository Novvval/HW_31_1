from django.contrib import admin
from ads.models import User, Location, Ad, Category, Selection

admin.site.register(Location)
admin.site.register(Ad)
admin.site.register(Category)
admin.site.register(User)
admin.site.register(Selection)
