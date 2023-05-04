from django.contrib import admin
from .models import Passenger
from import_export.admin import ImportExportActionModelAdmin

@admin.register(Passenger)
class PassengerAdmin(ImportExportActionModelAdmin):
    list_display = ['id', 'survived', 'p_class', 'full_name', 'sex', 'age', 'sib_sp', 'parch',  'ticket', 'fare', 'cabin', 'embarked']
    list_display_links = ['id', 'survived', 'p_class', 'full_name', 'sex', 'age', 'sib_sp', 'parch',  'ticket', 'fare', 'cabin', 'embarked']
    search_fields = ['id', 'full_name']