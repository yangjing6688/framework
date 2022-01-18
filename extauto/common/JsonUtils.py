import json
from common.Utils import Utils


class JsonUtils:
    def __init__(self):
        self.utils = Utils()

    def get_json_value(self, json_data, json_key, key_type='default'):
        """
         - This Keyword gets the key_str value from the api response json raw data
         :param json_data:  raw json data
         :param json_key: json key
         :param index: optional index of the array
         :return: value
         """
        self.utils.print_debug("JSON Data: ", json_data)
        self.utils.print_debug("JSON Data Type: ", type(json_data))
        self.utils.print_debug("JSON Key: ", json_key)
        self.utils.print_debug("JSON Key Type: ", key_type)

        json_values = json.loads(json_data)
        self.utils.print_debug("json_values: ", json_values)

        return json_values[json_key]

    def get_json_val(self, json_data, json_key, key_type='default'):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data
         :param json_data:  raw json data
         :param json_key: json key
         :param key_type: optional index of the array
         :return: value
         """
        self.utils.print_info("*************************************************")
        self.utils.print_info("JSON Data: ", json_data)
        self.utils.print_info("JSON Data Type: ", type(json_data))
        self.utils.print_info("JSON Key: ", json_key)
        self.utils.print_info("JSON Key Data Type: ", type(json_key))
        self.utils.print_info("JSON Key Type: ", key_type)

        if isinstance(json_data, bytes):
            json_values = json.loads(json_data.decode('utf-8'))
            if key_type == 'index':
                return json_values[int(json_key)]
            self.utils.print_info("JSON DATA is bytes. Returning Value: ", json_values[json_key])
            return json_values[json_key]

        elif isinstance(json_data, dict):
            self.utils.print_info("JSON DATA is dict. Returning Value: ", json_data[str(json_key)])
            return json_data[str(json_key)]

        elif isinstance(json_data, list):
            self.utils.print_info("JSON DATA is list. Returning Value: ", json_data[int(json_key)])
            return json_data[int(json_key)]

    def get_json_values(self, json_data, json_key):
        """
         - This Keyword is used to get the  key_str value from the api response json raw data
         :param json_data:  raw json data
         :param json_key: json key
         :param index: optional index of the array
         :return: value
         """
        json_keys = json_key.split(',')
        json_val = -1

        for key1 in json_keys:
            key_type, _key= key1.split('=')
            self.utils.print_debug("json_data: ", json_data)
            self.utils.print_debug("_key: ", _key)
            self.utils.print_debug("key_type: ", key_type)

            json_val = self.get_json_val(json_data, _key, key_type)
            json_data = json_val
        return json_val

    def get_json_value_as_string(self, json_data):
        """
        - This Keyword is used to get the  key_str value from the api response json raw data
        :param json_data:  raw json data from the API call to get the device ids
        :param device_mac: mac of the device to match the dict
        :param key_str:  key string to get the value
        :return: key_str value
        """
        encoding = 'utf-8'
        return json_data.decode(encoding)
