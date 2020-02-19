# django-cprofile-middleware

[![pypi-version]][pypi]

This is a simple profiling middleware for Django applications. I wrote it because I got tired of printing "start" "stop" "stop 2" in my programs to find the bottlenecks.

I found a simple example on @dcramer's [slideshare](http://www.slideshare.net/zeeg/django-con-high-performance-django-presentation) and modified it to support sorting.

## Installing

```bash
$ pip install django-cprofile-middleware
```

Then add ```django_cprofile_middleware.middleware.ProfilerMiddleware``` to the end your ```MIDDLEWARE``` in settings.py. This option was called ```MIDDLEWARE_CLASSES``` in versions of Django before [1.10](https://docs.djangoproject.com/en/1.10/topics/http/middleware/). 

For example:

```python
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'startup.do.work.FindProductMarketFitMiddleware',
    ...
    'django_cprofile_middleware.middleware.ProfilerMiddleware'
)
```

The profiler will only be available when the Django setting `DEBUG` is set to `True`. By default it's also required to be an authenticated user with `is_staff` set to `True` which is making the request to be profiled. The `is_staff` check can be configured as follows: 

```python
DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF = False
```

## Running & Sorting Results

Once you've installed it, log in as a user who has staff privileges and add ```?prof``` to any URL to see the profiler's stats. For example to see profile stats for ```http://localhost:8000/foo/```, visit ```http://localhost:8000/foo/?prof```.

You can also pass some options:

**count:** The number of results you'd like to see. Default is 100.

**sort:** The field you'd like to sort results by. Default is ```time```. For all the options you can pass, see the [docs for pstats](http://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats).

**download:** Download profile file, that can be visualized in multiple viewers, e.g. [SnakeViz](https://github.com/jiffyclub/snakeviz/) or [RunSnakeRun](http://www.vrplumber.com/programming/runsnakerun/)

## Enjoy!

Email me with any questions: [omar.bohsali@gmail.com](omar.bohsali@gmail.com).


[pypi]: https://pypi.org/project/django-cprofile-middleware/
[pypi-version]: https://img.shields.io/pypi/v/django-cprofile-middleware.svg
