from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages

# Create your views here.
from .models import *
from .forms import *
#from validation.EmailValidation import *

def signUp_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        response = HttpResponseRedirect("../signUp")
        response.delete_cookie('user')
        return response
    if request.method == "POST":
        signUp = SignUpForm(request.POST)
        if signUp.is_valid():
            signUp.save()
            return HttpResponseRedirect("../login")
        else:
            messages.error(request,"Error")
    signUp = SignUpForm()
    return render(request,"signUpForm.html",{'signUp' : signUp})

def login_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        response = HttpResponseRedirect("../welcome")
        response.delete_cookie('user')
        return response
    if request.method == "POST":
        login = LoginForm(request.POST)
        if login.is_valid():
            email = login.cleaned_data['email']
            pwd = login.cleaned_data['password']
            validUser = User.objects.filter(email = email).filter(password = pwd)
            if len(validUser) == 1:
                #need session to check from now that user have logged in
                response = HttpResponseRedirect("../welcome")
                response.set_cookie('user',email)
                return response
    login = LoginForm()
    return render(request,"login.html",{'login' : login})

def home_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        return render(request,"application.html",{'email':request.COOKIES["user"]})
    else:
        return HttpResponseRedirect("../login")
    #return HttpResponse("<a href = \"../welcome\">Welcome to GroceryList Editor Version 1.0  </a>")

def title_view(request,*args,**kwargs):
    if "user" in request.COOKIES:
        groceryList = GroceryListForm()
        email = request.COOKIES["user"]
        user = User.objects.filter(email = email).first()
        titles = UsersAndGrocery.objects.filter(userId = user).all()
        if request.method == "POST":
            groceryList = GroceryListForm(request.POST)
            if groceryList.is_valid():
                GroceryList.objects.create(title = groceryList.cleaned_data['title'],email = email)
                groceryList_id = GroceryList.objects.filter(title = groceryList.cleaned_data['title']).filter(email = email).first()
                UsersAndGrocery.objects.create(groceryListId = groceryList_id,userId = user,canEdit = True,canView = True,isAdmin = True,isCreator = True)

                #return render(request,"createGroceryListTitle.html",{'titles' : titles,'groceryList':groceryList})
        return render(request,"createGroceryListTitle.html",{'titles' : titles,'groceryList':groceryList})

    else:
        return HttpResponseRedirect("../welcome")

def groceryContent_view(request,id):
    if "user" in request.COOKIES:
        grocerListContentForm = GrocerListContentForm()
        email = request.COOKIES["user"]
        user = User.objects.filter(email = email).first()
        titles = UsersAndGrocery.objects.filter(userId = user).all()
        grocery_id = GroceryList.objects.get(id = id)
        if request.method == "POST":
            grocerListContentForm = GrocerListContentForm(request.POST)
            if grocerListContentForm.is_valid():
                GrocerListContent.objects.create(item = grocerListContentForm.cleaned_data['item'],groceryListId = grocery_id )

        contents = GrocerListContent.objects.filter(groceryListId = grocery_id).all()
        if len(contents) == 0 :
            contents = None
        grocerListContentForm = GrocerListContentForm()
        return render(request,"groceryContent.html",{'titles':titles,'id':id,'grocerListContentForm':grocerListContentForm,'contents':contents,'glist':grocery_id})
    else:
        return HttpResponseRedirect("../welcome")

def deleteTitle_view(request,id):
    r = GroceryList.objects.get(id = id)
    r.delete()

    return HttpResponseRedirect('../../createTitle')

def deleteContent_view(request,id):
    r = GrocerListContent.objects.get(id = id)
    groceryList_id = r.groceryListId.id
    r.delete()
    return HttpResponseRedirect('../../groceryTitle/'+str(groceryList_id))

def logout_view(request,*args,**kwargs):
    response = HttpResponseRedirect("../welcome")
    response.delete_cookie('user')
    return response
