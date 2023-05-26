# Author        : Rashmi Shahoo
# Description   : This XAPI utility will replace emails, phone numbers for all Ppsk users in an account,
#                 using XPI API calls, list end users, update end users
#                 It runs a bulk edit on all Ppsk users in an account,
#                 It will change all-
#                  Email address  as (str of 5 random characters  + int in incremental order +
#                  domain can be changed default is extremenetworks.com)
#                  #phone number  as ( 1- digit random number users utility to generate 10 digit random number )
#                  #sets sms delivery method , email delivery method  as empty string
#
# Comments      : This  can be used by a test in Pytest or Robot  to replace end users emails and password
#                 and set delivery method (sms/phone) to empty string when a new account is loaded in test environment.
#                 keyword to be used: update_all_ppsk_end_users_email_phon_delivery_methods

from extauto.common.Utils import Utils
from keywords.xapi_base.XapiBaseAuthorizationApi import XapiBaseAuthorizationApi
from keywords.xapi_base.XapiBaseAuthenticationApi import XapiBaseAuthenticationApi
from keywords.xapi_base.XapiBaseAccountApi import XapiBaseAccountApi
from keywords.xapi_base.XapiBaseConfigurationUserManagementApi import XapiBaseConfigurationUserManagementApi


# Standard Keyword imports
from extauto.common.CommonValidation import CommonValidation
from extauto.common.KeywordUtils import KeywordUtils
from tools.xapi.XapiHelper import XapiHelper
from ExtremeAutomation.Library.Utils.Singleton import Singleton

# Keyword imports required to run keywords implemented in this file
from extauto.xiq.xapi.manage.XapiDevices import XapiDevices
from extauto.xiq.flows.manage.Devices import Devices

class KeywordsUpdateAllPpskEndUsers(object, metaclass=Singleton):
    def __init__(self):
        # This is a singleton, avoid initializing for each instance
        if hasattr(self, 'initialized'):
            return
        self.initialized = True

        # Objects used by all keywords
        self.common_validation = CommonValidation()
        self.keyword_utils = KeywordUtils()
        self.xapi_helper = XapiHelper()

        # Object used to run keywords implemented in this file
        self.devices = Devices()
        self.xapiDevices = XapiDevices()

        self.utils = Utils()
        self.xapiBaseAuthorizationApi = XapiBaseAuthorizationApi()
        self.xapiBaseAuthenticationApi = XapiBaseAuthenticationApi()
        self.xapiBaseConfigurationUserManagementApi = XapiBaseConfigurationUserManagementApi()
        self.xapiBaseAccountApi = XapiBaseAccountApi()
        self.xapiHelper = XapiHelper()


    def update_all_ppsk_end_users_email_phone_delivery_methods(self, domain = "extremenetworks.com"):
        """
        # This method go through all pages and calls update user
        # default domain can be changed if needed.
        @param domain:default value is  "extremenetworks.com"( can be changed)
                - Keyword Usage:
        -   Robot:
        -      Library  keywords/gui/configure/UserManagement/Users/KeywordsUpdateAllPpskEndUsers.py
        -      update_all_ppsk_end_users_email_phone_delivery_methods      ${domain}
        -
        -   Pytest:
        -      Imports:
        -         from keywords.gui.configure.UserManagement.Users import KeywordsUpdateAllPpskEndUsers
        -      Calling KeywordsUpdateAllPpskEndUsers:
        -         Keywords_UpdateAllPpskEndUsers = KeywordsUpdateAllPpskEndUsers()
        -         Keywords_UpdateAllPpskEndUsers.update_all_ppsk_end_users_email_phone_delivery_methods(domain = "extremenetworks.com")
        -

        """

        self.domain = domain

        # Make a get_end_user call to get total pages
        data = self.get_end_users()

        total_pages = data.total_pages
        updated_indexes = 0

        # loop through all pages
        for page_count in range (1, total_pages+1):
            page = page_count
            self.utils.print_info("Getting Page:" + str(page))
            # call below method get_end_users in this file
            user_data = self.get_end_users(page_to_fetch = page)

            # Take each page and loop through all users to call update_end_users which in turn call api on each user
            for user_count in range(0, len(user_data.data)):
                updated_indexes = updated_indexes + 1
                self.utils.print_info(updated_indexes)

                # call below method update_end_user in this file
                self.update_end_user(user_data.data[user_count], updated_indexes)

        # Print total number of records updated and return to main
        self.utils.print_info("Total records updated :" + str(updated_indexes))
        return
    def get_end_users(self, page_to_fetch = 1):
        """This method will be called by above keyword method to get all end users
        :param page_to_fetch: page number to get users
        :return: The users for page no sent
        """
        # return to above function update_all_ppsk_end_users_email_phon_delivery_methods
        return self.xapiBaseConfigurationUserManagementApi.xapi_base_list_end_users(page=page_to_fetch, limit=100)


    def update_end_user(self, data, index):
        """
        This method  will be called by (above method)update_all_ppsk_end_users_email_phon_delivery_methods to makes a call to xapi_base_update_end_user to update a user details
        :param data: end user object
        :param index: index of the user to be updated
        :return:
        """
        payload = {
                    "email_address": self.utils.get_random_string(length=5) + str(index) + "@" + self.domain,
                    "phone_number": str(self.utils.get_random_integer(length=10, lower_limit=1000000000, upper_limit=9999999999)) ,
                    "email_password_delivery": "",
                    "sms_password_delivery": ""
                   }
        self.utils.print_info("Updating id: " + str(data.id))

        # Call xapi_base_update_end_user to update a user
        self.xapiBaseConfigurationUserManagementApi.xapi_base_update_end_user(id = data.id, xiq_update_end_user_request = payload)

        # Return to function update_all_ppsk_end_users_email_phone_delivery_methods function
        return
