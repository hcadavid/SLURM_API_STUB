from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.v0038_error import V0038Error
from openapi_server.models.v0038_meta import V0038Meta
from openapi_server.models.v0038_ping import V0038Ping
from openapi_server import util

from openapi_server.models.v0038_error import V0038Error  # noqa: E501
from openapi_server.models.v0038_meta import V0038Meta  # noqa: E501
from openapi_server.models.v0038_ping import V0038Ping  # noqa: E501

class V0038Pings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, meta=None, errors=None, pings=None):  # noqa: E501
        """V0038Pings - a model defined in OpenAPI

        :param meta: The meta of this V0038Pings.  # noqa: E501
        :type meta: V0038Meta
        :param errors: The errors of this V0038Pings.  # noqa: E501
        :type errors: List[V0038Error]
        :param pings: The pings of this V0038Pings.  # noqa: E501
        :type pings: List[V0038Ping]
        """
        self.openapi_types = {
            'meta': V0038Meta,
            'errors': List[V0038Error],
            'pings': List[V0038Ping]
        }

        self.attribute_map = {
            'meta': 'meta',
            'errors': 'errors',
            'pings': 'pings'
        }

        self._meta = meta
        self._errors = errors
        self._pings = pings

    @classmethod
    def from_dict(cls, dikt) -> 'V0038Pings':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_pings of this V0038Pings.  # noqa: E501
        :rtype: V0038Pings
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> V0038Meta:
        """Gets the meta of this V0038Pings.


        :return: The meta of this V0038Pings.
        :rtype: V0038Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: V0038Meta):
        """Sets the meta of this V0038Pings.


        :param meta: The meta of this V0038Pings.
        :type meta: V0038Meta
        """

        self._meta = meta

    @property
    def errors(self) -> List[V0038Error]:
        """Gets the errors of this V0038Pings.

        slurm errors  # noqa: E501

        :return: The errors of this V0038Pings.
        :rtype: List[V0038Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[V0038Error]):
        """Sets the errors of this V0038Pings.

        slurm errors  # noqa: E501

        :param errors: The errors of this V0038Pings.
        :type errors: List[V0038Error]
        """

        self._errors = errors

    @property
    def pings(self) -> List[V0038Ping]:
        """Gets the pings of this V0038Pings.

        slurm controller pings  # noqa: E501

        :return: The pings of this V0038Pings.
        :rtype: List[V0038Ping]
        """
        return self._pings

    @pings.setter
    def pings(self, pings: List[V0038Ping]):
        """Sets the pings of this V0038Pings.

        slurm controller pings  # noqa: E501

        :param pings: The pings of this V0038Pings.
        :type pings: List[V0038Ping]
        """

        self._pings = pings
