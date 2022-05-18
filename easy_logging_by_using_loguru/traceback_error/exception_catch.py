from loguru import logger

trace = logger.add('exception_catch_test.log')

def index_error(custom_list: list):
    for index in range(len(custom_list)):
        try:
            index_value = custom_list[index]
        except IndexError as  err:
            logger.exception(err)
            break

        if custom_list[index] < 2:
            custom_list.remove(index_value)


if __name__ == '__main__':
    index_error([1, 2, 3])