from datetime import datetime

class TempratureReading:
    """A temprature reading"""
    def __init__(self, reading):
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.temprature = reading

    def toJSON(self):
        return self.__dict__


def read_temprature():
    # TDOO: implement this!
    print('Reading temprature')  # TODO: change to logging
    return TempratureReading(14.2)
