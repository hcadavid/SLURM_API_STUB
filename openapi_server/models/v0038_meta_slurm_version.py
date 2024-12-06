from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class V0038MetaSlurmVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, major=None, micro=None, minor=None):  # noqa: E501
        """V0038MetaSlurmVersion - a model defined in OpenAPI

        :param major: The major of this V0038MetaSlurmVersion.  # noqa: E501
        :type major: int
        :param micro: The micro of this V0038MetaSlurmVersion.  # noqa: E501
        :type micro: int
        :param minor: The minor of this V0038MetaSlurmVersion.  # noqa: E501
        :type minor: int
        """
        self.openapi_types = {
            'major': int,
            'micro': int,
            'minor': int
        }

        self.attribute_map = {
            'major': 'major',
            'micro': 'micro',
            'minor': 'minor'
        }

        self._major = major
        self._micro = micro
        self._minor = minor

    @classmethod
    def from_dict(cls, dikt) -> 'V0038MetaSlurmVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0_0_38_meta_Slurm_version of this V0038MetaSlurmVersion.  # noqa: E501
        :rtype: V0038MetaSlurmVersion
        """
        return util.deserialize_model(dikt, cls)

    @property
    def major(self) -> int:
        """Gets the major of this V0038MetaSlurmVersion.

          # noqa: E501

        :return: The major of this V0038MetaSlurmVersion.
        :rtype: int
        """
        return self._major

    @major.setter
    def major(self, major: int):
        """Sets the major of this V0038MetaSlurmVersion.

          # noqa: E501

        :param major: The major of this V0038MetaSlurmVersion.
        :type major: int
        """

        self._major = major

    @property
    def micro(self) -> int:
        """Gets the micro of this V0038MetaSlurmVersion.

          # noqa: E501

        :return: The micro of this V0038MetaSlurmVersion.
        :rtype: int
        """
        return self._micro

    @micro.setter
    def micro(self, micro: int):
        """Sets the micro of this V0038MetaSlurmVersion.

          # noqa: E501

        :param micro: The micro of this V0038MetaSlurmVersion.
        :type micro: int
        """

        self._micro = micro

    @property
    def minor(self) -> int:
        """Gets the minor of this V0038MetaSlurmVersion.

          # noqa: E501

        :return: The minor of this V0038MetaSlurmVersion.
        :rtype: int
        """
        return self._minor

    @minor.setter
    def minor(self, minor: int):
        """Sets the minor of this V0038MetaSlurmVersion.

          # noqa: E501

        :param minor: The minor of this V0038MetaSlurmVersion.
        :type minor: int
        """

        self._minor = minor