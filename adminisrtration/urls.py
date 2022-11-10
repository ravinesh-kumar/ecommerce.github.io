from django.shortcuts import render
from django.contrib import admin
from django.urls import path,include
from.import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('logintable',views.logintable,name ="logintable"),
    path('contacttable',views.contacttable,name ="contacttable"),
    path('productupload',views.productupload,name ="productupload"),
    path('upload',views.upload,name ="upload"),
    path('producttable',views.producttable,name ="producttable"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

