# AccessIdentifier

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Access Identifier identifier | [optional] 
**caption** | **str** | Location caption | [optional] 
**enabled** | **bool** | &#x60;true&#x60; if the location is enabled, &#x60;false&#x60; otherwise | [optional] 
**locations_ids** | **list[int]** | array containing the location idenfifiers assigned to this access ID | [optional] 
**client_apps_ids** | **list[int]** | array containing the client apps idenfifiers assigned to this access ID | [optional] 
**locations** | [**list[Location]**](Location.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 
**client_apps** | [**list[ClientApp]**](ClientApp.md) | Returned only if requested by the &#x60;include&#x60; parameter. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

