class ObjectList(object):

    def __init__(self, string=None):
        """
        Init function
        """
        self.strList = string
        self.__properties = dict()
        self.modified = False
        self.inner_array = None
        self.parse()

    def get(self, index):
        """
        This function returns the object at the given index.
        """
        return self.inner_array[index]

    def get_all(self):
        """
        This function returns all objects in the ObjectList.
        """
        return self.inner_array

    def contians(self, val):
        """
        This function returns 'True' if the given value exists in the ObjectList.
        """
        return val in self.inner_array

    def size(self):
        """
        This function returns the number of objects in the ObjectList.
        """
        return len(self.inner_array)

    def add(self, val):
        """
        This function adds the given value to the ObjectList.
        """
        if self.inner_array is None:
            self.inner_array = []
        self.inner_array.update(self.parse_elements(val))
        self.strList += "," + str(val)

    def remove(self, val):
        """
        This function removes the given value from the ObjectList.
        """
        self.inner_array.remove(val)

    def __str__(self):
        """
        Returns both the original string and the parsed version.
        """
        ret_string = "Original String = " + self.strList
        ret_string += "\nParsed Values"  # + str(self.inner_array)
        index = 1
        for elm in self.inner_array:
            ret_string += "\n\t" + str(index) + ") " + str(elm)
            index += 1
        return ret_string

    def parse(self):
        """
        This function parses the ObjectList to populate the self.inner_array.
        """
        if self.inner_array is None:
            self.inner_array = []
        elif self.inner_array is not None and len(self.inner_array) > 0:
            return self.inner_array
        self.inner_array += self.parse_elements(self.strList)

    def parse_elements(self, values):
        """
        This function is defined in child classes.
        """
        pass
