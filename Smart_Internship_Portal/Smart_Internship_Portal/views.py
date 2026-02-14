from django.shortcuts import render

def test(request):
    return render(request, "Smart_Internship_Portal/index.html")