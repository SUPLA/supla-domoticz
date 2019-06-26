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


class AccessIdentifierUpdateRequest(object):
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
        'enabled': 'bool',
        'caption': 'str',
        'password': 'str',
        'locations_ids': 'list[int]',
        'client_apps_ids': 'list[int]'
    }

    attribute_map = {
        'enabled': 'enabled',
        'caption': 'caption',
        'password': 'password',
        'locations_ids': 'locationsIds',
        'client_apps_ids': 'clientAppsIds'
    }

    def __init__(self, enabled=None, caption=None, password=None, locations_ids=None, client_apps_ids=None):  # noqa: E501
        """AccessIdentifierUpdateRequest - a model defined in Swagger"""  # noqa: E501
        self._enabled = None
        self._caption = None
        self._password = None
        self._locations_ids = None
        self._client_apps_ids = None
        self.discriminator = None
        if enabled is not None:
            self.enabled = enabled
        if caption is not None:
            self.caption = caption
        if password is not None:
            self.password = password
        if locations_ids is not None:
            self.locations_ids = locations_ids
        if client_apps_ids is not None:
            self.client_apps_ids = client_apps_ids

    @property
    def enabled(self):
        """Gets the enabled of this AccessIdentifierUpdateRequest.  # noqa: E501


        :return: The enabled of this AccessIdentifierUpdateRequest.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this AccessIdentifierUpdateRequest.


        :param enabled: The enabled of this AccessIdentifierUpdateRequest.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def caption(self):
        """Gets the caption of this AccessIdentifierUpdateRequest.  # noqa: E501


        :return: The caption of this AccessIdentifierUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this AccessIdentifierUpdateRequest.


        :param caption: The caption of this AccessIdentifierUpdateRequest.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def password(self):
        """Gets the password of this AccessIdentifierUpdateRequest.  # noqa: E501

        Provide new password if you want to change it.  # noqa: E501

        :return: The password of this AccessIdentifierUpdateRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this AccessIdentifierUpdateRequest.

        Provide new password if you want to change it.  # noqa: E501

        :param password: The password of this AccessIdentifierUpdateRequest.  # noqa: E501
        :type: str
        """

        self._password = password

    @property
    def locations_ids(self):
        """Gets the locations_ids of this AccessIdentifierUpdateRequest.  # noqa: E501

        Locations identifiers to assign to this Access Identifier.  # noqa: E501

        :return: The locations_ids of this AccessIdentifierUpdateRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._locations_ids

    @locations_ids.setter
    def locations_ids(self, locations_ids):
        """Sets the locations_ids of this AccessIdentifierUpdateRequest.

        Locations identifiers to assign to this Access Identifier.  # noqa: E501

        :param locations_ids: The locations_ids of this AccessIdentifierUpdateRequest.  # noqa: E501
        :type: list[int]
        """

        self._locations_ids = locations_ids

    @property
    def client_apps_ids(self):
        """Gets the client_apps_ids of this AccessIdentifierUpdateRequest.  # noqa: E501

        Client Apps identifiers to assign to this Access Identifier. If client app is connected to any other Client ID, it will be disconnected from the old one before assigning.  # noqa: E501

        :return: The client_apps_ids of this AccessIdentifierUpdateRequest.  # noqa: E501
        :rtype: list[int]
        """
        return self._client_apps_ids

    @client_apps_ids.setter
    def client_apps_ids(self, client_apps_ids):
        """Sets the client_apps_ids of this AccessIdentifierUpdateRequest.

        Client Apps identifiers to assign to this Access Identifier. If client app is connected to any other Client ID, it will be disconnected from the old one before assigning.  # noqa: E501

        :param client_apps_ids: The client_apps_ids of this AccessIdentifierUpdateRequest.  # noqa: E501
        :type: list[int]
        """

        self._client_apps_ids = client_apps_ids

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
        if issubclass(AccessIdentifierUpdateRequest, dict):
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
        if not isinstance(other, AccessIdentifierUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
