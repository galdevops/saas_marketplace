from django.shortcuts import render

# Create your views here.


def users_test(request):
    return render(request, "backend/main.html")
