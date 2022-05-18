# 對 class 中的 method 和 static method 的代碼實例
from loguru import logger

trace = logger.add('class_traceback_test.log')

class Demo:
    @logger.catch
    def index_error(self, custom_list: list):
        for index in range(len(custom_list)):
            index_value = custom_list[index]
            if custom_list[index] < 2:
                custom_list.remove(index_value)

    @staticmethod
    @logger.catch
    def index_error_static(custom_list: list):
        for index in range(len(custom_list)):
            index_value = custom_list[index]
            if custom_list[index] < 2:
                custom_list.remove(index_value)


if __name__ == '__main__':
    # Demo().index_error([1, 2, 3])
    Demo.index_error_static([1, 2, 3])