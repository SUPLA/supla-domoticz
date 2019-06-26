# swagger_client.AccessIdentifiersApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_identifier**](AccessIdentifiersApi.md#create_access_identifier) | **POST** /accessids | Create a new Access Identifier
[**delete_access_identifier**](AccessIdentifiersApi.md#delete_access_identifier) | **DELETE** /accessids/{id} | Delete Access Identifier
[**get_access_identifier**](AccessIdentifiersApi.md#get_access_identifier) | **GET** /accessids/{id} | Get Access Identifier
[**get_access_identifiers**](AccessIdentifiersApi.md#get_access_identifiers) | **GET** /accessids | Get Access Identifiers list
[**update_access_identifier**](AccessIdentifiersApi.md#update_access_identifier) | **PUT** /accessids/{id} | Update Access Identifier

# **create_access_identifier**
> AccessIdentifier create_access_identifier()

Create a new Access Identifier

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
api_instance = swagger_client.AccessIdentifiersApi(swagger_client.ApiClient(configuration))

try:
    # Create a new Access Identifier
    api_response = api_instance.create_access_identifier()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessIdentifiersApi->create_access_identifier: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccessIdentifier**](AccessIdentifier.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_access_identifier**
> delete_access_identifier(id)

Delete Access Identifier

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
api_instance = swagger_client.AccessIdentifiersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Access Identifier
    api_instance.delete_access_identifier(id)
except ApiException as e:
    print("Exception when calling AccessIdentifiersApi->delete_access_identifier: %s\n" % e)
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

# **get_access_identifier**
> AccessIdentifier get_access_identifier(id, include=include)

Get Access Identifier

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
api_instance = swagger_client.AccessIdentifiersApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get Access Identifier
    api_response = api_instance.get_access_identifier(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessIdentifiersApi->get_access_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**AccessIdentifier**](AccessIdentifier.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_access_identifiers**
> list[AccessIdentifier] get_access_identifiers(include=include)

Get Access Identifiers list

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
api_instance = swagger_client.AccessIdentifiersApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get Access Identifiers list
    api_response = api_instance.get_access_identifiers(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessIdentifiersApi->get_access_identifiers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[AccessIdentifier]**](AccessIdentifier.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_access_identifier**
> AccessIdentifier update_access_identifier(body, id)

Update Access Identifier

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
api_instance = swagger_client.AccessIdentifiersApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccessIdentifierUpdateRequest() # AccessIdentifierUpdateRequest | 
id = 56 # int | 

try:
    # Update Access Identifier
    api_response = api_instance.update_access_identifier(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccessIdentifiersApi->update_access_identifier: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AccessIdentifierUpdateRequest**](AccessIdentifierUpdateRequest.md)|  | 
 **id** | **int**|  | 

### Return type

[**AccessIdentifier**](AccessIdentifier.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

