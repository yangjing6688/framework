class TrafficGenConstants:
    def __init__(self):
        pass

    # Don't allow values to be updated.
    def __setattr__(self, *_):
        pass

    # Chassis Types
    IXIA_CHASSIS = "ixia"
    SPIRENT_CHASSIS = "spirent"
    OSTINATO_CHASSIS = "ostinato"
    JETS_CHASSIS = "jets"
    IXLOAD_CHASSIS = "ixload"

    VM_IP = "0.0.0.0"
    JETS_PORT = "22"
    IXIA_PORT = "5678"
    SPIRENT_PORT = "5679"
    OSTINATO_PORT = "7878"
    IXLOAD_PORT = "5680"
    USER_NAME = "BASE_USER"
    PASSWORD = ""
