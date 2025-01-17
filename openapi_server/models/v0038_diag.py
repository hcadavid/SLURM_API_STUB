from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.v0038_diag_statistics import V0038DiagStatistics
from openapi_server.models.v0038_error import V0038Error
from openapi_server.models.v0038_meta import V0038Meta
from openapi_server import util

from openapi_server.models.v0038_diag_statistics import V0038DiagStatistics  # noqa: E501
from openapi_server.models.v0038_error import V0038Error  # noqa: E501
from openapi_server.models.v0038_meta import V0038Meta  # noqa: E501

class V0038Diag(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meta=None, errors=None, statistics=None):  # noqa: E501
        """V0038Diag - a model defined in OpenAPI

        :param meta: The meta of this V0038Diag.  # noqa: E501
        :type meta: V0038Meta
        :param errors: The errors of this V0038Diag.  # noqa: E501
        :type errors: List[V0038Error]
        :param statistics: The statistics of this V0038Diag.  # noqa: E501
        :type statistics: V0038DiagStatistics
        """
        self.openapi_types = {
            'meta': V0038Meta,
            'errors': List[V0038Error],
            'statistics': V0038DiagStatistics
        }

        self.attribute_map = {
            'meta': 'meta',
            'errors': 'errors',
            'statistics': 'statistics'
        }

        self._meta = meta
        self._errors = errors
        self._statistics = statistics

    @classmethod
    def from_dict(cls, dikt) -> 'V0038Diag':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_diag of this V0038Diag.  # noqa: E501
        :rtype: V0038Diag
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> V0038Meta:
        """Gets the meta of this V0038Diag.


        :return: The meta of this V0038Diag.
        :rtype: V0038Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: V0038Meta):
        """Sets the meta of this V0038Diag.


        :param meta: The meta of this V0038Diag.
        :type meta: V0038Meta
        """

        self._meta = meta

    @property
    def errors(self) -> List[V0038Error]:
        """Gets the errors of this V0038Diag.

        slurm errors  # noqa: E501

        :return: The errors of this V0038Diag.
        :rtype: List[V0038Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[V0038Error]):
        """Sets the errors of this V0038Diag.

        slurm errors  # noqa: E501

        :param errors: The errors of this V0038Diag.
        :type errors: List[V0038Error]
        """

        self._errors = errors

    @property
    def statistics(self) -> V0038DiagStatistics:
        """Gets the statistics of this V0038Diag.


        :return: The statistics of this V0038Diag.
        :rtype: V0038DiagStatistics
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics: V0038DiagStatistics):
        """Sets the statistics of this V0038Diag.


        :param statistics: The statistics of this V0038Diag.
        :type statistics: V0038DiagStatistics
        """

        self._statistics = statistics
