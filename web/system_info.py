import logging

import sensors.air_quality as aq
import sensors.temprature as tmp
import database.reading as dbr

# Defining logger for this module
log = logging.getLogger(__name__)


def get_temperature():
    return tmp.read_temprature().toJSON()


def get_air_quality(numReadings=1):
    log.debug('Retrieving: ' + str(numReadings))
    return dbr.read('mydbSchema', 'air_quality', numReadings)


def test():
    print('Hello, World!')
