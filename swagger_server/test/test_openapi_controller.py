# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestOpenapiController(BaseTestCase):
    """OpenapiController integration test stubs"""

    def test_openapi_get(self):
        """Test case for openapi_get

        Retrieve OpenAPI Specification
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/openapi',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_openapi_json_get(self):
        """Test case for openapi_json_get

        Retrieve OpenAPI Specification
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/openapi.json',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_openapi_v3_get(self):
        """Test case for openapi_v3_get

        Retrieve OpenAPI Specification
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/openapi/v3',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_openapi_yaml_get(self):
        """Test case for openapi_yaml_get

        Retrieve OpenAPI Specification
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/openapi.yaml',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
