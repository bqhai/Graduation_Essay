import logging


log_format = '%(asctime)s:''|%(levelname)s|\t''%(filename)s:''%(funcName)s():''%(lineno)d\t''--%(message)s'
logging.basicConfig(level=logging.DEBUG, filename='../log/run_time.log', filemode='a', format=log_format, datefmt='%d/%m/%Y %H:%M:%S')

