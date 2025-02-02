import logging


log_format = '%(asctime)s.%(msecs)03d ''|%(levelname)s|\t''%(filename)s:''%(funcName)s():''%(lineno)d ''--%(message)s'
logging.basicConfig(level=logging.INFO, filename='log/run_time.log', filemode='a', format=log_format, datefmt='%d/%m/%Y %H:%M:%S')

