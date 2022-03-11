from common.tools.remote.SeleniumServer import SeleniumServer
from common.tools.remote.Recording import Recording
from common.tools.remote.captiveportal.CaptivePortal import CaptivePortal
import sys

from sys import platform
if platform == "linux" or platform == "linux2":
    pass
elif platform == "darwin":
    from common.tools.remote.MacMuConnect import MacMuConnect as MuConnect
elif platform == "win32":
    from common.tools.remote.WinMuConnect import WinMuConnect as MuConnect


class RFTestClient(SeleniumServer, Recording, MuConnect, CaptivePortal):
    def __init__(self):
        SeleniumServer.__init__(self)
        Recording.__init__(self)
        MuConnect.__init__(self)
        CaptivePortal.__init__(self)


if __name__ == '__main__':
    from robotremoteserver import RobotRemoteServer
    RobotRemoteServer(RFTestClient(), *sys.argv[1:])
