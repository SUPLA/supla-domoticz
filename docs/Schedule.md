# Schedule

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Schedule identifier | [optional] 
**time_expression** | **str** | Schedule time expression in crontab notation (with some custom additions). | [optional] 
**action** | [**ChannelFunctionAction**](ChannelFunctionAction.md) |  | [optional] 
**action_param** | [**Object**](Object.md) | Depends on the action. | [optional] 
**mode** | **str** |  | [optional] 
**date_start** | **datetime** |  | [optional] 
**date_end** | **datetime** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**caption** | **str** |  | [optional] 
**retry** | **bool** |  | [optional] 
**channel_id** | **int** |  | [optional] 
**action_id** | **int** |  | [optional] 
**channel** | [**Channel**](Channel.md) |  | [optional] 
**closest_executions** | [**list[ScheduleClosestExecutions]**](ScheduleClosestExecutions.md) | Returned only if requested by the &#x60;include&#x60; parameter. Contains two arrays of maximum 3 closest past and future executions. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

