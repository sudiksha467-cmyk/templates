from django.shortcuts import render

def home(request):
    return render(request, 'book_cover.html')
