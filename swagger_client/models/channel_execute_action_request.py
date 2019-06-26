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
from swagger_client.models.channel_function_action_enum import ChannelFunctionActionEnum  # noqa: F401,E501


class ChannelExecuteActionRequest(object):
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
        'action': 'ChannelFunctionActionEnum',
        'percentage': 'int',
        'color': 'str',
        'color_brightness': 'int',
        'brightness': 'int'
    }

    attribute_map = {
        'action': 'action',
        'percentage': 'percentage',
        'color': 'color',
        'color_brightness': 'color_brightness',
        'brightness': 'brightness'
    }

    def __init__(self, action=None, percentage=None, color=None, color_brightness=None, brightness=None):  # noqa: E501
        """ChannelExecuteActionRequest - a model defined in Swagger"""  # noqa: E501
        self._action = None
        self._percentage = None
        self._color = None
        self._color_brightness = None
        self._brightness = None
        self.discriminator = None
        self.action = action
        if percentage is not None:
            self.percentage = percentage
        if color is not None:
            self.color = color
        if color_brightness is not None:
            self.color_brightness = color_brightness
        if brightness is not None:
            self.brightness = brightness

    @property
    def action(self):
        """Gets the action of this ChannelExecuteActionRequest.  # noqa: E501


        :return: The action of this ChannelExecuteActionRequest.  # noqa: E501
        :rtype: ChannelFunctionActionEnum
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ChannelExecuteActionRequest.


        :param action: The action of this ChannelExecuteActionRequest.  # noqa: E501
        :type: ChannelFunctionActionEnum
        """
        if action is None:
            raise ValueError("Invalid value for `action`, must not be `None`")  # noqa: E501

        self._action = action

    @property
    def percentage(self):
        """Gets the percentage of this ChannelExecuteActionRequest.  # noqa: E501


        :return: The percentage of this ChannelExecuteActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._percentage

    @percentage.setter
    def percentage(self, percentage):
        """Sets the percentage of this ChannelExecuteActionRequest.


        :param percentage: The percentage of this ChannelExecuteActionRequest.  # noqa: E501
        :type: int
        """

        self._percentage = percentage

    @property
    def color(self):
        """Gets the color of this ChannelExecuteActionRequest.  # noqa: E501


        :return: The color of this ChannelExecuteActionRequest.  # noqa: E501
        :rtype: str
        """
        return self._color

    @color.setter
    def color(self, color):
        """Sets the color of this ChannelExecuteActionRequest.


        :param color: The color of this ChannelExecuteActionRequest.  # noqa: E501
        :type: str
        """

        self._color = color

    @property
    def color_brightness(self):
        """Gets the color_brightness of this ChannelExecuteActionRequest.  # noqa: E501


        :return: The color_brightness of this ChannelExecuteActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._color_brightness

    @color_brightness.setter
    def color_brightness(self, color_brightness):
        """Sets the color_brightness of this ChannelExecuteActionRequest.


        :param color_brightness: The color_brightness of this ChannelExecuteActionRequest.  # noqa: E501
        :type: int
        """

        self._color_brightness = color_brightness

    @property
    def brightness(self):
        """Gets the brightness of this ChannelExecuteActionRequest.  # noqa: E501


        :return: The brightness of this ChannelExecuteActionRequest.  # noqa: E501
        :rtype: int
        """
        return self._brightness

    @brightness.setter
    def brightness(self, brightness):
        """Sets the brightness of this ChannelExecuteActionRequest.


        :param brightness: The brightness of this ChannelExecuteActionRequest.  # noqa: E501
        :type: int
        """

        self._brightness = brightness

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
        if issubclass(ChannelExecuteActionRequest, dict):
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
        if not isinstance(other, ChannelExecuteActionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other