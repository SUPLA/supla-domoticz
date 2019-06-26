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
from swagger_client.models.channel_function import ChannelFunction  # noqa: F401,E501
from swagger_client.models.channel_param import ChannelParam  # noqa: F401,E501
from swagger_client.models.channel_state import ChannelState  # noqa: F401,E501
from swagger_client.models.channel_type import ChannelType  # noqa: F401,E501
from swagger_client.models.device import Device  # noqa: F401,E501
from swagger_client.models.location import Location  # noqa: F401,E501


class Channel(object):
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
        'channel_number': 'int',
        'caption': 'str',
        'type': 'ChannelType',
        'function': 'ChannelFunction',
        'param1': 'ChannelParam',
        'param2': 'ChannelParam',
        'param3': 'ChannelParam',
        'text_param1': 'str',
        'text_param2': 'str',
        'text_param3': 'str',
        'alt_icon': 'int',
        'hidden': 'bool',
        'inherited_location': 'bool',
        'iodevice_id': 'int',
        'location_id': 'int',
        'function_id': 'int',
        'type_id': 'int',
        'user_icon_id': 'int',
        'iodevice': 'Device',
        'location': 'Location',
        'connected': 'bool',
        'state': 'ChannelState',
        'supported_functions': 'list[ChannelFunction]'
    }

    attribute_map = {
        'id': 'id',
        'channel_number': 'channelNumber',
        'caption': 'caption',
        'type': 'type',
        'function': 'function',
        'param1': 'param1',
        'param2': 'param2',
        'param3': 'param3',
        'text_param1': 'textParam1',
        'text_param2': 'textParam2',
        'text_param3': 'textParam3',
        'alt_icon': 'altIcon',
        'hidden': 'hidden',
        'inherited_location': 'inheritedLocation',
        'iodevice_id': 'iodeviceId',
        'location_id': 'locationId',
        'function_id': 'functionId',
        'type_id': 'typeId',
        'user_icon_id': 'userIconId',
        'iodevice': 'iodevice',
        'location': 'location',
        'connected': 'connected',
        'state': 'state',
        'supported_functions': 'supportedFunctions'
    }

    def __init__(self, id=None, channel_number=None, caption=None, type=None, function=None, param1=None, param2=None, param3=None, text_param1=None, text_param2=None, text_param3=None, alt_icon=None, hidden=None, inherited_location=None, iodevice_id=None, location_id=None, function_id=None, type_id=None, user_icon_id=None, iodevice=None, location=None, connected=None, state=None, supported_functions=None):  # noqa: E501
        """Channel - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._channel_number = None
        self._caption = None
        self._type = None
        self._function = None
        self._param1 = None
        self._param2 = None
        self._param3 = None
        self._text_param1 = None
        self._text_param2 = None
        self._text_param3 = None
        self._alt_icon = None
        self._hidden = None
        self._inherited_location = None
        self._iodevice_id = None
        self._location_id = None
        self._function_id = None
        self._type_id = None
        self._user_icon_id = None
        self._iodevice = None
        self._location = None
        self._connected = None
        self._state = None
        self._supported_functions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if channel_number is not None:
            self.channel_number = channel_number
        if caption is not None:
            self.caption = caption
        if type is not None:
            self.type = type
        if function is not None:
            self.function = function
        if param1 is not None:
            self.param1 = param1
        if param2 is not None:
            self.param2 = param2
        if param3 is not None:
            self.param3 = param3
        if text_param1 is not None:
            self.text_param1 = text_param1
        if text_param2 is not None:
            self.text_param2 = text_param2
        if text_param3 is not None:
            self.text_param3 = text_param3
        if alt_icon is not None:
            self.alt_icon = alt_icon
        if hidden is not None:
            self.hidden = hidden
        if inherited_location is not None:
            self.inherited_location = inherited_location
        if iodevice_id is not None:
            self.iodevice_id = iodevice_id
        if location_id is not None:
            self.location_id = location_id
        if function_id is not None:
            self.function_id = function_id
        if type_id is not None:
            self.type_id = type_id
        if user_icon_id is not None:
            self.user_icon_id = user_icon_id
        if iodevice is not None:
            self.iodevice = iodevice
        if location is not None:
            self.location = location
        if connected is not None:
            self.connected = connected
        if state is not None:
            self.state = state
        if supported_functions is not None:
            self.supported_functions = supported_functions

    @property
    def id(self):
        """Gets the id of this Channel.  # noqa: E501

        Channel identifier  # noqa: E501

        :return: The id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Channel.

        Channel identifier  # noqa: E501

        :param id: The id of this Channel.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def channel_number(self):
        """Gets the channel_number of this Channel.  # noqa: E501

        Channel ordinal number in its IO Device  # noqa: E501

        :return: The channel_number of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._channel_number

    @channel_number.setter
    def channel_number(self, channel_number):
        """Sets the channel_number of this Channel.

        Channel ordinal number in its IO Device  # noqa: E501

        :param channel_number: The channel_number of this Channel.  # noqa: E501
        :type: int
        """

        self._channel_number = channel_number

    @property
    def caption(self):
        """Gets the caption of this Channel.  # noqa: E501

        Channel caption  # noqa: E501

        :return: The caption of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._caption

    @caption.setter
    def caption(self, caption):
        """Sets the caption of this Channel.

        Channel caption  # noqa: E501

        :param caption: The caption of this Channel.  # noqa: E501
        :type: str
        """

        self._caption = caption

    @property
    def type(self):
        """Gets the type of this Channel.  # noqa: E501


        :return: The type of this Channel.  # noqa: E501
        :rtype: ChannelType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Channel.


        :param type: The type of this Channel.  # noqa: E501
        :type: ChannelType
        """

        self._type = type

    @property
    def function(self):
        """Gets the function of this Channel.  # noqa: E501


        :return: The function of this Channel.  # noqa: E501
        :rtype: ChannelFunction
        """
        return self._function

    @function.setter
    def function(self, function):
        """Sets the function of this Channel.


        :param function: The function of this Channel.  # noqa: E501
        :type: ChannelFunction
        """

        self._function = function

    @property
    def param1(self):
        """Gets the param1 of this Channel.  # noqa: E501


        :return: The param1 of this Channel.  # noqa: E501
        :rtype: ChannelParam
        """
        return self._param1

    @param1.setter
    def param1(self, param1):
        """Sets the param1 of this Channel.


        :param param1: The param1 of this Channel.  # noqa: E501
        :type: ChannelParam
        """

        self._param1 = param1

    @property
    def param2(self):
        """Gets the param2 of this Channel.  # noqa: E501


        :return: The param2 of this Channel.  # noqa: E501
        :rtype: ChannelParam
        """
        return self._param2

    @param2.setter
    def param2(self, param2):
        """Sets the param2 of this Channel.


        :param param2: The param2 of this Channel.  # noqa: E501
        :type: ChannelParam
        """

        self._param2 = param2

    @property
    def param3(self):
        """Gets the param3 of this Channel.  # noqa: E501


        :return: The param3 of this Channel.  # noqa: E501
        :rtype: ChannelParam
        """
        return self._param3

    @param3.setter
    def param3(self, param3):
        """Sets the param3 of this Channel.


        :param param3: The param3 of this Channel.  # noqa: E501
        :type: ChannelParam
        """

        self._param3 = param3

    @property
    def text_param1(self):
        """Gets the text_param1 of this Channel.  # noqa: E501


        :return: The text_param1 of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._text_param1

    @text_param1.setter
    def text_param1(self, text_param1):
        """Sets the text_param1 of this Channel.


        :param text_param1: The text_param1 of this Channel.  # noqa: E501
        :type: str
        """

        self._text_param1 = text_param1

    @property
    def text_param2(self):
        """Gets the text_param2 of this Channel.  # noqa: E501


        :return: The text_param2 of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._text_param2

    @text_param2.setter
    def text_param2(self, text_param2):
        """Sets the text_param2 of this Channel.


        :param text_param2: The text_param2 of this Channel.  # noqa: E501
        :type: str
        """

        self._text_param2 = text_param2

    @property
    def text_param3(self):
        """Gets the text_param3 of this Channel.  # noqa: E501


        :return: The text_param3 of this Channel.  # noqa: E501
        :rtype: str
        """
        return self._text_param3

    @text_param3.setter
    def text_param3(self, text_param3):
        """Sets the text_param3 of this Channel.


        :param text_param3: The text_param3 of this Channel.  # noqa: E501
        :type: str
        """

        self._text_param3 = text_param3

    @property
    def alt_icon(self):
        """Gets the alt_icon of this Channel.  # noqa: E501

        Chosen alternative icon idenifier. Should not be greater than `funciton.maxAlternativeIconIndex`  # noqa: E501

        :return: The alt_icon of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._alt_icon

    @alt_icon.setter
    def alt_icon(self, alt_icon):
        """Sets the alt_icon of this Channel.

        Chosen alternative icon idenifier. Should not be greater than `funciton.maxAlternativeIconIndex`  # noqa: E501

        :param alt_icon: The alt_icon of this Channel.  # noqa: E501
        :type: int
        """

        self._alt_icon = alt_icon

    @property
    def hidden(self):
        """Gets the hidden of this Channel.  # noqa: E501

        Whether this channel is shown on client apps or not  # noqa: E501

        :return: The hidden of this Channel.  # noqa: E501
        :rtype: bool
        """
        return self._hidden

    @hidden.setter
    def hidden(self, hidden):
        """Sets the hidden of this Channel.

        Whether this channel is shown on client apps or not  # noqa: E501

        :param hidden: The hidden of this Channel.  # noqa: E501
        :type: bool
        """

        self._hidden = hidden

    @property
    def inherited_location(self):
        """Gets the inherited_location of this Channel.  # noqa: E501

        Whether this channel inherits its IO Device's location (`true`) or not (`false`)  # noqa: E501

        :return: The inherited_location of this Channel.  # noqa: E501
        :rtype: bool
        """
        return self._inherited_location

    @inherited_location.setter
    def inherited_location(self, inherited_location):
        """Sets the inherited_location of this Channel.

        Whether this channel inherits its IO Device's location (`true`) or not (`false`)  # noqa: E501

        :param inherited_location: The inherited_location of this Channel.  # noqa: E501
        :type: bool
        """

        self._inherited_location = inherited_location

    @property
    def iodevice_id(self):
        """Gets the iodevice_id of this Channel.  # noqa: E501


        :return: The iodevice_id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._iodevice_id

    @iodevice_id.setter
    def iodevice_id(self, iodevice_id):
        """Sets the iodevice_id of this Channel.


        :param iodevice_id: The iodevice_id of this Channel.  # noqa: E501
        :type: int
        """

        self._iodevice_id = iodevice_id

    @property
    def location_id(self):
        """Gets the location_id of this Channel.  # noqa: E501


        :return: The location_id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Channel.


        :param location_id: The location_id of this Channel.  # noqa: E501
        :type: int
        """

        self._location_id = location_id

    @property
    def function_id(self):
        """Gets the function_id of this Channel.  # noqa: E501


        :return: The function_id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._function_id

    @function_id.setter
    def function_id(self, function_id):
        """Sets the function_id of this Channel.


        :param function_id: The function_id of this Channel.  # noqa: E501
        :type: int
        """

        self._function_id = function_id

    @property
    def type_id(self):
        """Gets the type_id of this Channel.  # noqa: E501


        :return: The type_id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._type_id

    @type_id.setter
    def type_id(self, type_id):
        """Sets the type_id of this Channel.


        :param type_id: The type_id of this Channel.  # noqa: E501
        :type: int
        """

        self._type_id = type_id

    @property
    def user_icon_id(self):
        """Gets the user_icon_id of this Channel.  # noqa: E501


        :return: The user_icon_id of this Channel.  # noqa: E501
        :rtype: int
        """
        return self._user_icon_id

    @user_icon_id.setter
    def user_icon_id(self, user_icon_id):
        """Sets the user_icon_id of this Channel.


        :param user_icon_id: The user_icon_id of this Channel.  # noqa: E501
        :type: int
        """

        self._user_icon_id = user_icon_id

    @property
    def iodevice(self):
        """Gets the iodevice of this Channel.  # noqa: E501


        :return: The iodevice of this Channel.  # noqa: E501
        :rtype: Device
        """
        return self._iodevice

    @iodevice.setter
    def iodevice(self, iodevice):
        """Sets the iodevice of this Channel.


        :param iodevice: The iodevice of this Channel.  # noqa: E501
        :type: Device
        """

        self._iodevice = iodevice

    @property
    def location(self):
        """Gets the location of this Channel.  # noqa: E501


        :return: The location of this Channel.  # noqa: E501
        :rtype: Location
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this Channel.


        :param location: The location of this Channel.  # noqa: E501
        :type: Location
        """

        self._location = location

    @property
    def connected(self):
        """Gets the connected of this Channel.  # noqa: E501


        :return: The connected of this Channel.  # noqa: E501
        :rtype: bool
        """
        return self._connected

    @connected.setter
    def connected(self, connected):
        """Sets the connected of this Channel.


        :param connected: The connected of this Channel.  # noqa: E501
        :type: bool
        """

        self._connected = connected

    @property
    def state(self):
        """Gets the state of this Channel.  # noqa: E501


        :return: The state of this Channel.  # noqa: E501
        :rtype: ChannelState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Channel.


        :param state: The state of this Channel.  # noqa: E501
        :type: ChannelState
        """

        self._state = state

    @property
    def supported_functions(self):
        """Gets the supported_functions of this Channel.  # noqa: E501


        :return: The supported_functions of this Channel.  # noqa: E501
        :rtype: list[ChannelFunction]
        """
        return self._supported_functions

    @supported_functions.setter
    def supported_functions(self, supported_functions):
        """Sets the supported_functions of this Channel.


        :param supported_functions: The supported_functions of this Channel.  # noqa: E501
        :type: list[ChannelFunction]
        """

        self._supported_functions = supported_functions

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
        if issubclass(Channel, dict):
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
        if not isinstance(other, Channel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
