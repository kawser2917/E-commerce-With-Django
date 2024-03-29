from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, myPasswordChangeForm, myPasswordResetForm,mySetPasswordForm
urlpatterns = [
    # path('', views.home),
    path('', views.home.as_view(),name="home"),
    # path('product-detail/<int:pk>', views.product_detail, name='product-detail'),
    path('product-detail/<int:pk>', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path("cart/",views.show_cart,name="cart"),
    path("pluscart/",views.plus_cart,name="pluscart"),
    path("minuscart/",views.minus_cart,name="minuscart"),
    path("removecart/",views.remove_cart,name="removecart"),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('topwear/', views.top_wear, name='topwear'),
    path('topwear/<slug:data>', views.top_wear, name='topweardata'),
    path('bottomwear/', views.bottom_wear, name='bottomwear'),
    path('bottomwear/<slug:data>', views.bottom_wear, name='bottomweardata'),
    # Login- Authentication
    path("accounts/login/",auth_views.LoginView.as_view(template_name = "app/login.html", authentication_form = LoginForm),name="login"),
    # Logout- Authentication
    path('logout/', auth_views.LogoutView.as_view(next_page ='login'),name="logout"),
    # PasswordChage - Authentication
    path('passwordchange/', auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html", form_class=myPasswordChangeForm, success_url='/passwordchangedone/'),name="changepassword"),
    # After changing pass it will rediret to this url and have to create and passwordchangedone.html file
    path("passwordchangedone/", auth_views.PasswordChangeDoneView.as_view(template_name='app/passwordchangedone.html'),name="passwordchangedone"),
    # Password reset- This is 1st step. After that it will redirect to password-reset/done/ url
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name="app/password_reset.html", form_class=myPasswordResetForm), name="password_reset"),
    # 2nd step of password reset
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"), name="password_reset_done"),
    # 3rd step: Here we need to make a form again
    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html", form_class=mySetPasswordForm), name="password_reset_confirm"),

    # 4th step
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complete.html"), name="password_reset_complete"),



    path('registration/', views.CustomerRegistration.as_view(), name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
