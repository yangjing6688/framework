import os
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerateAllApis import GenerateAllApis
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants
from ExtremeAutomation.Library.Device.Common.PlatformVariables.Library.PlatformVariableConstants \
    import PlatformVariableConstants


project_root = PathUtils.get_project_root()

# Network element input and output directories.
net_elem_inp = os.path.join(project_root, "ExtremeAutomation", "Apis", "NetworkElement", "ApiDefinition",
                            "PlatformVariables")
net_elem_out = os.path.join(project_root, "ExtremeAutomation", "Apis", "NetworkElement", "GeneratedApis",
                            "PlatformVariables")

# End system element input and output directories.
end_sys_inp = os.path.join(project_root, "ExtremeAutomation", "Apis", "EndSystemElement", "ApiDefinition",
                           "PlatformVariables")
end_sys_out = os.path.join(project_root, "ExtremeAutomation", "Apis", "EndSystemElement", "GeneratedApis",
                           "PlatformVariables")

# Ui element input and output directories.
ui_elem_inp = os.path.join(project_root, "ExtremeAutomation", "Apis", "UiElement", "ApiDefinition",
                           "PlatformVariables")
ui_elem_out = os.path.join(project_root, "ExtremeAutomation", "Apis", "UiElement", "GeneratedApis",
                           "PlatformVariables")

# Network element platform variable generation.
print("Generating Network Element Platform Variables...")
plat_var_gen = GenerateAllApis(GenerationConstants.DEVICE_TYPE_NET_ELEM,
                               GenerationConstants.API_TYPE_PLATFORM_VARIABLE,
                               PlatformVariableConstants.TYPE_NETWORK_ELEMENT,
                               net_elem_inp, net_elem_out, )
plat_var_gen.generate_all_apis()

# End system element platform variable generation.
print("\nGenerating Endsystem Element Platform Variables...")
plat_var_gen = GenerateAllApis(GenerationConstants.DEVICE_TYPE_END_SYS_ELEM,
                               GenerationConstants.API_TYPE_PLATFORM_VARIABLE,
                               PlatformVariableConstants.TYPE_END_SYSTEM_ELEMENT,
                               end_sys_inp, end_sys_out, )
plat_var_gen.generate_all_apis()

# Ui element platform variable generation.
print("\nGenerating UI Element Platform Variables...")
plat_var_gen = GenerateAllApis(GenerationConstants.DEVICE_TYPE_UI_ELEM,
                               GenerationConstants.API_TYPE_PLATFORM_VARIABLE,
                               PlatformVariableConstants.TYPE_UI_ELEMENT,
                               ui_elem_inp, ui_elem_out, )
plat_var_gen.generate_all_apis()
