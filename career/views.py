from django.shortcuts import render

# Create your views here.

def career_main(request):
    return render(request, 'career_main.html')


from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Hello, this is a test view!")