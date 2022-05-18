import logging

def fn():
    logger_module = logging.getLogger('module')
    ## Log Messages
    logger_module.debug('module debug message')
    logger_module.info('module info message')
    logger_module.warning('module warning message')
    logger_module.error('module error message')