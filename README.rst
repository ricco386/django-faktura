=======
Faktura
=======

.. image:: https://img.shields.io/pypi/pyversions/django-faktura.svg
   :target: https://pypi.org/project/django-faktura/

.. image:: https://codebeat.co/badges/2d56dde1-436c-4d31-81ca-108412aa417c
   :target: https://codebeat.co/projects/github-com-ricco386-django-faktura-master

.. image:: https://travis-ci.com/ricco386/django-faktura.svg?branch=master
   :target: https://travis-ci.com/ricco386/django-faktura

.. image:: https://img.shields.io/github/license/ricco386/django-faktura.svg
   :target: https://github.com/ricco386/django-faktura/blob/master/LICENSE

Faktura is a simple Django app to conduct Web-based invoice generation and evidence.

Dependencies
------------

For generating PDF we use https://wkhtmltopdf.org/ package. Make sure you have installed it in your OS.
Package installation will also download and install https://github.com/incuna/django-wkhtmltopdf.


Quick start
-----------

1. Install django-faktura via pip::

   pip install django-faktura

1. Add "faktura" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'wkhtmltopdf',  # Dependency for PDF generation
        'faktura',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('invoices/', include('faktura.urls')),

3. Run `python manage.py migrate` to create the faktura models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to manage your invoices (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/invoices/ to view the invoices list.

Settings
--------

In order to generate invoice PDF with `wkhtmltopdf`, make sure your project has `STATIC_ROOT` set.
If `STATIC_ROOT` is not set PDF generation will fail with `AttributeError` (#15).


Testing
-------

In order to run tests execute command::

     python setup.py test

We do have additional requirements for running tests in multiple Python and Django
environments via TOX. Install them (into your virtualenv)::

     pip install -r requirements-test.txt

To run complex test suite via TOX, execute command::

     tox

Support
-------

I did this app because SPy o.z. (non profit supporting Slovak Python community) needed
something for invoice evidence. I like to program and I wanted to try design a clean 
Django app and learn one or two things about testing stand alone app and packaging.

You can use my refferal link: https://m.do.co/c/18b211fa1d99 and create account with 
Digital Ocean and get $50 credit, and you'll help me out to cover my hosting costs.

If you like what I do (stuff like this django app, or my role in community), you can buy
me a coffee:

.. image:: https://img.shields.io/badge/Donate-PayPal-blue.svg
   :target: https://paypal.me/ricco386

.. image:: https://img.shields.io/badge/Donate-bitcoin-blue.svg
   :target: https://tallyco.in/RicCo386/

If you use this app for your business consider makeing a recurent donation:

.. image:: http://img.shields.io/liberapay/goal/RicCo.svg?logo=liberapay
   :target: https://liberapay.com/RicCo/donate
