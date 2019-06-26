# swagger_client.ChannelGroupsApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_channel_group**](ChannelGroupsApi.md#create_channel_group) | **POST** /channel-groups | Create a new channel group
[**delete_channel_group**](ChannelGroupsApi.md#delete_channel_group) | **DELETE** /channel-groups/{id} | Delete Channel Group
[**execute_channel_group_action**](ChannelGroupsApi.md#execute_channel_group_action) | **PATCH** /channel-groups/{id} | Execute action on the channel group
[**get_channel_group**](ChannelGroupsApi.md#get_channel_group) | **GET** /channel-groups/{id} | Get channel group by ID
[**get_channel_groups**](ChannelGroupsApi.md#get_channel_groups) | **GET** /channel-groups | Get channels list
[**update_channel_group**](ChannelGroupsApi.md#update_channel_group) | **PUT** /channel-groups/{id} | Update channel group

# **create_channel_group**
> ChannelGroup create_channel_group(body)

Create a new channel group

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelGroupRequest() # ChannelGroupRequest | 

try:
    # Create a new channel group
    api_response = api_instance.create_channel_group(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->create_channel_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelGroupRequest**](ChannelGroupRequest.md)|  | 

### Return type

[**ChannelGroup**](ChannelGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_channel_group**
> delete_channel_group(id)

Delete Channel Group

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Channel Group
    api_instance.delete_channel_group(id)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->delete_channel_group: %s\n" % e)
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

# **execute_channel_group_action**
> execute_channel_group_action(body, id)

Execute action on the channel group

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelExecuteActionRequest() # ChannelExecuteActionRequest | Defines an action to execute on channel group. The `action` key is always required. The rest of the keys are params depending on the chosen action. Read more on [Github Wiki](https://github.com/SUPLA/supla-cloud/wiki/Channel-Actions).
id = 56 # int | 

try:
    # Execute action on the channel group
    api_instance.execute_channel_group_action(body, id)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->execute_channel_group_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelExecuteActionRequest**](ChannelExecuteActionRequest.md)| Defines an action to execute on channel group. The &#x60;action&#x60; key is always required. The rest of the keys are params depending on the chosen action. Read more on [Github Wiki](https://github.com/SUPLA/supla-cloud/wiki/Channel-Actions). | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_group**
> ChannelGroup get_channel_group(id, include=include)

Get channel group by ID

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get channel group by ID
    api_response = api_instance.get_channel_group(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->get_channel_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**ChannelGroup**](ChannelGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_groups**
> list[ChannelGroup] get_channel_groups(include=include)

Get channels list

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get channels list
    api_response = api_instance.get_channel_groups(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->get_channel_groups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[ChannelGroup]**](ChannelGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel_group**
> ChannelGroup update_channel_group(body, id)

Update channel group

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
api_instance = swagger_client.ChannelGroupsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelGroupRequest() # ChannelGroupRequest | 
id = 56 # int | 

try:
    # Update channel group
    api_response = api_instance.update_channel_group(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelGroupsApi->update_channel_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelGroupRequest**](ChannelGroupRequest.md)|  | 
 **id** | **int**|  | 

### Return type

[**ChannelGroup**](ChannelGroup.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

