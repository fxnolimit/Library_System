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

# Show book information
def show_id(request, id):
    book_id = id
    context = {"book": Book.objects.get(id=book_id)}
    return render(request, "show.html", context)

# delete book 
def delete_id(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect("/list_all")

# edit book
def edit_id(request, id):
    book_id = id
    if request.method == "POST":
        title = request.POST["title"]
        author = request.POST["author"]
        year = request.POST["year"]
        pages = request.POST["pages"]
        description = request.POST["description"]
        # update the book instance then save to db
        book = Book.objects.get(id=book_id)
        book.title = title
        book.author = author
        book.year = year
        book.pages = pages
        book.description = description  
        book.save()
        return redirect("/show/"+ str(book.id))
    elif request.method == "GET":
        book = Book.objects.get(id=book_id)
        year = str(book.year)
        context = {"book": book, "year_format": year}
        return render(request, "edit.html", context)
    else:
        return HttpResponse("Operation not allowed")

