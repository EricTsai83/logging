from loguru import logger

# format 配置日誌記錄格式化模板
def format_log():
    """

    Returns:

    """
    trace = logger.add('template_test.log', format="{time:YYYY-MM-DD HH:mm:ss} {level} From {module}.{function} : {message}")

    logger.warning('This is warn information')

if __name__ == '__main__':
    format_log()