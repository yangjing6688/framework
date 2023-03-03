# Create a new XAPI class to match the UI keyword
The classed in the folders below contain keywords that should match up with the UI keywords under the flows directory. 
If you are added support for XAPI for a UI keyword, the class should be created in this directory based on where it is
located in the flows directory. 

# Review the UI keyword
You will need to review the UI keyword to order to understand what this keyword does and you will need to see if the 
XAPI SDK can do the same thing. If they keyword isn't fully supported we will need to write up a Jira ticket with 
the XAPI SDK team and get that addressed. If the UI keyword is fully supported we can implement the details below.

# How to Identity the XAPI SDK Support for UI Keyword
Here are a few tools to help you identify if a UI keyword can be converted to XAPI. The SDK is located (here)[http://pypi.org/project/extremecloudiq-api/]. 
You will need to download and install this package on your development system. Since you should already have the (Extreme_automation_framework)[] and
(Extreme_automation_tests)[https://github.com/extremenetworks/extreme_automation_tests] 

# Create the new XAPI class
This class should be in the same directory as the UI class counter part. Create a new directory and create a new class / functions
with the following name structure:


                File Name: Xapi<ui class name>.py
                Class Name: Xapi<ui class name>
                Function Name: xapi_<ui function name>



# Modify the UI keywords to call the new XAPI class
We need to modify the original UI keyword commment block with the following addition:

        
         Supported Modes:
            UI - default mode
            XAPI - kwargs XAPI_ENABLE=True (Will only support XAPI keywords in your test)

This will allow all users to know that this keyword now support the XAPI method. Nest we need to 
modify the original UI keywords with the following code:

        
            
    
    
            
