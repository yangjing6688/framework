*** Variables ***
${CMD_CAPWAP_CLIENT_STATE}          show capwap client | include state
${CMD_CAPWAP_HM_PRIMARY_NAME}       show capwap client | include "HiveManager Primary Name"
${CMD_CAPWAP_SERVER_IP}             show capwap client | include "CAPWAP server IP"


${OUTPUT_CAPWAP_STATUS}             Connected securely to the CAPWAP server
changes
