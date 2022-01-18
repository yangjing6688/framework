class NetsightutilitiesData(object):
    @staticmethod
    def install_netsight_data(arg_dict):
        return {"version": arg_dict["netsight_version"]}

    @staticmethod
    def restart_netsight_and_redeploy_war_file_data(arg_dict):
        pass

    @staticmethod
    def netsight_script_copy_data(arg_dict):
        return {'server_ip': arg_dict['server_ip'],
                'script_directory': arg_dict['script_directory'],
                "script_name": arg_dict["script_name"],
                'username': arg_dict['username'],
                'password': arg_dict['password'],
                'server_type': arg_dict['server_type'],
                'xmc_dir': arg_dict['xmc_dir']
                }

    @staticmethod
    def netsight_log_copy_data(arg_dict):
        return {"guid": arg_dict["guid"],
                'test_engine_ip': arg_dict['test_engine_ip'],
                'test_engine_username': arg_dict['test_engine_username'],
                'test_engine_pw': arg_dict['test_engine_pw'],
                'log_name': arg_dict['log_name']
                }
