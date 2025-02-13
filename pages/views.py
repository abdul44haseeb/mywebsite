from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')  # Use render to load the template