# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.veure_artistes, name='veure_artistes'),
    url(r'^introduir_artistes/$', views.intro_edit_artistes, name='introduir_artistes'),
    url(r'^rebreDades/$', views.rebreDades, name='rebreDades'),

]