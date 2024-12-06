from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class V0038ReservationPurgeCompleted(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, time=None):  # noqa: E501
        """V0038ReservationPurgeCompleted - a model defined in OpenAPI

        :param time: The time of this V0038ReservationPurgeCompleted.  # noqa: E501
        :type time: int
        """
        self.openapi_types = {
            'time': int
        }

        self.attribute_map = {
            'time': 'time'
        }

        self._time = time

    @classmethod
    def from_dict(cls, dikt) -> 'V0038ReservationPurgeCompleted':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0_0_38_reservation_purge_completed of this V0038ReservationPurgeCompleted.  # noqa: E501
        :rtype: V0038ReservationPurgeCompleted
        """
        return util.deserialize_model(dikt, cls)

    @property
    def time(self) -> int:
        """Gets the time of this V0038ReservationPurgeCompleted.

        amount of seconds this reservation will sit idle until it is revoked  # noqa: E501

        :return: The time of this V0038ReservationPurgeCompleted.
        :rtype: int
        """
        return self._time

    @time.setter
    def time(self, time: int):
        """Sets the time of this V0038ReservationPurgeCompleted.

        amount of seconds this reservation will sit idle until it is revoked  # noqa: E501

        :param time: The time of this V0038ReservationPurgeCompleted.
        :type time: int
        """

        self._time = time