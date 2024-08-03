from django.shortcuts import render

def resume(request):
    return render(request, 'portfolio/resume.html', {})