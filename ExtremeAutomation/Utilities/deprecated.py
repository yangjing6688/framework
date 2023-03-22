import warnings
from ExtremeAutomation.Library.Logger.Logger import Logger

class UnsupportedKeywordException(Exception):
    """Raised when the keyword is not supported"""
    pass

def deprecated(message):
    """
    To use:
        from ExtremeAutomation.Utilities.deprecated import deprecated
        @deprecated('This function is a duplicate of another function and will be removed from the framework soon.')
    :param message: The message for the warning
    :return: Decorated function
    """
    def deprecated_decorator(func):
        def deprecated_func(*args, **kwargs):
            warning_message_header = ("*" * 200) + "\n"
            warning_message = f"DEPRECATED FUNCTION WARNING -> {func.__name__} is a deprecated function and will be removed from the framework soon. {message}"
            full_warning_meesage = "\n\n" + warning_message_header + "\n\t" + warning_message + "\n\n" + warning_message_header + "\n\n"
            warnings.simplefilter('default', DeprecationWarning)
            warnings.warn(warning_message,
                            category=DeprecationWarning,
                            stacklevel=2)
            Logger().log_warn(full_warning_meesage)
            return func(*args, **kwargs)
        return deprecated_func
    return deprecated_decorator

def unsupported(message):
    """
    To use:
        from ExtremeAutomation.Utilities.deprecated import unsupported
        @unsupported('This function is not supported')
    :param message: The message for the exception
    :return: None, but will throw: UnsupportedKeywordException
    """
    def unsupported_decorator(func):
        def unsupported_func(*args, **kwargs):
            error_message_header = ("*" * 200) + "\n"
            error_message = f"UNSUPPORTED FUNCTION ERROR -> {func.__name__} is an unsupported function and can not be used. {message}"
            full_error_meesage = "\n\n" + error_message_header + "\n\t" + error_message + "\n\n" + error_message_header + "\n\n"
            Logger().log_error(full_error_meesage)
            raise UnsupportedKeywordException(full_error_meesage)
        return unsupported_func
    return unsupported_decorator
