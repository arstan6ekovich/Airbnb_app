from .models import Property, City
from modeltranslation.translator import TranslationOptions,register

@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('city_name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')