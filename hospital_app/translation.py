from .models import *
from modeltranslation.translator import TranslationOptions,register

@register(Hospital)
class HospitalTranslationOptions(TranslationOptions):
    fields = ('hospital_name', 'hospital_description')
