from django.urls import path

from . import views

urlpatterns = [

    path('user-list/<int:department_id>/', views.user_list_by_department, name='user_list_by_department'),
    path('user/<int:user_id>/', views.user_detail, name='user_detail'),

]