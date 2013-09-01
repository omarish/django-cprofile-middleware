from distutils.core import setup

setup(
    name = 'django-cprofile-middleware',
    packages = ['django_cprofile_middleware'],
    license = 'MIT',
    version = '0.1',
    description = 'Easily add cProfile profiling to django views.',
    author = 'Omar Bohsali',
    author_email = 'omar.bohsali@gmail.com',
    url = 'https://github.com/omarish/django-cprofile-middleware/',
    download_url = 'https://github.com/omarish/django-cprofile-middleware/tarball/0.1',
    keywords = ['django','profiling','cProfile'],
    classifiers = [],
)
