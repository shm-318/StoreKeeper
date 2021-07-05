from django.conf.urls import url,include
from django.urls import path
from . import views 
#from storekeeper import newapp

app_name='newapp'
urlpatterns = [
    url(r'^$',views.user_login,name='login'),
    url(r'^logout/',views.user_logout,name='logout'),
    url(r'^list/$',views.list,name='list'),
    url(r'^about/',views.about,name='about'),
    url(r'^contact/',views.contact,name='contact'),
    url(r'^register/$',views.register,name='register'),
    path('update/<str:pk>',views.updatelist,name='update'),
    path('delete/<str:pk>',views.deletelist,name='delete')
]
