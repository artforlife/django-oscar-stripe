=====
Usage
=====

To use Django Oscar Stripe in a project, add it to your `INSTALLED_APPS`:

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
