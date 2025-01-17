from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.v0038_error import V0038Error
from openapi_server.models.v0038_job_response_properties import V0038JobResponseProperties
from openapi_server.models.v0038_meta import V0038Meta
from openapi_server import util

from openapi_server.models.v0038_error import V0038Error  # noqa: E501
from openapi_server.models.v0038_job_response_properties import V0038JobResponseProperties  # noqa: E501
from openapi_server.models.v0038_meta import V0038Meta  # noqa: E501

class V0038JobsResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meta=None, errors=None, jobs=None):  # noqa: E501
        """V0038JobsResponse - a model defined in OpenAPI

        :param meta: The meta of this V0038JobsResponse.  # noqa: E501
        :type meta: V0038Meta
        :param errors: The errors of this V0038JobsResponse.  # noqa: E501
        :type errors: List[V0038Error]
        :param jobs: The jobs of this V0038JobsResponse.  # noqa: E501
        :type jobs: List[V0038JobResponseProperties]
        """
        self.openapi_types = {
            'meta': V0038Meta,
            'errors': List[V0038Error],
            'jobs': List[V0038JobResponseProperties]
        }

        self.attribute_map = {
            'meta': 'meta',
            'errors': 'errors',
            'jobs': 'jobs'
        }

        self._meta = meta
        self._errors = errors
        self._jobs = jobs

    @classmethod
    def from_dict(cls, dikt) -> 'V0038JobsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_jobs_response of this V0038JobsResponse.  # noqa: E501
        :rtype: V0038JobsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> V0038Meta:
        """Gets the meta of this V0038JobsResponse.


        :return: The meta of this V0038JobsResponse.
        :rtype: V0038Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: V0038Meta):
        """Sets the meta of this V0038JobsResponse.


        :param meta: The meta of this V0038JobsResponse.
        :type meta: V0038Meta
        """

        self._meta = meta

    @property
    def errors(self) -> List[V0038Error]:
        """Gets the errors of this V0038JobsResponse.

        slurm errors  # noqa: E501

        :return: The errors of this V0038JobsResponse.
        :rtype: List[V0038Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[V0038Error]):
        """Sets the errors of this V0038JobsResponse.

        slurm errors  # noqa: E501

        :param errors: The errors of this V0038JobsResponse.
        :type errors: List[V0038Error]
        """

        self._errors = errors

    @property
    def jobs(self) -> List[V0038JobResponseProperties]:
        """Gets the jobs of this V0038JobsResponse.

        job descriptions  # noqa: E501

        :return: The jobs of this V0038JobsResponse.
        :rtype: List[V0038JobResponseProperties]
        """
        return self._jobs

    @jobs.setter
    def jobs(self, jobs: List[V0038JobResponseProperties]):
        """Sets the jobs of this V0038JobsResponse.

        job descriptions  # noqa: E501

        :param jobs: The jobs of this V0038JobsResponse.
        :type jobs: List[V0038JobResponseProperties]
        """

        self._jobs = jobs
