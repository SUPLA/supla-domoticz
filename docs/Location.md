# Location

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Location identifier | [optional] 
**caption** | **str** | Location caption | [optional] 
**enabled** | **bool** | &#x60;true&#x60; if the location is enabled, &#x60;false&#x60; otherwise | [optional] 
**iodevices_ids** | **list[int]** | array containing the IO Devices identifiers assigned to this location | [optional] 
**channel_groups_ids** | **list[int]** | array containing the Channel groups identifiers assigned to this location | [optional] 
**channels_ids** | **list[int]** | array containing the Channels identifiers expicitely assigned to this location | [optional] 
**access_ids_ids** | **list[int]** | array containing the Access Identifiers identifiers assigned to this location | [optional] 
**password** | **str** | Location password (plain text). Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**iodevices** | [**list[Device]**](Device.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**channel_groups** | [**list[ChannelGroup]**](ChannelGroup.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**access_ids** | [**list[AccessIdentifier]**](AccessIdentifier.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**channels** | [**list[Channel]**](Channel.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)
