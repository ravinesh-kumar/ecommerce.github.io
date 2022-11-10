from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from.models import product
from frontend.models import loginids,contactdb
import os
from django.core.files.storage import FileSystemStorage

def logintable(request):
   z = loginids.objects.all()
   return render(request,'adminisrtration/logintable.html',{'data':z})

def contacttable(request):
    z = contactdb.objects.all()
    return render(request,'adminisrtration/contacttable.html',{'data':z})

def productupload(request):
    return render(request,'adminisrtration/productupload.html')

def producttable(request):
    z = product.objects.all()
    
    return render(request,'adminisrtration/producttable.html',{'data':z})

def upload(request):
    productname=request.POST['productname']
    price=request.POST['price']
    details=request.POST['details']

    #fetch the image
    filepath = request.FILES['myfile']
    filename = filepath.name #store file name

    file_type = os.path.splitext(str(filepath))[1]

    if(file_type==".jpg" or file_type==".jpeg" or file_type==".png"):
        obj = FileSystemStorage() #creating object of FileSystemStorage Class
        k   = obj.save(filename, filepath) # using save(FileName, FilePath) function
        uploaded_file_url = obj.url(k)
        
        k1=product(productname=productname,  price=price, details=details, image=filename)
        k1.save()
        return redirect(" ")
        
    else:
        return HttpResponse("Error! Invalid File")
    


