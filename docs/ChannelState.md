# ChannelState

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connected** | **bool** |  | 
**brightness** | **int** | &#x60;brightness&#x60; contains current dimmer brightness value in percent, integer from 0 to 100 | [optional] 
**color_brightness** | **int** | &#x60;color_brightness&#x60; is a color brightness in percent, integer from 0 to 100 | [optional] 
**color** | **str** | &#x60;color&#x60; contains the integer (hex) value of a current color, ranging from &#x60;0x000001&#x60; to &#x60;0xFFFFFF&#x60; | [optional] 
**depth** | [**BigDecimal**](BigDecimal.md) | &#x60;depth&#x60; contains current sensor value | [optional] 
**distance** | [**BigDecimal**](BigDecimal.md) | &#x60;distance&#x60; contains current sensor value | [optional] 
**humidity** | [**BigDecimal**](BigDecimal.md) | &#x60;humidity&#x60; contains current value of humidity provided by the sensor (including possibly configured delta adjustment), in percent; possible values from 0 to 100 | [optional] 
**on** | **bool** | &#x60;on&#x60; is either &#x60;true&#x60; or &#x60;false&#x60; depending on the switch state | [optional] 
**hi** | **bool** | &#x60;hi&#x60; is either &#x60;true&#x60; or &#x60;false&#x60; depending on sensor state | [optional] 
**partial_hi** | **bool** | &#x60;partial_hi&#x60; is either &#x60;true&#x60; or &#x60;false&#x60; depending on paired secondary opening sensor state | [optional] 
**is_calibrating** | **bool** | &#x60;is_calibrating&#x60; is &#x60;true&#x60; if the roller shutter has calibration in progres or if it hasn&#x27;t been finished for whatever reason | [optional] 
**shut** | **int** | &#x60;shut&#x60; is provided regardles off &#x60;is_calibrating&#x60; state and is an integer from 0 to 100, meaning the percantage of rolette being closed | [optional] 
**temperature** | [**BigDecimal**](BigDecimal.md) | &#x60;temperature&#x60; contains current value of temperature provided by the sensor (including possibly configured delta adjustment), in Celsius | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

