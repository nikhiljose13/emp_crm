"""employeecrm URL Configuration

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
from django.urls import path,include
from crm import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    #path('employee/add/',views.EmployeeCreateView.as_view(),name="emp-add"),
    
    path('employee/add/',views.EmployeeCreateView.as_view(),name="emp-add"),
    path('employee/all/',views.EmployeeListView.as_view(),name="emp-list"),
    path('employee/<int:pk>',views.EmployeeDetailView.as_view(),name="emp-details"),
    path('employee/<int:pk>/remove/',views.EmployeeDeleteView.as_view(),name="emp-delete"),
    path('employee/<int:pk>/change/',views.EmployeeUpdateView.as_view(),name="emp-edit"),
    path('auth/signup/',views.SignupView.as_view(),name="emp-signup"),
    path('',views.SigninView.as_view(),name="emp-signin"),
    path('auth/signout/',views.SingOutView.as_view(),name="emp-signout"),
    path("api/",include("api.urls"))
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
