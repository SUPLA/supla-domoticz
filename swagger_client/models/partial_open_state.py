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


class PartialOpenState(object):
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
        'connected': 'bool',
        'hi': 'bool',
        'partial_hi': 'bool'
    }

    attribute_map = {
        'connected': 'connected',
        'hi': 'hi',
        'partial_hi': 'partial_hi'
    }

    def __init__(self, connected=None, hi=None, partial_hi=None):  # noqa: E501
        """PartialOpenState - a model defined in Swagger"""  # noqa: E501
        self._connected = None
        self._hi = None
        self._partial_hi = None
        self.discriminator = None
        self.connected = connected
        if hi is not None:
            self.hi = hi
        if partial_hi is not None:
            self.partial_hi = partial_hi

    @property
    def connected(self):
        """Gets the connected of this PartialOpenState.  # noqa: E501


        :return: The connected of this PartialOpenState.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this PartialOpenState.


        :param connected: The connected of this PartialOpenState.  # noqa: E501
        :type: bool
        """
        if connected is None:
            raise ValueError("Invalid value for `connected`, must not be `None`")  # noqa: E501

        self._connected = connected

    @property
    def hi(self):
        """Gets the hi of this PartialOpenState.  # noqa: E501

        `hi` is either `true` or `false` depending on sensor state  # noqa: E501

        :return: The hi of this PartialOpenState.  # noqa: E501
        :rtype: bool
        """
        return self._hi

    @hi.setter
    def hi(self, hi):
        """Sets the hi of this PartialOpenState.

        `hi` is either `true` or `false` depending on sensor state  # noqa: E501

        :param hi: The hi of this PartialOpenState.  # noqa: E501
        :type: bool
        """

        self._hi = hi

    @property
    def partial_hi(self):
        """Gets the partial_hi of this PartialOpenState.  # noqa: E501

        `partial_hi` is either `true` or `false` depending on paired secondary opening sensor state  # noqa: E501

        :return: The partial_hi of this PartialOpenState.  # noqa: E501
        :rtype: bool
        """
        return self._partial_hi

    @partial_hi.setter
    def partial_hi(self, partial_hi):
        """Sets the partial_hi of this PartialOpenState.

        `partial_hi` is either `true` or `false` depending on paired secondary opening sensor state  # noqa: E501

        :param partial_hi: The partial_hi of this PartialOpenState.  # noqa: E501
        :type: bool
        """

        self._partial_hi = partial_hi

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
        if issubclass(PartialOpenState, dict):
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
        if not isinstance(other, PartialOpenState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other