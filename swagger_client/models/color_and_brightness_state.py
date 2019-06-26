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


class ColorAndBrightnessState(object):
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
        'brightness': 'int',
        'color_brightness': 'int',
        'color': 'str'
    }

    attribute_map = {
        'connected': 'connected',
        'brightness': 'brightness',
        'color_brightness': 'color_brightness',
        'color': 'color'
    }

    def __init__(self, connected=None, brightness=None, color_brightness=None, color=None):  # noqa: E501
        """ColorAndBrightnessState - a model defined in Swagger"""  # noqa: E501
        self._connected = None
        self._brightness = None
        self._color_brightness = None
        self._color = None
        self.discriminator = None
        self.connected = connected
        if brightness is not None:
            self.brightness = brightness
        if color_brightness is not None:
            self.color_brightness = color_brightness
        if color is not None:
            self.color = color

    @property
    def connected(self):
        """Gets the connected of this ColorAndBrightnessState.  # noqa: E501


        :return: The connected of this ColorAndBrightnessState.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this ColorAndBrightnessState.


        :param connected: The connected of this ColorAndBrightnessState.  # noqa: E501
        :type: bool
        """
        if connected is None:
            raise ValueError("Invalid value for `connected`, must not be `None`")  # noqa: E501

        self._connected = connected

    @property
    def brightness(self):
        """Gets the brightness of this ColorAndBrightnessState.  # noqa: E501

        `brightness` contains current dimmer brightness value in percent, integer from 0 to 100  # noqa: E501

        :return: The brightness of this ColorAndBrightnessState.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this ColorAndBrightnessState.

        `brightness` contains current dimmer brightness value in percent, integer from 0 to 100  # noqa: E501

        :param brightness: The brightness of this ColorAndBrightnessState.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

    @property
    def color_brightness(self):
        """Gets the color_brightness of this ColorAndBrightnessState.  # noqa: E501

        `color_brightness` is a color brightness in percent, integer from 0 to 100  # noqa: E501

        :return: The color_brightness of this ColorAndBrightnessState.  # noqa: E501
        :rtype: int
        """
        return self._color_brightness

    @color_brightness.setter
    def color_brightness(self, color_brightness):
        """Sets the color_brightness of this ColorAndBrightnessState.

        `color_brightness` is a color brightness in percent, integer from 0 to 100  # noqa: E501

        :param color_brightness: The color_brightness of this ColorAndBrightnessState.  # noqa: E501
        :type: int
        """

        self._color_brightness = color_brightness

    @property
    def color(self):
        """Gets the color of this ColorAndBrightnessState.  # noqa: E501

        `color` contains the integer (hex) value of a current color, ranging from `0x000001` to `0xFFFFFF`  # noqa: E501

        :return: The color of this ColorAndBrightnessState.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ColorAndBrightnessState.

        `color` contains the integer (hex) value of a current color, ranging from `0x000001` to `0xFFFFFF`  # noqa: E501

        :param color: The color of this ColorAndBrightnessState.  # noqa: E501
        :type: str
        """

        self._color = color

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
        if issubclass(ColorAndBrightnessState, dict):
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
        if not isinstance(other, ColorAndBrightnessState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
