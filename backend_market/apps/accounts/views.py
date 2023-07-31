from django.shortcuts import render

# Create your views here.


def d_test(request):
    return render(request, "backend/main.html")
