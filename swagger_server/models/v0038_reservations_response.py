# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v0038_error import V0038Error  # noqa: F401,E501
from swagger_server.models.v0038_meta import V0038Meta  # noqa: F401,E501
from swagger_server.models.v0038_reservation import V0038Reservation  # noqa: F401,E501
from swagger_server import util


class V0038ReservationsResponse(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, meta: V0038Meta=None, errors: List[V0038Error]=None, reservations: List[V0038Reservation]=None):  # noqa: E501
        """V0038ReservationsResponse - a model defined in Swagger

        :param meta: The meta of this V0038ReservationsResponse.  # noqa: E501
        :type meta: V0038Meta
        :param errors: The errors of this V0038ReservationsResponse.  # noqa: E501
        :type errors: List[V0038Error]
        :param reservations: The reservations of this V0038ReservationsResponse.  # noqa: E501
        :type reservations: List[V0038Reservation]
        """
        self.swagger_types = {
            'meta': V0038Meta,
            'errors': List[V0038Error],
            'reservations': List[V0038Reservation]
        }

        self.attribute_map = {
            'meta': 'meta',
            'errors': 'errors',
            'reservations': 'reservations'
        }
        self._meta = meta
        self._errors = errors
        self._reservations = reservations

    @classmethod
    def from_dict(cls, dikt) -> 'V0038ReservationsResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_reservations_response of this V0038ReservationsResponse.  # noqa: E501
        :rtype: V0038ReservationsResponse
        """
        return util.deserialize_model(dikt, cls)

    @property
    def meta(self) -> V0038Meta:
        """Gets the meta of this V0038ReservationsResponse.


        :return: The meta of this V0038ReservationsResponse.
        :rtype: V0038Meta
        """
        return self._meta

    @meta.setter
    def meta(self, meta: V0038Meta):
        """Sets the meta of this V0038ReservationsResponse.


        :param meta: The meta of this V0038ReservationsResponse.
        :type meta: V0038Meta
        """

        self._meta = meta

    @property
    def errors(self) -> List[V0038Error]:
        """Gets the errors of this V0038ReservationsResponse.

        slurm errors  # noqa: E501

        :return: The errors of this V0038ReservationsResponse.
        :rtype: List[V0038Error]
        """
        return self._errors

    @errors.setter
    def errors(self, errors: List[V0038Error]):
        """Sets the errors of this V0038ReservationsResponse.

        slurm errors  # noqa: E501

        :param errors: The errors of this V0038ReservationsResponse.
        :type errors: List[V0038Error]
        """

        self._errors = errors

    @property
    def reservations(self) -> List[V0038Reservation]:
        """Gets the reservations of this V0038ReservationsResponse.

        reservation info  # noqa: E501

        :return: The reservations of this V0038ReservationsResponse.
        :rtype: List[V0038Reservation]
        """
        return self._reservations

    @reservations.setter
    def reservations(self, reservations: List[V0038Reservation]):
        """Sets the reservations of this V0038ReservationsResponse.

        reservation info  # noqa: E501

        :param reservations: The reservations of this V0038ReservationsResponse.
        :type reservations: List[V0038Reservation]
        """

        self._reservations = reservations
