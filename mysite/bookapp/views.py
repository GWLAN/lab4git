# -*- coding: utf-8 -*-
from django.shortcuts import render
from bookapp.models import Author
from bookapp.models import Book
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

def index(request):
	return render_to_response('index.html')

def library(request):
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	is_click = False
	return render_to_response('library.html',{'AuthorList':lis,'BookList':lis2,"is_click":is_click})

def booklist(request):
	booklist = Book.objects.all()
	return render_to_response('booklist.html',{'booklist':booklist})	
    


	except Book.DoesNotExist:
		return render_to_response('addbook.html')
	else:
		return render_to_response('bookinformation.html',{'booktest':BookAim})


def serchwriter0(request):
    return render_to_response('serchwriter.html')

def serchwriter(request):
	word = request.POST['authorname']
	try:
		AuthorAim = Author.objects.get(Name = word)
		AuthorBooks = AuthorAim.book_set.all()	
		return render_to_response('library.html',{'Authors':AuthorAim,'AuthorBooks':AuthorBooks})  
	except Author.DoesNotExist:
		return render_to_response('addwriter.html') 


def DelBook(request,key):
	Aim = Book.objects.get(ISBN=key)
	Aim.delete()
	return  HttpResponseRedirect("/booklist")

def UpdateBook(request):
	Aim = Book.objects.get(ISBN=request.POST['update'])
	BookAuthor = Author.objects.get(AulthorID=Aim.AulthorID_id)
	return render_to_response('addbook.html',{'book':Aim,'author':BookAuthor})

def UpdateBook2(request):
	publisher = request.POST['book_publisher']
	date = request.POST['book_date']
	price = request.POST['book_price']
	Aim = Book.objects.get(ISBN=request.POST['book_ISBN'])
	Aim.Publisher =  publisher
	Aim.PublishDate = date
	Aim.Price = float(price)
	Aim.save()
	lis = Author.objects.all()
	lis2 = Book.objects.all()
	return render_to_response('library.html',{'AuthorList':lis,'BookList':lis2})

def information(request):
	is_click = True
	AuthorAim = Author.objects.get(AuthorID = request.POST['author_ID'])
	AuthorBooks = AuthorAim.book_set.all()
	return render_to_response("library.html",{"is_click":is_click,"book1":Book.objects.get(ISBN=request.POST['book_ISBN']),'Authors':AuthorAim,'AuthorBooks':AuthorBooks})
