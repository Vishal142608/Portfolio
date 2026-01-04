from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.http import FileResponse, HttpResponse
from .models import Profile, ContactMessage, Project, CV

def home(request):
    # Safe fetch: agar Profile table empty ya exist nahi karti
    try:
        profile = Profile.objects.first()
    except:
        profile = None

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save to DB (ContactMessage table bhi ensure migrate ho)
        if ContactMessage.objects.exists():
            ContactMessage.objects.create(
                full_name=full_name,
                email=email,
                message=message
            )

        # Send email
        try:
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
        except:
            pass  # Fail silently in production

        return redirect('portfolio-home')

    return render(request, 'home.html', {'profile': profile})


def download_cv(request):
    try:
        cv = CV.objects.last()  
    except:
        cv = None

    if not cv:
        return HttpResponse("CV not found", status=404)

    return FileResponse(cv.file.open('rb'), as_attachment=True, filename=cv.file.name.split('/')[-1])


def about(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None

    return render(request, 'about.html', {'profile': profile})


def skills(request):
    return render(request, "skills.html")


def content(request):
    try:
        profile = Profile.objects.first()
    except:
        profile = None

    return render(request, "content.html", {"profile": profile})


def projects(request):
    try:
        projects = Project.objects.all()
    except:
        projects = []

    return render(request, "project.html", {"projects": projects})


def experience(request):
    return render(request, 'experience.html')
