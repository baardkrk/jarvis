import logging
from datetime import datetime

log = logging.getLogger(__name__)


class TempratureReading:
    """A temprature reading"""
    def __init__(self, reading):
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.temprature = reading

    def toJSON(self):
        return self.__dict__


def read_temperature(device='default'):
    # TODO: implement this!
    log.info('Reading temperature on device \'{}\''.format(device))
    return TempratureReading(14.2)
