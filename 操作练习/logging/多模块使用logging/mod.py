import logging

import submod

logger = logging.getLogger('main.mod')
logger.info('logger of mod say something...')


def testLogger():
    logger.debug('this is mod.testLogger...')
    submod.tst()
