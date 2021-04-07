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
class AdminComment(admin.TabularInline):
    model = Comment

    extra = 0
    verbose_name = "Коментарий"
    verbose_name_plural = "Коментарии"

class AdminDocument(admin.TabularInline):
    model = Document
    extra = 0
    verbose_name = "Документ"
    verbose_name_plural = "Документы"

class AdminMaterialforItem(admin.TabularInline):
    model = MaterialforItem
    extra = 0
    verbose_name = "Материал"
    verbose_name_plural = "Материалы"



@admin.register(ItemProject)
class AdminItemProject(admin.ModelAdmin):
    # fields = (('mrf', 'rf'), 'subjectRF', 'address', 'status')
    list_display = ('address', 'contractor', 'status')
    list_filter = ('contractor', 'status')
    ordering = ('-data_ready_from_dogovor',)
    inlines = [
        AdminComment, AdminDocument, AdminMaterialforItem
    ]
    fieldsets = (
        ('Информация', {
            'description': "",
            'fields': (('mrf', 'rf'),
                       ('subjectRF', 'address'),
                       ('num_access_link', 'status'),
                       ('contractor', 'access'),
                       ('date_access_SMR', 'obemy_podany'),
                       ('ready_smr', 'data_priemki_rtk'),
                       ('foto_montaj_upload', 'smr_ready'),
                       ('rtk_ready', 'id_ready'),
                       ('act_ready', 'plan_data_ready_smr'),

                       'data_ready_from_dogovor')
        }),
        ('Дополнительная информация', {
            'classes': ('collapse',),
            'fields': ('komentariy',)
        }),
    )


# admin.site.register(ItemProject, AdminItemProject)


class AdminContractor(admin.ModelAdmin):
    list_display = ['name', 'telephone', 'address', 'user']


admin.site.register(Contractor, AdminContractor)

admin.site.register(Category)
# class AdminDocument(admin.ModelAdmin):
#     list_display = ['description', 'file', 'uploaded_at', 'item_proj', 'user_upload']
#
#
# admin.site.register(Document, AdminDocument)


# class AdminComment(admin.ModelAdmin):
#     list_display = ['date_create', 'author', 'item_p', 'text']
#
#
# admin.site.register(Comment, AdminComment)
