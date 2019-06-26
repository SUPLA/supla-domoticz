# swagger_client.SchedulesApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_schedule**](SchedulesApi.md#create_schedule) | **POST** /schedules | Create a new schedule
[**delete_schedule**](SchedulesApi.md#delete_schedule) | **DELETE** /schedules/{id} | Delete Schedule
[**enable_schedules**](SchedulesApi.md#enable_schedules) | **PATCH** /schedules | Enable schedules
[**get_schedule**](SchedulesApi.md#get_schedule) | **GET** /schedules/{id} | Get Schedule
[**get_schedules**](SchedulesApi.md#get_schedules) | **GET** /schedules | Get schedules list
[**update_schedule**](SchedulesApi.md#update_schedule) | **PUT** /schedules/{id} | Update schedule

# **create_schedule**
> Schedule create_schedule(body)

Create a new schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleRequest() # ScheduleRequest | 

try:
    # Create a new schedule
    api_response = api_instance.create_schedule(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->create_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)|  | 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_schedule**
> delete_schedule(id)

Delete Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Delete Schedule
    api_instance.delete_schedule(id)
except ApiException as e:
    print("Exception when calling SchedulesApi->delete_schedule: %s\n" % e)
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

# **enable_schedules**
> enable_schedules(body)

Enable schedules

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.SchedulesEnableRequest() # SchedulesEnableRequest | 

try:
    # Enable schedules
    api_instance.enable_schedules(body)
except ApiException as e:
    print("Exception when calling SchedulesApi->enable_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SchedulesEnableRequest**](SchedulesEnableRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedule**
> Schedule get_schedule(id, include=include)

Get Schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get Schedule
    api_response = api_instance.get_schedule(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->get_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_schedules**
> list[Schedule] get_schedules(include=include)

Get schedules list

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get schedules list
    api_response = api_instance.get_schedules(include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->get_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_schedule**
> Schedule update_schedule(body, id, enable=enable)

Update schedule

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
api_instance = swagger_client.SchedulesApi(swagger_client.ApiClient(configuration))
body = swagger_client.ScheduleRequest() # ScheduleRequest | 
id = 56 # int | 
enable = true # bool | Set to `true` to enable the schedule after saving. (optional)

try:
    # Update schedule
    api_response = api_instance.update_schedule(body, id, enable=enable)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SchedulesApi->update_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ScheduleRequest**](ScheduleRequest.md)|  | 
 **id** | **int**|  | 
 **enable** | **bool**| Set to &#x60;true&#x60; to enable the schedule after saving. | [optional] 

### Return type

[**Schedule**](Schedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

