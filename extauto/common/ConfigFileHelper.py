import re
import sys
import os
from pathlib import Path
from ExtremeAutomation.Imports import pytestConfigHelper
try:
    from robot.libraries.BuiltIn import BuiltIn
    from robot.libraries.BuiltIn import _Misc
    import robot.api.logger as logger
    from robot.api.deco import keyword
    ROBOT = True
except Exception:
    ROBOT = False
if "PYTEST_RUN_CONFIG" in os.environ:
    ROBOT = False


yamlRe = re.compile(r".*([a-z0-9_\-\.]+yaml$)")

if ROBOT:
    class ConfigFileHelper:
        ROBOT_LIBRARY_SCOPE = 'TEST SUITE'
        def __init__(self):
            self.variables = BuiltIn().get_variables(no_decoration=True)
            #BuiltIn().log_to_console(f"{self.variables}\n\n\n\n")

        def checkConfigRefresh(self):
            if 'REFRESH_CONFIG' not in self.variables and ('netelem1' in self.variables or \
                                ('ap1' in self.variables and 'name' in self.variables['ap1'])):
                self.set_ap1_default()
                return 1
            else:
                BuiltIn().log_to_console(f"CONFIGREFRESH ALREADY CALLED:\n{BuiltIn().get_variables(no_decoration=True)}")
            return 0

        def loadRdcAio(self):
            if 'RDC' in self.variables:
                if yamlRe.match(self.variables['RDC']):
                    # the RDC arg is a bypass rdc variable file
                    for p in sys.path:
                        rdcCfg = Path(p + '/Environments/' + self.variables['RDC'])
                        # myFile = glob.glob(str(testCfg))
                        if rdcCfg.exists():
                            tmpConfig = {}
                            pytestConfigHelper.load_yaml2(tmpConfig, rdcCfg, encoding='utf-8', roboIze=False)
                            for cfg_key in tmpConfig:
                                #BuiltIn().log_to_console(f"Found file with {cfg_key} val:{tmpConfig[cfg_key]}")
                                mykey = "${"+cfg_key+"}"
                                BuiltIn().set_global_variable(mykey, tmpConfig[cfg_key])
                else:
                    # RDC arg passed in RDC:prod.va or RDC:staging.oss2
                    tmpConfig = None
                    rdcList = self.variables['RDC'].split('.')
                    myRdcDep = rdcList[0].lower()
                    myRdcLoc = rdcList[1].lower()
                    if not myRdcLoc:
                        BuiltIn().log_to_console(f"! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
                        BuiltIn().log_to_console(f"The location is missing.  Should be RDC:prod.va or RDC:test.g2r1")
                        BuiltIn().log_to_console(f"! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ! ")
                        logger.debug(f"The location is missing.  Should be RDC:prod.va or RDC:test.g2r1")
                    for p in sys.path:
                        rdcCfg = Path(p + '/Environments/rdc_aio_servers.yaml')
                        # myFile = glob.glob(str(testCfg))
                        if rdcCfg.exists():
                            tmpConfig = {}
                            pytestConfigHelper.load_yaml2(tmpConfig, rdcCfg, encoding='utf-8', roboIze=False)
                    if myRdcDep in tmpConfig:
                        if myRdcLoc in tmpConfig[myRdcDep]:
                            for rdckey in tmpConfig[myRdcDep][myRdcLoc]:
                                rdcu = rdckey.upper()
                                #BuiltIn().log_to_console(f"Found {rdckey} up {rdcu} val:{tmpConfig[myRdcDep][myRdcLoc][rdckey]}")
                                logger.debug(f"Found {rdckey} up {rdcu} val:{tmpConfig[myRdcDep][myRdcLoc][rdckey]}")
                                mykey = "${"+rdckey+"}"
                                BuiltIn().set_global_variable(mykey, tmpConfig[myRdcDep][myRdcLoc][rdckey])


        def loadTestBed(self):
            if 'TestBed' in self.variables:
                if yamlRe.match(self.variables['TestBed']):
                    tbedRelPath = f"TestBeds/{self.variables['TestBed']}"
                    for p in sys.path:
                        testCfg = Path(p+'/'+tbedRelPath)
                        #myFile = glob.glob(str(testCfg))
                        if testCfg.exists():
                            tmpConfig = {}
                            pytestConfigHelper.load_yaml2(tmpConfig, testCfg, encoding='utf-8', roboIze='Native')
                            for cfg_key in tmpConfig:
                                BuiltIn().log_to_console(f"Loading {cfg_key} val:{tmpConfig[cfg_key]}")
            else:
                BuiltIn().log_to_console(f"Didn't find test bed")


        @keyword(name='refresh config')
        def set_ap1_default(self):
            """
            Returns old style of AP1_UPPER variables for first AP or allows
            substituting any AP# in the yaml file, based on model number if the variable
            AP_MODEL or AP is passed in on the command line
            """
            self.variables = BuiltIn().get_variables(no_decoration=True)
            BuiltIn().log_to_console(f"modify yaml settings INIT:\n{BuiltIn().get_variables(no_decoration=True)}")
            BuiltIn().set_global_variable("${REFRESH_CONFIG}", "Modified")
            search_model = None
            apkey = 'ap1'
            if 'AP_MODEL' in self.variables or 'AP' in self.variables:
                if 'AP_MODEL' in self.variables and 'AP' not in self.variables:
                    search_model = self.variables['AP_MODEL'].upper()
                elif 'AP_MODEL' not in self.variables and 'AP' in self.variables:
                    search_model = self.variables['AP'].upper()
                elif 'AP_MODEL' in self.variables and 'AP' in self.variables:
                    BuiltIn().log_to_console(f"-v AP_MODEL:value and -v AP:value duplicate variables.  Using AP_MODEL")
                    BuiltIn().log_to_console(f"-v AP_MODEL:value and -v AP:value duplicate variables.  Using AP_MODEL")
                    search_model = self.variables['AP_MODEL'].upper()
                for key in self.variables:
                    if isinstance(self.variables[key], dict):
                        for devinfo in self.variables[key]:
                            try:
                                if devinfo.upper() == 'MODEL' and self.variables[key][devinfo] == search_model:
                                    apkey = key
                                    #BuiltIn().log_to_console(f"AP set to {apkey}, model {search_model}")
                            except KeyError:
                                pass

            hit = 0
            for key in self.variables:
                if isinstance(self.variables[key], dict) and key == apkey:
                    for devinfo in self.variables[key]:
                        try:
                            modvar = f"AP1_{devinfo.upper()}"
                            modvar2 = "${"+modvar+"}"
                            amval = self.variables[key][devinfo]
                            #BuiltIn().log_to_console(f"Old style: {modvar2} {amval}")
                            BuiltIn().set_global_variable(str(modvar2), str(amval))
                            hit = 1
                        except KeyError:
                            pass
                    if hit and apkey != 'ap1':
                        keyvar = "${ap1}"
                        BuiltIn().set_global_variable(keyvar, self.variables[key])
                        #BuiltIn().log_to_console(f"{apkey} set to ap1: {self.variables[key]}")

            #
            #  ----   MU sections
            #
            if 'MU' in self.variables:
                mu_key = self.variables['MU']
                mu_upKey = 'MU1'   # passing in MU:mu2 sets mu2 as mu1 for test case usage.
                changeMu = 1
            else:
                mu_key = 'mu1'
                mu_upKey = 'MU1'
                changeMu = 0
            for key in self.variables:
                if isinstance(self.variables[key], dict):
                    if key == mu_key:
                        for devinfo in self.variables[key]:
                            try:
                                modvar = f"{mu_upKey}_{devinfo.upper()}"
                                modvar2 = "${" + modvar + "}"
                                amval = self.variables[key][devinfo]
                                #BuiltIn().log_to_console(f"Old style: {modvar2} {amval}")
                                BuiltIn().set_global_variable(str(modvar2), str(amval))
                            except KeyError:
                                pass
            if changeMu and mu_key != 'mu1':
                keyvar = "${mu1}"
                keyvar2 = "${"+mu_key+"}"
                try:
                    BuiltIn().set_global_variable(keyvar, self.variables[mu_key])
                    BuiltIn().set_global_variable(keyvar2, self.variables['mu1'])
                    #BuiltIn().log_to_console(f"{mu_key} set to mu1: {self.variables[mu_key]}")
                    #BuiltIn().log_to_console(f"mu1 set to {mu_key}: {self.variables['mu1']}")
                except KeyError as e:
                    BuiltIn().log_to_console(f"err hit {e}")
                    pass
            #
            #  Default netelem updates
            #
            netelemRe = re.compile("netelem[0-9]+")
            multiSerRe = re.compile(",")
            for key in self.variables:
                if isinstance(self.variables[key], dict) and netelemRe.match(key):
                    #BuiltIn().log_to_console(f"[+] {key}")
                    newNetelem = {}
                    for devinfo in self.variables[key]:
                        try:
                            newNetelem[devinfo] = self.variables[key][devinfo]
                        except KeyError:
                            pass
                    isStack = 0
                    stackSerList = []
                    stackJoin = ", "
                    try:
                        if 'stack' in newNetelem and 'slot1' in newNetelem['stack']:
                            isStack = 1
                            BuiltIn().log_to_console(f"[+] STACK FOUND")
                            if 'topology' not in newNetelem:
                                newNetelem['topology'] = 'Stack'
                            elif newNetelem['topology'].lower() != 'stack':
                                newNetelem['topology'] = 'Stack'
                            for mySlot in newNetelem['stack']:
                                if 'serial' in newNetelem['stack'][mySlot]:
                                    stackSerList.append(newNetelem['stack'][mySlot]['serial'])
                                else:
                                    BuiltIn().log_to_console(f"Stack {mySlot} is missing a serial number")
                            if len(stackSerList) > 0:
                                #BuiltIn().log_to_console(f"[+]Stack slots serial {stackJoin.join(stackSerList)}")
                                newNetelem['onboard_serial'] = stackJoin.join(stackSerList)
                            elif 'serial' in newNetelem:
                                #BuiltIn().log_to_console(f"[+]Stack missed slots serial {newNetelem['serial']}")
                                newNetelem['onboard_serial'] = newNetelem['serial']
                    except:
                        pass

                    if not isStack:
                        try:
                            if 'serial' in newNetelem and 'onboard_serial' not in newNetelem:
                                newNetelem['onboard_serial'] = newNetelem['serial']
                            if 'topology' not in newNetelem:
                                newNetelem['topology'] = 'Standalone'
                        except:
                            pass
                    keyvar = "${"+key+"}"
                    BuiltIn().set_global_variable(keyvar, newNetelem)

            self.variables = BuiltIn().get_variables(no_decoration=True)
            # Load the RDC default file.  Filter on -v RDC: variable input.  Make default old vars in any case
            self.loadRdcAio()
            BuiltIn().log_to_console(f"modify yaml settings AFTER:\n{BuiltIn().get_variables(no_decoration=True)}")

        def build_dict_of_elems(self, **kwargs):
            try:
                variables = BuiltIn().get_variables(no_decoration=True)
            except Exception as e:
                    raise e

            #netelems = NetworkElementUtils.get_device_names_from_variables(variables, "netelem")
            #netelem_dict = {}

        def get_device_names_from_variables(self, var_prefix):
            """Returns a list of all devices with the same var_prefix."""
            name_regex = "^" + var_prefix + "[0-9]+$"
            index_regex = "[0-9]+$"

            names = [key for key in self.variables.keys() if len(re.findall(name_regex, key)) == 1]
            indexes = [re.search(index_regex, i).group() for i in names]

            return [var_prefix + i for i in sorted(indexes, key=int)]

        def get_device_number(self, search_name):
            """
            Returns the DeviceNumber for the devicetypeDeviceNumber['name']
            Ex:
            For netelem2 the device number is "2"
            """
            for key in self.variables:
                if isinstance(self.variables[key], dict):
                    try:
                        if self.variables[key]["name"] == search_name:
                            return key
                    except KeyError:
                        pass

            raise ValueError("No device's with the name " + search_name + " found.")

else:
    class ConfigFileHelper:

        def __init__(self):
            self.harness = 'NOT ROBOT'

        def checkConfigRefresh(self):
            return 1