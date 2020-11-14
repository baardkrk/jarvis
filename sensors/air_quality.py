import logging

from datetime import datetime
from database import writing

log = logging.getLogger(__name__)


class AirQualityReading:
    """An air quality reading"""
    def __init__(self, co2_level):
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.co2_level = co2_level  # in ppm

    def toJSON(self):
        return self.__dict__


def read_air_quality(device='default'):
    # TODO: implement this!
    log.info('Reading air quality on device \'{}\'.'.format(device))
    return AirQualityReading(442.93)
