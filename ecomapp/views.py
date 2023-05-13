from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from ecomapp.models import Categorys
from ecomapp.models import Products
# Create your views here.
def home(request):
    return render(request,'index.html')
def loginpg(request):
    return render(request,'login.html')
def admpg(request):
    return render(request,'adminpage.html')
def login1(request):
 if request.method == 'POST':
    username=request.POST['username']
    password=request.POST['password']
    user = auth.authenticate(username=username, password=password) 
    #request.session["uid"]=user.id#session method part
    if user is not None:
        if user.is_staff:
            login(request,user)
            return redirect('admpg')
        else:
            login(request,user)
            auth.login(request,user)
            messages.info(request,f'Welcome{username}')
            return redirect('/')
        
    else:
        messages.info(request,'Invalid Username or Password. Try again.')
        return redirect('home')
 else:
     return redirect('home')
def logout(request):
    #if request.user.is_authenticated:(is authenticated method part)
    #request.session["uid"] = ""#session method part
    auth.logout(request)
    return redirect('home')
def addc(request):
    return render(request,'addcategory.html') 
def addcdb(request):
    if request.method=="POST":
        c_name=request.POST.get('c_name')
        categoryz=Categorys(c_name=c_name)
        categoryz.save()
        return redirect('addc')
def addp(request):
   products=Categorys.objects.all()
   return render(request,'addproduct.html',{'p':products})
def addpdb(request):
    if request.method=='POST':
        name=request.POST['name']
        print(name)
        desc=request.POST['desc']
        print(desc)
        price=request.POST['price']
        print(price)
        opt=request.POST['opt']
        print(opt)
        image=request.FILES.get('image')
        print(image)
        cat=Categorys.objects.get(id=opt)
        print(cat)
        prod=Products(name=name,desc=desc,price=price,image=image,category=cat)
        prod.save()
        return redirect('addp')
def show(request):
    prod=Products.objects.all()
    return render(request,'showproduct.html',{'p':prod}) 
def deletepage(request,pk):
    emp=Products.objects.get(id=pk)
    emp.delete()
    return redirect('show')   