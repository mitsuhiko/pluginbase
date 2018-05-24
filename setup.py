try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='pluginbase',
    author='Armin Ronacher',
    author_email='armin.ronacher@active-4.com',
    maintainer='Spencer McIntyre',
    maintainer_email='zeroSteiner@gmail.com',
    version='0.6',
    url='http://github.com/mitsuhiko/pluginbase',
    py_modules=['pluginbase'],
    description='A support library for building plugins sytems in Python.',
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
