import requests
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required, user_passes_test
from app.models import Contact,Medicines,ProductItems,MyOrders,Sell,FarmerProfile,customerProfile
import speech_recognition as sr
from django.http import JsonResponse
import json
import math
user=None
Farmer=None
is_loggedin=False
def Home(request):
    mymed=Medicines.objects.all()
    myprod=ProductItems.objects.all()
    context={"mymed":mymed,"myprod":myprod}
    return render(request, "Home.html",context)


def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        phon=request.POST.get("num")
        desc=request.POST.get("desc")
        query=Contact(name=name,email=email,phoneno=phon,desc=desc)
        query.save()
        messages.info(request,f"Thank You. Will Get back you soon {name}")

    return render(request, "contact.html")


def About(request):
    return render(request, "About.html")

def get_client_ip(request):
    # Get the client's IP address from the request object
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    # Mock IP for testing purposes
    if ip == '127.0.0.1' or ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
        ip = '8.8.8.8'  # Example public IP for testing, replace with your actual IP if needed
    return ip
def HandleSignup(request):
    # logic
    if request.method == "POST":

        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        location = request.POST.get("location")
        # print(uname,email,fname,lname,pass1,cpass)
        # ip_address = get_client_ip(request)
    
        # response = requests.get(f"http://ip-api.com/json/{ip_address}")
        # location_data = response.json()
    
        # if location_data['status'] == 'fail':
        #  location_data = {
        #     'query': ip_address,
        #     'message': location_data['message'],
        #     'status': location_data['status']
        # }
        url = "https://ip-geo-location.p.rapidapi.com/ip/check"

        querystring = {"format":"json"}

        headers = {
	       "X-RapidAPI-Key": "7c8882695amsh4b0ad0c6a6e06c5p13d11cjsnc2d71c2ed413",
	       "X-RapidAPI-Host": "ip-geo-location.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
       
        data=response.json()
        print(data['location']['latitude'])
        lat=data['location']['latitude']
        long=data['location']['longitude']
# check wheater user exists or not
        if(pass1 != cpass):
            messages.warning(request,"Password is'nt Matching")
            return redirect("/signup")
        customer=customerProfile.objects.all()
        # Check if username or email already exist
        
        for i in customer:
          if i.username==uname:
            messages.warning(request, "Username is already taken")
            return redirect("/signup")
          if i.email==email:
            messages.warning(request, "Email is already registered")
            return redirect("/signup")
        myuser = User.objects.create_user(email, uname, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        customerinsert = customerProfile(username=uname, email=email, firstname=fname, lastname=lname, password=pass1, location=location,latitude=lat,longitude=long)
        customerinsert.save()
        messages.success(request,"Signup Success")
        return redirect("/login")

    return render(request, "signup.html")

def farmerSignup(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        pass1 = request.POST.get("pass1")
        cpass = request.POST.get("pass2")
        location = request.POST.get("location")

        # Check if passwords match
        if pass1 != cpass:
            messages.warning(request, "Passwords do not match")
            return redirect("/farmer-signup")
        farmer=FarmerProfile.objects.all()
        myuser = User.objects.create_user(email, uname, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()
        # Check if username or email already exist
        
        for i in farmer:
          if i.username==uname:
            messages.warning(request, "Username is already taken")
            return redirect("/farmer-signup")
          if i.email==email:
            messages.warning(request, "Email is already registered")
            return redirect("/farmer-signup")

        # Create User object
        # myuser = User.objects.create_user(email, uname, pass1)
        # myuser.first_name = fname
        # myuser.last_name = lname
        # myuser.save()

        # Create FarmerProfile object
        farmerinsert = FarmerProfile(username=uname, email=email, firstname=fname, lastname=lname, password=pass1, location=location)
        farmerinsert.save()

        messages.success(request, "Signup successful")
        return redirect("/farmer")

    return render(request, "farmer-signup.html")
def HandleLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        # print(email,pass1)
        # myuser = authenticate(username=email, password=pass1)
     
        # users=customerProfile.objects.all()
        myuser = authenticate(username=email, password=pass1)
        global user
        user = customerProfile.objects.get(email=email)
        user.status=True
        user.save()
        print(user.status)
        # myuser = authenticate(username=email, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.info(request,"Login Successful")
            return redirect("/")

        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login")
        # for i in users:
        #     if i.email==email and i.password==pass1 :
        #          if myuser is not None:
        #             login(request, myuser)
        #             request.session['is_loggedin'] = True
        #             messages.info(request,"Login Successful")
                
        #             return redirect("/")
        #     else:
        #         messages.error(request,"Invalid Credentials")
                # return redirect("/login")

    return render(request, "login.html")

def farmerLogin(request):
    if request.method == "POST":
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        # print(email,pass1)
        # users=FarmerProfile.objects.all()
        # myuser = authenticate(username=email, password=pass1)
        myuser = authenticate(username=email, password=pass1)
        global Farmer
        Farmer= FarmerProfile.objects.get(email=email)
        Farmer.status=True
        # myuser = authenticate(username=email, password=pass1)
        if myuser is not None:
            login(request, myuser)
            messages.info(request,"Login Successful")
            return redirect("/")

        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login")

        # if myuser is not None:
        #     login(request, myuser)
        #     messages.info(request,"Login Successful")
        #     return redirect("/")

        

    return render(request, "farmer.html")

def HandleLogout(request):
    
    user.status=False
    user.save()
    logout(request)
    messages.warning(request,"Logout")
    return redirect("/login")


def medicines(request):
    mymed=Medicines.objects.all()
    context={"mymed":mymed}
    # print(context)
    return render(request,"medicines.html",context)

from itertools import groupby
from django.db.models import Count

def products(request):
    # location=
    products=Sell.objects.all()
    
    
   
    categories = Sell.objects.values('sell_category').annotate(total=Count('sell_category'))
    grouped_products = {}

    for category in categories:
        products = Sell.objects.filter(sell_category=category['sell_category'])
        grouped_products[category['sell_category']] = products

    context = {"grouped_products": grouped_products}
    return render(request, "products.html", context)


def myorders(request):
    # users=FarmerProfile.objects.all()
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login to place the Order....")
        return redirect("/login")
    
    # if not request.session.get('is_loggedin', False):
    #     messages.warning(request,"Please Login to place the Order....")
    #     return redirect("/login")
    
    print(request.user)
    mymed=Sell.objects.all()
    myprod=ProductItems.objects.all()
    
    # i am writing a logic to get the user details orders
    current_user=request.user.username
    print(current_user)
    # i am fetching the data from table MyOrders based on emailid
    items=MyOrders.objects.filter(email=current_user)
    # print(items)
    context={"myprod":myprod,"mymed":mymed,"items":items}
    if request.method =="POST":
        name=request.POST.get("name")
        print(name)
        email=request.POST.get("email")
        item=request.POST.get("items")
        quan=request.POST.get("quantity")
        address=request.POST.get("address")
        phone=request.POST.get("num")
        print(name,email,item,quan,address,phone)
        
        price=""
        for i in mymed:
            if item==i.sell_name:
                price=i.sell_price

            pass
        for i in myprod:
            if i.prod_name==item:
                price=i.prod_price

            pass

        newPrice=int(price)*int(quan)
        myquery=MyOrders(name=name,email=email,items=item,address=address,quantity=quan,price=newPrice,phone_num=phone)
        myquery.save()
        messages.info(request,f"Order is Successfull")
        return redirect("/orders")

    
    return render(request,"orders.html",context)

# def search(request):
#     query=request.GET["getdata"]
#     print(query)

#     dist=[]
#     users=customerProfile.objects.all()
#     x=users['latitude']-products['latitude']
#     x=x*x
#     y=users['longitude']-products['longitude']
#     y=y*y
#     dist.append(math.sqrt(x+y))
#     allPostsMedicines=Medicines.objects.filter(medicine_name__icontains=query)
#     allPostsProducts=ProductItems.objects.filter(prod_name__icontains=query)
#     allPosts=allPostsMedicines.union(allPostsProducts)
    
#     return render(request,"search.html",{"Med":allPostsMedicines,"Prod":allPostsProducts,"allItems":allPosts})

def search(request):
    query = request.GET.get("getdata", "")
    query=query.split()
    
    # Assuming latitude and longitude are passed in the request
    latitude = request.GET.get("latitude", 0)
    longitude = request.GET.get("longitude", 0)
    print(query[0],latitude,longitude)
    try:
        latitude = float(latitude)
        longitude = float(longitude)
    except ValueError:
        latitude = 0
        longitude = 0
    
    # Filter products based on the search query
    allPostsProducts = Sell.objects.filter(sell_name__icontains= query[0])
    
    # Calculate distance for each product and sort by distance
    products_with_distance = []
    for post in allPostsProducts:
        post_lat = post.latitude
        post_long = post.longitude
        
        if post_lat is not None and post_long is not None:
            x = (post_lat - latitude) ** 2
            y = (post_long - longitude) ** 2
            
            distance = math.sqrt(x + y)
            products_with_distance.append((distance, post))
    
    # Sort products by distance
    products_with_distance.sort(key=lambda x: x[0])
    
    # Extract sorted products
    sorted_products = [product for distance, product in products_with_distance]
    
    context = {
        "Prod": sorted_products,
        "allItems": sorted_products,
    }
    
    return render(request, "search.html", context)

def deleteOrder(request,id):
    print(id)
    query=MyOrders.objects.get(id=id)
    query.delete()
    messages.success(request,"Order Cancelled Successfully..")
    return redirect("/orders")
# @login_required
# @user_passes_test(lambda user: user.groups.filter(name='customers').exists())
def sell(request):
    if request.method == "POST":
        category = request.POST.get("sell_category")
        name = request.POST.get("sell_name")
        image = request.FILES.get("sell_image")  # Use request.FILES for file inputs
        price = request.POST.get("sell_price")
        description = request.POST.get("sell_description")
        farmer=FarmerProfile.objects.all()
        # location=''
        # user=''
        # for i in farmer:
        #     if request.user==i.username:
        #         location=i.location
        #         user=i.username
        url = "https://ip-geo-location.p.rapidapi.com/ip/check"

        querystring = {"format":"json"}

        headers = {
	       "X-RapidAPI-Key": "7c8882695amsh4b0ad0c6a6e06c5p13d11cjsnc2d71c2ed413",
	       "X-RapidAPI-Host": "ip-geo-location.p.rapidapi.com"
        }
        
        response = requests.get(url, headers=headers, params=querystring)
       
        data=response.json()
        print(data['location']['latitude'])
        lat=data['location']['latitude']
        long=data['location']['longitude']
        
        # Assuming 'sell_category' is a required field
        if category:
            # Assuming 'sell_price' needs to be converted to an integer
            try:
                price = int(price)
            except ValueError:
                messages.error(request, "Invalid price format. Please provide a valid number.")
                return redirect("sell")  # Redirect to the sell page on error
            
            # Create a Sell instance and save it
            myquery = Sell(
                sell_category=category,
                sell_name=name,
                sell_image=image,
                sell_price=price,
                sell_description=description,
                latitude=lat,
                longitude=long
                # ,
                # sell_location=location,
                # sell_by=user

            )
            myquery.save()
            messages.success(request, "Sell details saved successfully!")
            return redirect("/")  # Redirect to home page after successful save
        
        else:
            # Handle the case where 'sell_category' is not provided
            messages.error(request, "Sell category is required.")
            return redirect("sell")  # Redirect to the sell page
            
    return render(request, "sell.html")


#voicerecorder
def voice_recognition(request):
    return render(request, 'voice_recognition.html')

def recognize_speech(request):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        audio = r.listen(source, timeout=2)  # Adjust the timeout as needed

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en")

    except Exception as e:
        print(f"Error: {str(e)}")
        return JsonResponse({'text': 'Error'})

    query = str(query).lower()
    print(query)
    # print(Sell.objects.filter(sell_name__icontains= query))
    return JsonResponse({'text': query})

from googletrans import Translator,LANGUAGES
from deep_translator import GoogleTranslator

def hindi_recognition(request):
    def Listen():
        r = sr.Recognizer()

        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 4)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="hi")
        except Exception as e:
            print(f"Error: {e}")
            return "Error!!"

        query = str(query).lower()
        print(query)
        return query

    def translateHindToEng(text):
      try:
        translation = GoogleTranslator(source='hi', target='en').translate(text)
        print(f"You: {translation}.")
        return translation
      except Exception as e:
        print("An error occurred during translation. Please try again later.")
        print(f"Error details: {e}")
        return None
    def MicExecution():
        query = Listen()
        if query != "Error!!":
            result = translateHindToEng(query)
            # print(Sell.objects.filter(sell_name__icontains= result))
            return result
        else:
            return "Error occurred during speech recognition."

    return JsonResponse({'text': MicExecution()})
