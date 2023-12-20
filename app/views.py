from django.shortcuts import render,redirect
from django.views import View
from .models import Customer,Cart,OrderedPlaced,Product
from .forms import *
from django.contrib import messages
from django.db.models import Q
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

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
@method_decorator(login_required,name="dispatch")
class ProductDetailView(View):
 def get(self,request,pk):
  product = Product.objects.get(pk=pk)
  item_already_in_cart = False
  if request.user.is_authenticated:
    item_already_in_cart = Cart.objects.filter(Q(product=product.id) & Q(user=request.user)).exists()
  return render(request,"app/productdetail.html",{"product":product, "item_already_in_cart":item_already_in_cart})

@login_required
def add_to_cart(request):
 user = request.user
 product_id = request.GET.get("prod_id")
 product = Product.objects.get(id=product_id)
 Cart(user=user,product=product).save()
 return redirect('/cart')

# Plus cart
def plus_cart(request):
 if request.method == "GET":
  prod_id = request.GET["prod_id"]
  print(prod_id)
  c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
  c.quantity +=1
  c.save()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount =(p.quantity * p.product.discount_price)
   amount += tempamount
  data ={
  "quantity": c.quantity,
  "amount": amount,
  "total_amount": amount + shipping_amount,
  }
  return JsonResponse(data)
# Minus cart
def minus_cart(request):
 if request.method == "GET":
  prod_id = request.GET["prod_id"]
  print(prod_id)
  c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
  c.quantity -=1
  c.save()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount =(p.quantity * p.product.discount_price)
   amount += tempamount
 
  data ={
  "quantity": c.quantity,
  "amount": amount,
  "total_amount": amount + shipping_amount,
  }
  return JsonResponse(data)
# Remove cart
def remove_cart(request):
 if request.method == "GET":
  prod_id = request.GET["prod_id"]
  print(prod_id)
  c = Cart.objects.get(Q(product = prod_id) & Q(user=request.user))
  c.delete()
  amount = 0.0
  shipping_amount = 70.0
  cart_product = [p for p in Cart.objects.all() if p.user == request.user]
  for p in cart_product:
   tempamount =(p.quantity * p.product.discount_price)
   amount += tempamount
  data ={
  "amount": amount,
  "total_amount": amount + shipping_amount,
  }
  return JsonResponse(data)
   
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

@login_required
def address(request):
 add = Customer.objects.filter(user = request.user)
 return render(request, 'app/address.html',{"add":add,"active":"btn-primary"})

@login_required
def orders(request):
 op = OrderedPlaced.objects.filter(user = request.user)
 return render(request, 'app/orders.html',{"order_placed":op})

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


@login_required
def checkout(request):
 user = request.user
 add = Customer.objects.filter(user=user)
 cart_items = Cart.objects.filter(user=user)
 amount = 0.0
 shipping_amount = 70.00
 total_amount = 0.0
 cart_product = [p for p in Cart.objects.all() if p.user == request.user]
 if cart_product:
  for p in cart_product:
    tempamount =(p.quantity * p.product.discount_price)
    amount += tempamount
  total_amount = amount + shipping_amount
 return render(request, 'app/checkout.html',{"add":add,"total_amount":total_amount,"cart_items":cart_items})
@login_required
def payment_done(request):
 user = request.user
 custid = request.GET.get("custid")
 customer = Customer.objects.get(id = custid)
 cart = Cart.objects.filter(user = user)
 for c in cart:
  OrderedPlaced(user = user, customer=customer, product = c.product,quantity = c.quantity).save()
  c.delete()
 return redirect('orders')

@method_decorator(login_required,name="dispatch")
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
