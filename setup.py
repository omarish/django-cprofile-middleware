from distutils.core import setup

setup(
    name = 'django-cprofile-middleware',
    packages = ['django_cprofile_middleware'],
    license = 'MIT',
    version = '1.0',
    description = 'Easily add cProfile profiling to django views.',
    long_description = 'See https://github.com/omarish/django-cprofile-middleware/',
    author = 'Omar Bohsali',
    author_email = 'omar.bohsali@gmail.com',
    url = 'https://github.com/omarish/django-cprofile-middleware/',
    download_url = 'https://github.com/omarish/django-cprofile-middleware/tarball/v1.0',
    keywords = ['django','profiling','cProfile'],
    classifiers = [
        "Framework :: Django"
    ],
)
