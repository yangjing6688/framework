# The XAPI to GUI Keyword Support
This area of the framework is for XAPI to UI keyword support. Here you would be able to create new keywords that will support
the same functionality as the UI equivalent. These keywords are not designed to be called directly as the same functionality will 
be created for UI keyword. The UI keywords are intended to be used in the test cases. With the following flag set XAPI_ENABLE=True,
the XAPI version of the UI keyword will be called. You can set this at the test cases level in the test case file or you can set
the variable in Robot `-v XAPI_ENABLE:true` or in Pytest `--xapienable`. 

# Create a new XAPI class to match the UI keyword
The classes in the folders below contain keywords that should match up with the UI keywords under the flows directory. 
If you are added support for XAPI for a UI keyword, the class should be created in this directory based on where it is
located in the `Extreme_Automation_Framework\extauto\xiq\flows` directory. 

# Review the UI keyword
You will need to review the UI keyword to order to understand what this keyword does and you will need to see if the 
XAPI SDK can do the same thing. If they keyword isn't fully supported we will need to write up a Jira ticket with 
the XAPI SDK team and get that addressed. If the UI keyword has a set of XAPI(s) that are fully supported we can 
implement the details below.

# How to Identity the XAPI SDK Support for UI Keyword
Here are a few tools to help you identify if a UI keyword can be converted to XAPI. The SDK is located [here](http://pypi.org/project/extremecloudiq-api/). 
You will need to download and install this package on your development system. Since you should already have the [Extreme_automation_framework](https://github.com/extremenetworks/extreme_automation_framework) and
[Extreme_automation_tests](https://github.com/extremenetworks/extreme_automation_tests) on your development machine you can just install the requirement.txt file
from the tests repository. 

        cd <root for extreme_automation_tests>
        pip install -r requirements.txt

Next you can use the following website to see what Rest interfaces you could use support the UI Keywords.
[The ExtremeCloud IQ API](https://api.extremecloudiq.com/swagger-ui/index.html). The framework base keywords are located
in the following (directory)[https://github.com/extremenetworks/extreme_automation_framework/tree/main/keywords/xapi_base]. 
you can use these keywords that hook into the SDK in your XAPI framework class. Locate all of the classes that you will 
need to support the UI keywords from this code. 


# Create the new XAPI class
This class should be in the same directory structure as the UI class counter part. For example if your keyword file name is: `Extreme_automation_framework\extauto\xiq\flows\manage\devices.py` then the file for the XAPI should be located in the following
directory `Extreme_automation_framework\extauto\xiq\xapi\manage\xapiDevices.py` Create a new directory and create a new class / functions
with the following name structure. 

                File Name: Xapi<ui class name>.py
                Class Name: Xapi<ui class name>
                Function Name: xapi_<ui function name>

These new classes should be created in the following [directory](https://github.com/extremenetworks/extreme_automation_framework/tree/main/extauto/xiq/xapi)
The base class for all of the created class should be the [XapiHelper](https://github.com/extremenetworks/extreme_automation_framework/blob/main/tools/xapi/XapiHelper.py)
class. This class contains useful functions that you help you write the framework support for the UI keyword. 

                from tools.xapi.XapiHelper import XapiHelper

                class Xapi<class name>(XapiHelper):

Import the classes that you have located above in the keywords directory. You will notice all of the functions within the class 
are documented with the usage for the keyword.

                from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
        
                def __init__(self):
                    self.xapiBaseAccountApi = XapiBaseAccountApi()

You can use this to import the class and create the instance of the class in the constructor (`__init__(self)`). Since you 
have created a new function name for the UI keyword, you should be able to call the XAPI SDK based on the classes that you
have imported above and write the same functionality as the UI keyword. 


# Modify the UI keywords to call the new XAPI class
We need to modify the original UI keyword comment block with the following addition:

        
         Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

This will allow all users to know that this keyword now support the XAPI method. Next we need to 
modify the original UI keywords with the following code template. The if statements ensures the 
XAPI_ENABLE flag is set for the test or keyword and the call is to the new XAPI function. 
    
     if self.xapi<your new classname>.is_xapi_enabled(**kwargs):
            return self.<your new classname>.xapi_<your new function name>(..., **kwargs)



        
            
    
    
            
