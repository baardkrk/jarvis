import logging

log = logging.getLogger(__name__)


def read(schema, table, rows):
    log.info('Retrieving {} rows from {}.{}'.format(rows, schema, table))
    readings = 'a, b, c'
    return readings
