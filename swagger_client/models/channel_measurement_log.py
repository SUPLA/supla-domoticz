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


class ChannelMeasurementLog(object):
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
        'date_timestamp': 'int',
        'temperature': 'float',
        'humidity': 'float'
    }

    attribute_map = {
        'date_timestamp': 'date_timestamp',
        'temperature': 'temperature',
        'humidity': 'humidity'
    }

    def __init__(self, date_timestamp=None, temperature=None, humidity=None):  # noqa: E501
        """ChannelMeasurementLog - a model defined in Swagger"""  # noqa: E501
        self._date_timestamp = None
        self._temperature = None
        self._humidity = None
        self.discriminator = None
        if date_timestamp is not None:
            self.date_timestamp = date_timestamp
        if temperature is not None:
            self.temperature = temperature
        if humidity is not None:
            self.humidity = humidity

    @property
    def date_timestamp(self):
        """Gets the date_timestamp of this ChannelMeasurementLog.  # noqa: E501


        :return: The date_timestamp of this ChannelMeasurementLog.  # noqa: E501
        :rtype: int
        """
        return self._date_timestamp

    @date_timestamp.setter
    def date_timestamp(self, date_timestamp):
        """Sets the date_timestamp of this ChannelMeasurementLog.


        :param date_timestamp: The date_timestamp of this ChannelMeasurementLog.  # noqa: E501
        :type: int
        """

        self._date_timestamp = date_timestamp

    @property
    def temperature(self):
        """Gets the temperature of this ChannelMeasurementLog.  # noqa: E501

        Temperature in Celsius  # noqa: E501

        :return: The temperature of this ChannelMeasurementLog.  # noqa: E501
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        """Sets the temperature of this ChannelMeasurementLog.

        Temperature in Celsius  # noqa: E501

        :param temperature: The temperature of this ChannelMeasurementLog.  # noqa: E501
        :type: float
        """

        self._temperature = temperature

    @property
    def humidity(self):
        """Gets the humidity of this ChannelMeasurementLog.  # noqa: E501

        Humidity percent. Available only if channel function is `HUMIDITYANDTEMPERATURE`.  # noqa: E501

        :return: The humidity of this ChannelMeasurementLog.  # noqa: E501
        :rtype: float
        """
        return self._humidity

    @humidity.setter
    def humidity(self, humidity):
        """Sets the humidity of this ChannelMeasurementLog.

        Humidity percent. Available only if channel function is `HUMIDITYANDTEMPERATURE`.  # noqa: E501

        :param humidity: The humidity of this ChannelMeasurementLog.  # noqa: E501
        :type: float
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
        if issubclass(ChannelMeasurementLog, dict):
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
        if not isinstance(other, ChannelMeasurementLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other