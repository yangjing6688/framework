import os
from pprint import pprint
import yaml
import codecs
import tempfile

class DeviceCapability():

    def __init__(self, model):
        self.sysType = model
        self.capability = {}
        self.models = {}

    def loadModels(self):
        elib = os.path.dirname(os.path.realpath(__file__))
        deviceFile = os.path.join(elib, 'devices.yaml')
        with codecs.open(os.path.expanduser(deviceFile), 'r', 'utf-8') as f:
            self.models = yaml.safe_load(f.read())
        return self.models

    def getModelInfo(self):
        initCwd = os.getcwd()
        skipit = ['system', 'devices', 'interrupts', 'leds', 'buttons', 'thermal', 'fans', 'power', 'poe', 'watchdog',
                  'ports', 'vims']
        elib = os.path.dirname(os.path.realpath(__file__))
        ydir0 = os.path.join(elib, 'device_configs')
        ydir = os.path.join(elib, 'device_configs', 'Extreme', self.sysType)
        tempFile = os.path.join(ydir, 'temp.yaml')
        mfile = os.path.join(elib, 'device_configs', 'Extreme', self.sysType, 'manifest.yaml')
        with codecs.open(os.path.expanduser(mfile), 'r', 'utf-8') as f:
            parsed_config = yaml.safe_load(f.read())
            for k, v in parsed_config.items():
                if isinstance(v, list) and k == 'files':
                    for fl in v:
                        goyamls = []
                        ftype = ''
                        if isinstance(fl, dict):
                            for kf, vf in fl.items():
                                if kf == 'name':
                                    ftype = vf
                                if kf == 'filename':
                                    goyamls = vf
                        if len(goyamls) > 0:
                            if ftype in skipit:
                                continue
                            os.chdir(ydir)
                            try:
                                os.remove(tempFile)
                            except:
                                pass
                            #f1 = tempfile.TemporaryFile()
                            f1 = open(tempFile, "w")
                            for my in goyamls:
                                with open(my) as infile:
                                    f1.write(infile.read())
                                    infile.close()
                            #f1.seek(0)
                            f1.close()
                            f1 = open(tempFile, "r")
                            parsed = yaml.safe_load(f1.read())
                            f1.close
                            if 'capability' in parsed:
                                self.capability = parsed['capability']
                elif k != 'files':
                    pass
                else:
                    pass
        os.chdir(initCwd)
        return self.capability