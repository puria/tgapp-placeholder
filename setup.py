# -*- coding: utf-8 -*-
import sys, os

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

install_requires=[
    "TurboGears2 >= 2.1.4",
    "tgext.pluggable",
    "pillow",
    "requests"
]

testpkgs = [
    'WebTest >= 1.2.3',
    'nose',
    'coverage',
    'ming',
    'sqlalchemy',
    'zope.sqlalchemy',
    'repoze.who',
    'tw2.forms',
    'kajiki',
]

here = os.path.abspath(os.path.dirname(__file__))
try:
    README = open(os.path.join(here, 'README.rst')).read()
except IOError:
    README = ''

setup(
    name='tgapp-placeholder',
    version='1.0.0',
    description='Placeholder image on the fly for Turbogears2',
    long_description=README,
    author='Puria Nafisi Azizi',
    author_email='puria.nafisi@axant.it',
    url='http://github.com/puria/tgapp-placeholder',
    license='WTFPL',
    keywords='turbogears2.application placeholder dummy image',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=install_requires,
    include_package_data=True,
    package_data={'tgapp.placeholder': ['i18n/*/LC_MESSAGES/*.mo', 'templates/*/*', 'public/*/*']},
    entry_points="""
    """,
    zip_safe=False
)
