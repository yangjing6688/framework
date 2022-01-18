from ExtremeAutomation.Keywords.BaseClasses.UiKeywordBaseClass import UiKeywordBaseClass
from ExtremeAutomation.Apis.UiElement.GeneratedApis.Constants.EMC.EventsConstants import EventsConstants


class UiEventsKeywords(UiKeywordBaseClass):
    def __init__(self):
        super(UiEventsKeywords, self).__init__()
        self.api_const = self.constants.API_EVENTS
        self.command_const = EventsConstants()

    def events_set_event_types(self, element_name, event_types, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [event_types] -   Comma-separated list of event types to select in the Type drop down

        Selects the specified event types in the Type drop down for the Events table.
        NOTE: Any current selections are cleared.
        """
        args = {'event_types': event_types}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_SET_EVENT_TYPES, **kwargs)

    def events_click_next_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">" button to go to the next page in the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLICK_NEXT_PAGE, **kwargs)

    def events_click_prev_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<" button to go to the previous page in the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLICK_PREV_PAGE, **kwargs)

    def events_click_first_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "<<" button to go to the first page in the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLICK_FIRST_PAGE, **kwargs)

    def events_click_last_page(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the ">>" button to go to the last page in the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLICK_LAST_PAGE, **kwargs)

    def events_click_reset(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "Reset" button which clears the search field, clears the filters, and refreshes the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLICK_RESET, **kwargs)

    def events_set_column_filter(self, element_name, col_name, the_filter, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_name] -      Name of the column to filter
        [the_filter] -    Value to filter the column by:
                          if text type, should just be the string to enter
                          if check button type, a comma-separated list of values is accepted

        Sets a column filter for the specified column in the Events table.
        NOTE: not all columns have the filter capability.
        """
        args = {'col_name': col_name,
                "the_filter": the_filter}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_SET_COLUMN_FILTER, **kwargs)

    def events_enable_column_filter(self, element_name, col_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_name] -      Name of the column to enable the filter on

        Enables the column filter for the specified column in the Events table.
        """
        args = {'col_name': col_name}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_ENABLE_COLUMN_FILTER, **kwargs)

    def events_disable_column_filter(self, element_name, col_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_name] -      Name of the column to disable the filter on

        Disables the column filter for the specified column in the Events table.
        The check button is deselected, but the value is left intact (that is, the filter field is not cleared).
        """
        args = {'col_name': col_name}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_DISABLE_COLUMN_FILTER, **kwargs)

    def events_clear_column_filter(self, element_name, col_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [col_name] -      Name of the column to clear the filter on

        Clears the filter for the specified column.  Clears the filter value and deselects the Filter check box.
        """
        args = {'col_name': col_name}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLEAR_COLUMN_FILTER, **kwargs)

    def events_set_table_filter(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     String to enter in the table's filter field

        Enters the specified value into the search field of the Events table.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_SET_TABLE_FILTER, **kwargs)

    def events_clear_table_filter(self, element_name, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against

        Clicks the "X" in the search field to clear the filter from the Events table.
        """
        args = {}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CLEAR_TABLE_FILTER, **kwargs)

    def events_select_event(self, element_name, the_value, **kwargs):
        """
        Keyword Arguments:
        [element_names] - List of elements the keyword will be run against
        [the_value] -     String to enter in the table's filter field

        Selects the specified event in the Events table.
        NOTE: The event must be visible in the table - set the table filter, the column filter, or use the paging
              buttons to insure the event is visible.
        """
        args = {'the_value': the_value}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_SELECT_EVENT, **kwargs)

    def events_confirm_event_message_contains(self, element_name, event_str_list, exists, max_pages=0, **kwargs):
        """
        Keyword Arguments:
        [element_names]  - List of elements the keyword will be run against
        [event_str_list] - Comma separated list of strings to match in the Information column (event message attribute)
        [exists]         - Indicates whether or not the event is expected to be found (True/False)
        [max_pages]      - (Optional) Specifies the maximum number of pages to check;  if not specified, all pages will
                           be checked

        Searches for an event whose Information column (event message attribute) contains all of the specified strings.
        Will keep searching through each page of events until a match is found or all events have been checked, up to
        the max number of pages (optional - if not specified, all pages will be checked).
        """
        args = {'event_str_list': event_str_list,
                'exists': exists,
                'max_pages': max_pages}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CONFIRM_EVENT_MESSAGE_CONTAINS,
                                    **kwargs)

    # OBSOLETE KEYWORDS ================================================================================================
    def events_confirm_event_exists(self, element_name, event_list, event_ip, event_title, event_information,
                                    exists=True, max_attempts=0, **kwargs):
        """
        OBSOLETE
        Test Cases need to be updated with the new Keyword.
        """
        args = {'event_list': event_list,
                'event_ip': event_ip,
                'event_title': event_title,
                'event_information': event_information,
                'exists': exists,
                'max_attempts': max_attempts}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CONFIRM_EVENT_EXISTS, **kwargs)

    def events_confirm_event_event(self, element_name, event, **kwargs):
        """
        OBSOLETE
        Test Cases need to be updated with the new Keyword.
        """
        args = {'event': event}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CONFIRM_EVENT_EVENT, **kwargs)

    def events_confirm_event_event_and_information(self, element_name, event, information, max_attempts,
                                                   number_events_to_check=0, **kwargs):
        """
        OBSOLETE
        Test Cases need to be updated with the new Keyword.
        """
        args = {'event': event,
                'information': information,
                'max_attempts': max_attempts,
                'number_events_to_check': number_events_to_check}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_CONFIRM_EVENT_EVENT_AND_INFORMATION,
                                    **kwargs)

    def events_confirm_event_event_information_and_source(self, element_name, event, information, source,
                                                          max_attempts=0, number_events_to_check=0, exists=True,
                                                          **kwargs):
        """
        OBSOLETE
        Test Cases need to be updated with the new Keyword.
        """
        args = {'event': event,
                'information': information,
                'source': source,
                'max_attempts': max_attempts,
                'number_events_to_check': number_events_to_check,
                'exists': exists}

        return self.execute_keyword(element_name, args,
                                    self.command_const.EVENTS_CONFIRM_EVENT_EVENT_INFORMATION_AND_SOURCE, **kwargs)

    def events_set_event_type(self, element_name, event_type, **kwargs):
        """
        OBSOLETE
        Test Cases need to be updated with the new Keyword.
        """
        args = {'event_types': event_type}

        return self.execute_keyword(element_name, args, self.command_const.EVENTS_SET_EVENT_TYPES, **kwargs)
