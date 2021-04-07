from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home_view(request, *args, **kwargs):
    print(args, kwargs)
    print(request)
    print(request.user)
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    about_context = {
        "title" : "an about page",
        "about_text" : "This is about me me ME",
        "my_number" : 123456789,
        "my_list": [123, 456, 789, "abc"],
        "html_text" : "<h2>Hello there</h2>",
    }

    return render(request, "about.html", about_context)
