#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.conf.urls import url
from user import views

urlpatterns = [
    url(r'^send/sms/', views.send_sms),
    url(r'^register/', views.register, name='register'),  # "user:register"
]
