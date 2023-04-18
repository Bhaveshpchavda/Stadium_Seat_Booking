"""Stadium_Seat_Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from page.views import home_view,booking_view,dashboard_view,signup_view,login_view,signup,signin,signout
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_view, name='home'),
    path('booking/', booking_view, name='booking'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('login/', login_view, name='login'),    
    path('', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
    path('signin/', signin, name='signin'),
    path('signupval/', signup, name='signupval'),
    path('signout/',signout,name='signout'),

]
