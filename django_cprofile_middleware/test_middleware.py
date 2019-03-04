import unittest
from unittest import mock

from django.conf import settings
from django import http
from django import test
from django import views
from django.test import client

from django_cprofile_middleware import middleware

settings.configure()


class MiddlewareTest(unittest.TestCase):

    class SampleView(views.View):

        def get(self, request):
            return http.HttpResponse()

    def setUp(self):
        self.view = MiddlewareTest.SampleView()
        self.middleware = middleware.ProfilerMiddleware()
        self.request = client.RequestFactory().get('/sample/?prof')
        self.default_response = http.HttpResponse('default response')
        self.override_settings = {
            'DEBUG': True,
            'DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF': False}
        self.profile_content = '<pre>'.encode('utf-8')

    def test_profile(self):
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                self.request, self.view.get, (self.request,), {})
            response = self.middleware.process_response(
                self.request, self.default_response)
        self.assertTrue(response.content.startswith(self.profile_content))
        self.assertIn('function calls'.encode('utf-8'), response.content)
        self.assertEqual(response['Content-Type'], 'text/html; charset=utf-8')

    def test_download_profile(self):
        request = client.RequestFactory().get('/sample/?prof&download')
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                request, self.view.get, (request,), {})
            response = self.middleware.process_response(
                request, self.default_response)
        self.assertEqual(response['Content-Type'], 'application/octet-stream')

    def test_get_param_required(self):
        request = client.RequestFactory().get('/sample/')
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                request, self.view.get, (request,), {})
            response = self.middleware.process_response(
                request, self.default_response)
        self.assertEqual(response.content, self.default_response.content)

    def test_debug_required(self):
        self.override_settings['DEBUG'] = False
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                self.request, self.view.get, (self.request,), {})
            response = self.middleware.process_response(
                self.request, self.default_response)
        self.assertEqual(response.content, self.default_response.content)

    def test_staff_setting_no_user(self):
        self.override_settings[
            'DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF'] = True
        with test.override_settings(**self.override_settings):
            with self.assertRaises(AttributeError):
                self.middleware.process_view(
                    self.request, self.view.get, (self.request,), {})
                self.middleware.process_response(
                    self.request, self.default_response)

    def test_staff_setting_non_staff_user(self):
        self.override_settings[
            'DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF'] = True
        self.request.user = mock.MagicMock(is_staff=False)
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                self.request, self.view.get, (self.request,), {})
            response = self.middleware.process_response(
                self.request, self.default_response)
        self.assertEqual(response.content, self.default_response.content)

    def test_staff_setting_staff_user(self):
        self.override_settings[
            'DJANGO_CPROFILE_MIDDLEWARE_REQUIRE_STAFF'] = True
        self.request.user = mock.MagicMock(is_staff=True)
        with test.override_settings(**self.override_settings):
            self.middleware.process_view(
                self.request, self.view.get, (self.request,), {})
            response = self.middleware.process_response(
                self.request, self.default_response)
        self.assertTrue(response.content.startswith(self.profile_content))
