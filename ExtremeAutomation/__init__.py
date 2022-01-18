import sys
import re
import os
import site
import importlib


# pytest only
if "pytest" in sys.modules:
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
                os.environ['PYTHONPATH'] = loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin:'+os.environ.get('PYTHONPATH')
                sys.path.insert(1, loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
                site.addsitedir(loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
                site.PREFIXES.insert(0,loc[0]+'\\ExtremeAutomation\\PytestRobotBuiltin')
            else:
                nPath = loc[0]+'/ExtremeAutomation/PytestRobotBuiltin'
                os.environ['PYTHONPATH'] = loc[0]+'/ExtremeAutomation/PytestRobotBuiltin:'+os.environ.get('PYTHONPATH')
                sys.path.insert(1, loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
                site.addsitedir(loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
                site.PREFIXES.insert(0,loc[0]+'/ExtremeAutomation/PytestRobotBuiltin')
            site.getusersitepackages()
            site.main()
        elif loc2 and nPath:
            sys.path.insert( c, str(nPath) )
            break
        c = c+1
    roboWhackList=[]
    for key in sys.modules:
        if isinstance(key, dict):
            for k, v in key.items():
                patt = 'robot.*'
                loc = re.match(patt, k)
                if loc:
                    try:
                        roboWhackList.append(str(loc[0]))
                    except:
                        pass
        else:
            patt = 'robot.*'
            loc = re.match(patt, key)
            if loc:
                try:
                    roboWhackList.append(key)
                    continue
                except:
                    continue
    #bmod = None
    for robmod in roboWhackList:
        #print("whack {}".format(robmod))
        del sys.modules[robmod]
    importlib.invalidate_caches()
    os.environ['STATS_SERVICE_URL'] = 'https://autoiq-test.extremenetworks.com/stats/testStats'
    #print(sys.path)
