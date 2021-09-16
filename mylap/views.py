from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return HttpResponse("This is index page:")
def home(request):
    return render(request, "mylap/home.html",{})
def lob(request):
    book=Book()
    book.save()
    res=Book.objects.all()
    page =1
    if request.GET.get('pageId','') !='':
        page = str(request.GET.get('pageId',''))

    p = Paginator(res, 100)
    page_obj = p.get_page(page)
    return render(request,"mylap/lob.html", {"book_list":page_obj,"sort":""  , "totalPages": range(p.num_pages) })
def rform(request):
    return render(request, "mylap/rform.html",{})
def saveform(request):
    if request.method == 'POST':
        if request.POST["id"] =="":
            book=Book(title=request.POST['title'], author=request.POST['author'],ISBN=request.POST['ISBN'], edition=request.POST['edition'], publication=request.POST['publication'],price=request.POST['price'])
            book.save()
        elif request.POST["id"]!="":
            bookdb=getBook(int(request.POST["id"]))
            bookdb.ISBN=request.POST["ISBN"]
            bookdb.author=request.POST["author"]
            bookdb.title=request.POST["title"]
            bookdb.edition=request.POST["edition"]
            bookdb.publication=request.POST["publication"]
            bookdb.price=request.POST["price"]
            bookdb.save()
    else:
        print("save again:")
    return rform(request)
def editdetails(request,isbn):
    return render(request,"mylap/edit.html", {"book":getBook(isbn)})
def getBook(id):
    bookList = Book.objects.filter(id=id)
    book = Book()
    for x in bookList:
        book=x
        break
    return book
def edit(request,isbn):
    return render(request,"mylap/edit.html", {"book":getBook(isbn)})

def search(request):
    #res=Book.objects.all()
    res= Book.objects.filter(Q(ISBN__icontains=request.POST['search']) | Q(title__icontains=request.POST['search']) | Q(author__icontains=request.POST['search']) | Q(edition__icontains=request.POST['search']) | Q(publication__icontains=request.POST['search']) | Q(price__icontains=request.POST['search']))

    return render(request,"mylap/lob.html", {"book_list":res,"sort":""})
def price(request):
    return render(request,"mylap/price.html", {})

def ascen_order(request):
    b=Book.objects.order_by('price')
    return render(request,"mylap/lob.html", {"book_list":b,"sort":"asc"})

def decen_order(request):
    b=Book.objects.order_by('-price')
    return render(request,"mylap/lob.html", {"book_list":b,"sort":"Desc"})
