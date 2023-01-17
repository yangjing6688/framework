# Switch Keywords

## Introduction
The process to create a new keword is defined below. Keywords are generated from yaml files to ensure that all of the code 
will be generated the same way and the global features such as kwargs for keywords will be correctly implemented. When creating a
new keywords we will always start with the yaml file definition.

## Keyword Yaml File Definition
All switch keywords are generated with the yaml files located in the folllowing directory: `ExtremeAutomation\Apis\NetworkElements\ApiDefinition`
. The NetworkElements are the generic term given to the switch. Within this directory we have two directories based on the interaction with a switch.

### CommandApiDefinition
In the `CommandApiDefinition` directory, we have the list of commands that will be sent to the swtich. The command output will be returned to the caller. 
The directoires under this heading will contain a list of yaml files by protocol based on where they fit in this directory struture.
The user should be able to search for like keywords based on the protocol to see where the file is located or they can just open up 
the directories to find the file. For example if you were going to add a new vlan keyword you would look under the L2 directory and find
the vlan.yaml file and open it. You could also search on vlan (the protocol) and see where this file was located.

#### The yaml file stucture
The file will start with the feature name followed by the name of the keyword.

     feature_name:
         api_set_method_name:
             description: Information about the keyword function.
             uuid: uuid from https://www.uuidgenerator.net/version1
             arguments:
                 order: arg2,arg3,arg1
             apis:
                 CLI:
                     - [OS1,Platform,Version,Unit,Command,Prompt,PromptArgs,ConfirmationPhrases,ConfirmationArgs,IgnoreError,AddError]
                     - [OS2,Platform,Version,Unit,Command,Prompt,PromptArgs,ConfirmationPhrases,ConfirmationArgs,IgnoreError,AddError]
                 REST:
                     - [OS1,Platform,Version,Unit,Request Type,URI,Headers,Ignore Error String,Add Error String]
                 SNMP:
                     - [OS1,Platform,Version,Unit,SNMP Command Type,OID,SNMP Data Type,Value]


The after `feature_name` is the name of the keyword see `api_set_method_name` of the keyword. The name should follow the format:

    <action>_<event>
    Actions:
        create
        delete
        set
        clear
        enable
        disable
        verify
    Example: create_vlan()

* Next we have a `description` of the keyword. The user will fill in the description field with text about the new keyword.
* The `uuid` Here the user can generated or leave this field blank. When the code is genreated from these files, a new uuid will be generated.
* `Arguments` and `order' We are able to support all device types with these keywords and doing so requires us to make sure we have the correct
argument order in the keywords. In this field we list all of the arguments in the order that we expect them so that we can always be use that the 
correct arguments are passed in and used in the commands below.
* `apis` - We split up the apis info how the command will be send. `CLI` is for a command that will be sent via Telnet / SSH / Console, `REST` is 
for a command that can be sent via rest. `SNMP` is for a command that can be send by SNMP.

Within these areas the user can define a keyword and by completing the information for that section.

### CLI
* `OS` - The user would input the correct OS type. OS Types are found in this file 
[NetworkElementConstants.py](https://github.com/extremenetworks/extreme_automation_framework/blob/main/ExtremeAutomation/Library/Device/NetworkElement/Constants/NetworkElementConstants.py)
 the the framework by the variable OS_<type>.
* `Platform` - Set this to `base` by default. This is used in case of a new platform type is needed.
* `Version` - Set this to `baseversion` by default. This is used in case of a new version of firmware has a different command.
* `Unit` - Set this to `baseunit` by default. This is used in case a new unit type is needed. 
* `Command` - This is the command that will be send via the CLI. Special chars are {arg}, where `arg` is the argument name that was used in the `Arguments` and `order` above. Please think about all devices when choosing argument names.
* `Prompt` - This is if the command requires a prompt change. Prompts are found in this file [NetworkElementConstants.py](https://github.com/extremenetworks/extreme_automation_framework/blob/main/ExtremeAutomation/Library/Device/NetworkElement/Constants/NetworkElementConstants.py) under this section # CLI Prompts and by the variables marked PROMPT_<type>.
* `PromptArgs` - This are for any arguments that are needed for the prompt. 
* `ConfirmationPhrases` - In some CLI commands the CLI will ask a question. Here you would put that question. For example `Would you like to reboot (y/n)`. This can be list if there is more than one.
* `ConfirmationArgs` - In some CLI commands the ConfirmationPhrases requires input such as `(y/n)`, so here enter in the desired input value. This can be list if there is more than one.
* `IgnoreError` - Sometimes the command output will show a known error which will cause the keyword to file. In this case you can put in a list of values to ignore such as `error` if it appears in the output for the command.
* `AddError` - Here are can add new values to the list of strings to look for in the output of the command beyond the standard values.


### `TODO` - Rest
* OS1
* Platform
* Version
* Unit
* Request Type
* URI
* Headers
* Ignore Error String
* Add Error String

### `TODO` - SNMP
* OS1
* Platform
* Version
* Unit
* SNMP Command Type
* OID
* SNMP Data Type
* Value


## Generate the new keywords
Once the correct values have been entered into the yaml file(s), you are ready to generate the keywords. 

  1. Open a command prompt window and cd to extreme_automation_framework\ExtremeAutomation\Apis\
  2. Type in the command: `python GenerateApisFromDefinitionFiles.py`
     1. The Generator will load and print out:
     

      Device type? [1]
      [1] Network Element
      [2] Endsystem Element

  3. Choose 1 for Network Elemenet.
    

    What type of API is being parsed? [1]
    [1] Command
    [2] Parse



  4. Choose 1 for Command.


    What agent is being used? [1]
    [1] CLI
    [2] REST
    [3] SNMP



  5. Choose 1 for CLI, repeat steps 1-4 for other types if needed.
  6. This will generate the code and updated documentation for the framework.
     1. Code: extreme_automation_framework/ExtremeAutomation/Keywords/NetworkElementKeywords/GeneratedKeywords
     2. Documentation: extreme_automation_framework/ExtremeAutomation/Documentation/Generated






### `TODO` ParseApiDefinition
In the `ParseApiDefinition` directory, we have a list of parsers that will process the command output that was returned from a `CommandApiDefinition` call.
The directoires under this heading will contain a list of yaml files by protocol based on where they fit in this directory struture.
The user should be able to search for like keywords based on the protocol to see where the file is located or they can just open up 
the directories to find the file. For example if you were going to add a new vlan keyword you would look under the L2 directory and find
the vlan.yaml file and open it. You could also search on vlan (the protocol) and see where this file was located.

