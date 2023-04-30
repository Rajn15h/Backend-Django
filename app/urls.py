from app import views
from django.urls import path

urlpatterns = [
    
    path('',views.list),
    path('add/',views.addlist),
    path('listitem/<int:pk>/',views.listitem),
    path('update/<int:pk>/', views.update_items),
    path('delete/<int:pk>/',views.delete)
]
