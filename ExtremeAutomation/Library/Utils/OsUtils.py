import platform


class OsUtils(object):
    @staticmethod
    def is_windows():
        """Verifies if the current device's OS is Windows."""
        return platform.system().lower() == 'windows'

    @staticmethod
    def is_unix():
        """Verifies if the current device's OS is Unix/Linux."""
        return platform.system().lower() == 'linux'

    @staticmethod
    def get_platform():
        """Determines the current device's platform."""
        return platform.platform()
