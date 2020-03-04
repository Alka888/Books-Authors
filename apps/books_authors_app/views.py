from django.shortcuts import render, redirect
from .models import Author, Books


def index(request):
    content = {
        "books": Books.objects.all()
    }
    return render(request, 'books_authors_app/index.html', content)
# это функция как dictionary, какие значения мы указываем в нем они переходят на страницу которую видит пользователь Эта функция отображает первую страницу-Книги


def books(request):
    title = request.POST['title_book']
    desc = request.POST['desc']
    Books.objects.create(title=title, description=desc)
    return redirect('/')
# когда мы печаем в строку и нажимаем кнопку add. добавляем книгу к списку справа


def bookdet(request, id):
    ebook = Books.objects.get(id=id)
    authors = Author.objects.all()
    authorsofbook = ebook.authors.all()
    print(authorsofbook)
    content = {
        "books": ebook,
        "auth": authors,
        "authorsofbook": authorsofbook,
    }
    return render(request, 'books_authors_app/bookdetail.html', content)
# эта функция переводит нас на вторую страницу где находится информация о книге.


def bookaut(request):
    auth_id = request.POST["auth_id"]
    ebook = Books.objects.get(id=request.POST["ebookid"])
    ebook.authors.add(Author.objects.get(id=int(auth_id)))
    return redirect('/')
    # эта функция добавляет автора к книге на второй странице


def addauthor(request):
    content = {
        "author": Author.objects.all()
    }
    return render(request, 'books_authors_app/author.html', content)
# это функция как dictionary, какие значения мы указываем в нем они переходят на страницу которую видит пользователь, отображает третью страцицу-Авторы


def addauthorform(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    notes = request.POST['notes']
    Author.objects.create(first_name=first_name,
                          last_name=last_name, notes=notes)
    return redirect('/addauthor')
# когда мы печаем в строку и нажимаем кнопку add. добавляем автора к списку справа


def author(request, id):
    eauthor = Author.objects.get(id=id)
    authors = Author.objects.all()
    authorsofbook = eauthor.books.all()
    print(authorsofbook)
    content = {
        "books": eauthor,
        "auth": authors,
        "authorsofbook": authorsofbook,
    }
    return render(request, 'books_authors_app/authordetail.html', content)
# эта функция: мы нажимаем на вид и переходим на третью страницу и видим информ об авторе


def add_book_to_author(request, author_id):
    if request.method == "POST":
        this_author = Author.objects.get(id=author_id)
        this_book = Book.objects.get(id=request.POST["book_id"])
        this_author.books.add(this_book)
    return redirect('/addauthorform/' + author_id)
# эта функция на четвертой странице где мы можем довавить книгу к автору
