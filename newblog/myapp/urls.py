from django.contrib import admin
from django.urls import path,re_path,include
from .views import *

app_name = 'myapp'
urlpatterns = [
    path('index/',index,name = "index"),
    path('',index),
    path('register/',register,name = 'register'),
    path ('registering/',registering,name = 'registering'),
    path('logins/',logins,name = 'logins'),
    path('logining/',logining,name = 'logining'),
    path('logouts/',logouts,name = 'logouts'),
    re_path('articles_by_id/(\S*)/',articles_by_id,name = "articles_by_id"),
    re_path('myarticle_by_id/(\S*)/',myarticle_by_id,name = "myarticle_by_id"),
    path('create_article/',create_article,name = "create_article"),
    path('release/',release,name = "release"),
    path('emails/',emails,name = "emails"),
    path('userinfo/',userinfo,name = "userinfo"),
    path('resume/',resume,name = "resume"),
    path('change/',change,name = 'change'),
    path('translate/',translate,name ='translate'),
    path('word_translates/',word_translates,name = 'word_translates'),
    path('sentence_translates/',sentence_translates,name = 'sentence_translates'),
    path('test/',test,name = "test"),
    path('article_manage/',article_manage,name = 'article_manage'),
    path('change_article/',change_article,name = 'change_article'),
    path('search_username/',search_username,name ='search_username')
    # path('successful/',successful,name = 'successful'),
    # path('fail/',fail,name = 'fail'),


]
