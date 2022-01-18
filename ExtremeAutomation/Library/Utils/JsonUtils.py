import re
import json
import inspect
from ExtremeAutomation.Library.Utils.StringUtils import StringUtils
from ExtremeAutomation.Library.Logger.Logger import Logger


class JsonUtils(object):
    @staticmethod
    def convert_to_json(json_input, pretty_print):
        """Converts the supplied data into a json dictionary."""
        if pretty_print:
            return str(json.dumps(json_input, default=lambda o: o.__dict__, cls=JsonObjectEncoder, indent=2,
                                  sort_keys=False, skipkeys=True))
        else:
            return json.loads(
                json.dumps(json_input, default=lambda o: o.__dict__, cls=JsonObjectEncoder, indent=0, sort_keys=False,
                           skipkeys=True))

    @staticmethod
    def search_json(json_input, search_key, search_value, exact_match):
        """This function will verify that a specific key/value pair is present within the given json."""
        if not isinstance(json_input, dict):
            json_input = StringUtils.format_json_output(json_input)

        exact_match = StringUtils.string_to_boolean(exact_match)

        result, missing = JsonUtils.__recursive_search_json(json_input, search_key, search_value, exact_match)
        if missing is not None and missing != {} and missing != []:
            Logger().log_info("The following items were missing in the output: \n" +
                              "***Items are listed inside their nested locations***\n" + str(missing))

        return True if result else False

    @staticmethod
    def __recursive_search_json(json_input, search_key, search_value, exact_match):
        if json_input is None:
            return False, None

        result = False
        if search_key in json_input:
            if not exact_match:
                if (isinstance(json_input[search_key], dict) and isinstance(search_value, dict)) or \
                        (isinstance(json_input[search_key], list) and isinstance(search_value, list)):
                    return JsonUtils.__recursive_search_values(json_input[search_key], search_value)
            if str(json_input[search_key]) == str(search_value):
                return True, None

        if isinstance(json_input, dict):
            for key in json_input.keys():
                if isinstance(json_input[key], dict) or isinstance(json_input[key], list):
                    result, missing = JsonUtils.__recursive_search_json(json_input[key], search_key, search_value,
                                                                        exact_match)
                    if result is not None:
                        return result, missing

        elif isinstance(json_input, list):
            for item in json_input:
                if isinstance(item, dict) or isinstance(item, list):
                    result, missing = JsonUtils.__recursive_search_json(item, search_key, search_value, exact_match)
                    if result is not None:
                        return result, missing

        return result, {search_key: search_value}

    @staticmethod
    def __recursive_search_values(json_input, search_input):
        if isinstance(search_input, dict):
            not_found = {}
            result = True
            for key in search_input:
                if key in json_input:
                    if isinstance(search_input[key], dict) and isinstance(json_input[key], dict) or \
                            isinstance(search_input[key], list) and isinstance(json_input[key], list):
                        check, missing = JsonUtils.__recursive_search_values(json_input[key], search_input[key])
                        if missing is not None and missing != {} and missing != []:
                            not_found[key] = missing
                        if not check:
                            result = False
                    else:
                        if str(search_input[key]) != str(json_input[key]):
                            not_found[key] = search_input[key]
                            result = False
                else:
                    not_found[key] = search_input[key]
                    result = False
            return result, not_found
        else:
            not_found = []
            fail = False
            result = False
            if search_input == json_input:
                return True, None
            for item in search_input:
                result = False
                not_found.append(item)
                if isinstance(item, dict):
                    for j_item in json_input:
                        if isinstance(j_item, dict):
                            result, missing = JsonUtils.__recursive_search_values(j_item, item)
                            if result:
                                not_found.remove(item)
                                break
                    if not result:
                        fail = True
                elif isinstance(item, list):
                    for j_item in json_input:
                        if isinstance(j_item, list):
                            result, missing = JsonUtils.__recursive_search_values(j_item, item)
                            if result:
                                not_found.remove(item)
                                break
                    if not result:
                        fail = True
                else:
                    if item in json_input:
                        not_found.remove(item)

            return result if not fail else False, not_found

    @staticmethod
    def search_json_regex(json_input, search_key, search_value):
        """This function will verify that a specific key/value pair is present within the given json."""
        if not isinstance(json_input, dict):
            json_input = StringUtils.format_json_output(json_input)

        result, missing = JsonUtils.__recursive_regex_search_json(json_input, search_key, search_value)
        if missing is not None and missing != {} and missing != []:
            Logger().log_info("The following items were missing in the output: \n" +
                              "***Items are listed inside their nested locations***\n" + str(missing))

        return True if result else False

    @staticmethod
    def __recursive_regex_search_json(json_input, search_key, search_value):
        if json_input is None:
            return False, None

        if search_key in json_input:
            if (isinstance(json_input[search_key], dict) and isinstance(search_value, dict)) or \
                    (isinstance(json_input[search_key], list) and isinstance(search_value, list)):
                return JsonUtils.__recursive_regex_search_values(json_input[search_key], search_value)
            else:
                if re.search(str(search_value), str(json_input[search_key])):
                    return True, None

        if isinstance(json_input, dict):
            for key in json_input.keys():
                if isinstance(json_input[key], dict) or isinstance(json_input[key], list):
                    result, missing = JsonUtils.__recursive_regex_search_json(json_input[key], search_key, search_value)
                    if result is not None:
                        return result, missing

        elif isinstance(json_input, list):
            for item in json_input:
                if isinstance(item, dict) or isinstance(item, list):
                    result, missing = JsonUtils.__recursive_regex_search_json(item, search_key, search_value)
                    if result is not None:
                        return result, missing

    @staticmethod
    def __recursive_regex_search_values(json_input, search_input):
        if not search_input and type(search_input) == type(json_input):
            if not json_input:
                return True, None
            return False, json_input
        if isinstance(search_input, dict):
            not_found = {}
            result = True
            for key in search_input:
                if key in json_input:
                    if isinstance(search_input[key], dict) and isinstance(json_input[key], dict) or \
                            isinstance(search_input[key], list) and isinstance(json_input[key], list):
                        result, missing = JsonUtils.__recursive_regex_search_values(json_input[key], search_input[key])
                        if missing is not None and missing != {} and missing != []:
                            not_found[key] = missing
                    else:
                        if not re.search(str(search_input[key]), str(json_input[key])):
                            not_found[key] = search_input[key]
                            result = False
                else:
                    not_found[key] = search_input[key]
                    result = False
            return result, not_found
        else:
            not_found = []
            fail = False
            result = False
            if not isinstance(json_input, list):
                if re.search(str(search_input), str(json_input)):
                    return True, None
                else:
                    not_found.append(search_input)
                    return False, not_found
            else:
                for item in search_input:
                    result = False
                    not_found.append(item)
                    if isinstance(item, dict):
                        for j_item in json_input:
                            if isinstance(j_item, dict):
                                result, missing = JsonUtils.__recursive_regex_search_values(j_item, item)
                                if result:
                                    not_found.remove(item)
                                    break
                        if not result:
                            fail = True
                    elif isinstance(item, list):
                        for j_item in json_input:
                            if isinstance(j_item, list):
                                result, missing = JsonUtils.__recursive_regex_search_values(j_item, item)
                                if result:
                                    not_found.remove(item)
                                    break
                        if not result:
                            fail = True
                    else:
                        for j_item in json_input:
                            result = re.search(item, j_item)
                            if result:
                                not_found.remove(item)
                                break
                        if not result:
                            fail = True

            return result if not fail else False, not_found


class JsonObjectEncoder(json.JSONEncoder):
    def default(self, obj):
        """Encodes the provided object to json format."""
        if hasattr(obj, "to_json"):
            return self.default(obj.to_json())
        elif hasattr(obj, "__dict__"):
            d = dict(
                (key, value)
                for key, value in inspect.getmembers(obj) if not
                key.startswith("__") and not
                inspect.isabstract(value) and not
                inspect.isbuiltin(value) and not
                inspect.isfunction(value) and not
                inspect.isgenerator(value) and not
                inspect.isgeneratorfunction(value) and not
                inspect.ismethod(value) and not
                inspect.ismethoddescriptor(value) and not
                inspect.isroutine(value)
            )
            return self.default(d)
        return obj
