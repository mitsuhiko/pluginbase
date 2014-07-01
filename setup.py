try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pluginbase',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    version='0.3-dev',
    url='http://github.com/mitsuhiko/pluginbase',
    py_modules=['pluginbase'],
    description='A support library for building plugins sytems in Python.',
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
)
