from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class V0038DiagRpcu(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, user=None, user_id=None, count=None, average_time=None, total_time=None):  # noqa: E501
        """V0038DiagRpcu - a model defined in OpenAPI

        :param user: The user of this V0038DiagRpcu.  # noqa: E501
        :type user: str
        :param user_id: The user_id of this V0038DiagRpcu.  # noqa: E501
        :type user_id: int
        :param count: The count of this V0038DiagRpcu.  # noqa: E501
        :type count: int
        :param average_time: The average_time of this V0038DiagRpcu.  # noqa: E501
        :type average_time: int
        :param total_time: The total_time of this V0038DiagRpcu.  # noqa: E501
        :type total_time: int
        """
        self.openapi_types = {
            'user': str,
            'user_id': int,
            'count': int,
            'average_time': int,
            'total_time': int
        }

        self.attribute_map = {
            'user': 'user',
            'user_id': 'user_id',
            'count': 'count',
            'average_time': 'average_time',
            'total_time': 'total_time'
        }

        self._user = user
        self._user_id = user_id
        self._count = count
        self._average_time = average_time
        self._total_time = total_time

    @classmethod
    def from_dict(cls, dikt) -> 'V0038DiagRpcu':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_diag_rpcu of this V0038DiagRpcu.  # noqa: E501
        :rtype: V0038DiagRpcu
        """
        return util.deserialize_model(dikt, cls)

    @property
    def user(self) -> str:
        """Gets the user of this V0038DiagRpcu.

        user  # noqa: E501

        :return: The user of this V0038DiagRpcu.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user: str):
        """Sets the user of this V0038DiagRpcu.

        user  # noqa: E501

        :param user: The user of this V0038DiagRpcu.
        :type user: str
        """

        self._user = user

    @property
    def user_id(self) -> int:
        """Gets the user_id of this V0038DiagRpcu.

        user id  # noqa: E501

        :return: The user_id of this V0038DiagRpcu.
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id: int):
        """Sets the user_id of this V0038DiagRpcu.

        user id  # noqa: E501

        :param user_id: The user_id of this V0038DiagRpcu.
        :type user_id: int
        """

        self._user_id = user_id

    @property
    def count(self) -> int:
        """Gets the count of this V0038DiagRpcu.

        rpc count  # noqa: E501

        :return: The count of this V0038DiagRpcu.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count: int):
        """Sets the count of this V0038DiagRpcu.

        rpc count  # noqa: E501

        :param count: The count of this V0038DiagRpcu.
        :type count: int
        """

        self._count = count

    @property
    def average_time(self) -> int:
        """Gets the average_time of this V0038DiagRpcu.

        average time  # noqa: E501

        :return: The average_time of this V0038DiagRpcu.
        :rtype: int
        """
        return self._average_time

    @average_time.setter
    def average_time(self, average_time: int):
        """Sets the average_time of this V0038DiagRpcu.

        average time  # noqa: E501

        :param average_time: The average_time of this V0038DiagRpcu.
        :type average_time: int
        """

        self._average_time = average_time

    @property
    def total_time(self) -> int:
        """Gets the total_time of this V0038DiagRpcu.

        total time  # noqa: E501

        :return: The total_time of this V0038DiagRpcu.
        :rtype: int
        """
        return self._total_time

    @total_time.setter
    def total_time(self, total_time: int):
        """Sets the total_time of this V0038DiagRpcu.

        total time  # noqa: E501

        :param total_time: The total_time of this V0038DiagRpcu.
        :type total_time: int
        """

        self._total_time = total_time
