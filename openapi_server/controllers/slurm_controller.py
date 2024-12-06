import connexion
from typing import Dict
from typing import Tuple
from typing import Union

from openapi_server.models.v0038_diag import V0038Diag  # noqa: E501
from openapi_server.models.v0038_errors import V0038Errors  # noqa: E501
from openapi_server.models.v0038_jobs_response import V0038JobsResponse  # noqa: E501
from openapi_server.models.v0038_licenses import V0038Licenses  # noqa: E501
from openapi_server.models.v0038_nodes_response import V0038NodesResponse  # noqa: E501
from openapi_server.models.v0038_partitions_response import V0038PartitionsResponse  # noqa: E501
from openapi_server.models.v0038_pings import V0038Pings  # noqa: E501
from openapi_server.models.v0038_reservations_response import V0038ReservationsResponse  # noqa: E501
from openapi_server import util


def slurm_v0038_diag():  # noqa: E501
    """get diagnostics

     # noqa: E501


    :rtype: Union[V0038Diag, Tuple[V0038Diag, int], Tuple[V0038Diag, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_job(job_id):  # noqa: E501
    """get job info

     # noqa: E501

    :param job_id: Slurm JobID
    :type job_id: str

    :rtype: Union[V0038JobsResponse, Tuple[V0038JobsResponse, int], Tuple[V0038JobsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_jobs(update_time=None):  # noqa: E501
    """get list of jobs

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: Union[V0038JobsResponse, Tuple[V0038JobsResponse, int], Tuple[V0038JobsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_node(node_name):  # noqa: E501
    """get node info

     # noqa: E501

    :param node_name: Slurm Node Name
    :type node_name: str

    :rtype: Union[V0038NodesResponse, Tuple[V0038NodesResponse, int], Tuple[V0038NodesResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_nodes(update_time=None):  # noqa: E501
    """get all node info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: Union[V0038NodesResponse, Tuple[V0038NodesResponse, int], Tuple[V0038NodesResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_partition(partition_name, update_time=None):  # noqa: E501
    """get partition info

     # noqa: E501

    :param partition_name: Slurm Partition Name
    :type partition_name: str
    :param update_time: Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time.
    :type update_time: int

    :rtype: Union[V0038PartitionsResponse, Tuple[V0038PartitionsResponse, int], Tuple[V0038PartitionsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_partitions(update_time=None):  # noqa: E501
    """get all partition info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: Union[V0038PartitionsResponse, Tuple[V0038PartitionsResponse, int], Tuple[V0038PartitionsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_reservation(reservation_name, update_time=None):  # noqa: E501
    """get reservation info

     # noqa: E501

    :param reservation_name: Slurm Reservation Name
    :type reservation_name: str
    :param update_time: Filter if no reservation (not limited to reservation in URL) changed since update_time.
    :type update_time: int

    :rtype: Union[V0038ReservationsResponse, Tuple[V0038ReservationsResponse, int], Tuple[V0038ReservationsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_get_reservations(update_time=None):  # noqa: E501
    """get all reservation info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: Union[V0038ReservationsResponse, Tuple[V0038ReservationsResponse, int], Tuple[V0038ReservationsResponse, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_ping():  # noqa: E501
    """ping test

     # noqa: E501


    :rtype: Union[V0038Pings, Tuple[V0038Pings, int], Tuple[V0038Pings, int, Dict[str, str]]
    """
    return 'do some magic!'


def slurm_v0038_slurmctld_get_licenses():  # noqa: E501
    """get all Slurm tracked license info

     # noqa: E501


    :rtype: Union[V0038Licenses, Tuple[V0038Licenses, int], Tuple[V0038Licenses, int, Dict[str, str]]
    """
    return 'do some magic!'
