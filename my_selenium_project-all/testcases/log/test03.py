import logging
import logging.handlers
import datetime


mylogger = logging.getLogger('mylogger')
mylogger.setLevel(logging.DEBUG)

rf_handler = logging.handlers.TimedRotatingFileHandler('all.log', when='midnight', interval=1, backupCount=7, atTime=datetime.time(0, 0, 0, 0))
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

f_handler = logging.FileHandler('error.log')
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s[:%(lineno)d] - %(message)s"))

mylogger.addHandler(rf_handler)
mylogger.addHandler(f_handler)


mylogger.debug('debug message by dexter')
mylogger.info('info message by dexter')
mylogger.warning('warning message by dexter')
mylogger.error('error message by dexter')
mylogger.critical('critical message by dexter')