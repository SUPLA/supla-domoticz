# Device

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Device identifier | [optional] 
**name** | **str** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**comment** | **str** |  | [optional] 
**reg_date** | **datetime** |  | [optional] 
**reg_ipv4** | **int** |  | [optional] 
**last_connected** | **datetime** |  | [optional] 
**last_ipv4** | **int** |  | [optional] 
**software_version** | **str** |  | [optional] 
**g_uid_string** | **str** |  | [optional] 
**location_id** | **int** |  | [optional] 
**original_location_id** | **int** |  | [optional] 
**channels_ids** | **list[int]** |  | [optional] 
**connected** | **bool** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**original_location** | [**Location**](Location.md) |  | [optional] 
**channels** | [**list[Channel]**](Channel.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**schedules** | [**list[Schedule]**](Schedule.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

