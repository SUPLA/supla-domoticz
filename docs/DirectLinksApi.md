# swagger_client.DirectLinksApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_direct_link**](DirectLinksApi.md#create_direct_link) | **POST** /direct-links | Create a new Direct Link
[**delete_direct_link**](DirectLinksApi.md#delete_direct_link) | **DELETE** /direct-links/{id} | Delete Direct Link
[**get_direct_link**](DirectLinksApi.md#get_direct_link) | **GET** /direct-links/{id} | Get Direct Link
[**get_direct_link_audit**](DirectLinksApi.md#get_direct_link_audit) | **GET** /direct-links/{id}/audit | Get Direct Link audit
[**get_direct_links**](DirectLinksApi.md#get_direct_links) | **GET** /direct-links | Get Direct Links list
[**update_direct_link**](DirectLinksApi.md#update_direct_link) | **PUT** /direct-links/{id} | Update Direct Link

# **create_direct_link**
> DirectLink create_direct_link(body=body)

Create a new Direct Link

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
body = swagger_client.DirectLinkRequest() # DirectLinkRequest |  (optional)

try:
    # Create a new Direct Link
    api_response = api_instance.create_direct_link(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectLinksApi->create_direct_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DirectLinkRequest**](DirectLinkRequest.md)|  | [optional] 

### Return type

[**DirectLink**](DirectLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_direct_link**
> delete_direct_link(id)

Delete Direct Link

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Direct Link
    api_instance.delete_direct_link(id)
except ApiException as e:
    print("Exception when calling DirectLinksApi->delete_direct_link: %s\n" % e)
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

# **get_direct_link**
> DirectLink get_direct_link(id, include=include)

Get Direct Link

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get Direct Link
    api_response = api_instance.get_direct_link(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectLinksApi->get_direct_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**DirectLink**](DirectLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_link_audit**
> list[AuditEntry] get_direct_link_audit(id, page=page, page_size=page_size)

Get Direct Link audit

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
page = 56 # int | Page number, starting from 1. (optional)
page_size = 56 # int | Page size, default 10. (optional)

try:
    # Get Direct Link audit
    api_response = api_instance.get_direct_link_audit(id, page=page, page_size=page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectLinksApi->get_direct_link_audit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **page** | **int**| Page number, starting from 1. | [optional] 
 **page_size** | **int**| Page size, default 10. | [optional] 

### Return type

[**list[AuditEntry]**](AuditEntry.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_direct_links**
> list[DirectLink] get_direct_links(include=include, subject_type=subject_type, subject_id=subject_id)

Get Direct Links list

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)
subject_type = swagger_client.ActionableSubjectTypeEnum() # ActionableSubjectTypeEnum | Filter direct links by subjectType and subjectId (must go together). (optional)
subject_id = 56 # int | Filter direct links by subjectType and subjectId (must go together). (optional)

try:
    # Get Direct Links list
    api_response = api_instance.get_direct_links(include=include, subject_type=subject_type, subject_id=subject_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectLinksApi->get_direct_links: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 
 **subject_type** | [**ActionableSubjectTypeEnum**](.md)| Filter direct links by subjectType and subjectId (must go together). | [optional] 
 **subject_id** | **int**| Filter direct links by subjectType and subjectId (must go together). | [optional] 

### Return type

[**list[DirectLink]**](DirectLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_direct_link**
> DirectLink update_direct_link(id, body=body)

Update Direct Link

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
api_instance = swagger_client.DirectLinksApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
body = swagger_client.DirectLinkRequest() # DirectLinkRequest |  (optional)

try:
    # Update Direct Link
    api_response = api_instance.update_direct_link(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DirectLinksApi->update_direct_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **body** | [**DirectLinkRequest**](DirectLinkRequest.md)|  | [optional] 

### Return type

[**DirectLink**](DirectLink.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

