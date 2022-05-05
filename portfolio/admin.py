from django.contrib import admin
from .models import Project, ProjectImage, Testimonial, Service, Contact


# Register your models here.

class ProjectImageAdmin(admin.StackedInline):
    model = ProjectImage


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageAdmin]

    class Meta:
        model = Project


admin.site.register([Testimonial, Service, Contact])
