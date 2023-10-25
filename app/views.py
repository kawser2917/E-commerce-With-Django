from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Cart,OrderedPlaced,Product
from .forms import *
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')
class home(View):
 def get(self,request):
  topwears = Product.objects.filter(category='TW')
  bottomwears = Product.objects.filter(category='BW')
  mobile = Product.objects.filter(category='M')
  return render(request, 'app/home.html', {"topwears":topwears, "bottomwears": bottomwears, "mobiles":mobile})

# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  return render(request,"app/productdetail.html",{"product":product})

def add_to_cart(request):
 user = request.user
 product_id = request.GET.get("prod_id")
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

def show_cart(request):
 user = request.user
 cart = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.0
 total_amount = 0.0
 cart_product =[p for p in Cart.objects.all() if p.user == user]
 if cart_product:
  for p in cart_product:
   tempamount =(p.quantity * p.product.discount_price)
   amount += tempamount
   total_amount = amount + shipping_amount
  return render(request,'app/addtocart.html',{"carts":cart,"amount":amount,"totalamount":total_amount})
 else:
  return render(request,'app/emptycart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def address(request):
 add = Customer.objects.filter(user = request.user)
 return render(request, 'app/address.html',{"add":add,"active":"btn-primary"})

def orders(request):
 return render(request, 'app/orders.html')

# def change_password(request):
#  return render(request, 'app/changepassword.html')

def mobile(request,data=None):
  if data == None:
   mobile = Product.objects.filter(category ="M")
  elif data == "Apple" or data == "Samsung" or data == "Realme" or data == "Oneplus":
   mobile = Product.objects.filter(category="M").filter(brand = data)
  elif data == "below":
   mobile = Product.objects.filter(category="M").filter(discount_price__lt =10000)
  elif data == "above":
   mobile = Product.objects.filter(category="M").filter(discount_price__gt =10000)
  return render(request, 'app/mobile.html',{"mobiles":mobile})

def top_wear(request,data = None):
 if data == None:
  topwear = Product.objects.filter(category ="TW")
 elif data == "Easy" or data == "Armani" or data == 'Top10' or data == "Richman":
  topwear = Product.objects.filter(category = "TW").filter(brand = data)
 return render(request,'app/topwear.html',{"topwears":topwear})
def bottom_wear(request,data=None):
 if data == None:
  bottomwear = Product.objects.filter(category = "BW")
 elif data == "Easy" or data == "Armani" or data == 'Top10' or data == "Richman":
  bottomwear = Product.objects.filter(category = "BW").filter(brand = data)
 return render(request,'app/bottomwear.html',{"bottomwears":bottomwear})

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')
class CustomerRegistration(View):
 def get(self,request):
  form = CustomerRegistrationForm()
  return render(request,'app/customerregistration.html',{"form":form})
 def post(self,request):
  form = CustomerRegistrationForm(request.POST)
  if form.is_valid():
   message = messages.success(request,"Congratulation! Ragistration Successful")
   form.save()
  return render(request,'app/customerregistration.html',{"form":form})



def checkout(request):
 return render(request, 'app/checkout.html')

class ProfileView(View):
 def get(self,request):
  form = CustomerProfileView
  return render(request,"app/profile.html",{"form":form,"active":"btn-primary"})
 
 def post(self,request):
  form = CustomerProfileView(request.POST)
  if form.is_valid():
   usr = request.user
   name = form.cleaned_data['name']
   locality = form.cleaned_data['locality']
   city = form.cleaned_data['city']
   state = form.cleaned_data['state']
   zipcode = form.cleaned_data['zipcode']
   reg = Customer(user=usr, name=name, locality=locality,city=city,state=state,zipcode=zipcode)
   reg.save()
   messages.success(request,"Congratulation!! Profile Updated Successfully")
  return render(request,'app/profile.html',{'form':form,"active":"btn-primary"})
