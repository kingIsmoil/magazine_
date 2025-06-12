from rest_framework.urls import path
from .views import *
urlpatterns = [
    path('',CategoryListView.as_view()),
    path('create/',CategoryCreateView.as_view()),
    path('update/<int:id>',CategoryCreateView.as_view()),
    path('delete/<int:id>',CategoryCreateView.as_view()),
    
]