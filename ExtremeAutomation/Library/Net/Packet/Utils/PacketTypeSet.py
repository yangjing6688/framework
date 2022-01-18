import subprocess
cmd = subprocess.Popen('dir /b/s .. | grep.exe "Packet.py$"', shell=True, stdout=subprocess.PIPE)

all_packets = []
lines = []
for line in cmd.stdout:
    line = str(line.decode("utf-8")).strip()
    if str(line).find(".py") > 0:
        lines.append(line)
# lines.sort()

cmd = subprocess.Popen('dir /b/s .. | grep.exe "PacketHeader.py$"', shell=True, stdout=subprocess.PIPE)
headers = []
for line in cmd.stdout:
    line = str(line.decode("utf-8") ).strip()
    if str(line).find(".py") > 0:
        headers.append(line)

print("# ### Start Packets Auto-generated ####")
for line in lines:
    parts = line.split("\\")
    index = parts.index("ExtremeAutomation")
    path = ".".join(parts[index:]).replace(".py", "").strip()
    class_name = parts[-1].replace(".py", "").strip()
    print("from " + str(path) + " import " + str(class_name))
print("# ### End Packets Auto-generated ####")
print("")
print("# ### Start Packet Headers Auto-generated ####")
for line in headers:
    parts = line.split("\\")
    index = parts.index("ExtremeAutomation")
    path = ".".join(parts[index:]).replace(".py", "").strip()
    print("from " + str(path) + " import *")
print("# ### End Packet Headers Auto-generated ####")

print("#########" * 15)
print("# ## PASTE THIS INTO PacketClassifier")
print("# ### Start Pack Auto-generated ####")
print("\t\tname = name.upper()")
for line in lines:
    parts = line.split("\\")
    class_name = parts[-1].replace(".py", "").strip()
    print("\t\tif name == \"" + class_name.upper() + "\":")
    if "VlanStack" in class_name:
        print("\t\t\treturn " + class_name + "(0)")
    else:
        print("\t\t\treturn " + class_name + "()")
    if "ABSTRACT" not in class_name.upper():
        all_packets.append(class_name.upper())

print("#########" * 15)

print("# ### PASTE THIS INTO PacketClassifierConstants")
for p in all_packets:
    print("\t\t" + p + " = \"" + p + "\"")
print("\t\tALL_PACKETS = [")
for p in all_packets:
    print("\t\t\t\"" + p + "\",")
print("\t\t]")
