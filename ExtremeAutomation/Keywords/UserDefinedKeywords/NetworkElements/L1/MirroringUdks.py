from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementMirroringGenKeywords import NetworkElementMirroringGenKeywords


class MirroringUdks():
    def __init__(self) -> None:
        self.networkElementMirroringGenKeywords = NetworkElementMirroringGenKeywords()

    def Create_Port_Mirror_Enable_and_Verify(self, netelem_name, mirror_src,  mirror_dst, mirror_name, **kwargs):
        self.networkElementMirroringGenKeywords.mirroring_create_both(netelem_name, mirror_src,  mirror_dst, mirror_name, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_set_source_port_both(netelem_name, mirror_name, mirror_src, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_verify_port_mirror_exists(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_enable_port(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_verify_port_mirror_enabled(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)

    def Create_Ingress_Port_Mirror_Enable_and_Verify(self, netelem_name, mirror_src,  mirror_dst, mirror_name, **kwargs):
        self.networkElementMirroringGenKeywords.mirroring_create_ingress(netelem_name, mirror_src,  mirror_dst, mirror_name, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_set_source_port_both(netelem_name, mirror_name, mirror_src, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_verify_port_mirror_exists(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_enable_port(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_verify_port_mirror_enabled(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)

    def Remove_Port_Mirror_and_Verify(self, netelem_name, mirror_src=None, mirror_dst=None, mirror_name=None, **kwargs):
        self.networkElementMirroringGenKeywords.mirroring_disable_port(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_delete_port_mirror(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
        self.networkElementMirroringGenKeywords.mirroring_verify_port_mirror_does_not_exist(netelem_name, mirror_name, mirror_src, mirror_dst, **kwargs)
