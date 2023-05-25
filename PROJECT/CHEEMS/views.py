from django.shortcuts import render
from django.http import HttpResponse
from CHEEMS.form import customerForm
from CHEEMS.models import customerModel
from CHEEMS.models import dogModel
from CHEEMS.form import dogForm
from django.contrib import messages
# Create your views here.
def front(request):
    return render(request,'home.html')
def login(request):
    return render(request,"login.html")
def adminRegister(request):
    f=customerForm()
    return render(request,"Adminregister.html",{'form':f})
def registerAction(request):
    f=customerForm(request.POST or None)
    if(f.is_valid()):
        f.save()
        messages.success(request,"Registered Successfully")
        return render(request,"register.html",{'form':f})
    else:
        messages.error(request,"Registered Failed")
        return render(request,"register.html",{'form':f})
def allcustomer(request):
    c=customerModel.objects.all()
    if(not c):
        messages.error(request,"No Record Found ")
        return render(request,"Allcustomerlisty.html")
    else:
        return render(request,"Allcustomerlisty.html",
                      {"record":c})
def register(request):
    f=customerForm()
    return render(request,"register.html",{'form':f})
def login_logic(request):
    name=request.GET["txt1"]
    pass1=request.GET["txt2"]
    choice=request.GET["txt3"]
    if(choice=="Administrator"):
        if(name=="Admin123" and pass1=="1234"):
            return render(request,"adminhome.html")
        else:
            messages.info(request,"Invalid Credentials")
            return render(request,"login.html")
    else:
        d=customerModel.objects.all().filter(name=name,mobile=pass1).values()
        id=d[0]["id"]
        uname=d[0]["name"]

        print("Values",d)
        print("Id ",d[0]["id"])
        if(not d):
            messages.warning(request,"Invalid Credentials")
            return render(request,"login.html")
        else:
            request.session["user_id"]=id
            request.session["User_name"]=uname
            return render(request,"customerHome.html",{"name":uname})

  

def modifyAction(request):
        uid=request.GET["id"]
        st=int(request.GET["status"])
        print("User id ",uid)
        if(st == 1):
           print("Edit Works")
           d=customerModel.objects.filter(id=uid)
           return render (request,"customerEdit.html",{"rec":d})
        else:
            #print("Delete Click ")
            d=customerModel.objects.filter(id=uid).delete()
            c=customerModel.objects.all()
            if(not c):
                messages.error(request,"No Record Found ")
                return render(request,"Allcustomerlisty.html")
            else:
                return render(request,"Allcustomerlisty.html",
                            {"record":c})
def customerEditAction(request):
    uid=request.POST["id"]
    d=customerModel.objects.get(id=uid)
    f=customerForm(request.POST,instance=d)
    if(f.is_valid()):
        f.save()
    else:
        messages.error(request,"Error While Updating")
    c=customerModel.objects.all()
    return render(request,"AllcustomerListy.html",
                      {"record":c})

def BuyDogs(request):
    c=dogModel.objects.all()
    if(not c):
        messages.error(request,"No Record Found ")
        return render(request,"Buydogs.html")
    else:
        return render(request,"Allcustomerlisty.html",
                      {"record":c})