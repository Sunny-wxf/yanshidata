# coding=utf-8
import logging
import logging.handlers


class Log(object):
    __file = 'log.log'  # 日志文件名称
    __handler = False
    __fmt = '%(asctime)s - %(name)s - %(filename)s:[line:%(lineno)s] : %(message)s'  # 输出格式

    def __init__(self):
        logging.basicConfig(filename=self.__file, filemode='a+', format=self.__fmt)
        self.__handler = logging.StreamHandler()
        self.__handler.setLevel(logging.DEBUG)

        # 设置格式
        formatter = logging.Formatter(self.__fmt)
        self.__handler.setFormatter(formatter)
        return

    # 获取实例
    def get_instance(self, strname):
        logger = logging.getLogger(strname)
        logger.addHandler(self.__handler)
        logger.setLevel(logging.DEBUG)
        return logger


if __name__ == "__main__":
    log = Log()
    logging = log.get_instance('wangxiaofeng')
    logging.debug('123454')
