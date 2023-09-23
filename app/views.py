from django.shortcuts import render
from django.views import View
from .models import Customer,Cart,OrderedPlaced,Product

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
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

def change_password(request):
 return render(request, 'app/changepassword.html')

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

def customerregistration(request):
 return render(request, 'app/customerregistration.html')

def checkout(request):
 return render(request, 'app/checkout.html')
