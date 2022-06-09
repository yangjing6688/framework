import sys
import re
import os
import site
import importlib
importlib.import_module("robot.api")
importlib.import_module("robot")

# pytest only
if ("pytest" in sys.modules and "pytest.collect" in sys.modules) or os.getenv('PYTESTBUILTIN'):
    print("REMOVE ROBOT SITE-PACKAGES")
    c=0
    nPath = None
    for p in sys.path:
        #print("p - {} nPath:{}".format(p, nPath))
        patt  = '.*framework*'
        loc   = re.match(patt, p)
        patt2 = '.*site-packages'
        loc2  = re.match(patt2, p)
        if loc and nPath == None:
            #print("Making location {}".format(loc[0]+'\\ExtremeAutomation\\XiqImports'))
            if os.name == 'nt':
                nPath = loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin'
                os.environ['PYTHONPATH'] = loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin;'+os.environ.get('PYTHONPATH')
                sys.path.insert(1, loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
                site.addsitedir(loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
                site.PREFIXES.insert(0,loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
            else:
                nPath = loc[0]+'/ExtremeAutomation/PytestRobotBuiltin'
                os.environ['PYTHONPATH'] = loc[0]+'/ExtremeAutomation/PytestRobotBuiltin;'+os.environ.get('PYTHONPATH')
                sys.path.insert(1, loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
                site.addsitedir(loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
                site.PREFIXES.insert(0,loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
        elif loc2 and nPath:
            break
        c = c+1
    site.getusersitepackages()
    site.main()

    roboWhackList=[]
    for key in sys.modules:
        patt = 'robot.*'
        loc = re.match(patt, key)
        if loc:
            try:
                roboWhackList.append(key)
                continue
            except:
                continue
    patt2 = 'robot.api.*|robot.pars.*'
    for robmod in roboWhackList:
        loc = re.match(patt2, robmod)
        if not loc:
            #print("whack {}".format(robmod))
            del sys.modules[robmod]

    importlib.invalidate_caches()
    os.environ['STATS_SERVICE_URL'] = 'https://autoiq-test.extremenetworks.com/stats/testStats'

else:
    print(f"LEAVE ROBOT SITE-PACKAGES IN PLACE\n{os.environ}")
