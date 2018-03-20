import pstats

try:
    import cProfile as profile
except ImportError:
    import profile
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO

import django
from django.conf import settings
from django.http import HttpResponse

if django.VERSION >= (1, 10):
    from django.utils.deprecation import MiddlewareMixin
else:
    from django_cprofile_middleware.utils import MiddlewareMixin


class ProfilerMiddleware(MiddlewareMixin):
    """
    Simple profile middleware to profile django views. To run it, add ?prof to
    the URL like this:

        http://localhost:8000/view/?prof

    Optionally pass the following to modify the output:

    ?sort => Sort the output by a given metric. Default is time.
        See http://docs.python.org/2/library/profile.html#pstats.Stats.sort_stats
        for all sort options.

    ?count => The number of rows to display. Default is 100.

    ?download => Download profile file suitable for visualization. For example
        in snakeviz or RunSnakeRun

    This is adapted from an example found here:
    http://www.slideshare.net/zeeg/django-con-high-performance-django-presentation.
    """
    def can(self, request):
        return settings.DEBUG and 'prof' in request.GET and \
            request.user is not None and request.user.is_staff

    def process_view(self, request, callback, callback_args, callback_kwargs):
        if self.can(request):
            self.profiler = profile.Profile()
            args = (request,) + callback_args
            try:
                return self.profiler.runcall(
                    callback, *args, **callback_kwargs)
            except Exception:
                # we want the process_exception middleware to fire
                # https://code.djangoproject.com/ticket/12250
                return

    def process_response(self, request, response):
        if self.can(request):
            self.profiler.create_stats()
            if 'download' in request.GET:
                import marshal

                output = marshal.dumps(self.profiler.stats)
                response = HttpResponse(
                    output, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment;' \
                                                  ' filename=view.prof'
                response['Content-Length'] = len(output)
            else:
                io = StringIO()
                stats = pstats.Stats(self.profiler, stream=io)

                stats.strip_dirs().sort_stats(request.GET.get('sort', 'time'))
                stats.print_stats(int(request.GET.get('count', 100)))

                response = HttpResponse('<pre>%s</pre>' % io.getvalue())
        return response
