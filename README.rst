=======
Faktura
=======

.. image:: https://img.shields.io/pypi/pyversions/django-faktura.svg
.. image:: https://img.shields.io/pypi/djversions/django-faktura.svg
.. image:: https://img.shields.io/github/license/ricco386/django-faktura.svg

Faktura is a simple Django app to conduct Web-based invoice generation and evidence.

Quick start
-----------

1. Add "faktura" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'faktura',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('invoices/', include('faktura.urls')),

3. Run `python manage.py migrate` to create the faktura models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage your invoices (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/invoices/ to view the invoices list.

Support
-----

I did this app because SPy o.z. (non profit supporting Slovak Python community) needed
something for invoice evidence. I like to program and I wanted to try design a clean 
Django app and learn one or two things about testing stand alone app and packaging.

If you like what I do (stuff like this django app, or my role in community), you can buy me a coffee:

.. image:: https://img.shields.io/badge/Donate-PayPal-green.svg
   :target: https://paypal.me/ricco386

If you use this app for your business consider makeing a recurent donation:

.. image:: http://img.shields.io/liberapay/goal/RicCo.svg?logo=liberapay
   :target: https://liberapay.com/RicCo/donate
