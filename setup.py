import os
import sys

base_directory = os.path.dirname(__file__)

from setuptools import setup

DESCRIPTION = """\
PluginBase is a module for Python that enables the development of flexible \
plugin systems in Python.\
"""

with open(os.path.join(base_directory, 'README.md'), 'r') as file_h:
    long_description = file_h.read()

setup(
    name='pluginbase',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='Spencer McIntyre',
    maintainer_email='zeroSteiner@gmail.com',
    version='0.7',
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='http://github.com/mitsuhiko/pluginbase',
    py_modules=['pluginbase'],
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
    ]
)
