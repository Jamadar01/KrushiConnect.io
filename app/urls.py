from app import views
from django.urls import path,include

urlpatterns = [
    path("",views.Home,name="Home"),
    path('about',views.About,name="About"),
    path('contact',views.contact,name="contact"),
    path('signup',views.HandleSignup,name="HandleSignup"),
    path('farmer-signup',views.farmerSignup,name="farmerSignup"),
    path('login',views.HandleLogin,name="HandleLogin"),
    path('farmer',views.farmerLogin,name="farmerLogin"),
    path('logout',views.HandleLogout,name="HandleLogout"),
    path("medicines",views.medicines,name="medicines"),
    path("products",views.products,name="products"),
    path("orders",views.myorders,name="orders"),
    path("search",views.search,name="search"),
    path('sell',views.sell,name="sell"),
    path('voice_recognition/', views.voice_recognition, name='voice_recognition'),
    path('recognize_speech/', views.recognize_speech, name='recognize_speech'),
    path('hindi/', views.hindi_recognition, name='hindi_recognition'),
    path("orders/<id>",views.deleteOrder,name="deleteOrder"),
    



]
