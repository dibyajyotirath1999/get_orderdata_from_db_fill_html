from django.shortcuts import render
from fetchapp.models import *

def fetchdb(request):
    dbdata= fetchingdb.objects.all()
    return render (request,"fetchdb.html",{"dbdata":dbdata})


