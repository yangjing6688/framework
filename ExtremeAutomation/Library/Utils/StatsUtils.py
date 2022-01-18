# pylint: disable=C0103,R0903,C0301,W0703

""" Interface into the econ-stats microservice """

import inspect
import logging
import requests
import json
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def lineno():
    """ Return current line number (relative to caller) """
    return inspect.currentframe().f_back.f_lineno


class MicroserviceInterface():

    """ Define how we talk to the econ-stats microservice

        - Routes include:
              testStats/kwTiming
              testStats/kwEvent
    """

    defaultURL = 'https://autoiq-test.extremenetworks.com/stats/testStats'
    serviceURL = os.getenv('STATS_SERVICE_URL', defaultURL) + '/kwTiming'
    eventURL   = os.getenv('STATS_SERVICE_URL', defaultURL) + '/kwEvent'
    tfileURL   = os.getenv('STATS_SERVICE_URL', defaultURL) + '/testFile'


    headers = {
            'Content-Type': 'application/json',
            'accept': 'application/json',
            'authorization': 'PAT d0fa673140034e25a7cb3641846b7274'
        }


    def postStats(self,dataDict):

        """ Add data into the DB via the econ-stats microservice """

        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name

        logger.info("[+] Line %s: Entering function     : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Called from function  : %s()",lineno(),callingfunction_name)
        required = ['startTime','endTime','os','connectionType','hwType','testCaseUuid','keywordUuid']
        assert isinstance(dataDict,dict)
        for req in required:
            assert req

        logger.info("\n[+] Line %s: requests.post POSTING: %s\n",lineno(),dataDict)
        try:
            res = requests.post(self.serviceURL, headers=self.headers, json=dataDict)
        except Exception:
            logger.error("[ERROR] Line %s: requests.post returned: %s",lineno(),res.text)
            return False

        logger.info("[+] Line %s: requests.post returned: %s",lineno(),res.text)
        logger.info("[+] Line %s: Leaving function      : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Returning to function : %s()",lineno(),callingfunction_name)
        return True


    def postEvent(self,dataDict):

        """ Add data into the kwEvent table via the econ-stats microservice """

        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name

        logger.info("[+] Line %s: Entering function     : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Called from function  : %s()",lineno(),callingfunction_name)
        required = ['keywordUuid', 'keywordName']
        assert isinstance(dataDict,dict)
        for req in required:
            assert req

        logger.info("\n[+] Line %s: requests.post POSTING: %s\n",lineno(),dataDict)
        try:
            res = requests.post(self.eventURL, headers=self.headers, json=dataDict)
        except Exception:
            logger.error("[ERROR] Line %s: requests.post returned: %s",lineno(),res.text)
            return False

        logger.info("[+] Line %s: requests.post returned: %s",lineno(),res.text)
        logger.info("[+] Line %s: Leaving function      : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Returning to function : %s()",lineno(),callingfunction_name)
        return True

    def postTfile(self,dataDict) -> str:

        """ Add test file & repo name into the testFiles table via the econ-stats microservice """

        this_function_name   = inspect.currentframe().f_code.co_name
        callingfunction_name = inspect.currentframe().f_back.f_code.co_name

        logger.info("[+] Line %s: Entering function     : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Called from function  : %s()",lineno(),callingfunction_name)
        required = ['testfileUuid', 'testfileName', 'testfileRepo']
        assert isinstance(dataDict,dict)
        for req in required:
            assert req

        logger.info("\n[+] Line %s: requests.post POSTING: %s\n",lineno(),dataDict)
        try:
            res = requests.post(self.tfileURL, headers=self.headers, json=dataDict)
        except Exception:
            logger.error("[ERROR] Line %s: requests.post returned: %s",lineno(),res.text)
            return False

        retVal = json.loads(res.text)
        logger.info("[+] Line %s: requests.post returned: %s",lineno(),res.text)
        logger.info("[+] Line %s: Returning to caller   : %s",lineno(),retVal['result'])
        logger.info("[+] Line %s: Leaving function      : %s()",lineno(),this_function_name)
        logger.info("[+] Line %s: Returning to function : %s()",lineno(),callingfunction_name)
        return str(retVal['result'])
