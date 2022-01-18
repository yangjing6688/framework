from ExtremeAutomation.Library.Device.NetworkElement.NetelemLearning.Components.Component import Component


class ComponentCollection(Component):
    def __init__(self):
        super(ComponentCollection, self).__init__()

        self.components = []
        self.ports = []
        self._valid_components = []

    def is_component_valid(self, component):
        """
        This function checks if the passed component is valid, if it is True is returned
        otherwise raise an InvalidComponentError.
        """
        for valid_component in self._valid_components:
            if component.name() == valid_component.name():
                return True
        raise InvalidComponentError(component, self._valid_components)

    def add_component(self, component):
        """
        This function checks if the component is valid, if it is valid, it is added to the component list.
        """
        if self.is_component_valid(component):
            self.components.append(component)


class InvalidComponentError(TypeError):
    def __init__(self, component, valid_components):
        message = ("Passed component was " + component.name() + " which is not a valid component.\n" +
                   "Valid components are " + ",".join(valid_components) + ".")
        super(InvalidComponentError, self).__init__(message)
