#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from tornado.httpclient import AsyncHTTPClient
from tornado.testing import AsyncTestCase, gen_test
from tornado import httpclient


class MyTestCase2(AsyncTestCase):
    @gen_test
    async def test_http_login(self):
        buildRequest = httpclient.HTTPRequest('https://localhost/login',auth_username="user1", auth_password="pass1", validate_cert=False)
        client = AsyncHTTPClient(self.io_loop)
        response = await client.fetch(buildRequest)
        # Test contents of response
        self.assertEqual(200, response.code, f'200 != {response.code}')

    @gen_test
    async def test_request_Mongo(self):
        buildRequest = httpclient.HTTPRequest('https://localhost/?cpf=10000000028',auth_username="user1", auth_password="pass1", validate_cert=False)
        client = AsyncHTTPClient(self.io_loop)
        response = await client.fetch(buildRequest)
        # Test contents of response
        self.assertEqual(200, response.code, 'Valores Diferentes')


unittest.main()

