from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin

class HospitalImageInline(admin.TabularInline):
    model = HospitalImage
    extra = 1

@admin.register(Hospital)
class HospitalAdmin(TranslationAdmin):
    inlines = [HospitalImageInline]
    class Media:
        js = (
            'http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

admin.site.register(UserProfile)
admin.site.register(DepartmentCategory)
admin.site.register(Doctor)
admin.site.register(PatientProfile)
admin.site.register(Appointment)
admin.site.register(MedicalRecord)
admin.site.register(Feedback)
