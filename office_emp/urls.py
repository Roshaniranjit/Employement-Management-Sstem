from django.urls import path
from .views import index,all_emp,add_emp,search_emp,remove_emp
urlpatterns = [
    path('',index ,name = 'index'),
    path('all_emp/',all_emp, name = 'all_emp-page'),
    path('add_emp/',add_emp, name = 'add_emp-page'),
    path('remove_emp/',remove_emp, name = 'remove_emp'),
    path('search_emp/',search_emp, name = 'search_emp'),
    

]
