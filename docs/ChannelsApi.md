# swagger_client.ChannelsApi

All URIs are relative to *https://cloud.supla.org/api/v2.3.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_action**](ChannelsApi.md#execute_action) | **PATCH** /channels/{id} | Execute action on the channel
[**get_channel**](ChannelsApi.md#get_channel) | **GET** /channels/{id} | Get channel by ID
[**get_channel_measurement_logs**](ChannelsApi.md#get_channel_measurement_logs) | **GET** /channels/{id}/measurement-logs | Get measurement logs.
[**get_channel_measurement_logs_csv_file**](ChannelsApi.md#get_channel_measurement_logs_csv_file) | **GET** /channels/{id}/measurement-logs-csv | Get measurement logs as zipped CSV file.
[**get_channel_schedules**](ChannelsApi.md#get_channel_schedules) | **GET** /channels/{id}/schedules | Get schedules list of the channel
[**get_channels**](ChannelsApi.md#get_channels) | **GET** /channels | Get channels list
[**update_channel**](ChannelsApi.md#update_channel) | **PUT** /channels/{id} | Update channel

# **execute_action**
> execute_action(body, id)

Execute action on the channel

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelExecuteActionRequest() # ChannelExecuteActionRequest | Defines an action to execute on channel. The `action` key is always required. The rest of the keys are params depending on the chosen action. Read more on [Github Wiki](https://github.com/SUPLA/supla-cloud/wiki/Channel-Actions).
id = 56 # int | 

try:
    # Execute action on the channel
    api_instance.execute_action(body, id)
except ApiException as e:
    print("Exception when calling ChannelsApi->execute_action: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelExecuteActionRequest**](ChannelExecuteActionRequest.md)| Defines an action to execute on channel. The &#x60;action&#x60; key is always required. The rest of the keys are params depending on the chosen action. Read more on [Github Wiki](https://github.com/SUPLA/supla-cloud/wiki/Channel-Actions). | 
 **id** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel**
> Channel get_channel(id, include=include)

Get channel by ID

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get channel by ID
    api_response = api_instance.get_channel(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**Channel**](Channel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_measurement_logs**
> list[ChannelMeasurementLog] get_channel_measurement_logs(id, limit=limit, offset=offset)

Get measurement logs.

Supported channel functions: `THERMOMETER` and `HUMIDITYANDTEMPERATURE`. Logs ordered by date, descending.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
limit = 56 # int | Maximum items count in response, from 1 to 5000 (optional)
offset = 56 # int | Pagination offset (optional)

try:
    # Get measurement logs.
    api_response = api_instance.get_channel_measurement_logs(id, limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channel_measurement_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **limit** | **int**| Maximum items count in response, from 1 to 5000 | [optional] 
 **offset** | **int**| Pagination offset | [optional] 

### Return type

[**list[ChannelMeasurementLog]**](ChannelMeasurementLog.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_measurement_logs_csv_file**
> get_channel_measurement_logs_csv_file(id)

Get measurement logs as zipped CSV file.

Supported channel functions: `THERMOMETER` and `HUMIDITYANDTEMPERATURE`. Logs ordered by date, descending.

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 

try:
    # Get measurement logs as zipped CSV file.
    api_instance.get_channel_measurement_logs_csv_file(id)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channel_measurement_logs_csv_file: %s\n" % e)
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
 - **Accept**: application/zip, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_schedules**
> list[Schedule] get_channel_schedules(id, include=include)

Get schedules list of the channel

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
id = 56 # int | 
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)

try:
    # Get schedules list of the channel
    api_response = api_instance.get_channel_schedules(id, include=include)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channel_schedules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 

### Return type

[**list[Schedule]**](Schedule.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channels**
> list[Channel] get_channels(include=include, function=function, io=io, has_function=has_function)

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
include = ['include_example'] # list[str] | Specify what extra fields to include in the response. (optional)
function = [swagger_client.ChannelFunctionEnumNames()] # list[ChannelFunctionEnumNames] |  (optional)
io = 'io_example' # str | Return only `input` or `output` channels. (optional)
has_function = true # bool | Return only channels with (`true`) or without (`false`) chosen functions. (optional)

try:
    # Get channels list
    api_response = api_instance.get_channels(include=include, function=function, io=io, has_function=has_function)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->get_channels: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include** | [**list[str]**](str.md)| Specify what extra fields to include in the response. | [optional] 
 **function** | [**list[ChannelFunctionEnumNames]**](ChannelFunctionEnumNames.md)|  | [optional] 
 **io** | **str**| Return only &#x60;input&#x60; or &#x60;output&#x60; channels. | [optional] 
 **has_function** | **bool**| Return only channels with (&#x60;true&#x60;) or without (&#x60;false&#x60;) chosen functions. | [optional] 

### Return type

[**list[Channel]**](Channel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_channel**
> Channel update_channel(body, id)

Update channel

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
api_instance = swagger_client.ChannelsApi(swagger_client.ApiClient(configuration))
body = swagger_client.ChannelUpdateRequest() # ChannelUpdateRequest | 
id = 56 # int | 

try:
    # Update channel
    api_response = api_instance.update_channel(body, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChannelsApi->update_channel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChannelUpdateRequest**](ChannelUpdateRequest.md)|  | 
 **id** | **int**|  | 

### Return type

[**Channel**](Channel.md)

### Authorization

[BearerAuth](../README.md#BearerAuth), [OAuth2](../README.md#OAuth2)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

