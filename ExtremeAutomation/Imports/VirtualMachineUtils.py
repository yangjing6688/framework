############################################
# Virtual Machine Library
############################################
from ExtremeAutomation.Keywords.VirtualMachineKeywords.VirtualMachineManager import VirtualMachineManager
from ExtremeAutomation.Keywords.VirtualMachineKeywords.Virtualization.VirtualMachineControl import VirtualMachineControl


class VirtualMachineUtils():
    """
        Description: The default set of Virtual Machine functions. This will allow users to interact with the Virtual Machine.
    """
    def __init__(self):
        self.virtualMachineControl = VirtualMachineControl()
       
        ############################################
        # Virtual Machine Library
        ############################################
        self.virtualMachineManager = VirtualMachineManager()
        self.virtualMachineControl = VirtualMachineControl()