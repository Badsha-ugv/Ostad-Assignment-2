from django.urls import path 
from . import views 


urlpatterns = [
    path('',views.EmployeeView.as_view(),name='home'),
    path('<int:pk>/',views.EmployeeView.as_view(),name='detail'),
    path('add-employee/',views.add_employee, name='add_employee'),

    path('<int:pk>/update/',views.update_employee,name='update'),
    path('<int:pk>/delete/',views.delete_employee,name='delete'),

    
    
]