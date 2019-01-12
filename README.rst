=======
Faktura
=======

.. image:: https://img.shields.io/pypi/pyversions/django-faktura.svg
   :target: https://pypi.org/project/django-faktura/

.. image:: https://codebeat.co/badges/76c75008-f8a2-4ace-8ec4-c4f1b9183c6c
   :target: https://codebeat.co/projects/github-com-ricco386-django-faktura-master

.. image:: https://travis-ci.com/ricco386/django-faktura.svg?branch=master
   :target: https://travis-ci.com/ricco386/django-faktura

.. image:: https://img.shields.io/github/license/ricco386/django-faktura.svg
   :target: https://github.com/ricco386/django-faktura/blob/master/LICENSE

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
