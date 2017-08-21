=============================
Django Oscar Stripe
=============================

.. image:: https://badge.fury.io/py/django-oscar-stripe.svg
    :target: https://badge.fury.io/py/django-oscar-stripe

.. image:: https://travis-ci.org/artforlife/django-oscar-stripe.svg?branch=master
    :target: https://travis-ci.org/artforlife/django-oscar-stripe

.. image:: https://codecov.io/gh/artforlife/django-oscar-stripe/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/artforlife/django-oscar-stripe

Payment package for Django-Oscar and Stripe

Documentation
-------------

The full documentation is at https://django-oscar-stripe.readthedocs.io.

Quickstart
----------

Install Django Oscar Stripe::

    pip install django-oscar-stripe

Add it to your `INSTALLED_APPS`:

.. code-block:: python

    INSTALLED_APPS = (
        ...
        'django_oscar_stripe.apps.DjangoOscarStripeConfig',
        ...
    )

Add Django Oscar Stripe's URL patterns:

.. code-block:: python

    from django_oscar_stripe import urls as django_oscar_stripe_urls


    urlpatterns = [
        ...
        url(r'^', include(django_oscar_stripe_urls)),
        ...
    ]

Features
--------

* TODO

Running Tests
-------------

Does the code actually work?

::

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

Credits
-------

Tools used in rendering this package:

*  Cookiecutter_
*  `cookiecutter-djangopackage`_

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`cookiecutter-djangopackage`: https://github.com/pydanny/cookiecutter-djangopackage
