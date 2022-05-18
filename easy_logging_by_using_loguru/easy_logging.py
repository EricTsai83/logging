from loguru import logger

logger.debug('This is debug information')
logger.info('This is info information')
logger.warning('This is warn information')
logger.error('This is error information')

logger.add("./test1.log", rotation="1000KB", encoding="utf-8", enqueue=True, retention="10 days", level='INFO')
logger.info('This is info information')

# f-string
logger.info('If you are using Python {version}, prefer {feature} of course!', version='3.10', feature='loguru')


# 只輸出到文本，不在 console 輸出
# 清除之前的設置
logger.remove(handler_id=None) 

trace= logger.add('test2.log')

logger.error('This is error information')
logger.warning('This is warn information')

# compression 配置日誌壓縮格式
trace = logger.add('zip.log', compression='zip')
logger.warning('This is warn information')

# 只存 error log
def error_only(record):
    """
    error 日誌 判斷 
    Args:
        record: 

    Returns: 若日誌級別爲ERROR, 輸出TRUE

    """
    return record["level"].name == "ERROR"

# ERROR以外級別日誌被過濾掉
logger.add("error.log", filter=error_only)

logger.error('This is error information')
logger.warning('This is warn information')



