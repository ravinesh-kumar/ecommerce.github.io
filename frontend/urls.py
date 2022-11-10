from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.login,name ="login"),
    path('index',views.index,name ="index"),
    path('save1',views.save1,name ="save1"),
    path('save2',views.save2,name ="save2"),
    path('contact',views.contact,name ="contact"),
    path('save3',views.save3,name ="save3"),
    path('thanks',views.thanks,name ="thanks")
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
