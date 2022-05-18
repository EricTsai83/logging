from loguru import logger

trace= logger.add('traceback_catch_test.log')

@logger.catch
def index_error(custom_list: list):

    for index in range(len(custom_list)):
        index_value = custom_list[index]
        if custom_list[index] < 2 :
            custom_list.remove(index_value)

        print(index_value)

if __name__ == '__main__':
    index_error([1,2,3])