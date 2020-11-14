from datetime import datetime
from database import writing


class AirQualityReading:
    """An air quality reading"""
    def __init__(self, co2_level):
        self.timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
        self.co2_level = co2_level  # in ppm

    def toJSON(self):
        return self.__dict__


def read_air_quality():
    # TODO: implement this!
    print('Reading air quality')
    return AirQualityReading(442.93)
