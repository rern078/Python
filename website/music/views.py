from django.shortcuts import render
# from music.models import Album
from .models import User_Messages

# Create your views here.
# def home(request):
#       return render(request, 'home.html')
# def about(request):
#       return render(request, 'about.html')


# def home(request):
#       Albums = Album.objects.all()
#       return render(request, 'home.html', {'Albums': Albums})

def contact(request):
    success = False
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        
        # Create and save a new instance of User_Messages
        user_message = User_Messages(name=name, email=email, subject=subject, message=message)
        user_message.save()
        success = True
    return render(request, 'contact.html', {'success': success})