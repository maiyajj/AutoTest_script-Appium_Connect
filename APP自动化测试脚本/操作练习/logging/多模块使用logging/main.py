import logging.config

logging.config.fileConfig('logging.conf')
root_logger = logging.getLogger('root')
root_logger.debug('test root logger...')

logger = logging.getLogger('main')
logger.info('test main logger')
logger.info('start import module \'mod\'...')
import mod

logger.debug('let\'s test mod.testLogger()')
mod.testLogger()

root_logger.info('finish test...')
