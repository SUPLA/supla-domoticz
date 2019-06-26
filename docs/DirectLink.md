# DirectLink

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Direct Link identifier | [optional] 
**caption** | **str** | Direct Link caption | [optional] 
**executions_limit** | **int** |  | [optional] 
**last_used** | **datetime** |  | [optional] 
**last_ipv4** | **int** |  | [optional] 
**enabled** | **bool** |  | [optional] 
**disable_http_get** | **bool** |  | [optional] 
**active_date_range** | [**DirectLinkActiveDateRange**](DirectLinkActiveDateRange.md) |  | [optional] 
**slug** | **str** | Returned only immediately after creation | [optional] 
**url** | **str** | Returned only immediately after creation | [optional] 
**subject_id** | **int** |  | [optional] 
**subject_type** | [**ActionableSubjectTypeEnum**](ActionableSubjectTypeEnum.md) |  | [optional] 
**allowed_actions** | [**list[ChannelFunctionActionEnum]**](ChannelFunctionActionEnum.md) |  | [optional] 
**active** | **bool** |  | [optional] 
**inactive_reason** | **str** | Returned only if active is &#x60;false&#x60; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

