# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class V0038Node(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, architecture: str=None, burstbuffer_network_address: str=None, boards: int=None, boot_time: int=None, cores: int=None, cpu_binding: int=None, cpu_load: int=None, free_memory: int=None, cpus: int=None, features: str=None, active_features: str=None, gres: str=None, gres_drained: str=None, gres_used: str=None, mcs_label: str=None, name: str=None, next_state_after_reboot: str=None, next_state_after_reboot_flags: List[str]=None, address: str=None, hostname: str=None, state: str=None, state_flags: List[str]=None, operating_system: str=None, owner: str=None, partitions: List[str]=None, port: int=None, real_memory: int=None, reason: str=None, reason_changed_at: int=None, reason_set_by_user: str=None, slurmd_start_time: int=None, sockets: int=None, threads: int=None, temporary_disk: int=None, weight: int=None, tres: str=None, tres_used: str=None, tres_weighted: float=None, slurmd_version: str=None, alloc_cpus: int=None, idle_cpus: int=None, alloc_memory: int=None):  # noqa: E501
        """V0038Node - a model defined in Swagger

        :param architecture: The architecture of this V0038Node.  # noqa: E501
        :type architecture: str
        :param burstbuffer_network_address: The burstbuffer_network_address of this V0038Node.  # noqa: E501
        :type burstbuffer_network_address: str
        :param boards: The boards of this V0038Node.  # noqa: E501
        :type boards: int
        :param boot_time: The boot_time of this V0038Node.  # noqa: E501
        :type boot_time: int
        :param cores: The cores of this V0038Node.  # noqa: E501
        :type cores: int
        :param cpu_binding: The cpu_binding of this V0038Node.  # noqa: E501
        :type cpu_binding: int
        :param cpu_load: The cpu_load of this V0038Node.  # noqa: E501
        :type cpu_load: int
        :param free_memory: The free_memory of this V0038Node.  # noqa: E501
        :type free_memory: int
        :param cpus: The cpus of this V0038Node.  # noqa: E501
        :type cpus: int
        :param features: The features of this V0038Node.  # noqa: E501
        :type features: str
        :param active_features: The active_features of this V0038Node.  # noqa: E501
        :type active_features: str
        :param gres: The gres of this V0038Node.  # noqa: E501
        :type gres: str
        :param gres_drained: The gres_drained of this V0038Node.  # noqa: E501
        :type gres_drained: str
        :param gres_used: The gres_used of this V0038Node.  # noqa: E501
        :type gres_used: str
        :param mcs_label: The mcs_label of this V0038Node.  # noqa: E501
        :type mcs_label: str
        :param name: The name of this V0038Node.  # noqa: E501
        :type name: str
        :param next_state_after_reboot: The next_state_after_reboot of this V0038Node.  # noqa: E501
        :type next_state_after_reboot: str
        :param next_state_after_reboot_flags: The next_state_after_reboot_flags of this V0038Node.  # noqa: E501
        :type next_state_after_reboot_flags: List[str]
        :param address: The address of this V0038Node.  # noqa: E501
        :type address: str
        :param hostname: The hostname of this V0038Node.  # noqa: E501
        :type hostname: str
        :param state: The state of this V0038Node.  # noqa: E501
        :type state: str
        :param state_flags: The state_flags of this V0038Node.  # noqa: E501
        :type state_flags: List[str]
        :param operating_system: The operating_system of this V0038Node.  # noqa: E501
        :type operating_system: str
        :param owner: The owner of this V0038Node.  # noqa: E501
        :type owner: str
        :param partitions: The partitions of this V0038Node.  # noqa: E501
        :type partitions: List[str]
        :param port: The port of this V0038Node.  # noqa: E501
        :type port: int
        :param real_memory: The real_memory of this V0038Node.  # noqa: E501
        :type real_memory: int
        :param reason: The reason of this V0038Node.  # noqa: E501
        :type reason: str
        :param reason_changed_at: The reason_changed_at of this V0038Node.  # noqa: E501
        :type reason_changed_at: int
        :param reason_set_by_user: The reason_set_by_user of this V0038Node.  # noqa: E501
        :type reason_set_by_user: str
        :param slurmd_start_time: The slurmd_start_time of this V0038Node.  # noqa: E501
        :type slurmd_start_time: int
        :param sockets: The sockets of this V0038Node.  # noqa: E501
        :type sockets: int
        :param threads: The threads of this V0038Node.  # noqa: E501
        :type threads: int
        :param temporary_disk: The temporary_disk of this V0038Node.  # noqa: E501
        :type temporary_disk: int
        :param weight: The weight of this V0038Node.  # noqa: E501
        :type weight: int
        :param tres: The tres of this V0038Node.  # noqa: E501
        :type tres: str
        :param tres_used: The tres_used of this V0038Node.  # noqa: E501
        :type tres_used: str
        :param tres_weighted: The tres_weighted of this V0038Node.  # noqa: E501
        :type tres_weighted: float
        :param slurmd_version: The slurmd_version of this V0038Node.  # noqa: E501
        :type slurmd_version: str
        :param alloc_cpus: The alloc_cpus of this V0038Node.  # noqa: E501
        :type alloc_cpus: int
        :param idle_cpus: The idle_cpus of this V0038Node.  # noqa: E501
        :type idle_cpus: int
        :param alloc_memory: The alloc_memory of this V0038Node.  # noqa: E501
        :type alloc_memory: int
        """
        self.swagger_types = {
            'architecture': str,
            'burstbuffer_network_address': str,
            'boards': int,
            'boot_time': int,
            'cores': int,
            'cpu_binding': int,
            'cpu_load': int,
            'free_memory': int,
            'cpus': int,
            'features': str,
            'active_features': str,
            'gres': str,
            'gres_drained': str,
            'gres_used': str,
            'mcs_label': str,
            'name': str,
            'next_state_after_reboot': str,
            'next_state_after_reboot_flags': List[str],
            'address': str,
            'hostname': str,
            'state': str,
            'state_flags': List[str],
            'operating_system': str,
            'owner': str,
            'partitions': List[str],
            'port': int,
            'real_memory': int,
            'reason': str,
            'reason_changed_at': int,
            'reason_set_by_user': str,
            'slurmd_start_time': int,
            'sockets': int,
            'threads': int,
            'temporary_disk': int,
            'weight': int,
            'tres': str,
            'tres_used': str,
            'tres_weighted': float,
            'slurmd_version': str,
            'alloc_cpus': int,
            'idle_cpus': int,
            'alloc_memory': int
        }

        self.attribute_map = {
            'architecture': 'architecture',
            'burstbuffer_network_address': 'burstbuffer_network_address',
            'boards': 'boards',
            'boot_time': 'boot_time',
            'cores': 'cores',
            'cpu_binding': 'cpu_binding',
            'cpu_load': 'cpu_load',
            'free_memory': 'free_memory',
            'cpus': 'cpus',
            'features': 'features',
            'active_features': 'active_features',
            'gres': 'gres',
            'gres_drained': 'gres_drained',
            'gres_used': 'gres_used',
            'mcs_label': 'mcs_label',
            'name': 'name',
            'next_state_after_reboot': 'next_state_after_reboot',
            'next_state_after_reboot_flags': 'next_state_after_reboot_flags',
            'address': 'address',
            'hostname': 'hostname',
            'state': 'state',
            'state_flags': 'state_flags',
            'operating_system': 'operating_system',
            'owner': 'owner',
            'partitions': 'partitions',
            'port': 'port',
            'real_memory': 'real_memory',
            'reason': 'reason',
            'reason_changed_at': 'reason_changed_at',
            'reason_set_by_user': 'reason_set_by_user',
            'slurmd_start_time': 'slurmd_start_time',
            'sockets': 'sockets',
            'threads': 'threads',
            'temporary_disk': 'temporary_disk',
            'weight': 'weight',
            'tres': 'tres',
            'tres_used': 'tres_used',
            'tres_weighted': 'tres_weighted',
            'slurmd_version': 'slurmd_version',
            'alloc_cpus': 'alloc_cpus',
            'idle_cpus': 'idle_cpus',
            'alloc_memory': 'alloc_memory'
        }
        self._architecture = architecture
        self._burstbuffer_network_address = burstbuffer_network_address
        self._boards = boards
        self._boot_time = boot_time
        self._cores = cores
        self._cpu_binding = cpu_binding
        self._cpu_load = cpu_load
        self._free_memory = free_memory
        self._cpus = cpus
        self._features = features
        self._active_features = active_features
        self._gres = gres
        self._gres_drained = gres_drained
        self._gres_used = gres_used
        self._mcs_label = mcs_label
        self._name = name
        self._next_state_after_reboot = next_state_after_reboot
        self._next_state_after_reboot_flags = next_state_after_reboot_flags
        self._address = address
        self._hostname = hostname
        self._state = state
        self._state_flags = state_flags
        self._operating_system = operating_system
        self._owner = owner
        self._partitions = partitions
        self._port = port
        self._real_memory = real_memory
        self._reason = reason
        self._reason_changed_at = reason_changed_at
        self._reason_set_by_user = reason_set_by_user
        self._slurmd_start_time = slurmd_start_time
        self._sockets = sockets
        self._threads = threads
        self._temporary_disk = temporary_disk
        self._weight = weight
        self._tres = tres
        self._tres_used = tres_used
        self._tres_weighted = tres_weighted
        self._slurmd_version = slurmd_version
        self._alloc_cpus = alloc_cpus
        self._idle_cpus = idle_cpus
        self._alloc_memory = alloc_memory

    @classmethod
    def from_dict(cls, dikt) -> 'V0038Node':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_node of this V0038Node.  # noqa: E501
        :rtype: V0038Node
        """
        return util.deserialize_model(dikt, cls)

    @property
    def architecture(self) -> str:
        """Gets the architecture of this V0038Node.

        computer architecture  # noqa: E501

        :return: The architecture of this V0038Node.
        :rtype: str
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture: str):
        """Sets the architecture of this V0038Node.

        computer architecture  # noqa: E501

        :param architecture: The architecture of this V0038Node.
        :type architecture: str
        """

        self._architecture = architecture

    @property
    def burstbuffer_network_address(self) -> str:
        """Gets the burstbuffer_network_address of this V0038Node.

        BcastAddr  # noqa: E501

        :return: The burstbuffer_network_address of this V0038Node.
        :rtype: str
        """
        return self._burstbuffer_network_address

    @burstbuffer_network_address.setter
    def burstbuffer_network_address(self, burstbuffer_network_address: str):
        """Sets the burstbuffer_network_address of this V0038Node.

        BcastAddr  # noqa: E501

        :param burstbuffer_network_address: The burstbuffer_network_address of this V0038Node.
        :type burstbuffer_network_address: str
        """

        self._burstbuffer_network_address = burstbuffer_network_address

    @property
    def boards(self) -> int:
        """Gets the boards of this V0038Node.

        total number of boards per node  # noqa: E501

        :return: The boards of this V0038Node.
        :rtype: int
        """
        return self._boards

    @boards.setter
    def boards(self, boards: int):
        """Sets the boards of this V0038Node.

        total number of boards per node  # noqa: E501

        :param boards: The boards of this V0038Node.
        :type boards: int
        """

        self._boards = boards

    @property
    def boot_time(self) -> int:
        """Gets the boot_time of this V0038Node.

        timestamp of node boot  # noqa: E501

        :return: The boot_time of this V0038Node.
        :rtype: int
        """
        return self._boot_time

    @boot_time.setter
    def boot_time(self, boot_time: int):
        """Sets the boot_time of this V0038Node.

        timestamp of node boot  # noqa: E501

        :param boot_time: The boot_time of this V0038Node.
        :type boot_time: int
        """

        self._boot_time = boot_time

    @property
    def cores(self) -> int:
        """Gets the cores of this V0038Node.

        number of cores per socket  # noqa: E501

        :return: The cores of this V0038Node.
        :rtype: int
        """
        return self._cores

    @cores.setter
    def cores(self, cores: int):
        """Sets the cores of this V0038Node.

        number of cores per socket  # noqa: E501

        :param cores: The cores of this V0038Node.
        :type cores: int
        """

        self._cores = cores

    @property
    def cpu_binding(self) -> int:
        """Gets the cpu_binding of this V0038Node.

        Default task binding  # noqa: E501

        :return: The cpu_binding of this V0038Node.
        :rtype: int
        """
        return self._cpu_binding

    @cpu_binding.setter
    def cpu_binding(self, cpu_binding: int):
        """Sets the cpu_binding of this V0038Node.

        Default task binding  # noqa: E501

        :param cpu_binding: The cpu_binding of this V0038Node.
        :type cpu_binding: int
        """

        self._cpu_binding = cpu_binding

    @property
    def cpu_load(self) -> int:
        """Gets the cpu_load of this V0038Node.

        CPU load * 100  # noqa: E501

        :return: The cpu_load of this V0038Node.
        :rtype: int
        """
        return self._cpu_load

    @cpu_load.setter
    def cpu_load(self, cpu_load: int):
        """Sets the cpu_load of this V0038Node.

        CPU load * 100  # noqa: E501

        :param cpu_load: The cpu_load of this V0038Node.
        :type cpu_load: int
        """

        self._cpu_load = cpu_load

    @property
    def free_memory(self) -> int:
        """Gets the free_memory of this V0038Node.

        free memory in MiB  # noqa: E501

        :return: The free_memory of this V0038Node.
        :rtype: int
        """
        return self._free_memory

    @free_memory.setter
    def free_memory(self, free_memory: int):
        """Sets the free_memory of this V0038Node.

        free memory in MiB  # noqa: E501

        :param free_memory: The free_memory of this V0038Node.
        :type free_memory: int
        """

        self._free_memory = free_memory

    @property
    def cpus(self) -> int:
        """Gets the cpus of this V0038Node.

        configured count of cpus running on the node  # noqa: E501

        :return: The cpus of this V0038Node.
        :rtype: int
        """
        return self._cpus

    @cpus.setter
    def cpus(self, cpus: int):
        """Sets the cpus of this V0038Node.

        configured count of cpus running on the node  # noqa: E501

        :param cpus: The cpus of this V0038Node.
        :type cpus: int
        """

        self._cpus = cpus

    @property
    def features(self) -> str:
        """Gets the features of this V0038Node.


        :return: The features of this V0038Node.
        :rtype: str
        """
        return self._features

    @features.setter
    def features(self, features: str):
        """Sets the features of this V0038Node.


        :param features: The features of this V0038Node.
        :type features: str
        """

        self._features = features

    @property
    def active_features(self) -> str:
        """Gets the active_features of this V0038Node.

        list of a node's available features  # noqa: E501

        :return: The active_features of this V0038Node.
        :rtype: str
        """
        return self._active_features

    @active_features.setter
    def active_features(self, active_features: str):
        """Sets the active_features of this V0038Node.

        list of a node's available features  # noqa: E501

        :param active_features: The active_features of this V0038Node.
        :type active_features: str
        """

        self._active_features = active_features

    @property
    def gres(self) -> str:
        """Gets the gres of this V0038Node.

        list of a node's generic resources  # noqa: E501

        :return: The gres of this V0038Node.
        :rtype: str
        """
        return self._gres

    @gres.setter
    def gres(self, gres: str):
        """Sets the gres of this V0038Node.

        list of a node's generic resources  # noqa: E501

        :param gres: The gres of this V0038Node.
        :type gres: str
        """

        self._gres = gres

    @property
    def gres_drained(self) -> str:
        """Gets the gres_drained of this V0038Node.

        list of drained GRES  # noqa: E501

        :return: The gres_drained of this V0038Node.
        :rtype: str
        """
        return self._gres_drained

    @gres_drained.setter
    def gres_drained(self, gres_drained: str):
        """Sets the gres_drained of this V0038Node.

        list of drained GRES  # noqa: E501

        :param gres_drained: The gres_drained of this V0038Node.
        :type gres_drained: str
        """

        self._gres_drained = gres_drained

    @property
    def gres_used(self) -> str:
        """Gets the gres_used of this V0038Node.

        list of GRES in current use  # noqa: E501

        :return: The gres_used of this V0038Node.
        :rtype: str
        """
        return self._gres_used

    @gres_used.setter
    def gres_used(self, gres_used: str):
        """Sets the gres_used of this V0038Node.

        list of GRES in current use  # noqa: E501

        :param gres_used: The gres_used of this V0038Node.
        :type gres_used: str
        """

        self._gres_used = gres_used

    @property
    def mcs_label(self) -> str:
        """Gets the mcs_label of this V0038Node.

        mcs label if mcs plugin in use  # noqa: E501

        :return: The mcs_label of this V0038Node.
        :rtype: str
        """
        return self._mcs_label

    @mcs_label.setter
    def mcs_label(self, mcs_label: str):
        """Sets the mcs_label of this V0038Node.

        mcs label if mcs plugin in use  # noqa: E501

        :param mcs_label: The mcs_label of this V0038Node.
        :type mcs_label: str
        """

        self._mcs_label = mcs_label

    @property
    def name(self) -> str:
        """Gets the name of this V0038Node.

        node name to slurm  # noqa: E501

        :return: The name of this V0038Node.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this V0038Node.

        node name to slurm  # noqa: E501

        :param name: The name of this V0038Node.
        :type name: str
        """

        self._name = name

    @property
    def next_state_after_reboot(self) -> str:
        """Gets the next_state_after_reboot of this V0038Node.

        state after reboot  # noqa: E501

        :return: The next_state_after_reboot of this V0038Node.
        :rtype: str
        """
        return self._next_state_after_reboot

    @next_state_after_reboot.setter
    def next_state_after_reboot(self, next_state_after_reboot: str):
        """Sets the next_state_after_reboot of this V0038Node.

        state after reboot  # noqa: E501

        :param next_state_after_reboot: The next_state_after_reboot of this V0038Node.
        :type next_state_after_reboot: str
        """

        self._next_state_after_reboot = next_state_after_reboot

    @property
    def next_state_after_reboot_flags(self) -> List[str]:
        """Gets the next_state_after_reboot_flags of this V0038Node.

        node state flags  # noqa: E501

        :return: The next_state_after_reboot_flags of this V0038Node.
        :rtype: List[str]
        """
        return self._next_state_after_reboot_flags

    @next_state_after_reboot_flags.setter
    def next_state_after_reboot_flags(self, next_state_after_reboot_flags: List[str]):
        """Sets the next_state_after_reboot_flags of this V0038Node.

        node state flags  # noqa: E501

        :param next_state_after_reboot_flags: The next_state_after_reboot_flags of this V0038Node.
        :type next_state_after_reboot_flags: List[str]
        """

        self._next_state_after_reboot_flags = next_state_after_reboot_flags

    @property
    def address(self) -> str:
        """Gets the address of this V0038Node.

        state after reboot  # noqa: E501

        :return: The address of this V0038Node.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address: str):
        """Sets the address of this V0038Node.

        state after reboot  # noqa: E501

        :param address: The address of this V0038Node.
        :type address: str
        """

        self._address = address

    @property
    def hostname(self) -> str:
        """Gets the hostname of this V0038Node.

        node's hostname  # noqa: E501

        :return: The hostname of this V0038Node.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname: str):
        """Sets the hostname of this V0038Node.

        node's hostname  # noqa: E501

        :param hostname: The hostname of this V0038Node.
        :type hostname: str
        """

        self._hostname = hostname

    @property
    def state(self) -> str:
        """Gets the state of this V0038Node.

        current node state  # noqa: E501

        :return: The state of this V0038Node.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state: str):
        """Sets the state of this V0038Node.

        current node state  # noqa: E501

        :param state: The state of this V0038Node.
        :type state: str
        """

        self._state = state

    @property
    def state_flags(self) -> List[str]:
        """Gets the state_flags of this V0038Node.

        node state flags  # noqa: E501

        :return: The state_flags of this V0038Node.
        :rtype: List[str]
        """
        return self._state_flags

    @state_flags.setter
    def state_flags(self, state_flags: List[str]):
        """Sets the state_flags of this V0038Node.

        node state flags  # noqa: E501

        :param state_flags: The state_flags of this V0038Node.
        :type state_flags: List[str]
        """

        self._state_flags = state_flags

    @property
    def operating_system(self) -> str:
        """Gets the operating_system of this V0038Node.

        operating system  # noqa: E501

        :return: The operating_system of this V0038Node.
        :rtype: str
        """
        return self._operating_system

    @operating_system.setter
    def operating_system(self, operating_system: str):
        """Sets the operating_system of this V0038Node.

        operating system  # noqa: E501

        :param operating_system: The operating_system of this V0038Node.
        :type operating_system: str
        """

        self._operating_system = operating_system

    @property
    def owner(self) -> str:
        """Gets the owner of this V0038Node.

        User allowed to use this node  # noqa: E501

        :return: The owner of this V0038Node.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner: str):
        """Sets the owner of this V0038Node.

        User allowed to use this node  # noqa: E501

        :param owner: The owner of this V0038Node.
        :type owner: str
        """

        self._owner = owner

    @property
    def partitions(self) -> List[str]:
        """Gets the partitions of this V0038Node.

        assigned partitions  # noqa: E501

        :return: The partitions of this V0038Node.
        :rtype: List[str]
        """
        return self._partitions

    @partitions.setter
    def partitions(self, partitions: List[str]):
        """Sets the partitions of this V0038Node.

        assigned partitions  # noqa: E501

        :param partitions: The partitions of this V0038Node.
        :type partitions: List[str]
        """

        self._partitions = partitions

    @property
    def port(self) -> int:
        """Gets the port of this V0038Node.

        TCP port number of the slurmd  # noqa: E501

        :return: The port of this V0038Node.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port: int):
        """Sets the port of this V0038Node.

        TCP port number of the slurmd  # noqa: E501

        :param port: The port of this V0038Node.
        :type port: int
        """

        self._port = port

    @property
    def real_memory(self) -> int:
        """Gets the real_memory of this V0038Node.

        configured MB of real memory on the node  # noqa: E501

        :return: The real_memory of this V0038Node.
        :rtype: int
        """
        return self._real_memory

    @real_memory.setter
    def real_memory(self, real_memory: int):
        """Sets the real_memory of this V0038Node.

        configured MB of real memory on the node  # noqa: E501

        :param real_memory: The real_memory of this V0038Node.
        :type real_memory: int
        """

        self._real_memory = real_memory

    @property
    def reason(self) -> str:
        """Gets the reason of this V0038Node.

        reason for node being DOWN or DRAINING  # noqa: E501

        :return: The reason of this V0038Node.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this V0038Node.

        reason for node being DOWN or DRAINING  # noqa: E501

        :param reason: The reason of this V0038Node.
        :type reason: str
        """

        self._reason = reason

    @property
    def reason_changed_at(self) -> int:
        """Gets the reason_changed_at of this V0038Node.

        Time stamp when reason was set  # noqa: E501

        :return: The reason_changed_at of this V0038Node.
        :rtype: int
        """
        return self._reason_changed_at

    @reason_changed_at.setter
    def reason_changed_at(self, reason_changed_at: int):
        """Sets the reason_changed_at of this V0038Node.

        Time stamp when reason was set  # noqa: E501

        :param reason_changed_at: The reason_changed_at of this V0038Node.
        :type reason_changed_at: int
        """

        self._reason_changed_at = reason_changed_at

    @property
    def reason_set_by_user(self) -> str:
        """Gets the reason_set_by_user of this V0038Node.

        User that set the reason  # noqa: E501

        :return: The reason_set_by_user of this V0038Node.
        :rtype: str
        """
        return self._reason_set_by_user

    @reason_set_by_user.setter
    def reason_set_by_user(self, reason_set_by_user: str):
        """Sets the reason_set_by_user of this V0038Node.

        User that set the reason  # noqa: E501

        :param reason_set_by_user: The reason_set_by_user of this V0038Node.
        :type reason_set_by_user: str
        """

        self._reason_set_by_user = reason_set_by_user

    @property
    def slurmd_start_time(self) -> int:
        """Gets the slurmd_start_time of this V0038Node.

        timestamp of slurmd startup  # noqa: E501

        :return: The slurmd_start_time of this V0038Node.
        :rtype: int
        """
        return self._slurmd_start_time

    @slurmd_start_time.setter
    def slurmd_start_time(self, slurmd_start_time: int):
        """Sets the slurmd_start_time of this V0038Node.

        timestamp of slurmd startup  # noqa: E501

        :param slurmd_start_time: The slurmd_start_time of this V0038Node.
        :type slurmd_start_time: int
        """

        self._slurmd_start_time = slurmd_start_time

    @property
    def sockets(self) -> int:
        """Gets the sockets of this V0038Node.

        total number of sockets per node  # noqa: E501

        :return: The sockets of this V0038Node.
        :rtype: int
        """
        return self._sockets

    @sockets.setter
    def sockets(self, sockets: int):
        """Sets the sockets of this V0038Node.

        total number of sockets per node  # noqa: E501

        :param sockets: The sockets of this V0038Node.
        :type sockets: int
        """

        self._sockets = sockets

    @property
    def threads(self) -> int:
        """Gets the threads of this V0038Node.

        number of threads per core  # noqa: E501

        :return: The threads of this V0038Node.
        :rtype: int
        """
        return self._threads

    @threads.setter
    def threads(self, threads: int):
        """Sets the threads of this V0038Node.

        number of threads per core  # noqa: E501

        :param threads: The threads of this V0038Node.
        :type threads: int
        """

        self._threads = threads

    @property
    def temporary_disk(self) -> int:
        """Gets the temporary_disk of this V0038Node.

        configured MB of total disk in TMP_FS  # noqa: E501

        :return: The temporary_disk of this V0038Node.
        :rtype: int
        """
        return self._temporary_disk

    @temporary_disk.setter
    def temporary_disk(self, temporary_disk: int):
        """Sets the temporary_disk of this V0038Node.

        configured MB of total disk in TMP_FS  # noqa: E501

        :param temporary_disk: The temporary_disk of this V0038Node.
        :type temporary_disk: int
        """

        self._temporary_disk = temporary_disk

    @property
    def weight(self) -> int:
        """Gets the weight of this V0038Node.

        arbitrary priority of node for scheduling  # noqa: E501

        :return: The weight of this V0038Node.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight: int):
        """Sets the weight of this V0038Node.

        arbitrary priority of node for scheduling  # noqa: E501

        :param weight: The weight of this V0038Node.
        :type weight: int
        """

        self._weight = weight

    @property
    def tres(self) -> str:
        """Gets the tres of this V0038Node.

        TRES on node  # noqa: E501

        :return: The tres of this V0038Node.
        :rtype: str
        """
        return self._tres

    @tres.setter
    def tres(self, tres: str):
        """Sets the tres of this V0038Node.

        TRES on node  # noqa: E501

        :param tres: The tres of this V0038Node.
        :type tres: str
        """

        self._tres = tres

    @property
    def tres_used(self) -> str:
        """Gets the tres_used of this V0038Node.

        TRES used on node  # noqa: E501

        :return: The tres_used of this V0038Node.
        :rtype: str
        """
        return self._tres_used

    @tres_used.setter
    def tres_used(self, tres_used: str):
        """Sets the tres_used of this V0038Node.

        TRES used on node  # noqa: E501

        :param tres_used: The tres_used of this V0038Node.
        :type tres_used: str
        """

        self._tres_used = tres_used

    @property
    def tres_weighted(self) -> float:
        """Gets the tres_weighted of this V0038Node.

        TRES weight used on node  # noqa: E501

        :return: The tres_weighted of this V0038Node.
        :rtype: float
        """
        return self._tres_weighted

    @tres_weighted.setter
    def tres_weighted(self, tres_weighted: float):
        """Sets the tres_weighted of this V0038Node.

        TRES weight used on node  # noqa: E501

        :param tres_weighted: The tres_weighted of this V0038Node.
        :type tres_weighted: float
        """

        self._tres_weighted = tres_weighted

    @property
    def slurmd_version(self) -> str:
        """Gets the slurmd_version of this V0038Node.

        Slurmd version  # noqa: E501

        :return: The slurmd_version of this V0038Node.
        :rtype: str
        """
        return self._slurmd_version

    @slurmd_version.setter
    def slurmd_version(self, slurmd_version: str):
        """Sets the slurmd_version of this V0038Node.

        Slurmd version  # noqa: E501

        :param slurmd_version: The slurmd_version of this V0038Node.
        :type slurmd_version: str
        """

        self._slurmd_version = slurmd_version

    @property
    def alloc_cpus(self) -> int:
        """Gets the alloc_cpus of this V0038Node.

        Allocated CPUs  # noqa: E501

        :return: The alloc_cpus of this V0038Node.
        :rtype: int
        """
        return self._alloc_cpus

    @alloc_cpus.setter
    def alloc_cpus(self, alloc_cpus: int):
        """Sets the alloc_cpus of this V0038Node.

        Allocated CPUs  # noqa: E501

        :param alloc_cpus: The alloc_cpus of this V0038Node.
        :type alloc_cpus: int
        """

        self._alloc_cpus = alloc_cpus

    @property
    def idle_cpus(self) -> int:
        """Gets the idle_cpus of this V0038Node.

        Idle CPUs  # noqa: E501

        :return: The idle_cpus of this V0038Node.
        :rtype: int
        """
        return self._idle_cpus

    @idle_cpus.setter
    def idle_cpus(self, idle_cpus: int):
        """Sets the idle_cpus of this V0038Node.

        Idle CPUs  # noqa: E501

        :param idle_cpus: The idle_cpus of this V0038Node.
        :type idle_cpus: int
        """

        self._idle_cpus = idle_cpus

    @property
    def alloc_memory(self) -> int:
        """Gets the alloc_memory of this V0038Node.

        Allocated memory (MB)  # noqa: E501

        :return: The alloc_memory of this V0038Node.
        :rtype: int
        """
        return self._alloc_memory

    @alloc_memory.setter
    def alloc_memory(self, alloc_memory: int):
        """Sets the alloc_memory of this V0038Node.

        Allocated memory (MB)  # noqa: E501

        :param alloc_memory: The alloc_memory of this V0038Node.
        :type alloc_memory: int
        """

        self._alloc_memory = alloc_memory
