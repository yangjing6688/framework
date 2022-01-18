class Component(object):
    def name(self):
        """
        This function returns the name of a given component.
        """
        return self.__class__.__name__
