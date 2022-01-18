from ExtremeAutomation.Library.Device.Common.Apis.UiBaseApi import UiBaseApi as DfndrinventoryBase
# All imports above this line will be removed after generation.
# User imports must be added below.


class Dfndrinventory(DfndrinventoryBase):
    def dfndr_inventory_function(self, ui_cmd_obj, arg_dict):
        # This try/except is here to protect any inheritance that might be used.
        # If a super class is specified the super class's function will be called.
        # If no super class is specified the ui_cmd_obj is returned.
        # This can all be removed if a user implements the function.
        try:
            return super(Dfndrinventory, self).dfndr_inventory_function(ui_cmd_obj, arg_dict)
        except AttributeError:
            return self.base_function()
