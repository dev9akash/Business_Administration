from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='project-home'),
    path('stock/', views.stock, name='stock'),
    path('indent/', views.indent, name='requirement'),
    path('billing/', views.billing, name='project_billing')
]