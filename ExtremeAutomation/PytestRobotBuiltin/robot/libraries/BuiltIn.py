try:
    from pytest_testconfig import config
except Exception:
    pass

""" Pytest version of built in """
class BuiltIn(object):
    def __init__(self):
        pass

    @staticmethod
    def isRunningPytest():
        return True

    @staticmethod
    def get_variables(no_decoration=True):
        try:
            # Try pytest
            variables = config
        except Exception as e:
            raise e

        return variables

    @staticmethod
    def set_global_variable(key, value):
        try:
            config["${" + key + "}"] = value
        except Exception as e:
            raise e

    @staticmethod
    def get_variable_value(varname, default=None):
        value = default
        try:
            # Try pytest
            value = config[varname]
        except Exception as e:
            print(f"get_variable_value couldn't find variable {varname}, returning the default {default}")
        return value

    @staticmethod
    def set_global_variable(key, value):
        try:
            # Try pytest
            config[key] = value
        except Exception as e:
            raise e

        return value

    @staticmethod
    def log_to_console(txt):
        print(txt)

    @staticmethod
    def fail(msg=None):
        raise AssertionError(msg) if msg else AssertionError()
