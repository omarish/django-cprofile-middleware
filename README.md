django-cprofile-middleware
==========================

This is a simple profiling middleware for Django applications. I wrote it because I got tired of printing "start" "stop" "stop 2" in my programs to find the bottlenecks.

I found a simple example on @dcramer's [slideshare](http://www.slideshare.net/zeeg/django-con-high-performance-django-presentation) and modified it to support sorting.

## Installing

Add ```django_cprofile_middleware.middleware.ProfilerMiddleware``` to the end your ```MIDDLEWARE_CLASSES```. 

For example:

```
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'startup.do.work.FindProductMarketFitMiddleware',
    ...
    'django_cprofile_middleware.middleware.ProfilerMiddleware'
)
```

Again, add the profiler middleware to _the end_ of `MIDDLEWARE_CLASSES` so that it can include middleware operations in the profile.

## Running & Sorting Results

Once you've installed it, log in as a user who has staff privileges and add ```?prof``` to any URL to see the profiler's stats. For example to see profile stats for ```http://localhost:8000/foo/```, visit ```http://localhost:8000/foo/?prof```.

You can also pass some options:

**count:** The number of results you'd like to see. Default is 100.

**sort:** The field you'd like to sort results by. Default is ```time```. For all the options you can pass, see the [docs for pstats](http://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats).

## Enjoy!

Email me with any questions: [omar.bohsali@gmail.com](omar.bohsali@gmail.com).
