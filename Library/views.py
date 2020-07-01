from django.shortcuts import render, HttpResponse

# Home page
def index(request):
    return render(request, "index.html")

# Add a book
def create(request):
    return render(request, "create.html")

# List all books 
def list_all(request):
    return render(request, "list_all.html")