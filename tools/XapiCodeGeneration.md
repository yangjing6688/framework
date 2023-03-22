# How to generate the XAPI code for the SDK
The code is generated with the GenerateXApiBaseKeywords.py python file. It takes one argument for the directory of the ExtremeCloudIQ SDK API. 

1. Clone the repository for the ExtremeCloudIQ SDK - https://github.com/extremenetworks/ExtremeCloudIQ-SDK-Python
2. Clone the repository for the extreme_automation_framework - hhttps://github.com/extremenetworks/extreme_automation_framework
3. In the extreme_automation_framework, locate the GenerateXApiBaseKeywords.py python script located here: https://github.com/extremenetworks/extreme_automation_framework/tree/main/tools/xapi
4. In the ExtremeCloudIQ SDK, locate the API directory in the repository on your location machine: https://github.com/extremenetworks/ExtremeCloudIQ-SDK-Python/tree/main/extremecloudiq/api
5. Invoke the GenerateXApiBaseKeywords.py python script with the following argument -x <your local directory>/ExtremeCloudIQ-SDK-Python/extremecloudiq/api


            GenerateXApiBaseKeywords.py -x <your local directory>/ExtremeCloudIQ-SDK-Python/extremecloudiq/api

4. The XAPI code files will be generated in the extreme_automation_framework/keywords/xapi_base directory https://github.com/extremenetworks/extreme_automation_framework/tree/main/keywords/xapi_base
