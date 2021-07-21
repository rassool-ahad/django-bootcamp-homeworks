from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Table)
admin.site.register(Recepites)
admin.site.register(Orders)
admin.site.register(MenuItems)
admin.site.register(Category)
admin.site.register(Status)

