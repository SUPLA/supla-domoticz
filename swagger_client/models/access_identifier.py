# coding: utf-8

"""
    SUPLA Cloud API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 2.3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six
from swagger_client.models.client_app import ClientApp  # noqa: F401,E501
from swagger_client.models.location import Location  # noqa: F401,E501


class AccessIdentifier(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'caption': 'str',
        'enabled': 'bool',
        'locations_ids': 'list[int]',
        'client_apps_ids': 'list[int]',
        'locations': 'list[Location]',
        'client_apps': 'list[ClientApp]'
    }

    attribute_map = {
        'id': 'id',
        'caption': 'caption',
        'enabled': 'enabled',
        'locations_ids': 'locationsIds',
        'client_apps_ids': 'clientAppsIds',
        'locations': 'locations',
        'client_apps': 'clientApps'
    }

    def __init__(self, id=None, caption=None, enabled=None, locations_ids=None, client_apps_ids=None, locations=None, client_apps=None):  # noqa: E501
        """AccessIdentifier - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._caption = None
        self._enabled = None
        self._locations_ids = None
        self._client_apps_ids = None
        self._locations = None
        self._client_apps = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if caption is not None:
            self.caption = caption
        if enabled is not None:
            self.enabled = enabled
        if locations_ids is not None:
            self.locations_ids = locations_ids
        if client_apps_ids is not None:
            self.client_apps_ids = client_apps_ids
        if locations is not None:
            self.locations = locations
        if client_apps is not None:
            self.client_apps = client_apps

    @property
    def id(self):
        """Gets the id of this AccessIdentifier.  # noqa: E501

        Access Identifier identifier  # noqa: E501

        :return: The id of this AccessIdentifier.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccessIdentifier.

        Access Identifier identifier  # noqa: E501

        :param id: The id of this AccessIdentifier.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def caption(self):
        """Gets the caption of this AccessIdentifier.  # noqa: E501

        Location caption  # noqa: E501

        :return: The caption of this AccessIdentifier.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this AccessIdentifier.

        Location caption  # noqa: E501

        :param caption: The caption of this AccessIdentifier.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def enabled(self):
        """Gets the enabled of this AccessIdentifier.  # noqa: E501

        `true` if the location is enabled, `false` otherwise  # noqa: E501

        :return: The enabled of this AccessIdentifier.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AccessIdentifier.

        `true` if the location is enabled, `false` otherwise  # noqa: E501

        :param enabled: The enabled of this AccessIdentifier.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def locations_ids(self):
        """Gets the locations_ids of this AccessIdentifier.  # noqa: E501

        array containing the location idenfifiers assigned to this access ID  # noqa: E501

        :return: The locations_ids of this AccessIdentifier.  # noqa: E501
        :rtype: list[int]
        """
        return self._locations_ids

    @locations_ids.setter
    def locations_ids(self, locations_ids):
        """Sets the locations_ids of this AccessIdentifier.

        array containing the location idenfifiers assigned to this access ID  # noqa: E501

        :param locations_ids: The locations_ids of this AccessIdentifier.  # noqa: E501
        :type: list[int]
        """

        self._locations_ids = locations_ids

    @property
    def client_apps_ids(self):
        """Gets the client_apps_ids of this AccessIdentifier.  # noqa: E501

        array containing the client apps idenfifiers assigned to this access ID  # noqa: E501

        :return: The client_apps_ids of this AccessIdentifier.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_apps_ids

    @client_apps_ids.setter
    def client_apps_ids(self, client_apps_ids):
        """Sets the client_apps_ids of this AccessIdentifier.

        array containing the client apps idenfifiers assigned to this access ID  # noqa: E501

        :param client_apps_ids: The client_apps_ids of this AccessIdentifier.  # noqa: E501
        :type: list[int]
        """

        self._client_apps_ids = client_apps_ids

    @property
    def locations(self):
        """Gets the locations of this AccessIdentifier.  # noqa: E501

        Returned only if requested by the `include` parameter.  # noqa: E501

        :return: The locations of this AccessIdentifier.  # noqa: E501
        :rtype: list[Location]
        """
        return self._locations

    @locations.setter
    def locations(self, locations):
        """Sets the locations of this AccessIdentifier.

        Returned only if requested by the `include` parameter.  # noqa: E501

        :param locations: The locations of this AccessIdentifier.  # noqa: E501
        :type: list[Location]
        """

        self._locations = locations

    @property
    def client_apps(self):
        """Gets the client_apps of this AccessIdentifier.  # noqa: E501

        Returned only if requested by the `include` parameter.  # noqa: E501

        :return: The client_apps of this AccessIdentifier.  # noqa: E501
        :rtype: list[ClientApp]
        """
        return self._client_apps

    @client_apps.setter
    def client_apps(self, client_apps):
        """Sets the client_apps of this AccessIdentifier.

        Returned only if requested by the `include` parameter.  # noqa: E501

        :param client_apps: The client_apps of this AccessIdentifier.  # noqa: E501
        :type: list[ClientApp]
        """

        self._client_apps = client_apps

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(AccessIdentifier, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AccessIdentifier):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
