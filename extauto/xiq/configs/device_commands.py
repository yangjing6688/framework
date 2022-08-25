# MacOS commands
MAC_GET_WIFI_INTERFACE_NAME    =      "networksetup -listallhardwareports | awk '/Wi-Fi/{getline; print $2}'"
MAC_TURN_ON_OFF_WIFI_INTERFACE =      'networksetup -setairportpower '
MAC_CHECK_WIFI_CONNECTION      =       'networksetup -getairportnetwork '
MAC_SCAN_FOR_LIST_WIFI         =      '/System/Library/PrivateFrameworks/Apple80211.framework/Versions/A/Resources/airport scan '
MAC_CONNECT_TO_WIFI            =      'networksetup -setairportnetwork '
IFCONFIG                   =      'ifconfig '

# AP commands
AP_CAPWAP_OFF              =      'no capwap client enable'
AP_CAPWAP_ON               =      'capwap client enable'

