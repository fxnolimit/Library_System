from django.shortcuts import render, HttpResponse, redirect
from .models import Book

# Home page
def index(request):
    return render(request, "index.html")

# Add a book
def create(request):
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        year = request.POST["year"]
        pages = request.POST["pages"]
        description = request.POST["description"]

        new_book = Book(title=title, author=author, year=year, pages=pages, description=description)  
        new_book.save()

        return redirect("/list_all")
    elif request.method == "GET":
        return render(request, "create.html")
    else:
        return HttpResponse("Operation not allowed")

# List all books 
def list_all(request):
    return render(request, "list_all.html")