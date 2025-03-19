from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.user_form, name='user_form'),
    path('data/', views.user_data, name='user_data'),
]