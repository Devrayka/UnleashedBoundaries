from django.urls import path
from .import views

urlpatterns=[
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path('contact',views.contact,name="contact"),
    path('signup',views.signup,name="signup"),
    path('login',views.login,name="login"),
    path('fetchsignupdata',views.fetchsignupdata,name="fetchsignupdata"),
    path('checklogindata',views.checklogindata, name='checklogindata'),
    path('turf', views.turf, name='turf'),
    path('logout', views.logout, name='logout'),
    path('booking/<int:id>', views.booking, name='booking'),
    path('fetchturfdata',views.fetchturfdata, name='fetchturfdata'),
    path('product',views.product, name='product'),
    path('singleturf/<int:tid>',views.singleturf, name='singleturf'),
    path('singleproduct/<int:pid>',views.singleproduct, name='singleproduct'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('cart', views.cart, name='cart'),
    path('fetchturfdata', views.fetchturfdata, name='fetchturfdata'),
    path('booked', views.booked, name='booked'),
    path('increaseitem/<int:id>', views.increaseitem, name="increaseitem"),
    path('decreaseitem/<int:id>', views.decreaseitem, name="decreaseitem"),
    path('deleteitem/<int:id>', views.deleteitem, name='deleteitem'),
    path('deleteturf/<int:id>', views.deleteturf, name='deleteturf'),
    path('showorders',views.showorders,name="showorders"),
    path('placeorderproduct',views.placeorderproduct,name="placeorderproduct"),
    path('placeorderpage',views.placeorderpage,name="placeorderpage"),
    path('cancelorder/<int:id>', views.cancelorder, name="cancelorder"),
    path('singleorder/<int:id>', views.singleorder, name="singleorder"),
    path('findproduct', views.findproduct, name="findproduct"),
    path('feedback', views.feedback, name="feedback"),
    path("forgotpassword.html", views.forgotpasswordpage, name="forgotpassword.html"),
    path("forgotpassword", views.forgotpassword, name="forgotpassword"),
]