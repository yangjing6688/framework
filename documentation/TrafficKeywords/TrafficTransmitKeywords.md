# TrafficTransmitKeywords
Library Scope: test suite<br>
Named Arguments: Supported

## Introduction
Documentation for test library TrafficTransmitKeywords.

## Shortcuts
[Start Transmit On Port](#Start_Transmit_On_Port) | [Start Transmit On Port And Wait](#Start_Transmit_On_Port_And_Wait) | [Stop Transmit On Port](#Stop_Transmit_On_Port) | [Stop Transmit On Port And Wait](#Stop_Transmit_On_Port_And_Wait)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Start_Transmit_On_Port"></a>Start Transmit On Port | ports, delay_after=None, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[delay_after] - The amount of time to wait after starting the transmit. The default<br>                value is 0 seconds.<br><br>Starts transmitting streams on a given <tx_port>. |
| <a name="Start_Transmit_On_Port_And_Wait"></a>Start Transmit On Port And Wait | ports, max_wait=60, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[max_wait] - The maximum length the keyword should wait for the stream to complete.<br><br>Starts transmitting streams on a given <tx_port> and waits for them to complete. This keyword should<br>not be used if continuous streams have been configured. |
| <a name="Stop_Transmit_On_Port"></a>Stop Transmit On Port | ports, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Stops the transmitting streams on <tx_port>. |
| <a name="Stop_Transmit_On_Port_And_Wait"></a>Stop Transmit On Port And Wait | ports, wait=1, **kwargs | [ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[wait] - How long to wait after stopping the transmit. The default value is 1 second.<br><br>Stops the transmitting streams on <tx_port>. |
