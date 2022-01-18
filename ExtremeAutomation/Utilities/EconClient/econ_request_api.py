#!/usr/bin/env python3
# Standard Libraries
import json
from sys import platform
from pathlib import Path
import socket
import re
import glob
import codecs
import uuid
import requests
import os.path
from os import path
import shutil
from pprint import pprint

test_data = { 'base_url': 'test', 'testhost': None, 'testMount': None }

class econAPI():
    def __init__(self):
        if test_data['base_url']:
            self.base_url = test_data['base_url']
        else:
            self.base_url = 'prod'
        if self.base_url == 'local':
            self.BASE_ENDPOINT = "http://127.0.0.1:8087/"
            self.HEADERS = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
            }
        elif self.base_url == 'custom':
            self.BASE_ENDPOINT = "http://134.141.22.93:8087/"
            self.HEADERS = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'authorization': 'PAT d0fa673140034e25a7cb3641846b7274'
            }
            self.dockerVolume = "/tmp/results"
        elif self.base_url == 'test':
            self.BASE_ENDPOINT = "https://autoiq-test.extremenetworks.com/"
            self.HEADERS = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'authorization': 'PAT d0fa673140034e25a7cb3641846b7274'
            }
        else:
            self.BASE_ENDPOINT = "https://autoiq.extremenetworks.com/"
            self.HEADERS = {
                'Content-Type': 'application/json',
                'accept': 'application/json',
                'authorization': 'PAT f5321f6cc95211eba5e3164427672cc3'
            }
        if test_data['testhost']:
            self.myhost = test_data['testhost']
            self.testMode = 1
        else:
            self.myhost = socket.gethostname()
            self.testMode = None
        self.dockerVolume = "{}/results".format(Path.home())
        if platform == "win32":
            self.dockerVolume = "c:\\tmp\\automation\\results"
        self.postResults = 1
        self.testMount = test_data['testMount']

    def econRequest(self, ep, rtype='get', payload=None, ptype='dict'):
        oops = {"result": {"agentServer_uuid": None, "agentServerUuid": None, "APIERROR": "APIERROR"}, "error": ""}
        klist = ['key1','key2','key3','key4']
        op = payload
        route = []
        if payload:
            for k in klist:
                if k in payload:
                    route.append(op[k])
        if ptype == 'dict' and (rtype == 'post' or rtype == 'put'):
            payload = json.dumps(payload)
        if rtype == 'post':
            endPoint = "{}{}".format(self.BASE_ENDPOINT, ep)
            print("econRequest: {}".format(endPoint))
            r = requests.post(endPoint, data=payload, headers=self.HEADERS )
            try:
                return r.json()
            except:
                pass
                return oops
        elif rtype == 'put':
            if len(route) > 0:
                sep = '/'
                rpath = sep.join(route)
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, rpath)
            elif 'table' in payload and 'uuid' in payload:
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, op['uuid'])
            else:
                endPoint = "{}{}".format(self.BASE_ENDPOINT, ep)
            print("econRequest: {}".format(endPoint))
            r = requests.put(endPoint, data=payload, headers=self.HEADERS )
            try:
                return r.json()
            except:
                pass
                return oops
        elif rtype == 'delete':
            if len(route) > 0:
                sep = '/'
                rpath = sep.join(route)
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, rpath)
            elif payload:
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, payload)
            else:
                endPoint = "{}{}".format(self.BASE_ENDPOINT, ep)
            print("econRequest: {}".format(endPoint))
            r = requests.delete(endPoint, headers=self.HEADERS )
            try:
                return r.json()
            except:
                pass
                return oops
        elif rtype == 'get':
            if isinstance(payload, list):
                sep = '/'
                route = sep.join(payload)
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, route)
            elif payload:
                endPoint = "{}{}/{}".format(self.BASE_ENDPOINT, ep, payload)
            else:
                endPoint = "{}{}".format(self.BASE_ENDPOINT, ep)
            print("econRequest: {}".format(endPoint))
            r = requests.get(endPoint, headers=self.HEADERS )
            try:
                return r.json()
            except:
                pass
                return oops