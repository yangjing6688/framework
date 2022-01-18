from ExtremeAutomation.Library.Device.TrafficGeneration.Ixia.IxiaDevice import IxiaDevice
from ExtremeAutomation.Library.Logger.Logger import Logger

#############################################################
# ###  DO NOT USE THIS CLASS!!!!!
# ###  This is used solely to test new features on the Traffic Generating Devices.
# ###
#############################################################


class IxiaDeviceUnitTestObject(object):
    def __init__(self):
        self.username = "aaron"
        self.ixNetworkIp = "10.52.2.167"
        self.vm_port = 5678

        # # my old ports on 189
        self.dev = "10.52.2.189"
        self.vm = "10.59.5.62"
        self.tx_port = "1/1"
        self.rx_port = "1/2"

        # self.dev = "10.50.2.202"
        # self.vm = "10.52.2.167"
        # self.tx_port = "1/6"
        # self.rx_port = "1/7"

        #
        # # from corey this is the socket listener
        # self.dev = "10.52.2.189"
        # self.vm = "10.52.2.167"
        # self.tx_port = "2/1"
        # self.rx_port = "2/2"

        # steve mays IxLoad
        # self.dev = "10.52.3.48"
        # self.vm = "10.52.22.11"
        # self.tx_port = "9/13"
        # self.rx_port = "9/16"

        self.dev_object = IxiaDevice()

    def connect_and_take_ports(self):

        traffic_device = self.dev_object  # instantiate an Ixia Device
        traffic_device.logger.console_level = Logger.TRACE

        # connect to the Ixia_Device
        traffic_device.connect(self.vm, self.vm_port)
        # alternatively inline version
        traffic_device.tgen_debug = True
        if traffic_device.is_connected() and traffic_device.is_initialized():
            ixia_ver = traffic_device.get_version().replace(" ", "")
            traffic_device.logger.log_info(ixia_ver)
            # traffic_device.tgen_debug = True
            kw_results = traffic_device.take_port_ownership(self.dev, self.username,
                                                            [self.tx_port, self.rx_port], reset=True)
            # kw_results = traffic_device.take_port_ownership(self.dev, self.username, [self.tx_port, self.rx_port],
            #                                                 True, {"duplex": "half"})
            # traffic_device.take_port_ownership(device_object.dev, device_object.username, device_object.tx_port, True)
            # traffic_device.take_port_ownership(device_object.dev, device_object.username, device_object.rx_port, True)

            # traffic_device.tgen_debug = False

            traffic_device.logger.log_info("clear the statics of ports " + self.tx_port + " and " + self.rx_port + "\n")
            traffic_device.clear_statistics_and_filters(self.tx_port)
            traffic_device.clear_statistics_and_filters(self.rx_port)
            return traffic_device
        else:
            return False


"""
# load HLTAPI library

package require Ixia



# some variables used in the script

set ixia(device) 1.1.1.2

set tx_port 4/1

set rx_port 4/3

set tx_mac 0000.0000.0001

set rx_mac 0000.0000.0002

set tx_ip 100.0.4.1

set rx_ip 100.0.4.3

set mask 255.255.255.0

set rate_pps 2000

set ip_size 256



# call ixia::connect to connect to the chassis and reserve ports

set connect_info [ixia::connect\

-reset\

-device $ixia(device)\

-port_list $tx_port $rx_port\

-username ciscoUser]



# checking whether connection process succeeds

if { [keylget connect_info status] == $FAILURE } {

puts "Failed to connect to $ixia(device): \

[keylget connect_info log]"

return

}



# getting handles; they are the references used in subsequent calls

set tx_handle [keylget connect_info port_handle.$ixia(device).$tx_port]

set rx_handle [keylget connect_info port_handle.$ixia(device).$rx_port]



# configuring interfaces

set interface_info [ixia::interface_config \

-port_handle $tx_handle $rx_handle \

-src_mac_addr $tx_mac $rx_mac \

-intf_ip_addr $tx_ip $rx_ip \

-netmask $mask $mask \

-autonegotiation 0 ]

# checking interface config

if { [keylget interface_info status] == $FAILURE } {

puts "Failed to configure interfaces: \

[keylget interface_info log]"

return

}



# clean up all streams; note that ixia::traffic_config

# accepts only one port handle at a time

foreach phandle [list $tx_handle $rx_handle] {

set traffic_info [ixia::traffic_config \

-mode reset \

-port_handle $phandle]

if {[keylget traffic_info status] == $FAILURE} {

puts "Failed to reset traffic streams: \

[keylget traffic_info log]"

return

}

}



# setting up a traffic stream from tx port to rx port

set stream_info [ixia::traffic_config\

-mode create\

-port_handle $tx_handle\

-l3_protocol ipv4\

-ip_src_addr $tx_ip\

-ip_dst_addr $rx_ip\

-l3_length $ip_size\

-transmit_mode continuous\

-mac_src $tx_mac\

-mac_dst_mode discovery\

-rate_pps $rate_pps]



# checking stream creation

if {[keylget stream_info status] == $FAILURE} {

puts "Failed to create a traffic streams: \

[keylget stream_info log]"

return

}



# obtain the stream ID for reference

set streamID [keylget stream_info stream_id]



# clearing stats at both sides before running traffic

set stats_info [ixia::traffic_control \

-port_handle $tx_handle $rx_handle\

-action clear_stats]

if {[keylget stats_info status] != $SUCCESS} {

return "Failed to clean stats: \

[keylget stats_info log]"

}



# start TX

set run_info [ixia::traffic_control\

-port_handle $tx_handle $rx_handle\

-action run]

if {[keylget run_info status] != $SUCCESS} {

return "Failed to start TX: \

[keylget run_info log]"

}



# wait for 3 seconds as traffic running

after 3000

# stop traffic

set stop_info [ixia::traffic_control\

-port_handle $tx_handle $rx_handle\

-action stop]

if {[keylget stop_info status] != $SUCCESS} {

return "Failed to stop TX: \

[keylget stop_info log]"

}



# get stats

set stats [ixia::traffic_stats\

-port_handle $tx_handle $rx_handle \

-mode streams]

if {[keylget stats status] == $FAILURE} {

return "Failed to get stats:\

[keylget stats log]"

}



# display stats for the stream

set tx_pkts [keylget stats $tx_handle.stream.$streamID.tx.total_pkts]

set rx_pkts [keylget stats $rx_handle.stream.$streamID.rx.total_pkts]

set delay [keylget stats $rx_handle.stream.$streamID.rx.avg_delay]

puts "Stream TX $tx_pkts; RX $rx_pkts; avg latency: $delay ns"



# clean up

set cleanup_info [ixia::cleanup_session\

-port_handle $tx_handle $rx_handle\

-reset]

if {[keylget cleanup_info status] == $FAILURE} {

return "Failed to clean up:\

[keylget cleanup_info log]"

}
"""
