from django.contrib import admin
from django.urls import path,include
from.import views
urlpatterns = [
    path('',views.home,name='home'),
    path('loginpg',views.loginpg,name='loginpg'),
    path('admpg',views.admpg,name='admpg'),
    path('login1',views.login1,name='login1'),
    path('logout',views.logout,name='logout'),
    path('addc',views.addc,name='addc'),
    path('addcdb',views.addcdb,name='addcdb'),
    path('addp',views.addp,name='addp'),
    path('addpdb',views.addpdb,name='addpdb'),
    path('show',views.show,name='show'),
    path('deletepage/<int:pk>',views.deletepage,name='deletepage'),
]