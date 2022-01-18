"""
This class outlines all the constants for the macsec API.

Although the constants are a dictionary you do not need to pass a key to retrieve a constant.
The super class handles that. Simply call <feature>Constants.<constant> and the string at 
key "constant" will be returned.

The tags are for generation purposes and can be ignored.
The link key is useful in pycharm to navigate to the API referenced by the constant.

Example...
>> print(MacsecConstants().<SOME_CONSTANT>)
some_constant
"""
from ExtremeAutomation.Library.Utils.Constants.ApiConstants import ApiConstants


class MacsecConstants(ApiConstants):
    def __init__(self):
        super(MacsecConstants, self).__init__()
        self.VERIFY_MACSEC_CA = {"constant": "verify_macsec_ca",
                                 "tags": ["PARSE_CLI"],
                                 "link": self.link.verify_macsec_ca}
        self.VERIFY_MACSEC_CA_CKN = {"constant": "verify_macsec_ca_ckn",
                                     "tags": ["PARSE_CLI"],
                                     "link": self.link.verify_macsec_ca_ckn}
        self.VERIFY_MACSEC_CA_PORT = {"constant": "verify_macsec_ca_port",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.verify_macsec_ca_port}
        self.VERIFY_MACSEC_CIPHER_SUITE = {"constant": "verify_macsec_cipher_suite",
                                           "tags": ["PARSE_CLI"],
                                           "link": self.link.verify_macsec_cipher_suite}
        self.VERIFY_MACSEC_CONFIDENTIALITY_OFFSET = {"constant": "verify_macsec_confidentiality_offset",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_macsec_confidentiality_offset}
        self.VERIFY_MACSEC_INCLUDE_SCI = {"constant": "verify_macsec_include_sci",
                                          "tags": ["PARSE_CLI"],
                                          "link": self.link.verify_macsec_include_sci}
        self.VERIFY_MACSEC_MKA_ACTOR_PRIORITY = {"constant": "verify_macsec_mka_actor_priority",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_macsec_mka_actor_priority}
        self.VERIFY_MACSEC_ON_PORT = {"constant": "verify_macsec_on_port",
                                      "tags": ["PARSE_CLI"],
                                      "link": self.link.verify_macsec_on_port}
        self.VERIFY_MACSEC_PEER_ELECTED_KEY_SERVER = {"constant": "verify_macsec_peer_elected_key_server",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_macsec_peer_elected_key_server}
        self.VERIFY_MACSEC_PORT_CIPHER_SUITE_ADMIN = {"constant": "verify_macsec_port_cipher_suite_admin",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_macsec_port_cipher_suite_admin}
        self.VERIFY_MACSEC_PORT_CIPHER_SUITE_OPER = {"constant": "verify_macsec_port_cipher_suite_oper",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_macsec_port_cipher_suite_oper}
        self.VERIFY_MACSEC_PORT_CONFIDENTIALITY_OFFSET_ADMIN = {"constant": "verify_macsec_port_confidentiality_offset_admin",
                                                                "tags": ["PARSE_CLI"],
                                                                "link": self.link.verify_macsec_port_confidentiality_offset_admin}
        self.VERIFY_MACSEC_PORT_CONFIDENTIALITY_OFFSET_OPER = {"constant": "verify_macsec_port_confidentiality_offset_oper",
                                                               "tags": ["PARSE_CLI"],
                                                               "link": self.link.verify_macsec_port_confidentiality_offset_oper}
        self.VERIFY_MACSEC_PORT_CONNECTION_STATUS = {"constant": "verify_macsec_port_connection_status",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_macsec_port_connection_status}
        self.VERIFY_MACSEC_REPLAY_PROTECT = {"constant": "verify_macsec_replay_protect",
                                             "tags": ["PARSE_CLI"],
                                             "link": self.link.verify_macsec_replay_protect}
        self.VERIFY_MACSEC_RX_PORT_ASSOCIATION_NUMBER = {"constant": "verify_macsec_rx_port_association_number",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.verify_macsec_rx_port_association_number}
        self.VERIFY_MACSEC_RX_PORT_KEY_NUMBER = {"constant": "verify_macsec_rx_port_key_number",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_macsec_rx_port_key_number}
        self.VERIFY_MACSEC_RX_PORT_NO_ERRORS = {"constant": "verify_macsec_rx_port_no_errors",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.verify_macsec_rx_port_no_errors}
        self.VERIFY_MACSEC_RX_SA_OK_PACKETS = {"constant": "verify_macsec_rx_sa_ok_packets",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.verify_macsec_rx_sa_ok_packets}
        self.VERIFY_MACSEC_RX_SC_OCTETS_DECRYPTED = {"constant": "verify_macsec_rx_sc_octets_decrypted",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_macsec_rx_sc_octets_decrypted}
        self.VERIFY_MACSEC_RX_SC_OK_PACKETS = {"constant": "verify_macsec_rx_sc_ok_packets",
                                               "tags": ["PARSE_CLI"],
                                               "link": self.link.verify_macsec_rx_sc_ok_packets}
        self.VERIFY_MACSEC_SELF_ELECTED_KEY_SERVER = {"constant": "verify_macsec_self_elected_key_server",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_macsec_self_elected_key_server}
        self.VERIFY_MACSEC_TX_PORT_ASSOCIATION_NUMBER = {"constant": "verify_macsec_tx_port_association_number",
                                                         "tags": ["PARSE_CLI"],
                                                         "link": self.link.verify_macsec_tx_port_association_number}
        self.VERIFY_MACSEC_TX_PORT_KEY_NUMBER = {"constant": "verify_macsec_tx_port_key_number",
                                                 "tags": ["PARSE_CLI"],
                                                 "link": self.link.verify_macsec_tx_port_key_number}
        self.VERIFY_MACSEC_TX_PORT_NO_ERRORS = {"constant": "verify_macsec_tx_port_no_errors",
                                                "tags": ["PARSE_CLI"],
                                                "link": self.link.verify_macsec_tx_port_no_errors}
        self.VERIFY_MACSEC_TX_SA_ENCRYPTED_PACKETS = {"constant": "verify_macsec_tx_sa_encrypted_packets",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_macsec_tx_sa_encrypted_packets}
        self.VERIFY_MACSEC_TX_SC_ENCRYPTED_PACKETS = {"constant": "verify_macsec_tx_sc_encrypted_packets",
                                                      "tags": ["PARSE_CLI"],
                                                      "link": self.link.verify_macsec_tx_sc_encrypted_packets}
        self.VERIFY_MACSEC_TX_SC_OCTETS_ENCRYPTED = {"constant": "verify_macsec_tx_sc_octets_encrypted",
                                                     "tags": ["PARSE_CLI"],
                                                     "link": self.link.verify_macsec_tx_sc_octets_encrypted}
