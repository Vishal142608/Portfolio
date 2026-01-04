from django.db import models

class Profile(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/')


class ContactMessage(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name


class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    github_link = models.URLField(blank=True)
    live_link = models.URLField(blank=True)

    def __str__(self):
        return self.title


class CV(models.Model):
    name = models.CharField(max_length=100, default="Vishal_Saini_CV")
    file = models.FileField(upload_to='cvs/')  # media/cvs/ folder
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
