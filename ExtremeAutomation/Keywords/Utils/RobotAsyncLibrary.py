import time
import logging
import threading
from io import StringIO
from robot.libraries.BuiltIn import BuiltIn
from robot.running.context import EXECUTION_CONTEXTS
from ExtremeAutomation.Library.Logger.Logger import Logger
from ExtremeAutomation.Keywords.FailureException import FailureException


class ThreadFilter(logging.Filter):
    def __init__(self, thread_name):
        super(ThreadFilter, self).__init__()
        self.thread_name = thread_name

    def filter(self, record):  # noqa: A003
        """
        Check the record's thread name against the thread filter's thread name, if they match
        allow the record.
        """
        return self.thread_name == record.threadName


class KeywordThread(object):
    """
    This class is used to keep info about a keyword thread together.

    It is also responsible for logging the keyword data after the thread has completed.
    """

    # Creates a logger object for the KeywordThread, this doesn't need to change
    # for each instance.
    logger = Logger()

    # Map each log level to the logger function to log at that level. Used
    # later in log_data.
    log_level_map = {"INFO": logger.log_info,
                     "DEBUG": logger.log_debug,
                     "TRACE": logger.log_trace,
                     "WARN": logger.log_warn,
                     "ERROR": logger.log_error}

    def __init__(self, thread, kw):
        self.thread = thread
        self.kw = kw
        self.thread_name = thread.name
        self.data = StringIO()
        self.log_handler = None

    def log_data(self):
        """
        This function parses through the keyword log data after the keyword thread
        finishes completion. It iterates over each message and logs it at the
        appropriate level.
        """
        # Split the data in the StringIO() object on "||" and remove any empty lines, we don't
        # need to log those.
        log_data_split = [i.strip() for i in self.data.getvalue().split("||") if i.strip() != ""]

        # For every message in the split log_data get the log level, if the level is in the
        # log_level_map get the message then call the log_level_map function that matches
        # the level.
        for msg in log_data_split:
            msg_split = msg.split(" - ")
            log_level = msg_split[1].strip()

            if log_level in self.log_level_map:
                log_msg = msg_split[3]
                self.log_level_map[log_level](log_msg)

    def handle(self):
        """
        This function removes log handler from the main log after the thread has completed.
        """
        self.logger.logger.removeHandler(self.log_handler)


class RobotAsyncLibrary(object):
    """
    Robot library for running keywords asynchronously. Allows for keywords to be started
    in separate threads and then join them later either individually or all at once.
    """

    logger = Logger()
    built_in = BuiltIn()

    def __init__(self):
        self.threads = {}

    def create_keyword_thread(self, kw, *args):
        """
        Creates a thread for the given keyword.

        Keyword Arguments:
            kw - The (string) name of the keyword that should be run. The name should
                 follow robot naming conventions. For example show_vlan, Show VLAN, and show vlan
                 would all be acceptable.
            *args - All the args that should be passed to the keyword. This should be a >2 space delimited
                    string listing the arguments.

        Example Usage:
            ${handle} =  Start Threaded Keyword  Create VLAN  device_name  11
        """
        # Log the keywords args.
        self.logger.log_trace("Keyword Arguments: [ {0} ]".format(" | ".join(args)))

        # Log the keyword that is being started in a thread. If a device name was passed
        # append that to the log message.
        dev_str = " on " + args[0] if len(args) > 1 else ""
        self.logger.log_info("Starting threaded keyword {0}{1}.".format(kw, dev_str))

        # Create the keyword thread. This returns the "handle" assigned to
        # the keyword, which is the created thread's name.
        return self.__create_thread(kw, args)

    def wait_for_thread(self, handle, timeout=60):
        """
        Waits for the given thread to finish execution before moving onto the next keyword.

        It will wait up to timeout seconds before considering the keyword a failure.

        Keyword Arguments:
            handle - The (string) handle that identifies the thread to wait for. The handle is returned
                     when a thread is created.
            timeout - The (string||int) amount of time in seconds the keyword should wait before considering
                      the keyword a failure.

        Example Usage:
            Wait for Thread  ${handle}  10
        """
        result = self.__wait_for_join(handle, timeout)

        # If we were unable to join the thread within <timeout> seconds fail the keyword.
        if not result:
            raise FailureException("Could not join " + handle + " within " + str(timeout) + " seconds.")
        self.logger.log_info("Threaded keyword " + handle + " finished execution.")

    def wait_for_all_threads(self, timeout=60):
        """
        Waits for all started threads to complete execution.

        This calls "wait_for_thread"
        as a keyword for each thread in the threads dictionary. This adds a separate entry
        in the log for each keyword, which makes parsing the thread output easier.

        Keyword Arguments:
            timeout - The (string/int) amount of time in seconds EACH thread should wait
            before considering the keyword a failure.

        Example Usage:
            Wait for All Threads  10
        """
        # Create a copy of self.threads because "wait_for_thread" will delete completed
        # threads. If the dictionary is changed during iteration an exception is thrown.
        # Using a cache avoids this issue.
        thread_cache = dict(self.threads)

        for handle in thread_cache:
            self.built_in.run_keyword("wait_for_thread", handle, timeout)

    def __wait_for_join(self, handle, timeout):
        """
        Tries to join the given thread. If the thread is able to join within <timeout> seconds
        True is returned, otherwise False. If the thread was joined it's thread is marked as
        handled and deleted from the threads dict.
        """
        # Attempt to convert the timeout to an int.
        try:
            timeout = int(timeout)
        except ValueError:
            timeout = 60

        # Get the KeywordThread object from the threads dictionary.
        kw_thread = self.threads[handle]

        # Call join(), this waits for the thread to complete before returning.
        result = self.__join_thread_with_timeout(kw_thread.thread, timeout)

        # Log all data logged during the keyword execution. We add a new log
        # handler to handle each threads output. We also filter out any log data
        # not from the MainThread in the main library logger.
        kw_thread.log_data()

        # If the thread was joined successfully call handle() on the KeywordThread to remove
        # it's log handler. Then delete the KeywordThread object.
        if result:
            kw_thread.handle()
            del self.threads[handle]

        return result

    def __configure_logger(self, thread_name):
        """
        This configures the logger to handle messages from each thread. This is needed because we cannot
        log messages to the MainThread while inside a keyword thread. The robot log becomes corrupted
        because messages are added outside of a keyword execution. The logger is reconfigured to filter
        out non-MainThread messages. Any messages from a keyword thread are handled by their own handler.
        This handler filters out all messages that are not from the originally created thread.
        """
        # Creates a logging StreamHandler using the StringIO() object created by
        # the KeywordThread object.
        handler = logging.StreamHandler(self.threads[thread_name].data)

        # Store the current thread's log handler in it's corresponding KeywordThread
        # object. This is needed so the handler can be removed later.
        self.threads[thread_name].log_handler = handler

        # Adds a formatter to the handler. This matches the usual log formatter with the exception
        # of the thread name prepended and "||" appended. "||" is used later to split each message
        # as they are logged as a single string in the StringIO() object.
        formatter = logging.Formatter(thread_name + " - %(levelname)s - %(asctime)s - %(message)s||")
        handler.setFormatter(formatter)

        # Add a filter to the handler. This filter filters out any message is not created by
        # the thread in the given KeywordThread object.
        handler.addFilter(ThreadFilter(thread_name))

        # Add the created handler to the main logger.
        self.logger.logger.addHandler(handler)

    def __create_thread(self, kw, args):
        """
        This function is responsible to creating and starting a KeywordThread. It creates a wrapper
        function which configures the logger and accesses internal robot methods to start a keyword
        without the normal robot logging features. Again this is needed to avoid corrupting the
        output.xml file.
        """
        def thread_wrapper():
            # Quick delay before actually starting the threads execution. This
            # is to avoid issues log messages after starting a thread.
            time.sleep(.25)

            # Configure the logger using the created thread's name.
            self.__configure_logger(threading.current_thread().getName())

            # Get the current robot execution context.
            context = EXECUTION_CONTEXTS.current

            # Get the keyword runner for the given keyword.
            runner = context.get_runner(kw)

            # This code comes from robots ._run method directly. We cannot use ._run() because
            # it logs the arguments of each keyword in a separate logger. This causes all the
            # arguments from everything thread to appear in the first wait_for_thread, which
            # is undesirable. Instead, we call the code after the arg log, then log the
            # manually so they appear in the correct threads wait.
            positional, named = runner._handler.resolve_arguments(args, context.variables)
            r = runner._runner_for(context, runner._handler.current_handler(), positional, dict(named))
            runner._run_with_output_captured_and_signal_monitor(r, context)

        # Create the keyword thread with a target of the thread_wrapper function.
        t = threading.Thread(target=thread_wrapper)

        # Mark each keyword thread as a daemon. This will prevent the robot test
        # from hanging when completed if there are zombie threads. All threads will
        # be stopped once the main thread is done.
        t.daemon = True

        # Create the KeywordThread object based on the Thread() object and keyword name.
        # Then add the created KeywordThread object to the threads dictionary using the
        # thread's name as the key.
        keyword_thread = KeywordThread(t, kw)
        self.threads[t.name] = keyword_thread

        # Start the thread and return its name.
        t.start()
        return t.name

    @staticmethod
    def __join_thread_with_timeout(thread, timeout):
        """
        This function attempts to join a thread. First it tries to join the thread, timing
        out after 1 second. Since .join() always returns None we need to check is_alive()
        to determine if the thread joined or timed out. If is_alive is false it joined otherwise
        it did not. We try this for <timeout> seconds before returning False, otherwise we return
        True.
        """
        start = time.time()
        thread_alive = True

        while time.time() - start < timeout and thread_alive:
            thread.join(1)
            thread_alive = thread.is_alive()
            if not thread_alive:
                return True
        return False
