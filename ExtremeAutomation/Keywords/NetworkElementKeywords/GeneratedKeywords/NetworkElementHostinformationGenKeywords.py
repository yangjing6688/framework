"""
Keyword class for all hostinformation cli commands.
"""
from ExtremeAutomation.Keywords.BaseClasses.NetworkElementKeywordBaseClass import NetworkElementKeywordBaseClass
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.ParseApis.Constants.HostinformationConstants import \
    HostinformationConstants as ParseConstants
from ExtremeAutomation.Apis.NetworkElement.GeneratedApis.CommandApis.Constants.HostinformationConstants import \
    HostinformationConstants as CommandConstants
# All imports above this line will be removed after generation.
# User imports must be added below.


class NetworkElementHostinformationGenKeywords(NetworkElementKeywordBaseClass):
    def __init__(self):
        super(NetworkElementHostinformationGenKeywords, self).__init__()
        self.cmd_const = CommandConstants()
        self.parse_const = ParseConstants()
        self.api_const = "hostinformation"

    def hostinformation_set_prompt(self, device_name, prompt_name='', **kwargs):
        """
        Description: Sets the system prompt.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS
        """
        args = {
            "prompt_name": prompt_name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_PROMPT,
                                    **kwargs)

    def hostinformation_set_host_contact(self, device_name, contact='', **kwargs):
        """
        Description: Sets the host contact.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS, EXOS, EOS
        """
        args = {
            "contact": contact
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOST_CONTACT,
                                    **kwargs)

    def hostinformation_set_host_name(self, device_name, name='', **kwargs):
        """
        Description: Sets the host name.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS, EXOS, EOS
        """
        args = {
            "name": name
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOST_NAME,
                                    **kwargs)

    def hostinformation_set_host_location(self, device_name, location='', **kwargs):
        """
        Description: Sets the host location.

        Supported Agents and OS:
            CLI: VOSS
            SNMP: VOSS, EXOS, EOS
        """
        args = {
            "location": location
        }

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.SET_HOST_LOCATION,
                                    **kwargs)

    def hostinformation_clear_prompt(self, device_name, **kwargs):
        """
        Description: Clears the system prompt restoring it to the default setting.

        Supported Agents and OS:
            CLI: VOSS
        """
        args = {}

        return self.execute_keyword(device_name, args,
                                    self.cmd_const.CLEAR_PROMPT,
                                    **kwargs)

    # ##################################################################################################################
    #   Inspection Keywords   ##########################################################################################
    # ##################################################################################################################

    def hostinformation_verify_system_prompt(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name]  - The device the keyword will run against.
        [prompt_name]  - The system prompt name.

        Verifies the system prompt name.
        """
        args = {"prompt_name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_SYSTEM_NAME,
                                           self.parse_const.CHECK_PROMPT, True,
                                           "The system prompt is correctly set to {prompt_name}.",
                                           "The system prompt IS NOT set to {prompt_name}!",
                                           **kwargs)

    def hostinformation_verify_host_location(self, device_name, location='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [location]    - The physical location of this node (e.g., `telephone closet, 3rd floor').
        Verifies the value of the host location.
        """
        args = {"location": location}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_LOCATION,
                                           self.parse_const.CHECK_HOST_LOCATION, True,
                                           "Host location is {location}.",
                                           "Host location is NOT {location}!",
                                           **kwargs)

    def hostinformation_verify_host_contact(self, device_name, contact='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [contact]     - The textual identification of the contact person for this managed node,
                         together with information on how to contact this person.

        Verifies the value of the host contact.
        """
        args = {"contact": contact}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_CONTACT,
                                           self.parse_const.CHECK_HOST_CONTACT, True,
                                           "Host contact is {contact}.",
                                           "Host contact is NOT {contact}!",
                                           **kwargs)

    def hostinformation_verify_host_name(self, device_name, name='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [name]        - An administratively-assigned name for this managed node.  By convention, this is the node's
                        fully-qualified domain name.

        Verifies the value of the host name.
        """
        args = {"name": name}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_NAME,
                                           self.parse_const.CHECK_HOST_NAME, True,
                                           "Host name is {name}.",
                                           "Host name is NOT {name}!",
                                           **kwargs)

    def hostinformation_verify_host_system_id(self, device_name, system_id='', **kwargs):
        """
        Keyword Arguments:
        [device_name] - The device the keyword will run against.
        [system_id]   - The vendor's authoritative identification of the
                        network management subsystem contained in the
                        entity in it's assigned textual form.
                        This value is allocated within the SMI
                        enterprises subtree (1.3.6.1.4.1) and provides an
                        easy and unambiguous means for determining what
                        kind of box is being managed.

        Verifies the value of the host system identifier.
        """
        args = {"system_id": system_id}

        return self.execute_verify_keyword(device_name, args, self.cmd_const.SHOW_HOST_OBJECT_ID,
                                           self.parse_const.CHECK_HOST_SYSTEM_ID, True,
                                           "Host system id is {system_id}.",
                                           "Host system id is NOT {system_id}!",
                                           **kwargs)
