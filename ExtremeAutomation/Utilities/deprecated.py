import warnings
from ExtremeAutomation.Library.Logger.Logger import Logger

def deprecated(message):
  def deprecated_decorator(func):
      def deprecated_func(*args, **kwargs):
          warning_message_header = "***********************************************************************************************************************************************************************************************************************************\n"
          warning_message = "DEPRECATED FUNCTION WARNING -> {} is a deprecated function. This method can be removed from the framework at anytime. {}".format(func.__name__, message)
          full_warning_meesage = "\n\n" + warning_message_header + "\n\t" + warning_message + "\n\n" + warning_message_header + "\n\n"
          warnings.warn(warning_message,
                        category=DeprecationWarning,
                        stacklevel=2)
          warnings.simplefilter('default', DeprecationWarning)
          Logger().log_warn(full_warning_meesage)
          return func(*args, **kwargs)
      return deprecated_func
  return deprecated_decorator
