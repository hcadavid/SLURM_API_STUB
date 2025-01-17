from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.v0038_meta_plugin import V0038MetaPlugin
from openapi_server.models.v0038_meta_slurm import V0038MetaSlurm
from openapi_server import util

from openapi_server.models.v0038_meta_plugin import V0038MetaPlugin  # noqa: E501
from openapi_server.models.v0038_meta_slurm import V0038MetaSlurm  # noqa: E501

class V0038Meta(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, plugin=None, slurm=None):  # noqa: E501
        """V0038Meta - a model defined in OpenAPI

        :param plugin: The plugin of this V0038Meta.  # noqa: E501
        :type plugin: V0038MetaPlugin
        :param slurm: The slurm of this V0038Meta.  # noqa: E501
        :type slurm: V0038MetaSlurm
        """
        self.openapi_types = {
            'plugin': V0038MetaPlugin,
            'slurm': V0038MetaSlurm
        }

        self.attribute_map = {
            'plugin': 'plugin',
            'slurm': 'Slurm'
        }

        self._plugin = plugin
        self._slurm = slurm

    @classmethod
    def from_dict(cls, dikt) -> 'V0038Meta':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The v0.0.38_meta of this V0038Meta.  # noqa: E501
        :rtype: V0038Meta
        """
        return util.deserialize_model(dikt, cls)

    @property
    def plugin(self) -> V0038MetaPlugin:
        """Gets the plugin of this V0038Meta.


        :return: The plugin of this V0038Meta.
        :rtype: V0038MetaPlugin
        """
        return self._plugin

    @plugin.setter
    def plugin(self, plugin: V0038MetaPlugin):
        """Sets the plugin of this V0038Meta.


        :param plugin: The plugin of this V0038Meta.
        :type plugin: V0038MetaPlugin
        """

        self._plugin = plugin

    @property
    def slurm(self) -> V0038MetaSlurm:
        """Gets the slurm of this V0038Meta.


        :return: The slurm of this V0038Meta.
        :rtype: V0038MetaSlurm
        """
        return self._slurm

    @slurm.setter
    def slurm(self, slurm: V0038MetaSlurm):
        """Sets the slurm of this V0038Meta.


        :param slurm: The slurm of this V0038Meta.
        :type slurm: V0038MetaSlurm
        """

        self._slurm = slurm
