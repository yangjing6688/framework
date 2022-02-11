from ExtremeAutomation.Library.Utils.DotDict import DotDict
from pytest_testconfig import load_yaml
import sys
import os
import codecs
from pathlib import Path
import re

class PytestConfigHelper():
    def __init__(self, config):

        self.node_count = 0
        self.dut_list = []

        try:
            roboIzeAllConfiguration(config)
            self.config = DotDict(config)
        except Exception as e:
            print(e)
            #pass

        try:
            self.lab = config['LAB']
        except:
            self.lab = None

        # Tgen 1
        try:
            self.tgen1 = DotDict(config['tgen1'])
            self.tgen1_name = config['tgen1']['name']

            #Tgen ports
            self.tgen_dut1_port_a = DotDict(config['tgen_ports']['netelem1']['port_a'])
            self.tgen_dut1_port_b = DotDict(config['tgen_ports']['netelem1']['port_b'])
            self.tgen_dut1_port_c = DotDict(config['tgen_ports']['netelem1']['port_c'])
            self.tgen_dut1_port_d = DotDict(config['tgen_ports']['netelem1']['port_d'])
        except:
            pass

        #Tgen dut 2
        try:
            self.tgen_dut2_port_a = DotDict(config['tgen_ports']['netelem2']['port_a'])
            self.tgen_dut2_port_b = DotDict(config['tgen_ports']['netelem2']['port_b'])
            self.tgen_dut2_port_c = DotDict(config['tgen_ports']['netelem2']['port_c'])
            self.tgen_dut2_port_d = DotDict(config['tgen_ports']['netelem2']['port_d'])
            self.tgen_ports_dut2 = config['tgen_ports']['netelem2']
        except:
            pass

        #Tgen dut 3
        try:
            self.tgen_dut3_port_a = DotDict(config['tgen_ports']['netelem3']['port_a'])
            self.tgen_dut3_port_b = DotDict(config['tgen_ports']['netelem3']['port_b'])
            self.tgen_dut3_port_c = DotDict(config['tgen_ports']['netelem3']['port_c'])
            self.tgen_dut3_port_d = DotDict(config['tgen_ports']['netelem3']['port_d'])
            self.tgen_ports_dut3 = config['tgen_ports']['netelem3']
        except:
            pass

        #Tgen dut 4
        try:
            self.tgen_dut4_port_a = DotDict(config['tgen_ports']['netelem4']['port_a'])
            self.tgen_dut4_port_b = DotDict(config['tgen_ports']['netelem4']['port_b'])
            self.tgen_dut4_port_c = DotDict(config['tgen_ports']['netelem4']['port_c'])
            self.tgen_dut4_port_d = DotDict(config['tgen_ports']['netelem4']['port_d'])
            self.tgen_ports_dut4 = config['tgen_ports']['netelem4']
        except:
            pass

        #Tgen dut 5
        try:
            self.tgen_dut5_port_a = DotDict(config['tgen_ports']['netelem5']['port_a'])
            self.tgen_dut5_port_b = DotDict(config['tgen_ports']['netelem5']['port_b'])
            self.tgen_dut5_port_c = DotDict(config['tgen_ports']['netelem5']['port_c'])
            self.tgen_dut5_port_d = DotDict(config['tgen_ports']['netelem5']['port_d'])
            self.tgen_ports_dut5 = config['tgen_ports']['netelem5']
        except:
            pass


        try:
            # DUT 1
            self.dut1 = DotDict(config['netelem1'])
            self.dut1_name = config['netelem1']['name']
            self.node_count += 1
            self.dut1_os = config['netelem1']['os']
            self.dut1_platform = config['netelem1']['platform']
            self.dut1_model = config['netelem1']['model']
            self.dut_list.append('dut1')
        except:
            pass
        # tgen ports
        try:
            self.dut1_tgen_port_a = DotDict(config['netelem1']['tgen']['port_a'])
            self.dut1_tgen_port_b = DotDict(config['netelem1']['tgen']['port_b'])
            self.dut1_tgen_port_c = DotDict(config['netelem1']['tgen']['port_c'])
            self.dut1_tgen_port_d = DotDict(config['netelem1']['tgen']['port_d'])
        except:
            pass

        try:
            #ISL ports
            self.dut1_isl_dut2_port_a = DotDict(config['netelem1']['isl']['port_a'])
            self.dut1_isl_dut2_port_b = DotDict(config['netelem1']['isl']['port_b'])
            self.dut1_isl_dut2_port_c = DotDict(config['netelem1']['isl']['port_c'])
            self.dut1_isl_dut2_port_d = DotDict(config['netelem1']['isl']['port_d'])
            self.dut1_isl_dut3_port_a = DotDict(config['netelem1']['isl']['port_e'])
            self.dut1_isl_dut3_port_b = DotDict(config['netelem1']['isl']['port_f'])
            self.dut1_isl_dut3_port_c = DotDict(config['netelem1']['isl']['port_g'])
            self.dut1_isl_dut3_port_d = DotDict(config['netelem1']['isl']['port_h'])
            self.dut1_isl_dut4_port_a = DotDict(config['netelem1']['isl']['port_i'])
            self.dut1_isl_dut4_port_b = DotDict(config['netelem1']['isl']['port_j'])
            self.dut1_isl_dut4_port_c = DotDict(config['netelem1']['isl']['port_k'])
            self.dut1_isl_dut4_port_d = DotDict(config['netelem1']['isl']['port_l'])
            self.dut1_isl_dut5_port_a = DotDict(config['netelem1']['isl']['port_m'])
            self.dut1_isl_dut5_port_b = DotDict(config['netelem1']['isl']['port_n'])
            self.dut1_isl_dut5_port_c = DotDict(config['netelem1']['isl']['port_o'])
            self.dut1_isl_dut5_port_d = DotDict(config['netelem1']['isl']['port_p'])
        except:
            pass


        try:
            # dut1 topology
            self.dut1_topology = 'standalone'
            if 'stack' in config['netelem1']:
                self.dut1_topology = 'stack'
                try:
                    self.dut1_slot1_console_ip = DotDict(config['netelem1']['stack']['slot1']['console_ip'])
                    self.dut1_slot1_console_port = DotDict(config['netelem1']['stack']['slot1']['console_port'])
                    self.dut1_slot2_console_ip = DotDict(config['netelem1']['stack']['slot2']['console_ip'])
                    self.dut1_slot2_console_port = DotDict(config['netelem1']['stack']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        try:
            if 'vpex' in config['netelem1']:
                self.dut1_topology = 'vpex'
                try:
                    self.dut1_slot1_console_ip = DotDict(config['netelem1']['vpex']['slot1']['console_ip'])
                    self.dut1_slot1_console_port = DotDict(config['netelem1']['vpex']['slot1']['console_port'])
                    self.dut1_slot2_console_ip = DotDict(config['netelem1']['vpex']['slot2']['console_ip'])
                    self.dut1_slot2_console_port = DotDict(config['netelem1']['vpex']['slot2']['console_port'])
                except:
                    pass
        except:
            pass

        # DUT 2
        try:
            self.dut2 = DotDict(config['netelem2'])
            self.node_count += 1
            self.dut2_name = config['netelem2']['name']
            self.dut2_os = config['netelem2']['os']
            self.dut2_platform = config['netelem2']['platform']
            self.dut2_model = config['netelem2']['model']
            self.dut_list.append('dut2')
        except:
            pass

        try:

            # tgen ports
            self.dut2_tgen_port_a = DotDict(config['netelem2']['tgen']['port_a'])
            self.dut2_tgen_port_b = DotDict(config['netelem2']['tgen']['port_b'])
            self.dut2_tgen_port_c = DotDict(config['netelem2']['tgen']['port_c'])
            self.dut2_tgen_port_d = DotDict(config['netelem2']['tgen']['port_d'])
        except:
            pass

        try:
            #ISL ports
            self.dut2_isl_dut1_port_a = DotDict(config['netelem2']['isl']['port_a'])
            self.dut2_isl_dut1_port_b = DotDict(config['netelem2']['isl']['port_b'])
            self.dut2_isl_dut1_port_c = DotDict(config['netelem2']['isl']['port_c'])
            self.dut2_isl_dut1_port_d = DotDict(config['netelem2']['isl']['port_d'])
            self.dut2_isl_dut3_port_a = DotDict(config['netelem2']['isl']['port_e'])
            self.dut2_isl_dut3_port_b = DotDict(config['netelem2']['isl']['port_f'])
            self.dut2_isl_dut3_port_c = DotDict(config['netelem2']['isl']['port_g'])
            self.dut2_isl_dut3_port_d = DotDict(config['netelem2']['isl']['port_h'])
            self.dut2_isl_dut4_port_a = DotDict(config['netelem2']['isl']['port_i'])
            self.dut2_isl_dut4_port_b = DotDict(config['netelem2']['isl']['port_j'])
            self.dut2_isl_dut4_port_c = DotDict(config['netelem2']['isl']['port_k'])
            self.dut2_isl_dut4_port_d = DotDict(config['netelem2']['isl']['port_l'])
            self.dut2_isl_dut5_port_a = DotDict(config['netelem2']['isl']['port_m'])
            self.dut2_isl_dut5_port_b = DotDict(config['netelem2']['isl']['port_n'])
            self.dut2_isl_dut5_port_c = DotDict(config['netelem2']['isl']['port_o'])
            self.dut2_isl_dut5_port_d = DotDict(config['netelem2']['isl']['port_p'])
        except:
            pass
        # dut2 topology
        self.dut2_topology = 'standalone'
        try:
            if 'stack' in config['netelem2']:
                self.dut2_topology = 'stack'
                try:
                    self.dut2_slot1_console_ip = DotDict(config['netelem2']['stack']['slot1']['console_ip'])
                    self.dut2_slot1_console_port = DotDict(config['netelem2']['stack']['slot1']['console_port'])
                    self.dut2_slot2_console_ip = DotDict(config['netelem2']['stack']['slot2']['console_ip'])
                    self.dut2_slot2_console_port = DotDict(config['netelem2']['stack']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        try:
            if 'vpex' in config['netelem2']:
                self.dut2_topology = 'vpex'
                try:
                    self.dut2_slot1_console_ip = DotDict(config['netelem2']['vpex']['slot1']['console_ip'])
                    self.dut2_slot1_console_port = DotDict(config['netelem2']['vpex']['slot1']['console_port'])
                    self.dut2_slot2_console_ip = DotDict(config['netelem2']['vpex']['slot2']['console_ip'])
                    self.dut2_slot2_console_port = DotDict(config['netelem2']['vpex']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        # DUT 3
        try:
            self.dut3 = DotDict(config['netelem3'])
            self.node_count += 1
            self.dut3_name = config['netelem3']['name']
            self.dut3_os = config['netelem3']['os']
            self.dut3_platform = config['netelem3']['platform']
            self.dut3_model = config['netelem3']['model']
            self.dut_list.append('dut3')
        except:
            pass

        try:
            # tgen ports
            self.dut3_tgen_port_a = DotDict(config['netelem3']['tgen']['port_a'])
            self.dut3_tgen_port_b = DotDict(config['netelem3']['tgen']['port_b'])
            self.dut3_tgen_port_c = DotDict(config['netelem3']['tgen']['port_c'])
            self.dut3_tgen_port_d = DotDict(config['netelem3']['tgen']['port_d'])
        except:
            pass

        try:
            #ISL ports
            self.dut3_isl_dut1_port_a = DotDict(config['netelem3']['isl']['port_a'])
            self.dut3_isl_dut1_port_b = DotDict(config['netelem3']['isl']['port_b'])
            self.dut3_isl_dut1_port_c = DotDict(config['netelem3']['isl']['port_c'])
            self.dut3_isl_dut1_port_d = DotDict(config['netelem3']['isl']['port_d'])
            self.dut3_isl_dut2_port_a = DotDict(config['netelem3']['isl']['port_e'])
            self.dut3_isl_dut2_port_b = DotDict(config['netelem3']['isl']['port_f'])
            self.dut3_isl_dut2_port_c = DotDict(config['netelem3']['isl']['port_g'])
            self.dut3_isl_dut2_port_d = DotDict(config['netelem3']['isl']['port_h'])
            self.dut3_isl_dut4_port_a = DotDict(config['netelem3']['isl']['port_i'])
            self.dut3_isl_dut4_port_b = DotDict(config['netelem3']['isl']['port_j'])
            self.dut3_isl_dut4_port_c = DotDict(config['netelem3']['isl']['port_k'])
            self.dut3_isl_dut4_port_d = DotDict(config['netelem3']['isl']['port_l'])
            self.dut3_isl_dut5_port_a = DotDict(config['netelem3']['isl']['port_m'])
            self.dut3_isl_dut5_port_b = DotDict(config['netelem3']['isl']['port_n'])
            self.dut3_isl_dut5_port_c = DotDict(config['netelem3']['isl']['port_o'])
            self.dut3_isl_dut5_port_d = DotDict(config['netelem3']['isl']['port_p'])
        except:
            pass
        # dut3 topology
        self.dut3_topology = 'standalone'
        try:
            if 'stack' in config['netelem3']:
                self.dut3_topology = 'stack'
                try:
                    self.dut3_slot1_console_ip = DotDict(config['netelem3']['stack']['slot1']['console_ip'])
                    self.dut3_slot1_console_port = DotDict(config['netelem3']['stack']['slot1']['console_port'])
                    self.dut3_slot2_console_ip = DotDict(config['netelem3']['stack']['slot2']['console_ip'])
                    self.dut3_slot2_console_port = DotDict(config['netelem3']['stack']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        try:
            if 'vpex' in config['netelem3']:
                self.dut3_topology = 'vpex'
                try:
                    self.dut3_slot1_console_ip = DotDict(config['netelem3']['vpex']['slot1']['console_ip'])
                    self.dut3_slot1_console_port = DotDict(config['netelem3']['vpex']['slot1']['console_port'])
                    self.dut3_slot2_console_ip = DotDict(config['netelem3']['vpex']['slot2']['console_ip'])
                    self.dut3_slot2_console_port = DotDict(config['netelem3']['vpex']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        # DUT 4
        try:
            self.dut4 = DotDict(config['netelem4'])
            self.node_count += 1
            self.dut4_name = config['netelem4']['name']
            self.dut4_os = config['netelem4']['os']
            self.dut4_platform = config['netelem4']['platform']
            self.dut4_model = config['netelem4']['model']
            self.dut_list.append('dut4')
        except:
            pass

        try:
            # tgen ports
            self.dut4_tgen_port_a = DotDict(config['netelem4']['tgen']['port_a'])
            self.dut4_tgen_port_b = DotDict(config['netelem4']['tgen']['port_b'])
            self.dut4_tgen_port_c = DotDict(config['netelem4']['tgen']['port_c'])
            self.dut4_tgen_port_d = DotDict(config['netelem4']['tgen']['port_d'])
        except:
            pass

        try:
            #ISL ports
            self.dut4_isl_dut1_port_a = DotDict(config['netelem4']['isl']['port_a'])
            self.dut4_isl_dut1_port_b = DotDict(config['netelem4']['isl']['port_b'])
            self.dut4_isl_dut1_port_c = DotDict(config['netelem4']['isl']['port_c'])
            self.dut4_isl_dut1_port_d = DotDict(config['netelem4']['isl']['port_d'])
            self.dut4_isl_dut2_port_a = DotDict(config['netelem4']['isl']['port_e'])
            self.dut4_isl_dut2_port_b = DotDict(config['netelem4']['isl']['port_f'])
            self.dut4_isl_dut2_port_c = DotDict(config['netelem4']['isl']['port_g'])
            self.dut4_isl_dut2_port_d = DotDict(config['netelem4']['isl']['port_h'])
            self.dut4_isl_dut3_port_a = DotDict(config['netelem4']['isl']['port_i'])
            self.dut4_isl_dut3_port_b = DotDict(config['netelem4']['isl']['port_j'])
            self.dut4_isl_dut3_port_c = DotDict(config['netelem4']['isl']['port_k'])
            self.dut4_isl_dut3_port_d = DotDict(config['netelem4']['isl']['port_l'])
            self.dut4_isl_dut5_port_a = DotDict(config['netelem4']['isl']['port_m'])
            self.dut4_isl_dut5_port_b = DotDict(config['netelem4']['isl']['port_n'])
            self.dut4_isl_dut5_port_c = DotDict(config['netelem4']['isl']['port_o'])
            self.dut4_isl_dut5_port_d = DotDict(config['netelem4']['isl']['port_p'])
        except:
            pass
        # dut4 topology
        self.dut4_topology = 'standalone'
        try:
            if 'stack' in config['netelem4']:
                self.dut4_topology = 'stack'
                try:
                    self.dut4_slot1_console_ip = DotDict(config['netelem4']['stack']['slot1']['console_ip'])
                    self.dut4_slot1_console_port = DotDict(config['netelem4']['stack']['slot1']['console_port'])
                    self.dut4_slot2_console_ip = DotDict(config['netelem4']['stack']['slot2']['console_ip'])
                    self.dut4_slot2_console_port = DotDict(config['netelem4']['stack']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        try:
            if 'vpex' in config['netelem4']:
                self.dut4_topology = 'vpex'
                try:
                    self.dut4_slot1_console_ip = DotDict(config['netelem4']['vpex']['slot1']['console_ip'])
                    self.dut4_slot1_console_port = DotDict(config['netelem4']['vpex']['slot1']['console_port'])
                    self.dut4_slot2_console_ip = DotDict(config['netelem4']['vpex']['slot2']['console_ip'])
                    self.dut4_slot2_console_port = DotDict(config['netelem4']['vpex']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        # DUT 5
        try:
            self.dut5 = DotDict(config['netelem5'])
            self.node_count += 1
            self.dut5_name = config['netelem5']['name']
            self.dut5_os = config['netelem5']['os']
            self.dut5_platform = config['netelem5']['platform']
            self.dut5_model = config['netelem5']['model']
            self.dut_list.append('dut5')
        except:
            pass

        try:
            # tgen ports
            self.dut5_tgen_port_a = DotDict(config['netelem5']['tgen']['port_a'])
            self.dut5_tgen_port_b = DotDict(config['netelem5']['tgen']['port_b'])
            self.dut5_tgen_port_c = DotDict(config['netelem5']['tgen']['port_c'])
            self.dut5_tgen_port_d = DotDict(config['netelem5']['tgen']['port_d'])
        except:
            pass

        try:
            #ISL ports
            self.dut5_isl_dut1_port_a = DotDict(config['netelem5']['isl']['port_a'])
            self.dut5_isl_dut1_port_b = DotDict(config['netelem5']['isl']['port_b'])
            self.dut5_isl_dut1_port_c = DotDict(config['netelem5']['isl']['port_c'])
            self.dut5_isl_dut1_port_d = DotDict(config['netelem5']['isl']['port_d'])
            self.dut5_isl_dut2_port_a = DotDict(config['netelem5']['isl']['port_e'])
            self.dut5_isl_dut2_port_b = DotDict(config['netelem5']['isl']['port_f'])
            self.dut5_isl_dut2_port_c = DotDict(config['netelem5']['isl']['port_g'])
            self.dut5_isl_dut2_port_d = DotDict(config['netelem5']['isl']['port_h'])
            self.dut5_isl_dut3_port_a = DotDict(config['netelem5']['isl']['port_i'])
            self.dut5_isl_dut3_port_b = DotDict(config['netelem5']['isl']['port_j'])
            self.dut5_isl_dut3_port_c = DotDict(config['netelem5']['isl']['port_k'])
            self.dut5_isl_dut3_port_d = DotDict(config['netelem5']['isl']['port_l'])
            self.dut5_isl_dut4_port_a = DotDict(config['netelem5']['isl']['port_m'])
            self.dut5_isl_dut4_port_b = DotDict(config['netelem5']['isl']['port_n'])
            self.dut5_isl_dut4_port_c = DotDict(config['netelem5']['isl']['port_o'])
            self.dut5_isl_dut4_port_d = DotDict(config['netelem5']['isl']['port_p'])
        except:
            pass
        # dut5 topology
        self.dut5_topology = 'standalone'
        try:
            if 'stack' in config['netelem5']:
                self.dut5_topology = 'stack'
                try:
                    self.dut5_slot1_console_ip = DotDict(config['netelem5']['stack']['slot1']['console_ip'])
                    self.dut5_slot1_console_port = DotDict(config['netelem5']['stack']['slot1']['console_port'])
                    self.dut5_slot2_console_ip = DotDict(config['netelem5']['stack']['slot2']['console_ip'])
                    self.dut5_slot2_console_port = DotDict(config['netelem5']['stack']['slot2']['console_port'])
                except:
                    pass
        except:
            pass
        try:
            if 'vpex' in config['netelem5']:
                self.dut5_topology = 'vpex'
                try:
                    self.dut5_slot1_console_ip = DotDict(config['netelem5']['vpex']['slot1']['console_ip'])
                    self.dut5_slot1_console_port = DotDict(config['netelem5']['vpex']['slot1']['console_port'])
                    self.dut5_slot2_console_ip = DotDict(config['netelem5']['vpex']['slot2']['console_ip'])
                    self.dut5_slot2_console_port = DotDict(config['netelem5']['vpex']['slot2']['console_port'])
                except:
                    pass
        except:
            pass

    def createTgenPort(self, tgenName, tgenPort):
        return {"tgen_name": tgenName, "ifname": tgenPort}

    def locateCfg(self, cfgFile, search=[]):
        keyList = ['xiq', 'xiqse', 'econ', 'econxiq']
        sites = ['RDU','SALEM','BANGALORE','CHENNAI','SJ']
        cfgDirs  = { 'xiq' : ['/testsuites/xiq/config/', '/testsuites/xiq/env/', '/testsuites/xiq/topologies/'],
                    'xiqse' : ['/testsuites/xiqse/config/', '/testsuites/xiqse/env/', '/testsuites/xiqse/topologies/'],
                    'econ' : ['/Environments/','/TestBeds/','/TestBeds/RDU/Prod/','/TestBeds/SALEM/Prod/',
                              '/TestBeds/RDU/Dev/','/TestBeds/RDU/Demo/','/TestBeds/SALEM/Demo/','/TestBeds/SALEM/Dev/',
                              '/TestEnvironments/','/TestEnvironments/Rdu/Physical/Exos/',
                              '/TestEnvironments/Rdu/Virtual/Exos/', '/TestEnvironments/Salem/Physical/Demo/',
                              '/TestEnvironments/Salem/Physical/Dev/'],
                    'econxiq': ['/Environments/','/TestBeds/','/TestBeds/RDU/Prod/','/TestBeds/SALEM/Prod/',
                              '/TestBeds/RDU/Dev/', '/TestBeds/RDU/Demo/', '/TestBeds/SALEM/Demo/', '/TestBeds/SALEM/Dev/',
                              '/TestEnvironments/Xiq/', '/TestEnvironments/Xiq/Base/','/TestEnvironments/Xiq/Rdu/',
                              '/TestEnvironments/Xiq/Salem/', '/TestEnvironments/Rdu/Physical/Exos/',
                              '/TestEnvironments/Rdu/Virtual/Exos/', '/TestEnvironments/Salem/Physical/Demo/',
                              '/TestEnvironments/Salem/Physical/Dev/' ],
                    'extr': ['/Environments/', '/TestBeds/', '/TestBeds/BANGALORE/', '/TestBeds/CHENNAI/',
                             '/TestBeds/RDU/', '/TestBeds/SALEM/', '/TestBeds/SJ/', '/TestBeds/Templates/',
                             '/TestBeds/RDU/Demo/', '/TestBeds/RDU/Dev/', '/TestBeds/RDU/Prod/',
                             '/TestBeds/SALEM/Demo/', '/TestBeds/SALEM/Dev/','/TestBeds/SALEM/Prod/',
                             '/TestBeds/SJ/Demo/','/TestBeds/SJ/Dev/','/TestBeds/SJ/Prod/',
                             '/TestBeds/BANGALORE/Demo/','/TestBeds/BANGALORE/Dev/','/TestBeds/BANGALORE/Prod/',
                             '/TestBeds/CHENNAI/Demo/','/TestBeds/CHENNAI/Dev/','/TestBeds/CHENNAI/Prod/'
                             ]
                    }

        for p in sys.path:
            testCfg = Path(p+'/'+cfgFile)
            if testCfg.exists():
                return testCfg

        p1 = '*cw_automation*'
        p2 = 'econ-automation-tests.*'
        p3 = 'extreme_automation_tests.*'
        if search:
            for p in sys.path:
                if 'xiqse' in search and re.match(p1, p):
                    for cd in cfgDirs['xiqse']:
                        testCfg = Path(p + cd + cfgFile)
                        if testCfg.exists():
                            return testCfg
                if 'xiq' in search and re.match(p1, p):
                    for cd in cfgDirs['xiq']:
                        testCfg = Path(p + cd + cfgFile)
                        if testCfg.exists():
                            return testCfg
                if 'econ' in search and (re.match(p2, p) or re.match(p3, p)):
                    for cd in cfgDirs['econ']:
                        testCfg = Path(p + cd + cfgFile)
                        if testCfg.exists():
                            return testCfg
                if 'econxiq' in search and (re.match(p2, p) or re.match(p3, p)):
                    for cd in cfgDirs['econxiq']:
                        testCfg = Path(p + cd + cfgFile)
                        if testCfg.exists():
                            return testCfg
                if 'extr' in search and re.match(p3, p):
                    for cd in cfgDirs['extr']:
                        testCfg = Path(p + cd + cfgFile)
                        if testCfg.exists():
                            return testCfg
        for p in sys.path:
            for srch in keyList:
                for cd in cfgDirs[srch]:
                    testCfg = Path(p + cd + cfgFile)
                    if testCfg.exists():
                        return testCfg
        return None

    def loadAdditionalConfig(self, config, cfgFile='', search=[], roboIze=False):
        cfg = self.locateCfg(cfgFile, search)
        if cfg:
            print("Found configuration file {}".format(cfg))
            if roboIze:
                load_yaml2(config, cfg, encoding='utf-8')
            else:
                load_yaml(cfg, encoding='utf-8')
        else:
            print("Could not locate configuration file {}".format(cfgFile))
        if roboIze:
            xiqVarList = ['${ELEMENT_INFO}', '${OUTPUT DIR}', '${TEST_NAME}', '${PROXY_STATUS}',
                          '${LOG_LEVEL}', '${ELEMENT_DELAY}', '${BROWSER}', '${WEB_DRIVER_LOC}',
                          '${OS_PLATFORM}']
            for xiqvar in xiqVarList:
                if xiqvar not in config.keys():
                    config[xiqvar] = ''

def merge_map2(original, to_add, roboIze=True):
    """ Merges a new map of configuration recursively with an older one """
    p1 = '^\$\{'
    for k, v in to_add.items():
        if isinstance(v, dict) and k in original and isinstance(original[k],
                                                                dict):
            merge_map2(original[k], v)
        else:
            original[k] = v
            if roboIze and not re.match(p1, k):
                roboK = '${' + k + '}'
                original[roboK] = v

def load_yaml2(config, yaml_file, encoding, roboIze=True):
    """ Load the passed in yaml configuration file """
    try:
        import yaml
    except (ImportError):
        raise Exception('unable to import YAML package. Can not continue.')

    with codecs.open(os.path.expanduser(yaml_file), 'r', encoding) as f:
        parsed_config = yaml.safe_load(f.read())
        merge_map2(config, parsed_config, roboIze)
        
def roboIzeAllConfiguration(config):
    # For all variables
    p1 = '^\$\{'
    forLoopDict = config.copy()
    for key, value in forLoopDict.items():
        if not re.match(p1, key):
            # robotize keys that have not already be done.
            robotKey = '${' + key + '}'
            config[robotKey] = value
    


