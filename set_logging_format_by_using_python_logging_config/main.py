import logging
import logging.config
from utils import module

# Loads The Config File
logging.config.fileConfig('./logging.ini')
# create a logger with the name from the config file. 
logger_root = logging.getLogger('root')


for i in range(75):
    logger_root.info(i)
    
# Log Messages
logger_root.debug('debug message')
logger_root.info('info message')
logger_root.warning('warning message')
logger_root.error('error message')

module.fn()