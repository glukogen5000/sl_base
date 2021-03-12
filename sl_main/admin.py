from django.contrib import admin
from .models import *


# class School_admin(admin.ModelAdmin):
#     list_display = ('Name', 'Address', 'Contact', 'Status_name', 'StatusID', 'StatusKD')
# admin.site.register()
# admin.site.register(School, School_admin)
# class itemAdmin(admin.ModelAdmin):
#     fieldsets = [
#         ('address', {'fields': ["address"]})
#     ]
#
admin.site.register(ItemProject)
admin.site.register(Contractor)
# admin.site.register(ItemProject, itemAdmin)

# admin.site.register(FeedFilePhoto)
# admin.site.register(FeedFileAkt)
# admin.site.register(FeedFileID)
