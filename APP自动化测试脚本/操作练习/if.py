import logging

logging.basicConfig(level=logging.DEBUG,
                    format=("[%(asctime)s] %(levelname)s:%(message)s", "%Y-%m-%d %H:%M:%S"),
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='myapp.log',
                    filemode='w')

logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
