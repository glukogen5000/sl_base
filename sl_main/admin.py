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

class AdminItemProject(admin.ModelAdmin):
    list_display = ['address', 'contractor', 'status']
admin.site.register(ItemProject, AdminItemProject)




class AdminContractor(admin.ModelAdmin):
    list_display = ['name', 'telephone', 'address', 'user']


admin.site.register(Contractor, AdminContractor)
# admin.site.register(ItemProject, itemAdmin)

# admin.site.register(Document)



# admin.site.register(FeedFileID)
class AdminDocument(admin.ModelAdmin):
    list_display = ['description', 'file', 'uploaded_at', 'item_proj', 'user_upload']


admin.site.register(Document, AdminDocument)


class AdminComment(admin.ModelAdmin):
    list_display = ['date_create', 'author', 'item_p', 'text']

admin.site.register(Comment, AdminComment)