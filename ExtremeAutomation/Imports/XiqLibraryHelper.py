from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Imports.XiqLibrary import XiqLibrary

try:
    import pytest
except:
    Logger().log_warn("Unable to load the pytest library")


class XiqLibraryHelper():
    
    def __init__(self):
        pass
    #def __init__(self, username, password, capture_version=False, code="default", url="default", incognito_mode="False"):
    #    self.init_xiq_libaries_and_login(username=username, password=password, capture_version=capture_version, code=code, url=url, incognito_mode=incognito_mode)
        
    def init_xiq_libaries_and_login(self, username, password, capture_version=False, code="default", url="default", incognito_mode="False"):
        self.xiq = XiqLibrary()
        res = self.xiq.init_xiq_libaries_and_login(username=username, password=password, capture_version=capture_version, code=code, url=url, incognito_mode=incognito_mode)
        if res != 1:
            pytest.fail('(XiqLibraryHelper) Could not Login')
            
    def deactivate_xiq_libaries_and_logout(self):
        self.xiq.login.logout_user()
        self.xiq.login.quit_browser()
        self.xiq = None