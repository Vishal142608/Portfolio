from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
# from django.http import HttpResponse
from django.conf import settings
from django.http import FileResponse, HttpResponse
from .models import Profile, ContactMessage, Project, CV


def home(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # save to DB
        ContactMessage.objects.create(
            full_name=full_name,
            email=email,
            message=message
        )

        # send email
        send_mail(
            subject=f"New Contact Message from {full_name}",
            message=f"""
Name: {full_name}
Email: {email}

Message:
{message}
""",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False,
        )

        return redirect('portfolio-home') 

    return render(request, 'home.html', {'profile': profile})



def download_cv(request):
    # Yahan hum latest CV ko fetch kar rahe hain
    cv = CV.objects.last()  
    if not cv:
        return HttpResponse("CV not found", status=404)

    # Browser me download ke liye
    return FileResponse(cv.file.open('rb'), as_attachment=True, filename=cv.file.name.split('/')[-1])

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})


def skills(request):
    return render(request, "skills.html")


def content(request):
    profile = Profile.objects.first()
    return render(request, "content.html", {"profile": profile})
    

def projects(request):
    projects = Project.objects.all()
    return render(request, "project.html", {"projects": projects})


def experience(request):
    return render(request, 'experience.html')
