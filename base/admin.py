from django.contrib import admin
from .models import Performance
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class PerformanceResource(resources.ModelResource):

    class Meta:
        model = Performance

class PerformanceAdmin(ImportExportModelAdmin):
    resource_class = PerformanceResource

admin.site.register(Performance, PerformanceAdmin)