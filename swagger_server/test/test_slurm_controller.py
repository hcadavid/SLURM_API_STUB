# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.v0038_diag import V0038Diag  # noqa: E501
from swagger_server.models.v0038_errors import V0038Errors  # noqa: E501
from swagger_server.models.v0038_jobs_response import V0038JobsResponse  # noqa: E501
from swagger_server.models.v0038_licenses import V0038Licenses  # noqa: E501
from swagger_server.models.v0038_nodes_response import V0038NodesResponse  # noqa: E501
from swagger_server.models.v0038_partitions_response import V0038PartitionsResponse  # noqa: E501
from swagger_server.models.v0038_pings import V0038Pings  # noqa: E501
from swagger_server.models.v0038_reservations_response import V0038ReservationsResponse  # noqa: E501
from swagger_server.test import BaseTestCase


class TestSlurmController(BaseTestCase):
    """SlurmController integration test stubs"""

    def test_slurm_v0038_diag(self):
        """Test case for slurm_v0038_diag

        get diagnostics
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/diag',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_job(self):
        """Test case for slurm_v0038_get_job

        get job info
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/job/{job_id}'.format(job_id='job_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_jobs(self):
        """Test case for slurm_v0038_get_jobs

        get list of jobs
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/jobs',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_node(self):
        """Test case for slurm_v0038_get_node

        get node info
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/node/{node_name}'.format(node_name='node_name_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_nodes(self):
        """Test case for slurm_v0038_get_nodes

        get all node info
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/nodes',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_partition(self):
        """Test case for slurm_v0038_get_partition

        get partition info
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/partition/{partition_name}'.format(partition_name='partition_name_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_partitions(self):
        """Test case for slurm_v0038_get_partitions

        get all partition info
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/partitions',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_reservation(self):
        """Test case for slurm_v0038_get_reservation

        get reservation info
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/reservation/{reservation_name}'.format(reservation_name='reservation_name_example'),
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_get_reservations(self):
        """Test case for slurm_v0038_get_reservations

        get all reservation info
        """
        query_string = [('update_time', 789)]
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/reservations',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_ping(self):
        """Test case for slurm_v0038_ping

        ping test
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/ping',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_slurm_v0038_slurmctld_get_licenses(self):
        """Test case for slurm_v0038_slurmctld_get_licenses

        get all Slurm tracked license info
        """
        response = self.client.open(
            '/hcadavid6/slurm-rest_api_ro/0.0.38/slurm/v0.0.38/licenses',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
