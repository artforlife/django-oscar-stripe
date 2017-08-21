# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from django_oscar_stripe.urls import urlpatterns as django_oscar_stripe_urls

urlpatterns = [
    url(r'^', include(django_oscar_stripe_urls, namespace='django_oscar_stripe')),
]
