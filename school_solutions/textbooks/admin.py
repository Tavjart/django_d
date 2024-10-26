from django.contrib import admin
from .models import Textbook, Solution, Subject, GradeLevel
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import CSVUploadForm
from .utils import import_csv

# Register your models here.
admin.site.register(Textbook)
admin.site.register(Subject)
admin.site.register(GradeLevel)


class SolutionAdmin(admin.ModelAdmin):
    change_list_template = "admin/solutions_changelist.html"  # Шаблон для кнопки импорта

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('import-csv/', self.import_csv),
        ]
        return custom_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            form = CSVUploadForm(request.POST, request.FILES)
            if form.is_valid():
                csv_file = form.cleaned_data['csv_file']
                import_csv(csv_file)
                self.message_user(request, "CSV файл успешно импортирован")
                return HttpResponseRedirect("../")
        else:
            form = CSVUploadForm()

        context = {
            'form': form,
            'opts': self.model._meta,
        }
        return render(request, "admin/csv_form.html", context)


admin.site.register(Solution, SolutionAdmin)
