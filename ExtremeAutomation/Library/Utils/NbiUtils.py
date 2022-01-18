class NbiUtils(object):
    def compare_dictionaries(self, dict_1, dict_2, dict_1_name, dict_2_name, path=""):
        """
        Compare two dictionaries recursively to find non matching elements. Used to compare the dict version of two
        JSON strings for NBI.

        Returns a string containing the errors. If the dicts completely match it returns ''.
        """
        err = ''
        key_err = ''
        value_err = ''
        old_path = path
        for k in dict_1.keys():
            path = old_path + "[%s]" % k
            if k not in dict_2:
                key_err += "Key %s%s not in %s\n" % (dict_2_name, path, dict_2_name)
            else:
                if isinstance(dict_1[k], dict) and isinstance(dict_2[k], dict):
                    err += self.compare_dictionaries(dict_1[k], dict_2[k], dict_1_name, dict_2_name, path)
                else:
                    if dict_1[k] != dict_2[k]:
                        value_err += "Value of %s%s (%s) not same as %s%s (%s)\n"\
                            % (dict_1_name, path, dict_1[k], dict_2_name, path, dict_2[k])

        return key_err + value_err + err
