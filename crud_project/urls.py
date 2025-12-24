"""
URL configuration for crud_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from crud_app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
     path('admin/', admin.site.urls),
     path("",views.show,name='home'),
     path('recycle/', views.recycle_bin, name='recycle_bin'),
     path("form/",views.form,name='form'),
     path("delete/<int:id>",views.delete_data,name="delete_data"),
     path("restore/<int:id>",views.restore_data,name="restore_data"),
     path("edit/<int:id>",views.edit,name="edit"),     
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
