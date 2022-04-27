from django.urls import path
from . import views


urlpatterns = [
	path('register/', views.registerPage, name="register"),
	path('login/', views.loginPage, name="login"),  
	path('',views.home,name="home"),
	path('adminlogin/',views.admin,name="adminlogin"),
	path('addbook/',views.addbook,name="addbook"),
	path('updatebook/<pk>',views.updatebook,name="updatebook"),
	path('deletebook/<pk>',views.deletebook,name="deletebook"),
	path('logout/', views.logoutUser, name="logout"),
]