# TrafficStreamConfigurationKeywords
Library Scope: test suite<br>
Named Arguments: Supported

## Introduction
Documentation for test library TrafficStreamConfigurationKeywords.

## Shortcuts
[Add All Streams To Port](#Add_All_Streams_To_Port) | [Add Stream To Port](#Add_Stream_To_Port) | [Configure Collection On Ports](#Configure_Collection_On_Ports) | [Configure Stream Count](#Configure_Stream_Count) | [Configure Stream Ip Dst Mode Increment](#Configure_Stream_Ip_Dst_Mode_Increment) | [Configure Stream Ip Dst Mode Random](#Configure_Stream_Ip_Dst_Mode_Random) | [Configure Stream Ip Src Mode Increment](#Configure_Stream_Ip_Src_Mode_Increment) | [Configure Stream Ip Src Mode Random](#Configure_Stream_Ip_Src_Mode_Random) | [Configure Stream Mac Dst Mode Increment](#Configure_Stream_Mac_Dst_Mode_Increment) | [Configure Stream Mac Dst Mode Random](#Configure_Stream_Mac_Dst_Mode_Random) | [Configure Stream Mac Src Mode Increment](#Configure_Stream_Mac_Src_Mode_Increment) | [Configure Stream Mac Src Mode Random](#Configure_Stream_Mac_Src_Mode_Random) | [Configure Stream Mode Advance](#Configure_Stream_Mode_Advance) | [Configure Stream Mode Continuous](#Configure_Stream_Mode_Continuous) | [Configure Stream Mode Continuous Burst](#Configure_Stream_Mode_Continuous_Burst) | [Configure Stream Mode Return To Id](#Configure_Stream_Mode_Return_To_Id) | [Configure Stream Mode Single Burst](#Configure_Stream_Mode_Single_Burst) | [Configure Stream Packet](#Configure_Stream_Packet) | [Configure Stream Packet Collection](#Configure_Stream_Packet_Collection) | [Configure Stream Rate](#Configure_Stream_Rate) | [Configure Stream Unit](#Configure_Stream_Unit) | [Remove All Streams From Port](#Remove_All_Streams_From_Port)
***

## Keywords
| Keyword | Arguments | Documentation |
|---------|-----------|---------------|
| <a name="Add_All_Streams_To_Port"></a>Add All Streams To Port | ports, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Applies all previously configured streams to a traffic generator port.<br><br>Calling this function will clear the internal stream configuration, the configuration will still<br>be applied to the port. |
| <a name="Add_Stream_To_Port"></a>Add Stream To Port | ports, stream_number, clear_all_streams=False, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_number] - The stream configuration to load and apply to the port.<br>[clear_all_streams] - If set to true all previously configured streams will be removed from the port<br>                      before configuring a new stream.<br><br>Applies a stream configuration to a traffic generator port. |
| <a name="Configure_Collection_On_Ports"></a>Configure Collection On Ports | ports, stream_number, collection_name, **kwargs | Keyword Arguments:<br>[traffic_gen_name] - The name of the traffic generator the port exists on.<br>[ports] - This is expected to be a list of ports. Each port will be configured with a different<br>          from the collection (in order).<br>[stream_number] - The stream number the configuration should be applied to.<br>[collection_name] - The name of the packet collection to use. |
| <a name="Configure_Stream_Count"></a>Configure Stream Count | ports, stream_numbers, count, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[count] - The number of packets that should be transmitted by the stream.<br><br>Configures the number of packet a given stream should transmit. |
| <a name="Configure_Stream_Ip_Dst_Mode_Increment"></a>Configure Stream Ip Dst Mode Increment | ports, stream_numbers, count, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[count] - How many times the destination IP should be incremented.<br><br>Configures the destination IP to increment <count> times. |
| <a name="Configure_Stream_Ip_Dst_Mode_Random"></a>Configure Stream Ip Dst Mode Random | ports, stream_numbers, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[mask] - Which part of the IP address should be masked. Only the unmasked portions will be randomized.<br>         The mask value should be formatted as follows "255.255.0.0".<br><br>Configures the destination IP to be randomized for any unmasked portion of the address. |
| <a name="Configure_Stream_Ip_Src_Mode_Increment"></a>Configure Stream Ip Src Mode Increment | ports, stream_numbers, count, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[count] - How many times the source IP should be incremented.<br><br>Configures the source IP to increment <count> times. |
| <a name="Configure_Stream_Ip_Src_Mode_Random"></a>Configure Stream Ip Src Mode Random | ports, stream_numbers, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[mask] - Which part of the IP address should be masked. Only the unmasked portions will be randomized.<br>         The mask value should be formatted as follows "255.255.0.0".<br><br>Configures the source IP to be randomized for any unmasked portion of the address. |
| <a name="Configure_Stream_Mac_Dst_Mode_Increment"></a>Configure Stream Mac Dst Mode Increment | ports, stream_numbers, count, step=1, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[count] - How many times the destination mac should be incremented.<br>[step] - How much to increment each destination mac.<br><br>Configures the destination mac to increment by <step>, <count> times. |
| <a name="Configure_Stream_Mac_Dst_Mode_Random"></a>Configure Stream Mac Dst Mode Random | ports, stream_numbers, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[mask] - Which part of the mac address should be masked. Only the unmasked portions will be randomized.<br>         The mask value should be formatted as follows "XX XX XX XX 00 00" where X is masked an 0 is unmasked.<br><br>Configures the destination mac to be randomized for any unmasked portion of the address. |
| <a name="Configure_Stream_Mac_Src_Mode_Increment"></a>Configure Stream Mac Src Mode Increment | ports, stream_numbers, count, step=1, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[count] - How many times the source mac should be incremented.<br>[step] - How much to increment each source mac.<br><br>Configures the source mac to increment by <step>, <count> times. |
| <a name="Configure_Stream_Mac_Src_Mode_Random"></a>Configure Stream Mac Src Mode Random | ports, stream_numbers, mask=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[mask] - Which part of the mac address should be masked. Only the unmasked portions will be randomized.<br>         The mask value should be formatted as follows "XX XX XX XX 00 00" where X is masked an 0 is unmasked.<br><br>Configures the source mac to be randomized for any unmasked portion of the address. |
| <a name="Configure_Stream_Mode_Advance"></a>Configure Stream Mode Advance | ports, stream_numbers, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br><br>Configures the streams mode to advance. |
| <a name="Configure_Stream_Mode_Continuous"></a>Configure Stream Mode Continuous | ports, stream_numbers, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br><br>Configures the streams mode to continuous. |
| <a name="Configure_Stream_Mode_Continuous_Burst"></a>Configure Stream Mode Continuous Burst | ports, stream_numbers, inter_burst_gap=None, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[inter_burst_gap] - Sets the delay in MS between each burst.<br><br>Configures the streams mode to continuous burst. |
| <a name="Configure_Stream_Mode_Return_To_Id"></a>Configure Stream Mode Return To Id | ports, stream_numbers, return_id, count=None, **kwargs | Keyword Arguments:<br>[ports] - The traffic gen port(s) the stream will be configured on.<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[return_id] - The stream ID to return to.<br>[count] - Optional argument, sets how many times the stream should return to the configured Id.<br>          if passed the mode will be set to return to id for count. If not set the mode will be<br>          set to return to id (continuous).<br><br>Configures the streams mode to either return to id or return to id for count if the count argument<br>is provided. |
| <a name="Configure_Stream_Mode_Single_Burst"></a>Configure Stream Mode Single Burst | ports, stream_numbers, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br><br>Configures the streams mode to single burst. |
| <a name="Configure_Stream_Packet"></a>Configure Stream Packet | ports, stream_numbers, packet_name, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[packet_name] - The name of the packet to apply to the stream.<br><br>Configures a packet to a given stream. |
| <a name="Configure_Stream_Packet_Collection"></a>Configure Stream Packet Collection | ports, collection_name, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[collection_name] - The name of the packet collection to use.<br><br>Configures a packet collection onto a port. When using a packet collection it is expected that only<br>one stream is configured. When a packet collection is applied any value applied using the<br>"configure_stream_packet" keyword will be lost.<br><br>When a stream configured with a packet collection is applied to a port the remaining configuration<br>will be applied using stream ID 1. |
| <a name="Configure_Stream_Rate"></a>Configure Stream Rate | ports, stream_numbers, rate, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[rate] - The integer rate that should be applied to the stream.<br><br>Configures the transmit rate of a given stream. |
| <a name="Configure_Stream_Unit"></a>Configure Stream Unit | ports, stream_numbers, unit, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br>[stream_numbers] - The stream number(s) the configuration should be applied to.<br>[unit] - The unit that should be applied to the stream. Valid units are "pps", "bps", "kbps", "mbps",<br>         "gbps", "percent", and "%".<br><br>Configures the transmit unit for a given stream. |
| <a name="Remove_All_Streams_From_Port"></a>Remove All Streams From Port | ports, **kwargs | Keyword Arguments:<br>[ports] - This must be a list which contains the name of the traffic generator and the<br>          traffic generator port. Example ["tgen_1", "1/1/11"].<br><br>Removes all streams configured on a given traffic generator port also clears internal stream configurations. |