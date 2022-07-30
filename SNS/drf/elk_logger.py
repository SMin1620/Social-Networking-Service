import logging, logstash

log_format = logging.Formatter('\n[%(levelname)s|%(name)s|%(filename)s:%(lineno)s] %(asctime)s > %(message)s')


def create_logger(logger_name):
    logger = logging.getLogger(logger_name)
    if len(logger.handlers) > 0:  # 로거가 이미 존재하는 경우
        return logger

    logger.setLevel(logging.INFO)
    logger.addHandler(logstash.TCPLogstashHandler('localhost', 5000, version=1))  #

    return logger
