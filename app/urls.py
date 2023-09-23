from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.home),
    path('', views.home.as_view(),name="home"),
    # path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('topwear/', views.top_wear, name='topwear'),
    path('topwear/<slug:data>', views.top_wear, name='topweardata'),
    path('bottomwear/', views.bottom_wear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottom_wear, name='bottomweardata'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
