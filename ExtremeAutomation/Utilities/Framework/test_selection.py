from ExtremeAutomation.Imports.pytestConfigHelper import PytestConfigHelper
from ExtremeAutomation.Utilities.Framework.device_capabilities import DeviceCapability

class CheckExecution():

    def __init__(self, request, config):
        self.request = request
        self.tb  = PytestConfigHelper(config)

    def requiredPlatform(self):
        devCap = DeviceCapability(self.tb.dut1_model)
        models = devCap.loadModels()
        reqList = []
        if self.request.node.get_closest_marker('required_platform').args[0]:
            for plat in self.request.node.get_closest_marker('required_platform').args:
                reqList.append(plat)
                myPlat = str(plat).lower()
                modelGroup = []
                if myPlat in models:
                    modelGroup = models[myPlat]
                print(f"I found platform {myPlat}")
                if self.tb.dut1_topology == myPlat or str(self.tb.dut1_model) in modelGroup:
                    returnList = [True, myPlat]
                    return returnList
            return [None, reqList]

    def skipPlatform(self):
        devCap = DeviceCapability(self.tb.dut1_model)
        models = devCap.loadModels()
        if self.request.node.get_closest_marker('skip_platform').args[0]:
            for plat in self.request.node.get_closest_marker('skip_platform').args:
                myPlat = str(plat).upper()
                modelGroup = []
                if myPlat in models:
                    print(f"P{myPlat}myPlat {models[myPlat]}")
                    modelGroup = models[myPlat]
                if self.tb.dut1_topology == myPlat or str(self.tb.dut1_model) in modelGroup:
                    return myPlat
            return None

    def requiredCapability(self):
        devCap = DeviceCapability(self.tb.dut1_model)
        capability = devCap.getModelInfo()
        capList = []
        capValueList = []
        capTrue = 0
        if self.request.node.get_closest_marker('required_capability').args[0]:
            for cap in self.request.node.get_closest_marker('required_capability').args:
                if cap in capability:
                    capList.append(cap)
                    capValueList.append(capability[cap])
            if len(capValueList) > 0:
                for cval in capValueList:
                    if cval:
                        return [True, capList]   # Capability args are OR.  If any is true, test supported
            if not capTrue and self.tb.dut1_os != 'voss':
                    return [False, capList]   # Capability not available on DUT1
            else:
                return [True, 'No capability entry for device. Assume support']   # There were no capability matches

    def requiredNos(self):
        reqList = []
        if self.request.node.get_closest_marker('required_nos').args[0]:
            dut1Nos = self.tb.dut1_os
            for nos in self.request.node.get_closest_marker('required_nos').args:
                reqList.append(nos)
                myNos = str(nos).lower()
                if str(dut1Nos).lower() == myNos:
                    returnList = [True, dut1Nos]
                    return [True, dut1Nos]
            return [None, reqList]

    def skipNos(self):
        reqList = []
        if self.request.node.get_closest_marker('skip_nos').args[0]:
            dut1Nos = self.tb.dut1_os
            for nos in self.request.node.get_closest_marker('skip_nos').args:
                reqList.append(nos)
                myNos = str(nos).lower()
                if str(dut1Nos).lower() == myNos:
                    returnList = [True, dut1Nos]
                    return [True, dut1Nos]
            return [None, reqList]