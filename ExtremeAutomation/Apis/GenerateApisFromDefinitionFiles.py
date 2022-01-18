from ExtremeAutomation.Library.Utils.PathUtils import PathUtils
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerateAllApis import GenerateAllApis
from ExtremeAutomation.Apis.ApiGeneration.Library.GenerationConstants import GenerationConstants
from ExtremeAutomation.Apis.ApiGeneration.CreateKeywords.CreateCliKeywords import CreateCliKeywords
import traceback
# from ExtremeAutomation.Library.Device.Common.ApiGeneration.CreateApi.CreateNorthboundKeywords \
#     import CreateNorthboundKeywords

# ###  A COMMENT IS DEFINITLY NEEDED HERE  ###

ALL_DEVICE_TYPES = [GenerationConstants.DEVICE_TYPE_NET_ELEM,
                    # GenerationConstants.DEVICE_TYPE_UI_ELEM,
                    GenerationConstants.DEVICE_TYPE_END_SYS_ELEM]

project_root = PathUtils.get_project_root()


def create_api_map():
    return_map = {
        GenerationConstants.DEVICE_TYPE_NET_ELEM: {
            "api_types":
                [GenerationConstants.API_TYPE_COMMAND,
                 GenerationConstants.API_TYPE_PARSE],
            "agent_types":
                [GenerationConstants.AGENT_TYPE_CLI,
                 GenerationConstants.AGENT_TYPE_REST,
                 GenerationConstants.AGENT_TYPE_SNMP]},
        GenerationConstants.DEVICE_TYPE_END_SYS_ELEM: {
            "api_types":
                [GenerationConstants.API_TYPE_COMMAND,
                 GenerationConstants.API_TYPE_PARSE],
            "agent_types":
                [GenerationConstants.AGENT_TYPE_CLI,
                 GenerationConstants.AGENT_TYPE_REST,
                 GenerationConstants.AGENT_TYPE_XMC_REST]},
        GenerationConstants.DEVICE_TYPE_UI_ELEM: {
            "api_types":
                [GenerationConstants.API_TYPE_COMMAND],
            "agent_types":
                [GenerationConstants.AGENT_TYPE_SELENIUM],
            "app_type":
                [GenerationConstants.APPLICATION_TYPE_EMC,
                 GenerationConstants.APPLICATION_TYPE_XCA,
                 GenerationConstants.APPLICATION_TYPE_GIM,
                 GenerationConstants.APPLICATION_TYPE_XMC,
                 GenerationConstants.APPLICATION_TYPE_EWC,
                 GenerationConstants.APPLICATION_TYPE_ECIQ,
                 GenerationConstants.APPLICATION_TYPE_DFNDR]
        }}

    return return_map


def get_info_from_user_v2(api_map):
    print("Device type? [1]")
    for i in range(len(ALL_DEVICE_TYPES)):
        print("[" + str(i + 1) + "] " + ALL_DEVICE_TYPES[i].replace("_", " ").title())

    dev_type = input("\n>>> ")
    dev_type_loop = True

    while dev_type_loop:
        if dev_type.isdigit():
            if int(dev_type) - 1 in range(len(ALL_DEVICE_TYPES)):
                dev_type_loop = False
                dev_type = int(dev_type) - 1
            else:
                print(("Integer must be in range " + str(range(len(ALL_DEVICE_TYPES))[0] + 1) + " - " +
                       str(range(len(ALL_DEVICE_TYPES))[-1] + 1)))
                dev_type = input("\n>>> ")
        elif dev_type == "":
            dev_type_loop = False
            dev_type = 0
        else:
            print("Please enter a valid integer.")
            dev_type = input("\n>>> ")

    valid_api_types = api_map[ALL_DEVICE_TYPES[dev_type]]["api_types"]
    valid_agent_types = api_map[ALL_DEVICE_TYPES[dev_type]]["agent_types"]

    print("What type of API is being parsed? [1]")
    for i in range(len(valid_api_types)):
        print("[" + str(i + 1) + "] " + valid_api_types[i].capitalize())

    api_type = input("\n>>> ")
    api_type_loop = True

    while api_type_loop:
        if api_type.isdigit():
            if int(api_type) - 1 in range(len(valid_api_types)):
                api_type_loop = False
                api_type = int(api_type) - 1
            else:
                print(("Integer must be in range " + str(range(len(valid_api_types))[0] + 1) + " - " +
                       str(range(len(valid_api_types))[-1] + 1)))
                api_type = input("\n>>> ")
        elif api_type == "":
            api_type_loop = False
            api_type = 0
        else:
            print("Please enter a valid integer.")
            api_type = input("\n>>> ")

    print("What agent is being used? [1]")
    for i in range(len(valid_agent_types)):
        print("[" + str(i + 1) + "] " + valid_agent_types[i])

    agent_type = input("\n>>> ")
    agent_type_loop = True

    while agent_type_loop:
        if agent_type.isdigit():
            if int(agent_type) - 1 in range(len(valid_agent_types)):
                agent_type_loop = False
                agent_type = int(agent_type) - 1
            else:
                print(("Integer must be in range " + str(range(len(valid_agent_types))[0] + 1) + " - " +
                       str(range(len(valid_agent_types))[-1] + 1)))
                agent_type = input("\n>>> ")
        elif agent_type == "":
            agent_type_loop = False
            agent_type = 0
        else:
            print("Please enter a valid integer.")
            agent_type = input("\n>>> ")

    if valid_agent_types[agent_type] == GenerationConstants.AGENT_TYPE_SELENIUM:
        valid_application_types = api_map[ALL_DEVICE_TYPES[dev_type]]["app_type"]
        print("What application is being used? [1]")
        for i in range(len(valid_application_types)):
            print("[" + str(i + 1) + "] " + valid_application_types[i])

        application_type = input("\n>>> ")
        application_type_loop = True

        while application_type_loop:
            if application_type.isdigit():
                if int(application_type) - 1 in range(len(valid_application_types)):
                    application_type_loop = False
                    application_type = int(application_type) - 1
                else:
                    print(("Integer must be in range " + str(range(len(valid_application_types))[0] + 1) + " - " +
                           str(range(len(valid_application_types))[-1] + 1)))
                    application_type = input("\n>>> ")
            elif application_type == "":
                application_type_loop = False
                application_type = 0
            else:
                print("Please enter a valid integer.")
                application_type = input("\n>>> ")

        return (ALL_DEVICE_TYPES[dev_type], valid_api_types[api_type], valid_agent_types[agent_type],
                valid_application_types[application_type])
    else:
        return ALL_DEVICE_TYPES[dev_type], valid_api_types[api_type], valid_agent_types[agent_type], None


if __name__ == '__main__':
    main_api_map = create_api_map()
    main_dev_type, main_api_type, main_agent_type, main_app_type = get_info_from_user_v2(main_api_map)
    try:
        gen_apis = GenerateAllApis(main_dev_type, main_api_type, main_agent_type, main_app_type)
        gen_apis.generate_all_apis()

        # If we are generating Network Element APIs, for CLI agent, also generate the Command Keywords
        if (main_dev_type == GenerationConstants.DEVICE_TYPE_NET_ELEM and
                main_api_type == GenerationConstants.API_TYPE_COMMAND):
            CreateCliKeywords().create_keywords(gen_apis.csv_parser.all_parsed_csvs, gen_apis.csv_parser.keyword_info)

        # # If we are generating Endsystem northbound apis, also generate the parse apis.
        # if (main_dev_type == GenerationConstants.DEVICE_TYPE_END_SYS_ELEM and
        #         main_agent_type == GenerationConstants.AGENT_TYPE_NORTHBOUND):
        #     gen_apis = GenerateAllApis(main_dev_type, GenerationConstants.API_TYPE_PARSE, main_agent_type)
        #     gen_apis.generate_all_apis()
        #     CreateNorthboundKeywords().create_keywords(gen_apis.csv_parser.all_parsed_csvs)
    except Exception as e:
        print("An exception was caught. API and Keyword generation aborted.")
        print(e)
        print(''.join(traceback.format_tb(e.__traceback__)))
