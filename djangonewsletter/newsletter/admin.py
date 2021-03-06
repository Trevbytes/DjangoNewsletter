import csv
from django.contrib import admin
from .models import NewsletterSignup
from django.http import HttpResponse


class ExportCsvMixin:
    """Code to write data as a CSV file"""
    def export_as_csv(self, request, queryset):

        meta = self.model._meta
        field_names = [field.name for field in meta.fields]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])

        return response

    export_as_csv.short_description = "Export Selected"


class NewsletterAdmin(admin.ModelAdmin, ExportCsvMixin):
    """An admin class taging relevent data and allowing
    the data to be exported as a CSV file."""
    fields = ('full_name', 'email', 'postcode',)
    list_display = ('full_name', 'email', 'postcode',)
    ordering = ('-full_name',)
    actions = ["export_as_csv"]


admin.site.register(NewsletterSignup, NewsletterAdmin)
