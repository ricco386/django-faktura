import os
from setuptools import find_packages, setup
from faktura import __version__ as VERSION, __author__ as AUTHOR

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-faktura',
    version=VERSION,
    install_requires=[
        'django-wkhtmltopdf',
    ],
    packages=find_packages(),
    include_package_data=True,
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
    license='MIT License',
    description='A simple Django app to create and manage invoices.',
    long_description=README,
    url='https://github.com/ricco386/django-faktura',
    author=AUTHOR,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 2.0',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
