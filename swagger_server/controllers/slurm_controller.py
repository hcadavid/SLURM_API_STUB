import connexion
import six

from swagger_server.models.v0038_diag import V0038Diag  # noqa: E501
from swagger_server.models.v0038_errors import V0038Errors  # noqa: E501
from swagger_server.models.v0038_jobs_response import V0038JobsResponse  # noqa: E501
from swagger_server.models.v0038_licenses import V0038Licenses  # noqa: E501
from swagger_server.models.v0038_nodes_response import V0038NodesResponse  # noqa: E501
from swagger_server.models.v0038_partitions_response import V0038PartitionsResponse  # noqa: E501
from swagger_server.models.v0038_pings import V0038Pings  # noqa: E501
from swagger_server.models.v0038_reservations_response import V0038ReservationsResponse  # noqa: E501
from swagger_server import util


def slurm_v0038_diag():  # noqa: E501
    """get diagnostics

     # noqa: E501


    :rtype: V0038Diag
    """
    return 'do some magic!'


def slurm_v0038_get_job(job_id):  # noqa: E501
    """get job info

     # noqa: E501

    :param job_id: Slurm JobID
    :type job_id: str

    :rtype: V0038JobsResponse
    """
    return 'do some magic!'


def slurm_v0038_get_jobs(update_time=None):  # noqa: E501
    """get list of jobs

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: V0038JobsResponse
    """
    return 'do some magic!'


def slurm_v0038_get_node(node_name):  # noqa: E501
    """get node info

     # noqa: E501

    :param node_name: Slurm Node Name
    :type node_name: str

    :rtype: V0038NodesResponse
    """
    return 'do some magic!'


def slurm_v0038_get_nodes(update_time=None):  # noqa: E501
    """get all node info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: V0038NodesResponse
    """
    return 'do some magic!'


def slurm_v0038_get_partition(partition_name, update_time=None):  # noqa: E501
    """get partition info

     # noqa: E501

    :param partition_name: Slurm Partition Name
    :type partition_name: str
    :param update_time: Filter if there were no partition changes (not limited to partition in URL endpoint) since update_time.
    :type update_time: int

    :rtype: V0038PartitionsResponse
    """
    return 'do some magic!'


def slurm_v0038_get_partitions(update_time=None):  # noqa: E501
    """get all partition info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: V0038PartitionsResponse
    """
    return 'do some magic!'


def slurm_v0038_get_reservation(reservation_name, update_time=None):  # noqa: E501
    """get reservation info

     # noqa: E501

    :param reservation_name: Slurm Reservation Name
    :type reservation_name: str
    :param update_time: Filter if no reservation (not limited to reservation in URL) changed since update_time.
    :type update_time: int

    :rtype: V0038ReservationsResponse
    """
    return 'do some magic!'


def slurm_v0038_get_reservations(update_time=None):  # noqa: E501
    """get all reservation info

     # noqa: E501

    :param update_time: Filter if changed since update_time. Use of this parameter can result in faster replies.
    :type update_time: int

    :rtype: V0038ReservationsResponse
    """
    return 'do some magic!'


def slurm_v0038_ping():  # noqa: E501
    """ping test

     # noqa: E501


    :rtype: V0038Pings
    """
    return 'do some magic!'


def slurm_v0038_slurmctld_get_licenses():  # noqa: E501
    """get all Slurm tracked license info

     # noqa: E501


    :rtype: V0038Licenses
    """
    return 'do some magic!'
