class Constants(object):
    # Don't allow values to be updated
    def __setattr__(self, *_):
        pass
