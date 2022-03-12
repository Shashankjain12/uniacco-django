from django.contrib import admin
from uniacco_api.models import UserLoginHistory
from import_export.admin import ImportExportModelAdmin
# Register your models here.

# for adding import export functionality to csv file
@admin.register(UserLoginHistory)
class UserLoginHistoryAdmin(ImportExportModelAdmin):
    pass