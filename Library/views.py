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
        # create the Book instance then save to db
        new_book = Book(title=title, author=author, year=year, pages=pages, description=description)  
        new_book.save()
        return redirect("/show/"+ str(new_book.id))
    elif request.method == "GET":
        return render(request, "create.html")
    else:
        return HttpResponse("Operation not allowed")

# List all books 
def list_all(request):
    context = {"books": Book.objects.all()}
    return render(request, "list_all.html", context)

def show_id(request, id):
    book_id = id
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "show.html", context)