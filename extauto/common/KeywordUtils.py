import time
import inspect
from tools.xapi.XapiHelper import XapiHelper
from extauto.common.Utils import Utils
from uuid import UUID
from extauto.common.CommonValidation import CommonValidation
from ExtremeAutomation.Library.Utils.Singleton import Singleton

def is_valid_uuid(uuid_to_test, version=4):
    """
    Check if uuid_to_test is a valid UUID.

     Parameters
    ----------
    uuid_to_test : str
    version : {1, 2, 3, 4}

     Returns
    -------
    `True` if uuid_to_test is a valid UUID, otherwise `False`.

     Examples
    --------
    >>> is_valid_uuid('c9bf9e57-1685-4c89-bafb-ff5af830be8a')
    True
    >>> is_valid_uuid('c9bf9e58')
    False
    """

    try:
        uuid_obj = UUID(uuid_to_test, version=version)
    except ValueError:
        return False
    return str(uuid_obj) == uuid_to_test


class KeywordImplementations(object, metaclass=Singleton):
    """
    A utility used to determine which keyword implementation should be executed

    Keywords can be implemented in more than one way.  For example, the same keyword can be implemented in the GUI
    as well as XAPI.  This class is used to determine which implementations are available for each keyword as well as
    to determine which implementation should be used when running a test.
    """
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        self.xapiHelper = XapiHelper()
        self.utils = Utils()
        self.common_validation = CommonValidation()

        # The following dictionaries contain information about keyword implementations. This will be used to
        # tell the code if the particular keyword has support for the implementation type.  The dictionaries can also
        # be used to enable or disable a particular implementation type.  The structure is as follows:
        #  {
        #     keyword_name: {
        #        "implemented" : True/False
        #        "enabled" : True/False
        #        "default_enabled" : "True/False
        #     }
        #   }
        #
        #  implemented:  Indicates if the keyword is implemented for the implementation type associated with
        #       the variable.  For example, for the gui_keywords variable the value for "implemented" would indicate
        #       whether the keyword was implemented for the GUI.
        #
        #  enabled: Indicates if the associated keyword is enabled for the implementation type associated with the
        #       variable.
        #
        #  default_enabled: Used to return the enabled state back to the default state in the event a test changes
        #       whether a keyword is enabled for the implementation type associated with the variable.  For example if
        #       a test explicitly disables a keyword then want to change it back to the default state (which may have
        #       been disabled anyway) the test would be able to get the default_state from this attribute.
        #
        self.gui_keywords = {}
        self.xapi_keywords = {}

        # The following is used to indicate which keyword implementation should be preferred during the test run.
        # This value can be changed throughout the test.  For example, a test writer may want to use XAPI during setup
        # and teardown but use GUI during the rest of the test.
        #
        # We'll default to GUI
        self.preferred_implementation = 'GUI'

        # If the test was started with XAPI_ENABLE in the environment then the user wants to prefer XAPI during the
        # entire test run so we'll change the default to XAPI in that case.
        if self.xapiHelper.is_xapi_enabled():
            self.preferred_implementation = 'XAPI'

        # This variable indicates all the possible keyword implementations
        self.supported_keyword_implementations = ['GUI', 'XAPI']

        # Every keyword must have a UUID in order to store keyword data in an application database.  As keywords
        # are called the UUIDs of the keywords are stored here.
        self.keyword_uuids = {}

        # When logging in via GUI or XAPI we'll set these to True so we know that keywords can use that implementation
        self.xapi_active = False
        self.gui_active = False

        # It's possible to run tests and require all keywords to run a specific version of a keyword.  For example,
        # if the user sets 'XAPI_ONLY' to True and passes it into login_user() as a kwarg then the test must run
        # only XAPI keywords.  No GUI keywords can be run in that case.  Similarly, if xapi is not enabled then the
        # test must run ONLY GUI based keywords and XAPI keyword would fail.
        #
        # If the user doesn't run tests in only XAPI or GUI mode then it'll run tests in a combination mode where
        # the tests will run XAPI or GUI implementations depending on the global attribute 'preferred_implementation'
        # and individual keyword 'implemented' settings.
        self.xapi_only = False
        self.gui_only = False

        # When running tests with multiple windows the user may login more than once.  We don't want to logout of
        # XAPI until all of the windows are closed to avoid logging out of XAPI too early and invalidating the
        # credentials.  The following value keeps track of the number of times the GUI has been logged into.
        self.gui_login_count = 0

    def set_xapi_active(self, new_value: bool = True):
        """
        Sets xapi_active attribute to True or False

        The xapi_active attribute is used to determine if the user has logged into XAPI.  If so, then it's okay to
        run XAPI keywords.  If the user has not logged into XAPI then it's not okay to run XAPI keywords because the
        keywords will fail

        :param new_value: The value to be set for xapi_active attribute
        :return: None
        """

        # Make sure we were passed in a boolean value
        if not isinstance(new_value, bool):
            new_value = True

        # Save the desired or default value
        self.xapi_active = new_value
        return None

    def set_gui_active(self, new_value: bool = True):
        """
        Sets gui_active attribute to True or False

        The gui_active attribute is used to determine if the user has logged into the GUI.  If so, then it's okay to
        run GUI keywords.  If the user has not logged into the GUI then it's not okay to run GUI keywords because the
        keywords will fail

        :param new_value: The value to be set for gui_active attribute
        :return: None
        """

        # Make sure we were passed in a boolean value
        if not isinstance(new_value, bool):
            new_value = True

        # Save the desired or default value
        self.gui_active = new_value

        # Keep track of the number of GUI logins so we logout of XAPI only when ther are no GUI logins left
        if new_value == True:
            self.gui_login_count += 1

        return None

    def set_keyword_uuid(self, keyword_uuid, keyword_name=None, **kwargs):
        """
        Set the UUID for a keyword based on the keyword_name

        :param keyword_uuid - The UUID to be associated with the keyword
        :param keyword_name - The name of the keyword that will be assigned the UUID.  If a keyword_name is not
               supplied the name will be assumed to be the name of the calling method.

        :return True if the UUID for the keyword was recorded, else False

        """
        # Use the passed in keyword name or get the name of the calling function if a name was not passed in
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]

        # Make sure the caller passed in a valid UUID
        if not is_valid_uuid(keyword_uuid):
            return False

        # Record the UUID for this keyword
        self.keyword_uuids[keyword_name] = keyword_uuid
        return True
    def get_uuid_from_keyword_name(self, keyword_name):
        """
        Given a keyword_name get the associated keyword UUID.

        The keyword UUID is a unique identifier assigned to each keyword when the keyword is moved to the keywords
        directory in the extreme_automation_framework repository.

        :param keyword_name: The name of the keyword for which the UUID is desired
        :return: The UUID of the keyword identified by keyword_name or None if the keyword's UUID has not been recorded
        """
        return self.keywords_uuids.get(keyword_name, None)

    def select_keyword_implementation(self, keyword_name=None, **kwargs):
        """
        Given a keyword, determine which implementation (if any) should be run

        This method will determine which implementation (GUI, XAPI etc.) should be run based on configuration settings.
        If no runnable implementation is available for the keyword this method will raise an error.

        Note:
           Users have an option of using XAPI_ONLY when running their test.  If the user puts that value into
           the kwargs prior to running login_user then the test must run only XAPI implementations.  If there is a
           keyword doesn't have an XAPI implementation then the test must fail.

        :return: The implementation that should be run for the keyword based on current configuration settings and
                 keyword supported implementations.  The value will be returned as a string.  The list
                 of valid strings can be found in the {self.supported_keyword_implementations} attribute.

                 If a valid implementation does not exist this method will return an empty string ('')
        """

        # If the keyword_name is not passed in, use the calling function as the keyword_name
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]

        # Determine the ability to run the keyword in the various implementations
        gui_ok = self._is_gui_enabled(keyword_name) and self.gui_active
        xapi_ok = self._is_xapi_enabled(keyword_name) and self.xapi_active

        # If there is no valid implementation then return: None
        if gui_ok != True and xapi_ok != True:
            kwargs['fail_msg'] = f"Keyword [{keyword_name}] does not have a valid/enabled implementation"
            self.common_validation.fault(**kwargs)
            return ''

        # If the kwarg XAPI_ENABLE is passed in, then the caller wants to explicitly use XAPI
        if kwargs.get('XAPI_ENABLE'):
            if xapi_ok:
                self.utils.print_info(f"Selecting XAPI keyword implementation for: '{keyword_name}' -- XAPI_ENABLE passed in via kwargs")
                return 'XAPI'
            else:
                kwargs['fail_msg'] = f"Keyword [{keyword_name}] does not have a valid/enabled XAPI implementation and kwargs has XAPI_ENABLE"
                self.common_validation.fault(**kwargs)

        # Run the keyword's preferred implementation if a preferred implementation for the keyword exists
        if gui_ok and self.gui_keywords[keyword_name]["gui_preferred"]:
            self.utils.print_info(f"Selecting GUI keyword implementation for: '{keyword_name}' -- GUI is the preferred implementation for this keyword")
            return 'GUI'
        if xapi_ok and self.xapi_keywords[keyword_name]["xapi_preferred"]:
            self.utils.print_info(f"Selecting XAPI keyword implementation for: '{keyword_name}' -- XAPI is the preferred implementation for this keyword")
            return 'XAPI'

        # Run the global preferred implementation if it's available
        if self.preferred_implementation == 'XAPI' and xapi_ok:
            self.utils.print_info(f"Selecting GUI keyword implementation for: '{keyword_name}' -- GUI is the global preferred implementation")
            return 'XAPI'
        if self.preferred_implementation == 'GUI' and gui_ok:
            self.utils.print_info(f"Selecting XAPI keyword implementation for: '{keyword_name}' -- XAPI is the global preferred implementation")
            return 'GUI'

        # At this point the preferred method is not available but there is a valid implementation to run.  By default,
        # prefer the GUI method
        if gui_ok:
            self.utils.print_info(f"Selecting GUI keyword implementation for: '{keyword_name}' -- by default")
            return 'GUI'
        elif xapi_ok:
            self.utils.print_info(f"Selecting XAPI keyword implementation for: '{keyword_name}' -- by default")
            return 'XAPI'
        else:
            kwargs['fail_msg'] = f"Unable to select implementation for keyword '{keyword_name}'"
            self.common_validation.fault(**kwargs)
            return ''

    def _is_gui_enabled(self, keyword_name):
        """
        Determines if a keyword is enabled for the GUI.  If enabled the GUI based keyword can be run.
        :return: True if the keyword exists and is enabled for the GUI, otherwise returns False
        """
        if keyword_name in self.gui_keywords.keys():
            implemented = self.gui_keywords[keyword_name].get("implemented", False)
            enabled = self.gui_keywords[keyword_name].get("enabled", False)
            return implemented and enabled
        else:
            return False

    def _is_xapi_enabled(self, keyword_name):
        """
        Determines if a keyword is enabled for the XAPI.  If enabled the XAPI based keyword can be run.
        :return: True if the keyword exists and is enabled for the XAPI, otherwise returns False
        """
        if keyword_name in self.xapi_keywords.keys():
            implemented = self.xapi_keywords[keyword_name].get("implemented", False)
            enabled = self.xapi_keywords[keyword_name].get("enabled", False)
            return implemented and enabled
        else:
            return False

    def xapi_enable(self, keyword_name):
        """
        Enable XAPI support for the specified keyword
        :param keyword_name: The keyword which will be enabled for XAPI implementation
        :return: None
        """
        self.xapi_keywords[keyword_name]["enabled"] = True
        return None

    def gui_enable(self, keyword_name):
        """
        Enable GUI support for the specified keyword
        :param keyword_name: The keyword which will be enabled for GUI implementation
        :return: None
        """
        self.gui_keywords[keyword_name]["enabled"] = True
        return None

    def xapi_disable(self, keyword_name):
        """
        Disable XAPI support for the specified keyword
        :param keyword_name: The keyword which will be disabled for XAPI implementation
        :return: None
        """
        self.xapi_keywords[keyword_name]["enabled"] = False
        return None
    def gui_disable(self, keyword_name):
        """
        Disable GUI support for the specified keyword
        :param keyword_name: The keyword which will be disabled for GUI implementation
        :return: None
        """
        self.gui_keywords[keyword_name]["enabled"] = False
        return None

    def not_supported(self, **kwargs):
        """
        "Run" a keyword that is "Not Supported", return a value indicating whether the keyword should fail or not

        There are some keywords that will never support certain keyword implementations.  For example, "quit_browswer"
        will never have support for XAPI because XAPI does not use a browser.  This means if the keyword is called
        in a test case for an XAPI only test the keyword is really a NOOP.  In this case, the keyword must return
        whatever the caller is expecting.  For example, if the caller is expecting the keyword to pass, then it must
        return the return code expected for the keyword when it passes.  If the caller is expecting the keyword to fail,
        then it must return a return code that indicates the keyword failed.

        A keyword that is "not supported" is different from a keyword that is "not implemented".  A keyword that is
        "not supported" indicates that we will not ever implement the keyword for the implementation_type.  A keyword
        that is "not implemented" means the keyword should be implemented for the implementation_type but just hasn't
        been implemented yet.

        This method will return True, if the "not supported" keyword should return a "Passed" return_code.  The method
        will return False, if the "not supported" keyword should return a "Failed" return_code.  For example, when
        the kwargs include "expect_error=True".

        :return: True: if the keyword should return a "Passed" return_code.  False: if the keyword should return a
             "Failed" return_code.
        """
        kwargs["not_supported"] = True
        return self.common_validation.validate(None, None, **kwargs);


    def gui_implemented(self, keyword_name=None, enable_keyword=True, prefer_gui=False):
        """
        Record GUI support for the keyword

        This method is to be called by initial keyword code to indicate the keyword is supported via the GUI.

        :param keyword_name:  If provided, indicates which keyword has been implemented for the gui.  If not
           provided the name of the calling function will be used.
        :param enable_keyword: If True the keyword will be enabled, if False the keyword will be disabled and the
           gui implementation won't be used until it is enabled.
        :return: None
        """

        # Use the passed in keyword name or get the name of the calling function if a name was not passed in
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]

        # Create the keyword name in the gui_keyword dictionary if it hasn't already been created
        if keyword_name not in self.gui_keywords.keys():
            self.gui_keywords[keyword_name] = {}

        # Save the implemented status of this keyword
        self.gui_keywords[keyword_name]["implemented"] = True
        self.gui_keywords[keyword_name]["gui_preferred"] = prefer_gui

        # Record whether or not the keyword is enabled
        if enable_keyword:
            self.gui_keywords[keyword_name]["enabled"] = True
        else:
            self.gui_keywords[keyword_name]["enabled"] = False
        return None

    def xapi_implemented(self, keyword_name=None, enable_keyword=True, prefer_xapi=False):
        """
        Record GUI support for the keyword

        This method is to be called by initial keyword code to indicate the keyword is supported via XAPI

        :param enable_keyword: If True the keyword will be enabled, if False the keyword will be disabled and the
           XAPI implementation won't be used until it is enabled.
        :return: None
        """
        # Use the passed in keyword name or get the name of the calling function if a name was not passed in
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]

        # Create the keyword name in the gui_keyword dictionary if it hasn't already been created
        if keyword_name not in self.xapi_keywords.keys():
            self.xapi_keywords[keyword_name] = {}

        # Save the implemented status of this keyword
        self.xapi_keywords[keyword_name]["implemented"] = True
        self.xapi_keywords[keyword_name]["xapi_preferred"] = prefer_xapi

        # Record whether or not the keyword is enabled
        if enable_keyword:
            self.xapi_keywords[keyword_name]["enabled"] = True
        else:
            self.xapi_keywords[keyword_name]["enabled"] = False
        return None

    def set_preferred_implementation(self, preferred_implemenation: str = "GUI"):
        """
        Set the preferred implementation to run for all keywords run during this test
        :param preferred_implemenation: The preferred implementation that should be run for all keywords.
             This should be one of:
                 GUI
                 XAPI
        :return: True if {preferred_implementation} is valid and has been saved; otherwise False
        """

        # Validate {preferred_implementation}
        if not preferred_implemenation in ['GUI', 'XAPI']:
            return False

        # Save the preferred keyword implementation
        self.preferred_implementation = preferred_implemenation
        return True

class KeywordTiming(object, metaclass=Singleton):
    """
    A utility used to calculate and record the amount of time each keyword takes
    """
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        self.timing_dict = {}
        self.current_keyword_name = ''
        self.current_keyword_implementation = ''
        self.current_keyword_start_time = None
        self.utils = Utils()
        self.common_validation = CommonValidation()

    def start(self, keyword_name: str = None, keyword_implementation: str = 'GUI'):
        """
        Starts recording the amount of time it takes for this keyword to run

        Parameters:
          keyword_implementation: How the running version of the keyword is implemented.  This can be any string
            that defines an implementation type.  Current expected values are 'GUI' or 'XAPI'
        """

        # Use the keyword name passed in if one was passed in.  Otherwise, assume the keyword name is the caller
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]

        # Save information for the current timing period.  This will get reset if this method is called again before
        # calling end().  Only one keyword can be timed at one time.
        self.current_keyword_name = keyword_name
        self.current_keyword_implementation = keyword_implementation
        self.current_keyword_start_time = time.time()

    def end(self, keyword_name: str = None, **kwargs):

        # If timing was never started then don't record the end
        if not self.current_keyword_name:
            self.utils.print_warning(f"Keyword [{keyword_name}] has called end() to end timing a keyword, but currently no keywords are being timed")
            return

        # Make sure the keyword that is currently being timed is the one that is ending
        if keyword_name is None:
            keyword_name = inspect.stack()[1][3]
        if keyword_name != self.current_keyword_name:
            self.utils.print_warning(f"Keyword [{keyword_name}] has called end() to end timing a keyword, but the keyword currently being timed is [{self.current_keyword_name}]")
            return

        # Calculate how long it took to run the current keyword
        end_time = time.time()
        execution_time = (end_time - self.current_keyword_start_time)

        # Create a record of the length of time it took to run this keyword
        timing_dict = {
            "start_time": self.current_keyword_start_time,
            "end_time": end_time,
            "execution_time": execution_time
        }

        # Print the keyword timing data
        self.utils.print_info(f"** Keyword Timing ** {self.current_keyword_implementation} ** {self.current_keyword_name} - {execution_time}")

        # Add the results of this keyword to the timing dictionary.  Results are stored in an array so if a keyword
        # is called multiple times it will capture each call
        if self.current_keyword_name in self.timing_dict.keys() and self.current_keyword_implementation in self.timing_dict[self.current_keyword_name].keys():
            self.timing_dict[self.current_keyword_name][self.current_keyword_implementation].append(timing_dict)
        else:
            self.timing_dict = {
                self.current_keyword_name:  {
                    self.current_keyword_implementation: [timing_dict]
                }
            }


        # Reset keyword timing information for the current keyword
        self.current_keyword_start_time = None
        self.current_keyword_name = None


class KeywordUtils(object, metaclass=Singleton):

    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        self.utils = Utils()
        self.implementations = KeywordImplementations()
        self.timing = KeywordTiming()

    def wait_for_elements_to_load(self, find, wait_time=1, loop_max=30, **args):
        """Waits for the number of found elements to stabilize in order to avoid stale elements.
        Stops once the numbers are the same between two subsequent cycles.

        :param find: function
            Function to find the elements.
        :param wait_time : int
            Duration to wait for loading
        :param loop_max : int
            Maximum number of times to check if the count of elements has changed.
        :return found elements for which to wait for
        :raises ExceededWaitForElementsCountToStabilizeLimitException
            If max_check_cycles is reached.
        """

        elements = find()
        last_count = len(elements)
        current_count = -1
        loop_index = 0

        while last_count != current_count and loop_index < loop_max:
            time.sleep(wait_time)  # Allow for elements to load
            elements = find()
            last_count = current_count
            current_count = len(elements)
            self.utils.print_info(
                f"Getting: current_count = {current_count}, last_count = {last_count}, loop_index = {loop_index}")

            # Fail safe... If we keep getting different counts for loop_max seconds then fail
            loop_index = loop_index + 1

        if loop_index >= loop_max:
            raise Exception(loop_max)

        return find()
