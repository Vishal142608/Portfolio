from django.contrib import admin
from .models import Profile, Project, CV

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'live_link')

@admin.register(CV)
class CVAdmin(admin.ModelAdmin):
    list_display = ('name', 'file', 'uploaded_at')
