import os
import re
import sys

base_directory = os.path.dirname(__file__)

try:
    from setuptools import setup, find_packages
except ImportError:
    print('This project needs setuptools in order to build. Install it using your package')
    print('manager (usually python-setuptools) or via pip (pip install setuptools).')
    sys.exit(1)

try:
    with open(os.path.join(base_directory, 'README.rst')) as file_h:
        long_description = file_h.read()
except OSError:
    sys.stderr.write('README.rst is unavailable, can not generate the long description\n')
    long_description = None

with open(os.path.join(base_directory, 'pluginbase.py')) as file_h:
    match = re.search(r'^__version__\s*=\s*([\'"])(?P<version>\d+(\.\d)*)\1$', file_h.read(), flags=re.MULTILINE)
if match is None:
    raise RuntimeError('Unable to find the version information')
version = match.group('version')

DESCRIPTION = """\
PluginBase is a module for Python that enables the development of flexible \
plugin systems in Python.\
"""

setup(
    name='pluginbase',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='Spencer McIntyre',
    maintainer_email='zeroSteiner@gmail.com',
    version=version,
    description=DESCRIPTION,
    long_description=long_description,
    url='http://github.com/mitsuhiko/pluginbase',
    py_modules=['pluginbase'],
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
