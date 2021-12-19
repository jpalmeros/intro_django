from django.shortcuts import render


def home(request):
    return render(request, "home.html", {})


def about(request):
    my_name = "Hola, mi nombre es Jose Palmer"
    return render(request, "about.html", {"my_name": my_name})


def contact(request):
    return render(request, "contact.html", {})
