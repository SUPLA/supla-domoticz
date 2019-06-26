# swagger_client.LocationsApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_location**](LocationsApi.md#create_location) | **POST** /locations | Create a new location
[**delete_location**](LocationsApi.md#delete_location) | **DELETE** /locations/{id} | Delete location
[**get_location**](LocationsApi.md#get_location) | **GET** /locations/{id} | Get location by ID
[**get_locations**](LocationsApi.md#get_locations) | **GET** /locations | Get locations list
[**update_location**](LocationsApi.md#update_location) | **PUT** /locations/{id} | Update location

# **create_location**
> Location create_location()

Create a new location

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))

try:
    # Create a new location
    api_response = api_instance.create_location()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->create_location: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Location**](Location.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_location**
> delete_location(id, include=include)

Delete location

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Delete location
    api_instance.delete_location(id, include=include)
except ApiException as e:
    print("Exception when calling LocationsApi->delete_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_location**
> Location get_location(id, include=include)

Get location by ID

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get location by ID
    api_response = api_instance.get_location(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_locations**
> list[Location] get_locations(include=include)

Get locations list

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get locations list
    api_response = api_instance.get_locations(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->get_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[Location]**](Location.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_location**
> Location update_location(body, id, include=include)

Update location

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
api_instance = swagger_client.LocationsApi(swagger_client.ApiClient(configuration))
body = swagger_client.LocationUpdateRequest() # LocationUpdateRequest | 
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Update location
    api_response = api_instance.update_location(body, id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LocationsApi->update_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**LocationUpdateRequest**](LocationUpdateRequest.md)|  | 
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**Location**](Location.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

