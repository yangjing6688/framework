# provide the ability to check in / out test beds
#
# Check out example:
# python tbedmgr_resource -t rdu_x460g2_stk_pod1_4node.yaml -o -r "test out script" -w -d 48
#
# Check in example:
# python tbedmgr_resource -t rdu_x460g2_stk_pod1_4node.yaml -i
#
# Include standard modules
import argparse
import requests
import time
import sys
import re


#######################################################################################
# Functions
#######################################################################################
def isValidGUID(guid_value):
    regex = "^[{]?[0-9a-fA-F]{8}" + "-([0-9a-fA-F]{4}-)" + "{3}[0-9a-fA-F]{12}[}]?$"
    p = re.compile(regex)
    if (str == None):
        return False
    if(re.search(p, guid_value)):
        return True
    else:
        return False

def getTestbedUUIDFromFile(yamlFileName):
    uuid = None
    try:
        endPoint = BASE_ENDPOINT + 'tbedmgr/testbed'
        req = requests.get(endPoint, headers=HEADERS, timeout=5 )
        results = req.json()
        if req.status_code == 200 and len(results['errors']) == 0:
            testbed_data = results['result']
            for test_bed_data in testbed_data:
                if test_bed_data['configFileName'] == yamlFileName:
                    uuid = test_bed_data['testbed_uuid']
                    if not isValidGUID(uuid):
                        sys.exit(f"ERROR: test bed GUID is not valid {uuid}")
                    break
        else:
            sys.exit(f"ERROR: Unable to connect to {endPoint}")
    except Exception as e:
        print(e)
    return uuid

def getTestbedLockIDFromFile(yamlFileName):
    lock_uuid = None
    try:
        endPoint = BASE_ENDPOINT + 'tbedmgr/locks/lockedTestbeds'
        req = requests.get(endPoint, headers=HEADERS, timeout=5 )
        results = req.json()
        if req.status_code == 200 and len(results['errors']) == 0:
            testbed_lock_data = results['result']
            for data in testbed_lock_data:
                if data['configFileName'] == yamlFileName:
                    lock_uuid = data['lock_uuid']
                    if not isValidGUID(lock_uuid):
                        sys.exit(f"ERROR: lock GUID is not valid {lock_uuid}")
                    break
        else:
            sys.exit(f"ERROR: Unable to connect to {endPoint}")
    except Exception as e:
        print(e)
    return lock_uuid

def checkoutTestBed(testbed_uuid, duration, lockReason):
    uuid = None
    try:
        endPoint = BASE_ENDPOINT + 'tbedmgr/locks/lockTestbed'
        payloadLock = {}
        payloadLock['testbed_uuid'] = testbed_uuid
        payloadLock['requestedDuration'] = duration
        payloadLock['lockReason'] = lockReason

        req = requests.post(endPoint, json=payloadLock, headers=HEADERS, timeout=5 )
        results = req.json()
        if req.status_code == 201 and len(results['errors']) == 0:
            return results['result']
        else:
            return None
    except Exception as e:
        print(e)
    return uuid

def checkinTestBed(lock_uuid):
    try:
        endPoint = BASE_ENDPOINT + 'tbedmgr/locks/deleteTestBedLock/' + str(lock_uuid)
        req = requests.delete(endPoint, json={}, headers=HEADERS, timeout=5 )
        results = req.json()
        if req.status_code == 200 and len(results['errors']) == 0:
            return True
        else:
            return False
    except Exception as e:
        print(e)
    return False


#######################################################################################
# Script
#######################################################################################

# Initiate the parser
parser = argparse.ArgumentParser()

# Add long and short argument
group = parser.add_mutually_exclusive_group()
group.add_argument("--checkin", "-i", help="Check in a test bed", action="store_true")
group.add_argument("--checkout", "-o", help="Check out a test bed", action="store_true")
parser.add_argument("--testbed", "-t", help="Test Bed yaml file (for the action of checkout / in)")
parser.add_argument("--lockreason", "-r", help="lock reason")
parser.add_argument("--lockduration", "-d", help="lock duration")
parser.add_argument("--wait", "-w", help="Wait until the test bed to be locked", action="store_true")
parser.add_argument("--tbedmgrendpoint", "-e", help="End point", default='https://autoiq.extremenetworks.com/')
parser.add_argument("--pat", "-p", help="The PAT for AutoIQ")

# Read arguments from the command line
args = parser.parse_args()

if not args.pat:
    sys.exit("ERROR: Need to have the -p or --pat option!")

if not args.testbed:
    sys.exit("ERROR: Need to have the -t or --testbed option!")

if not args.checkin and not args.checkout:
    sys.exit("ERROR: Need to have the -o or -i option for an action")

if args.tbedmgrendpoint != 'https://autoiq.extremenetworks.com/':
    print("NON PROD MODE SELECTED!")

HEADERS = { 'Content-Type': 'application/json',
            'accept': 'application/json',
            'authorization': 'PAT ' + args.pat
          }

BASE_ENDPOINT = args.tbedmgrendpoint

testbed_uuid = getTestbedUUIDFromFile(args.testbed)
if testbed_uuid == None:
    sys.exit("ERROR: unable to get the test bed UUID!")

return_text = ''
if args.checkin:
    print(f'Check in the file: {args.testbed}')
    lock_uuid = getTestbedLockIDFromFile(args.testbed)
    if lock_uuid:
        testbed_checked_in = checkinTestBed(lock_uuid)
        print(f"TESTBED CHECK IN: {testbed_checked_in}")
        if not testbed_checked_in:
            sys.exit("ERROR: Failed to Checked in test bed!")
    else:
        sys.exit("ERROR: unable to get the test bed lock UUID!")

elif args.checkout:
    if not args.lockreason or not args.lockduration:
        sys.exit("ERROR: Need to have the -d (lock duration) and -r (lock reason) options for checkout!")

    print(f'Check out the file: {args.testbed}')
    if args.wait:
        testbed_checked_out = checkoutTestBed(testbed_uuid, args.lockduration, args.lockreason)
        print(f"Checkout returned: {testbed_checked_out}")
        while(testbed_checked_out == None):
            print("Waiting 30 seconds")
            time.sleep(30)
            testbed_checked_out = checkoutTestBed(testbed_uuid, args.lockduration, args.lockreason)
            print(f"Checkout returned: {testbed_checked_out}")
    else:
        testbed_checked_out = checkoutTestBed(testbed_uuid, args.lockduration, args.lockreason)
        if testbed_checked_out == None:
            sys.exit("ERROR: Failed to check out the test bed!")
    print(f"TESTBED CHECK OUT: {testbed_checked_out}")


print('completed')
sys.exit()
