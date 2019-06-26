# swagger_client.UserIconsApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_user_icon**](UserIconsApi.md#create_user_icon) | **POST** /user-icons | Create a new User Icon
[**delete_user_icon**](UserIconsApi.md#delete_user_icon) | **DELETE** /user-icons/{id} | Delete User Icon
[**get_user_icons**](UserIconsApi.md#get_user_icons) | **GET** /user-icons | Get user icons
[**user_icons_id_image_index_get**](UserIconsApi.md#user_icons_id_image_index_get) | **GET** /user-icons/{id}/{imageIndex} | Get User Icon image at specified index

# **create_user_icon**
> AccessIdentifier create_user_icon(function=function, source_icon=source_icon, image1=image1, image2=image2, image3=image3, image4=image4)

Create a new User Icon

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
api_instance = swagger_client.UserIconsApi(swagger_client.ApiClient(configuration))
function = swagger_client.ChannelFunctionEnumNames() # ChannelFunctionEnumNames |  (optional)
source_icon = 56 # int |  (optional)
image1 = 'image1_example' # str |  (optional)
image2 = 'image2_example' # str |  (optional)
image3 = 'image3_example' # str |  (optional)
image4 = 'image4_example' # str |  (optional)

try:
    # Create a new User Icon
    api_response = api_instance.create_user_icon(function=function, source_icon=source_icon, image1=image1, image2=image2, image3=image3, image4=image4)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserIconsApi->create_user_icon: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **function** | [**ChannelFunctionEnumNames**](.md)|  | [optional] 
 **source_icon** | **int**|  | [optional] 
 **image1** | **str**|  | [optional] 
 **image2** | **str**|  | [optional] 
 **image3** | **str**|  | [optional] 
 **image4** | **str**|  | [optional] 

### Return type

[**AccessIdentifier**](AccessIdentifier.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_icon**
> delete_user_icon(id)

Delete User Icon

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
api_instance = swagger_client.UserIconsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete User Icon
    api_instance.delete_user_icon(id)
except ApiException as e:
    print("Exception when calling UserIconsApi->delete_user_icon: %s\n" % e)
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

# **get_user_icons**
> list[UserIcon] get_user_icons(include=include, function=function, ids=ids)

Get user icons

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
api_instance = swagger_client.UserIconsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)
function = [swagger_client.ChannelFunctionEnumNames()] # list[ChannelFunctionEnumNames] | Return only icons for given function (optional)
ids = [56] # list[int] | Return only icons with given identifiers (optional)

try:
    # Get user icons
    api_response = api_instance.get_user_icons(include=include, function=function, ids=ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserIconsApi->get_user_icons: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 
 **function** | [**list[ChannelFunctionEnumNames]**](ChannelFunctionEnumNames.md)| Return only icons for given function | [optional] 
 **ids** | [**list[int]**](int.md)| Return only icons with given identifiers | [optional] 

### Return type

[**list[UserIcon]**](UserIcon.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **user_icons_id_image_index_get**
> str user_icons_id_image_index_get(id, image_index)

Get User Icon image at specified index

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
api_instance = swagger_client.UserIconsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
image_index = 56 # int | 

try:
    # Get User Icon image at specified index
    api_response = api_instance.user_icons_id_image_index_get(id, image_index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserIconsApi->user_icons_id_image_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **image_index** | **int**|  | 

### Return type

**str**

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: image/*

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

