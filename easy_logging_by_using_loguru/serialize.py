from loguru import logger
import platform

# 日誌序列化
trace= logger.add('serialize_test.log', serialize=True)

logger.info('If you are using Python {version}, prefer {feature} of course!', version=platform.python_version(), feature='f-strings')