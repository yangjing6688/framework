class Singleton(type):
    """
    Use this metaclass to create a singleton. To use set metaclass=Singleton in
    the class declaration.

    For example...

    class MyClass(object, metaclass=Singleton):
        def __init__(self):
            pass
    """

    def __init__(cls, name, bases, _dict):
        super(Singleton, cls).__init__(name, bases, _dict)
        cls.instance = None

    def __call__(cls, *args, **kwargs):
        """
        This function checks to see if an instance of the class has been created. If it has
        we return the existing instance, otherwise instantiate one.
        """
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instance
