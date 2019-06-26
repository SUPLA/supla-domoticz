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
from swagger_client.models.big_decimal import BigDecimal  # noqa: F401,E501


class HumidityState(object):
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
        'humidity': 'BigDecimal'
    }

    attribute_map = {
        'connected': 'connected',
        'humidity': 'humidity'
    }

    def __init__(self, connected=None, humidity=None):  # noqa: E501
        """HumidityState - a model defined in Swagger"""  # noqa: E501
        self._connected = None
        self._humidity = None
        self.discriminator = None
        self.connected = connected
        if humidity is not None:
            self.humidity = humidity

    @property
    def connected(self):
        """Gets the connected of this HumidityState.  # noqa: E501


        :return: The connected of this HumidityState.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this HumidityState.


        :param connected: The connected of this HumidityState.  # noqa: E501
        :type: bool
        """
        if connected is None:
            raise ValueError("Invalid value for `connected`, must not be `None`")  # noqa: E501

        self._connected = connected

    @property
    def humidity(self):
        """Gets the humidity of this HumidityState.  # noqa: E501

        `humidity` contains current value of humidity provided by the sensor (including possibly configured delta adjustment), in percent; possible values from 0 to 100  # noqa: E501

        :return: The humidity of this HumidityState.  # noqa: E501
        :rtype: BigDecimal
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this HumidityState.

        `humidity` contains current value of humidity provided by the sensor (including possibly configured delta adjustment), in percent; possible values from 0 to 100  # noqa: E501

        :param humidity: The humidity of this HumidityState.  # noqa: E501
        :type: BigDecimal
        """

        self._humidity = humidity

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
        if issubclass(HumidityState, dict):
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
        if not isinstance(other, HumidityState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other