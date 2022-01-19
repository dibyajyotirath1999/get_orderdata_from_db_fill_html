from django.contrib import admin
from fetchapp.models import *

class dbdata_admin(admin.ModelAdmin):
    list_display=["sl_no","iname","iquantity","price"]
admin.site.register(fetchingdb,dbdata_admin)