#!/usr/bin/env python

from django.shortcuts import render
from .models import Book
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import  render
from django.http import Http404

def index(request):

    all_books = Book.objects.all()
    # template = loader.get_template('books/index.html')
    context= {

        'all_book': all_books
    }
    # return HttpResponse(all_books.name)
    # return HttpResponse(template.render(context,request))

    return render(request, 'books/index.html' ,context)

def details(reuest,book_id):
    try:
       Book_detail= Book.objects.get(id=book_id)
    except  Book_detail.DoesNotExist:
        raise Http404("Details not found")
    return render(reuest,'books/detail.html',{'Book_detail':Book_detail})

    # return HttpResponse("<h2> This is the details of" + str(book_id) + "</h2>")



