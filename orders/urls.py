from django.urls import path

from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("login", views.login_view, name="login"),
	path("logout", views.logout_view, name="logout"),
	path("signin", views.to_sign, name ="signin"),
	path("signed", views.signin_view, name="signed"),
	#path("car", views.car_view, name="car"),
	path("inside/<regular_name>/<regular_price>",views.additem,name="additem"),
	path("inside/<int:id>",views.deleteitem,name="deleteitem"),
	path("insidel/<regular_name>/<regular_price>",views.additemlarge,name="additemlarge"),
	path("insides/<regular_name>/<regular_price>",views.additemsmall,name="additemsmall"),
	path("confirmed",views.confirmedorder,name="confirmedorder"),
	path("seeorder",views.seeorder,name="seeorder"),
	path("insidet/<regular_name>",views.additemtopping,name="additemtopping")
]
