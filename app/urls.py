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
    path('productDetailPage/<id>', views.product_detail, name='product_detail'),
    path('addToCart/<id>', views.add_to_cart, name='add_to_cart'),
    path('viewCart/', views.viewCart, name='viewCart'),
    path('add_feedback/<id>', views.add_feedback, name='add_feedback'),
    path('userProfile/<str:email>', views.viewUserProfile, name='view_user_profile'),
    path('userProfile/edit/<str:email>', views.editUserProfile, name='edit_user_profile'),


]
