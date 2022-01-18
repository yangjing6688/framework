from ExtremeAutomation.Keywords.NetworkElementKeywords.GeneratedKeywords.NetworkElementLoginconfigGenKeywords import NetworkElementLoginconfigGenKeywords


class LoginUdks():
    def __init__(self) -> None:
        self.networkElementLoginconfigGenKeywords = NetworkElementLoginconfigGenKeywords()

    def Create_Administrative_User_and_Verify(self, device_name,   username,  passwd, **kwargs):
        self.networkElementLoginconfigGenKeywords.loginconfig_create_admin_account(device_name, username, passwd, **kwargs)
        self.networkElementLoginconfigGenKeywords.loginconfig_verify_admin_account_exists(device_name, username, **kwargs)

    def Remove_Administrative_User_and_Verify(self, device_name,    username, **kwargs):
        self.networkElementLoginconfigGenKeywords.loginconfig_delete_account(device_name, username, **kwargs)
        self.networkElementLoginconfigGenKeywords.loginconfig_verify_admin_account_does_not_exist(device_name, username, **kwargs)
