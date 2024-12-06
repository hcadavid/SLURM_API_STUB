# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.v0038_node_allocation_sockets import V0038NodeAllocationSockets  # noqa: F401,E501
from swagger_server import util


class V0038NodeAllocation(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, memory: int=None, cpus: int=None, sockets: V0038NodeAllocationSockets=None, nodename: str=None):  # noqa: E501
        """V0038NodeAllocation - a model defined in Swagger

        :param memory: The memory of this V0038NodeAllocation.  # noqa: E501
        :type memory: int
        :param cpus: The cpus of this V0038NodeAllocation.  # noqa: E501
        :type cpus: int
        :param sockets: The sockets of this V0038NodeAllocation.  # noqa: E501
        :type sockets: V0038NodeAllocationSockets
        :param nodename: The nodename of this V0038NodeAllocation.  # noqa: E501
        :type nodename: str
        """
        self.swagger_types = {
            'memory': int,
            'cpus': int,
            'sockets': V0038NodeAllocationSockets,
            'nodename': str
        }

        self.attribute_map = {
            'memory': 'memory',
            'cpus': 'cpus',
            'sockets': 'sockets',
            'nodename': 'nodename'
        }
        self._memory = memory
        self._cpus = cpus
        self._sockets = sockets
        self._nodename = nodename

    @classmethod
    def from_dict(cls, dikt) -> 'V0038NodeAllocation':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_node_allocation of this V0038NodeAllocation.  # noqa: E501
        :rtype: V0038NodeAllocation
        """
        return util.deserialize_model(dikt, cls)

    @property
    def memory(self) -> int:
        """Gets the memory of this V0038NodeAllocation.

        amount of assigned job memory  # noqa: E501

        :return: The memory of this V0038NodeAllocation.
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory: int):
        """Sets the memory of this V0038NodeAllocation.

        amount of assigned job memory  # noqa: E501

        :param memory: The memory of this V0038NodeAllocation.
        :type memory: int
        """

        self._memory = memory

    @property
    def cpus(self) -> int:
        """Gets the cpus of this V0038NodeAllocation.

        number of assigned job CPUs  # noqa: E501

        :return: The cpus of this V0038NodeAllocation.
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus: int):
        """Sets the cpus of this V0038NodeAllocation.

        number of assigned job CPUs  # noqa: E501

        :param cpus: The cpus of this V0038NodeAllocation.
        :type cpus: int
        """

        self._cpus = cpus

    @property
    def sockets(self) -> V0038NodeAllocationSockets:
        """Gets the sockets of this V0038NodeAllocation.


        :return: The sockets of this V0038NodeAllocation.
        :rtype: V0038NodeAllocationSockets
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets: V0038NodeAllocationSockets):
        """Sets the sockets of this V0038NodeAllocation.


        :param sockets: The sockets of this V0038NodeAllocation.
        :type sockets: V0038NodeAllocationSockets
        """

        self._sockets = sockets

    @property
    def nodename(self) -> str:
        """Gets the nodename of this V0038NodeAllocation.

        node name  # noqa: E501

        :return: The nodename of this V0038NodeAllocation.
        :rtype: str
        """
        return self._nodename

    @nodename.setter
    def nodename(self, nodename: str):
        """Sets the nodename of this V0038NodeAllocation.

        node name  # noqa: E501

        :param nodename: The nodename of this V0038NodeAllocation.
        :type nodename: str
        """

        self._nodename = nodename
