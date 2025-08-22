from django.urls import path
from .views import *

urlpatterns = [
    path('items/', ItemView.as_view(), name='item-list'),
    path('menu/',views.menu_list,name="menu_list"),
    path('feedback/',views.feedback_submit,name="feedback_submit"),
    path('feedback/list,',views.feedback_list,name="feedback_list")
]