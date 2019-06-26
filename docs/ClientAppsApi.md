# swagger_client.ClientAppsApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_client_app**](ClientAppsApi.md#delete_client_app) | **DELETE** /client-apps/{id} | Delete Client App
[**get_client_apps**](ClientAppsApi.md#get_client_apps) | **GET** /client-apps | Get client apps
[**update_client_app**](ClientAppsApi.md#update_client_app) | **PUT** /client-apps/{id} | Update client app

# **delete_client_app**
> delete_client_app(id)

Delete Client App

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ClientAppsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Client App
    api_instance.delete_client_app(id)
except ApiException as e:
    print("Exception when calling ClientAppsApi->delete_client_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_apps**
> list[ClientApp] get_client_apps(include=include)

Get client apps

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ClientAppsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get client apps
    api_response = api_instance.get_client_apps(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAppsApi->get_client_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[ClientApp]**](ClientApp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_client_app**
> ClientApp update_client_app(body, id)

Update client app

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: OAuth2
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.ClientAppsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ClientAppUpdateRequest() # ClientAppUpdateRequest | 
id = 56 # int | 

try:
    # Update client app
    api_response = api_instance.update_client_app(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAppsApi->update_client_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ClientAppUpdateRequest**](ClientAppUpdateRequest.md)|  | 
 **id** | **int**|  | 

### Return type

[**ClientApp**](ClientApp.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

