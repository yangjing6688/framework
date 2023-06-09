from configparser import ConfigParser
import os
from ExtremeAutomation.Utilities.EconClient.econ_request_api import econAPI
import sys
import re
import json
from pathlib import Path
from robot.api.parsing import ModelVisitor
import glob

qtest_marker_re  = re.compile(r'TC[A-Z]{0,3}[\-_][0-9]+', flags=re.IGNORECASE)
fallback_testbed_names = ['testbed_1_node', 'testbed_2_node', 'testbed_3_node', 'testbed_4_node', 'testbed_5_node', 'testbed_adsp', 'testbed_none', 'testbed_not_required']
reserved_tags_re = re.compile(r'production|regression|nightly|sanity|p[1-5]')
PYTESTINI_PATH = 'pytest.ini'

def readPytestIni():
    try:
        parser = ConfigParser()
        parser.read(PYTESTINI_PATH)

        marker_list = parser['pytest']['markers'].split('\n')
        testbed_markers = []
        for item in marker_list:
            marker = item.split(':')[0] # Grab only the name of the marker/tag ignore the description
            if marker.startswith('testbed_'):
                testbed_markers.append(marker)

    # This will only work when the CI is running this script. Fallback to a static list otherwise
    except Exception:
        testbed_markers = fallback_testbed_names

    return testbed_markers


class RobotTestData(ModelVisitor):

    def __init__(self, node):
        self.suite_file = ''
        self.suite_name = ''
        self.tests = {}
        self.tags = {}
        self.global_tags = set()
        self.qTestTags = set()
        self.tcCount = 0
        # Read in testbed markers from pytest.ini
        self.testbed_tags = readPytestIni()

    def visit_File(self, node):
        self.suite_file = node.source
        self.tags[self.suite_file] = set()
        sname_raw = os.path.basename(node.source).split('.')[0]
        self.suite_name = sname_raw.replace("_", " ")
        self.suite_name = self.suite_name.title()
        #print(f"File '{node.source}' Title '{self.suite_name}' has following tests:")

        # Call `generic_visit` to visit also child nodes.
        self.generic_visit(node)

    def visit_ForceTags(self, node):
        #print(f"- {node.get_values('ARGUMENT')} (on line {node.lineno})")
        for nTag in node.get_values('ARGUMENT'):
            nTag = nTag.strip()
            self.addTag(nTag)
            self.global_tags.add(nTag)
    def visit_DefaultTags(self, node):
        #print(f"- {node.get_values('ARGUMENT')} (on line {node.lineno})")
        for nTag in node.get_values('ARGUMENT'):
            nTag = nTag.strip()
            self.addTag(nTag)
            self.global_tags.add(nTag)
    def visit_TestCase(self, node):
        self.tests.update({node.name: {'tags': []}})
        for statement in node.body:
            # Get tags at test case level.
            try:
                if statement.type == "TAGS":
                    self.tests[node.name]['tags'] = list(statement.values)
                    for tag in statement.values:
                        self.addTag(tag.strip())
                    break # We found our tags. Time to bail
            except AttributeError:
                # Hit an object without a "type" attribute. Skip to the next object
                continue

    def print_suite(self):
        goodCaseName = re.compile(r"(test_[0-9a-zA-Z\[\]\-_\.]+)")
        relative_path = os.path.relpath(self.suite_file,  os.getcwd())
        output_dict = {
            relative_path: {}
        }

        print(f'Suite: {self.suite_name}')

        for test_name in self.tests:
            self.tcCount += 1
            print(f"{self.tcCount} Test Case - {test_name}")

            self.tests[test_name]['tags'].extend(self.global_tags)

            # Set results
            nameOK = True if goodCaseName.match(test_name) else False
            dev_exists = True if 'development' in self.tests[test_name]['tags'] else False

            qtest_tags = []
            qtest_pass = False
            uppercase_check = True    # True = all tags lowercase, False = atleast one tag with uppercase letters
            reserved_tags_check = False  # True = atleast one reserved tag found, False = no reserved tags used
            testbed_tag_exists = False
            for tag in self.tests[test_name]['tags']:
                if tag in self.testbed_tags:
                    testbed_tag_exists = True
                qtest_match = qtest_marker_re.fullmatch(tag)
                if qtest_match:
                    qtest_tags.append(qtest_match[0])
                    qtest_pass = True
                if not tag.islower():
                    uppercase_check = False
                if reserved_tags_re.fullmatch(tag):
                    reserved_tags_check = True

            testcase_info = {
                "all_tags_lower_case": uppercase_check,
                "contains_development": dev_exists,
                "valid_qtest_tag": qtest_pass,
                "qtest_tags": qtest_tags,
                "valid_test_name": nameOK,
                "contains_testbed_tag": testbed_tag_exists,
                "contains_reserved_tag": reserved_tags_check,
                "marker_list": list(self.tests[test_name]['tags']),
                "testcase_name": test_name

            }

            # Keyed on relative path of testcase file, then function name
            output_dict[relative_path].setdefault(test_name, testcase_info)


        return output_dict

    def addTag(self, inTag):
        # filter qTest tags
        if qtest_marker_re.search(inTag):
            self.qTestTags.add(inTag)
        # add tag to set
        self.tags[self.suite_file].add(inTag)

class PytestItems():
    def __init__(self, session):
        self.session = session
        self.what = {}
        self.testcount = 0
        self.existingModules = {}
        self.modPart = {}
        self.modlist = []
        self.newModules = []
        self.foundMods = {}
        self.nodeByMod = {}
        self.mc = {}
        self.PT = PathTools()
        # Read in testbed markers from pytest.ini
        self.testbed_markers = readPytestIni()

    def get_inventory_info(self):
        goodCaseName = re.compile(r"(test_[0-9a-zA-Z\[\]\-_\.]+)")
        output_dict = {}
        cwd = os.getcwd()

        if self.session.config.option.get_test_info is not None:
            for item in self.session.items:
                caseNodes = 1
                self.testcount += 1
                mlist = []
                markers = item.keywords.__dict__['_markers']
                ignore_markers = re.compile(r"true|false|[0-9]+\-[0-9]+|TRUE|FALSE|True|False|pytestmark|parametrize")

                # make list of user created markers
                qtest_tags = []
                qtest_pass = False
                uppercase_check = True    # True = all tags lowercase, False = atleast one tag with uppercase letters
                reserved_tags_check = False  # True = atleast one reserved tag found, False = no reserved tags used
                testbed_tag_exists = False
                for (k, v) in markers.items():
                    marker = str(k).strip()
                    # Skip markers we don't care about. pyTest intenal, etc.
                    if ignore_markers.match(marker):
                        continue
                    if v and k != item.name:
                        if marker in self.testbed_markers:
                            if marker.endswith('node'):
                                caseNodes = int(marker.split('_')[1])
                            testbed_tag_exists = True
                        qtest_match = qtest_marker_re.fullmatch(marker)
                        if qtest_match:
                            qtest_tags.append(qtest_match[0])
                            qtest_pass = True
                        if not marker.islower():
                            uppercase_check = False
                        if reserved_tags_re.fullmatch(marker):
                            reserved_tags_check = True

                        mlist.append(marker)
                # Set results
                relative_path = os.path.relpath(item.fspath,  cwd)
                nameOK = True if goodCaseName.match(item.name) else False
                dev_exists = True if 'development' in mlist else False

                testcase_info = {
                    "all_tags_lower_case": uppercase_check,
                    "contains_development": dev_exists,
                    "valid_qtest_tag": qtest_pass,
                    "qtest_tags": qtest_tags,
                    "valid_test_name": nameOK,
                    "contains_testbed_tag": testbed_tag_exists,
                    "contains_reserved_tag": reserved_tags_check,
                    "marker_list": mlist

                }

                # Keyed on relative path of testcase file, then function name
                output_dict.setdefault(relative_path, {}).setdefault(item.name, testcase_info)


                # Test module stuff
                parts = self.PT.pathParts(item.fspath)
                post = self.PT.getModNameFromFolders('pytest', parts)
                if post['TestModule'] not in self.modlist:
                    self.nodeByMod[post['TestModule']] = caseNodes
                    self.modlist.append(post['TestModule'])
                    cat = post['Category']
                    if not cat:
                        cat = 'functional'
                    modPart = {"TestModule": post['TestModule'], 'category': cat, 'repoPath': post['RepoPath']}
                    mstuff = {'category': cat, 'repoPath': post['RepoPath']}
                    self.newModules.append(modPart)
                    self.foundMods.update({post['TestModule'] : mstuff})
                    self.mc[post['TestModule']] = 1
                else:
                    self.mc[post['TestModule']] += 1
                    if int(self.nodeByMod[post['TestModule']]) < int(caseNodes):
                        self.nodeByMod[post['TestModule']] = caseNodes
                #print("Count:{} {}".format(self.testcount,post))

            for md in self.newModules:
                self.foundMods[md['TestModule']]['nodeCount'] = self.nodeByMod[md['TestModule']]
                self.foundMods[md['TestModule']]['numCases'] = self.mc[md['TestModule']]
                # print("Module: {} Category: {} RepoPath: {} Count: {}".format(md['TestModule'],
                #                          md['category'],md['repoPath'],self.mc[md['TestModule']]))

        # Output CICD info
        print(json.dumps(output_dict))
        with open(f'{cwd}/pytest_data.json', 'w') as outfile:
            json.dump(output_dict, outfile)

        if self.session.config.option.get_test_info in ['insert', 'checkdb'] :
            h = "econ_auto"
            qCat = 'functional'
            ec = econAPI()
            getData = {
                "nosList": [ "EXOS", "VOSS" ],
                "category": "functional"
            }
            res = ec.econRequest('tbedmgr/jobmgr/jobConfig/testModules',
                                 rtype='post', payload=getData)
            if 'result' in res:
                finalFoundMods = []
                skipNewMod = []
                bypassList = ['DefaultTemplate', 'Dummy', 'DefaultTemplateUI', 'DetermineTBStatus', 'XiQ']
                tmList = res['result']['testModuleList']
                for tm in tmList:
                    if tm['harness'] != h:
                        continue
                    else:
                        try:
                            if tm['name'] in self.modlist or self.foundMods[tm['name']]['category'] != qCat:
                                skipNewMod.append(tm['name'])
                        except:
                            dbonly = {'category': qCat, 'repoPath': 'NA', 'nodeCount': 'NA', 'numCases': 'NA'}
                            self.foundMods.update({post['TestModule'] : dbonly})

                for mm in self.modlist:
                    if qCat != self.foundMods[mm]['category']:
                        continue
                    else:
                        finalFoundMods.append(mm)
                goList1 = list(set(finalFoundMods) - set(skipNewMod))
                goList = []
                for ggg in goList1:
                    if ggg in bypassList:
                        continue
                    goList.append(ggg)

                print("bypass:{}\nskip:{}\ninsert:{}".format(bypassList,skipNewMod,goList))
        if self.session.config.option.get_test_info == 'insert':
            if len(goList) > 0:
                for goTm in goList:
                    tmData ={"name": goTm,
                        "description": goTm+" Pytest Test Module",
                        "qeOwner": "TBD",
                        "automationOwner": "TBD",
                        "maxNodes": str(self.nodeByMod[goTm]),
                        "deprecated": "0",
                        "harnessType": h,
                        "testModuleCategory": qCat,
                        "nosList": [
                            "EXOS", "VOSS"
                        ],
                        "firstReleaseList": [
                            "31.0", "8.1"
                        ],
                        "lastReleaseList": [
                            "99.9", "99.9"
                        ],
                        "testRepository": "econ-automation-tests",
                        "testDirPath": self.foundMods[goTm]['repoPath']
                    }
                    print("tmdata {}".format(tmData))
                    res = ec.econRequest('tbedmgr/jobmgr/jobConfig/createTestModule',
                                         rtype='post', payload=tmData)
                    print(res)


class PathTools():
    def __init__(self):
        self.path = ""
        self.rootDir = {"pytest": ["extreme_automation_tests", "econ-automation-tests"], "robot": "cw_automation"}
        self.testDirList = { "pytest" : { "Demos": ["pytest", "robot"],
                                                "Tests": ["Pytest", "Staging", "Prod"]},
                                   "robot" :  {"testsuites": ["app", "xiq", "xiqse"],
                                                 "Tests":  ["Robot"]
                                               }
                                   }
        self.ignoreDir = ["TestCases"]
        self.cats = {"functional": "functional", "Functional": "functional", "System": "systems"}


    def pathParts(self, path):
        folders = []
        while 1:
            path, folder = os.path.split(path)

            if folder != "":
                folders.append(folder)
            elif path != "":
                folders.append(path)

                break
        folders.reverse()
        return folders

    def getModNameFromFolders(self, harness, folders):
        out = {}
        pStart = 0
        pEnd = 0
        newFolders = []
        testMod = None
        cat = None
        rootOK = 0
        for rootD in self.rootDir[harness]:
            if rootD in folders:
                pStart = folders.index(rootD)
                rootOK = 1
        if not rootOK:
            return out
        for (k, v) in self.testDirList[harness].items():
            if k in folders:
                if harness in v:
                    if harness in folders:
                        modLow = folders.index(harness)
                        modInd = modLow + 1
                        tcInd  = modInd + 1
                        testMod = folders[modInd]
                        pEnd = modInd
                        if folders[tcInd] == "TestCases":
                            print("Found TestCases")
                            pEnd = folders.index("TestCases")

                else:
                    for nDir in v:
                        if nDir in folders:
                            modLow = folders.index(nDir)
                            catInd = modLow + 1
                            if folders[catInd] in self.cats:
                                cat = self.cats[folders[catInd]]
                                modInd = catInd + 1
                                testMod = folders[modInd]
                            else:
                                modInd = catInd
                                testMod = folders[modInd]
                            tcInd = modInd + 1
                            if folders[tcInd] == "TestCases":
                                pEnd = tcInd
                            else:
                                pEnd = modInd
        newFolders = folders[pStart:pEnd+1]
        sep = "/"
        p = sep.join(newFolders)
        out = {"TestModule": testMod, "Category": cat, "RepoPath": p}
        return out

    def locateCfg(self, cfgFile):
        for p in sys.path:
            parts = self.pathParts(p)
            tbedDir = Path(p+'/TestBeds')
            if os.path.isdir(tbedDir) and 'extreme_automation_tests' in parts:
                myCfgSrch = f'{tbedDir}/**/{cfgFile}'
                myCfgFile = glob.glob(myCfgSrch, recursive = True)
                if len(myCfgFile) > 0:
                    return myCfgFile[0]
        print(f"WARNING!! {cfgFile} could not be located")
        return None

    def locateEnv(self, envFile):
        for p in sys.path:
            parts = self.pathParts(p)
            envDir = Path(p+'/Environments')
            if os.path.isdir(envDir) and 'extreme_automation_tests' in parts:
                myEnvSrch = f'{envDir}/**/{envFile}'
                myEnvFile = glob.glob(myEnvSrch, recursive = True)
                if len(myEnvFile) > 0:
                    return myEnvFile[0]
        print(f"WARNING!! {envFile} could not be located")
        return None

    def locateTopo(self, topoFile):
        for p in sys.path:
            parts = self.pathParts(p)
            envDir = Path(p+'/Environments')
            if os.path.isdir(envDir) and 'extreme_automation_tests' in parts:
                myTopoSrch = f'{envDir}/**/{topoFile}'
                myTopoFile = glob.glob(myTopoSrch, recursive = True)
                if len(myTopoFile) > 0:
                    return myTopoFile[0]
        print(f"WARNING!! {topoFile} could not be located")
        return None