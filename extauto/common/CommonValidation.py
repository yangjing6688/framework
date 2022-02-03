from common.Utils import Utils
import traceback

class CommonValidation():
    
    def __init__(self):
        self.utils = Utils()
    
    def validate(self, value, expectedValue, **kwargs):
        """
        Description: Validate the input values for framework
        
        kwargs:
        
            fail_msg = The message to print on failure
            pass_msg = The message to print on success
            ignore_cli_feedback = which ignores any errors or output from the keyword
            expect_error = verifies that an error was returned by the keyword
        """
        default_fail_msg = "The keyword had a result of fail"
        fail_msg = self.get_kwarg(kwargs, "fail_msg", default_fail_msg)
        pass_msg = self.get_kwarg(kwargs, "pass_msg", "")
        
        # If the keyword is supported check for the existence of two kwargs.
        # ignore_cli_feedback, which ignores any errors or output from the keyword when
        # determining keyword pass/fail. expect_error, which verifies that an error
        # was returned by the keyword.
        ignore_cli = self.get_kwarg_bool(kwargs, "ignore_cli_feedback", False)
        expect_error = self.get_kwarg_bool(kwargs, "expect_error", False)
        
        # Get the expected value test result
        test_result = False
        if value == expectedValue:
            test_result = True

        # If we are enabling both of this options that isn't allowed!
        if ignore_cli and expect_error:
            raise ValueError("Both ignore_cli_feedback and expect_error cannot be enabled.")
        
        # First check if there was a cli error.
        if not test_result and ignore_cli:
            test_result = True
        
        if expect_error and not test_result:
            test_result = True
        elif expect_error and test_result:
            test_result = False
            
        # print the output
        if test_result:
            self.utils.print_info(pass_msg)
        else:
            # Print the error message
            self.utils.print_info(fail_msg)
            
            # if we have the default fail msg, let's print the calling stack trace so users can find the failing keyword.
            if fail_msg == default_fail_msg:
                for line in traceback.format_stack():
                    self.utils.print_info(line.strip())
        
        return test_result
                
            
    