#Author : Jordan Montenegro

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import RegularPizza,SicilianPizza,Toppings,Pasta,Salads,DinnerPlatters,Subs,Order,Confirmed_order
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.db.models import Sum


from .forms import SignUpForm

# Create your views here.



#def car_view(request):
#	return render(request, "orders/login.html", {"message": "added to the car"})

def seeorder(request):
	context = {
        "orders": Confirmed_order.objects.filter(username=request.user)
	}
	print(context["orders"])
	return render(request, "orders/showorders.html", context)
	
	
def index(request):
    if not request.user.is_authenticated:
        return render(request, "orders/login.html", {"message": None})
    context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
	}
    return render(request, "orders/inside.html", context)
	
def to_sign(request):
	return render(request, "orders/signin.html")
	



def additem(request, regular_name,regular_price):
	print(request.user,regular_name,regular_price)
	#obj=Order.objects.all().aggregate(Sum('price'))
	
	regular_price=float(regular_price)
	f=Order(username=request.user,name=regular_name,price=regular_price)
	f.save()
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	#total=Order.objects.all().aggregate(Sum('price'))
	return render(request, "orders/inside.html", context)
	#return HttpResponseRedirect(reverse("index", args=(regular_name,)))
	
def additemsmall(request, regular_name,regular_price):
	print(request.user,regular_name,regular_price)
	#obj=Order.objects.all().aggregate(Sum('price'))
	
	regular_price=float(regular_price)
	f=Order(username=request.user,name=regular_name+" small ",price=regular_price)
	f.save()
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	#total=Order.objects.all().aggregate(Sum('price'))
	return render(request, "orders/inside.html", context)
	#return HttpResponseRedirect(reverse("index", args=(regular_name,)))
	
def additemtopping(request, regular_name):
	print(request.user,regular_name)
	#obj=Order.objects.all().aggregate(Sum('price'))
	
	#regular_price=float(regular_price)
	f=Order(username=request.user,name=regular_name + " topping ",price=0.00)
	f.save()
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	#total=Order.objects.all().aggregate(Sum('price'))
	return render(request, "orders/inside.html", context)
	#return HttpResponseRedirect(reverse("index", args=(regular_name,)))

def additemlarge(request, regular_name,regular_price):
	
	#obj=Order.objects.all().aggregate(Sum('price'))
	
	regular_price=float(regular_price)
	print(request.user,regular_name,regular_price)
	#regular_name=regular_name+" large"
	print(regular_name)
	f=Order(username=request.user,name=regular_name+" large ",price=regular_price)
	f.save()
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	#total=Order.objects.all().aggregate(Sum('price'))
	return render(request, "orders/inside.html", context)
	#return HttpResponseRedirect(reverse("index", args=(regular_name,)))

def deleteitem(request,id):
	Order.objects.filter(id=id).delete()
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	return render(request, "orders/inside.html", context)

def confirmedorder(request):
	orders1=Order.objects.filter(username=request.user)
	#print(orders)
	confirmedorder=""
	totalprice=0
	for f in orders1:
		#print(f.name)
		confirmedorder=confirmedorder+f.name+" -- "
		totalprice=totalprice+f.price
	#print(confirmedorder)
	#print(totalprice)
	#total1=Order.objects.all().aggregate(Sum('price'))
	
	f=Confirmed_order(username=request.user,orders=confirmedorder,total=str(totalprice))
	print(f.total)
	f.save()
	Order.objects.all().delete()
	
	context = {
        "user": request.user,
		"menu_regular_pizza": RegularPizza.objects.all(),
		"menu_sicilian_pizza": SicilianPizza.objects.all(), 
		"toppings": Toppings.objects.all(),
		"subs": Subs.objects.all(),
		"pasta": Pasta.objects.all(),
		"salads": Salads.objects.all(),
		"dinner_platters": DinnerPlatters.objects.all(),
		"order":Order.objects.all(),
		"total":Order.objects.all().aggregate(Sum('price'))
		#"total":obj["price__sum"]
		#"total":Order.objects.
		#"order":regular_name,
		#"price"
	}
	#total=Order.objects.all().aggregate(Sum('price'))
	return render(request, "orders/inside.html", context)
	

def signin_view(request):
	username1 = request.POST.get("username1",False)
	password = request.POST.get("password",False)
	firstname = request.POST.get("firstname",False)
	lastname = request.POST.get("lastname",False)
	confirm_password = request.POST.get("confirm_password",False)
	mail= request.POST.get("mail",False)
	
	
	print(username1)
	#return HttpResponse("THIS IS THE SIGNINVIEW")
	#if request.method == 'POST':
	#user=User.objects.create_user('juan', 'juan@thebeatles.com', 'johnpassword')
	if password==confirm_password and username1 != "" and password !="":
		user=User.objects.create_user(username1, mail, password)
		user.first_name=firstname
		user.last_name=lastname
		user.save()
	else :
		return render(request, "orders/signin.html", {"message": "Password does not match"})
	
	return HttpResponseRedirect(reverse("index"))
	
def login_view(request):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})
	