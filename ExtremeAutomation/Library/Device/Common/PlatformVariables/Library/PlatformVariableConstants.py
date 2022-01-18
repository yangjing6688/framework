class PlatformVariableConstants(object):
    TYPE_NETWORK_ELEMENT = "NetworkElement"
    TYPE_END_SYSTEM_ELEMENT = "EndsystemElement"
    TYPE_UI_ELEMENT = "UiElement"

    YAML_NETWORK_ELEM_PREFIX = "netelem"
    YAML_END_SYSTEM_ELEM_PREFIX = "endsys"
    YAML_UI_ELEM_PREFIX = "uielem"

    # Don't allow values to be updated
    def __setattr__(self, *_):
        pass
