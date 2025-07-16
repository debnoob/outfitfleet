from django.shortcuts import render, redirect
from django.contrib.auth import logout as django_logout  # Imported as django_logout
from django.contrib import messages


from datetime import datetime, timedelta
from django.shortcuts import render, redirect,get_object_or_404, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from admin_panel.models import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login as django_login
# from .serializers import ProductSerializer, LoginSerializer, AssignSerializer, AssetSerializer, UserSerializer, BarcodeUpdateSerializer, RequestAssetSerializer, SubcategorySerializer, AllocationSerializer
from django.utils import timezone
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder
from geopy.geocoders import Nominatim
from django.db.models import Count
import json
from datetime import date
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Shop
from .models import Manufacturer
from .models import Category
from .serializers import SignupUserSerializer
from .models import SignupUser


# Create your views here.

@login_required(login_url='signin')
def index(request):
    return render(request, 'index.html')

def signin(request):
    if request.user.is_authenticated:
        return redirect('index')  # Redirect if already logged in

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)  # Ensure username == email

        if user is not None:
            login(request, user)
            return redirect('index')  # Redirect to the dashboard or homepage
        else:
            return render(request, "signin.html", {"e_msg": "Invalid email or password"})

    return render(request, 'signin.html')

def logout_view(request):
    django_logout(request)  # Explicitly call the imported alias
    return redirect('signin')

def productlist(request):
    # filter = request.GET.get('filter')
    # print(filter)
    # if filter:  # Check if a filter is provided
    #     # Filter assets where the assigned user's station matches the filter value
    #     assets = Asset.objects.filter(assign_to__station__station_name=filter)
    #     print(assets)
    # else:
    #      assets = Asset.objects.all()
    #     # If no filter is provided, fetch all assets
     
    
    # return render(request, 'productlist.html', {'asset': assets})
    return render(request,"productlist.html")
def category_list(request):
    categories = Category.objects.all()
    return render(request, "page-list-category.html", {"categories": categories})


def add_product(request):
    return render(request,"page-add-product.html")
def add_category(request):
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_code = request.POST.get('category_code')
        if category_name and category_code:
            Category.objects.create(category_name=category_name, category_code=category_code)
            messages.success(request, "Category added successfully!")
            return redirect('page-list-category')
        else:
            messages.error(request, "All fields are required.")
    return render(request, "page-add-category.html")

def delete_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    category.delete()
    messages.success(request, "Category deleted successfully!")
    return redirect('page-list-category')

def edit_category(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category_name = request.POST.get('category_name')
        category_code = request.POST.get('category_code')
        if category_name and category_code:
            category.category_name = category_name
            category.category_code = category_code
            category.save()
            messages.success(request, "Category updated successfully!")
            return redirect('page-list-category')
        else:
            messages.error(request, "All fields are required.")
    return render(request, "page-edit-category.html", {"category": category})

def list_sale(request):
    return render(request,"page-list-sale.html")
def add_sale(request):
    return render(request,"page-add-sale.html")
def list_purchase(request):
    return render(request,"page-list-purchase.html")
def add_purchase(request):
    return render(request,"page-add-purchase.html")
def list_returns(request):
    return render(request,"page-list-returns.html")
def add_returns(request):
    return render(request,"page-add-return.html")
def list_customers(request):
    shops = Shop.objects.all()  # Fetch all shop records
    return render(request,"page-list-customers.html", {'shops': shops})
def add_customers(request):
    if request.method == 'POST':
        shop_name = request.POST['shop_name']
        owner_name = request.POST['owner_name']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        gst_number = request.POST.get('gst_number')
        business_type = request.POST['business_type']
        country = request.POST['country']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        shop_logo = request.FILES.get('shop_logo')

        shop = Shop(
            shop_name=shop_name,
            owner_name=owner_name,
            email=email,
            phone_number=phone_number,
            gst_number=gst_number,
            business_type=business_type,
            country=country,
            state=state,
            city=city,
            address=address,
            shop_logo=shop_logo
        )
        shop.save()
        

        messages.success(request, 'Shop registered successfully!')
        return redirect('page-list-customers')
    return render(request,"page-add-customers.html")



def list_users(request):
    return render(request,"page-list-users.html")
def add_users(request):
    return render(request,"page-add-users.html")
def list_suppliers(request):
    manufacturers = Manufacturer.objects.all()
    return render(request,"page-list-suppliers.html", {'manufacturers': manufacturers})
    
    return render(request,"page-list-suppliers.html")


def add_supplier(request):
    if request.method == "POST":
        # Handle form submission
        company_name = request.POST.get('company_name')
        contact_name = request.POST.get('contact_name')
        email = request.POST.get('email')
        phone_number = request.POST.get('phone_number')
        gst_number = request.POST.get('gst_number')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        country = request.POST.get('country')
        website = request.POST.get('website')
        product_categories = request.POST.get('product_categories')
        password = request.POST.get('password')
        terms_accepted = request.POST.get('terms') == 'on'  # Convert the "on" string to True/False

        # Handle file upload (logo)
        logo = request.FILES.get('logo')

        # Create and save Manufacturer object
        manufacturer = Manufacturer(
            company_name=company_name,
            contact_name=contact_name,
            email=email,
            phone_number=phone_number,
            gst_number=gst_number,
            address=address,
            city=city,
            state=state,
            country=country,
            website=website,
            product_categories=product_categories,
            logo=logo,
            password=password,  # You should hash the password before saving it
            terms_accepted=terms_accepted
        )
        
        manufacturer.save()  # Save the new manufacturer to the database

        # Add success message
        messages.success(request, f"{company_name} has been successfully registered.")

        return redirect('page-list-suppliers')  # Redirect to a success page or list of suppliers

    else:
        # If GET request, render the form
        return render(request, "page-add-supplier.html")


@api_view(['POST'])
def signup_api(request):
    serializer = SignupUserSerializer(data=request.data)
    if serializer.is_valid():
        # Create SignupUser instance
        SignupUser.objects.create(
            username=serializer.validated_data['username'],
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']  # In production, hash this password
        )
        return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def page_report(request):
    return render(request,"page-report.html")
def user_profile(request):
    return render(request,"app/user-profile.html")
def user_add(request):
    return render(request,"app/user-add.html")
def user_list(request):
    return render(request,"app/user-list.html")
