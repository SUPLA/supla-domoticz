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


class ChannelType(object):
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
        'id': 'float',
        'name': 'str',
        'caption': 'str',
        'output': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'caption': 'caption',
        'output': 'output'
    }

    def __init__(self, id=None, name=None, caption=None, output=None):  # noqa: E501
        """ChannelType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._caption = None
        self._output = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if caption is not None:
            self.caption = caption
        if output is not None:
            self.output = output

    @property
    def id(self):
        """Gets the id of this ChannelType.  # noqa: E501

        Channel type identifier  # noqa: E501

        :return: The id of this ChannelType.  # noqa: E501
        :rtype: float
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChannelType.

        Channel type identifier  # noqa: E501

        :param id: The id of this ChannelType.  # noqa: E501
        :type: float
        """
        allowed_values = [1000, 1010, 1020, 1500, 2000, 2010, 2020, 2900, 3000, 3010, 3022, 3020, 3032, 3030, 3034, 3036, 3038, 3042, 3044, 3048, 3050, 3100, 4000, 4010, 4020]  # noqa: E501
        if id not in allowed_values:
            raise ValueError(
                "Invalid value for `id` ({0}), must be one of {1}"  # noqa: E501
                .format(id, allowed_values)
            )

        self._id = id

    @property
    def name(self):
        """Gets the name of this ChannelType.  # noqa: E501


        :return: The name of this ChannelType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChannelType.


        :param name: The name of this ChannelType.  # noqa: E501
        :type: str
        """
        allowed_values = ["SENSORNO", "SENSORNC", "DISTANCESENSOR", "CALLBUTTON", "RELAYHFD4", "RELAYG5LA1A", "RELAY2XG5LA1A", "RELAY", "THERMOMETERDS18B20", "DHT11", "DHT21", "DHT22", "AM2301", "AM2302", "THERMOMETER", "HUMIDITYSENSOR", "HUMIDITYANDTEMPSENSOR", "WINDSENSOR", "PRESSURESENSOR", "RAINSENSOR", "WEIGHTSENSOR", "WEATHER_STATION", "DIMMER", "RGBLEDCONTROLLER", "DIMMERANDRGBLED"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

    @property
    def caption(self):
        """Gets the caption of this ChannelType.  # noqa: E501


        :return: The caption of this ChannelType.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this ChannelType.


        :param caption: The caption of this ChannelType.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def output(self):
        """Gets the output of this ChannelType.  # noqa: E501

        Whether the channel is output type (i.e. can take action) or input (i.e. provide data)  # noqa: E501

        :return: The output of this ChannelType.  # noqa: E501
        :rtype: bool
        """
        return self._output

    @output.setter
    def output(self, output):
        """Sets the output of this ChannelType.

        Whether the channel is output type (i.e. can take action) or input (i.e. provide data)  # noqa: E501

        :param output: The output of this ChannelType.  # noqa: E501
        :type: bool
        """

        self._output = output

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
        if issubclass(ChannelType, dict):
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
        if not isinstance(other, ChannelType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
