import os
from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Library.Documentation.DocGenerator.LibdocXmlToMd import LibdocXmlToMd


project_root = PathUtils.get_project_root()
keyword_dir = os.path.join(project_root, "ExtremeAutomation", "Keywords")
llk_out_dir = os.path.join(project_root, "ExtremeAutomation", "Documentation", "LowLevelKeywordDocs")
udk_out_dir = os.path.join(project_root, "ExtremeAutomation", "Documentation", "UserDefinedKeywordDocs")

# Input Folders
netelem_inp = os.path.join(keyword_dir, "NetworkElementKeywords")
endsys_inp = os.path.join(keyword_dir, "EndsystemKeywords")
traffic_inp = os.path.join(keyword_dir, "TrafficKeywords")
ui_inp = os.path.join(keyword_dir, "UiKeywords")
udk_inp = os.path.join(keyword_dir, "UserDefinedKeywords")

# Output Folders
netelem_out = os.path.join(llk_out_dir, "NetworkElementKeywords")
endsys_out = os.path.join(llk_out_dir, "EndSystemKeywords")
traffic_out = os.path.join(llk_out_dir, "TrafficKeywords")
ui_out = os.path.join(llk_out_dir, "UiKeywords")

# Generate network element keyword markdown.
md_gen = LibdocXmlToMd(netelem_inp, netelem_out)
md_gen.add_file_to_black_list("MultiauthSession.py", "TlvUtils.py", "MultiauthSessionUnitTests.py",
                              "KeywordBaseClass.py")
md_gen.create_md_files()

# Generate endsystem element keyword markdown.
md_gen = LibdocXmlToMd(endsys_inp, endsys_out)
md_gen.create_md_files()

# Generate traffic keyword markdown.
md_gen = LibdocXmlToMd(traffic_inp, traffic_out)
md_gen.add_file_to_black_list("CaptureConfig.py", "CaptureConfigManager.py", "StreamConfig.py",
                              "StreamConfigManager.py", "trafficPortConfigManager.py", "GenerateRobotVariables.py",
                              "PacketDefaultConstants.py", "PacketTypeConstants.py", "PacketInspectionUtils.py",
                              "PacketDictionary.py", "KeywordBaseClass.py")
md_gen.create_md_files()

# Generate UI element keyword markdown.
md_gen = LibdocXmlToMd(ui_inp, ui_out)
md_gen.create_md_files()

# Generate UDK markdown.
md_gen = LibdocXmlToMd(udk_inp, udk_out_dir, kw_extension=".robot")
md_gen.create_md_files()
