# Channel

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Channel identifier | [optional] 
**channel_number** | **int** | Channel ordinal number in its IO Device | [optional] 
**caption** | **str** | Channel caption | [optional] 
**type** | [**ChannelType**](ChannelType.md) |  | [optional] 
**function** | [**ChannelFunction**](ChannelFunction.md) |  | [optional] 
**param1** | [**ChannelParam**](ChannelParam.md) |  | [optional] 
**param2** | [**ChannelParam**](ChannelParam.md) |  | [optional] 
**param3** | [**ChannelParam**](ChannelParam.md) |  | [optional] 
**text_param1** | **str** |  | [optional] 
**text_param2** | **str** |  | [optional] 
**text_param3** | **str** |  | [optional] 
**alt_icon** | **int** | Chosen alternative icon idenifier. Should not be greater than &#x60;funciton.maxAlternativeIconIndex&#x60; | [optional] 
**hidden** | **bool** | Whether this channel is shown on client apps or not | [optional] 
**inherited_location** | **bool** | Whether this channel inherits its IO Device&#x27;s location (&#x60;true&#x60;) or not (&#x60;false&#x60;) | [optional] 
**iodevice_id** | **int** |  | [optional] 
**location_id** | **int** |  | [optional] 
**function_id** | **int** |  | [optional] 
**type_id** | **int** |  | [optional] 
**user_icon_id** | **int** |  | [optional] 
**iodevice** | [**Device**](Device.md) |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**connected** | **bool** |  | [optional] 
**state** | [**ChannelState**](ChannelState.md) |  | [optional] 
**supported_functions** | [**list[ChannelFunction]**](ChannelFunction.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

