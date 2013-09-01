from distutils.core import setup

setup(
    name = 'django_cprofile_middleware',
    packages = ['django_cprofile_middleware'], # this must be the same as the name above
    version = '0.1',
    description = 'Easily add cProfile profiling to django views.',
    author = 'Omar Bohsali',
    author_email = 'omar.bohsali@gmail.com',
    url = 'https://github.com/omarish/django-cprofile-middleware/',   # use the URL to the github repo
    # download_url = 'https://github.com/peterldowns/mypackage/tarball/0.1', # I'll explain this in a second
    keywords = ['django','profiling','cProfile'], # arbitrary keywords
    classifiers = [],
)
