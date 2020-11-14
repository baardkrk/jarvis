# Including packages from parent directory
import os
import sys
sys.path.append(os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        '..'
    )))

import sensors.air_quality as aq
import sensors.temprature as tmp
import database.reading as dbr


def get_temprature():
    return tmp.read_temprature().toJSON()


def get_air_quality(numReadings):
    print('Retrieving: ' + str(numReadings))
    return dbr.read('', '', numReadings)


def test():
    print('Hello, World!')
