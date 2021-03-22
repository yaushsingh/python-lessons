import logging
#logging.basicConfig(format = '%(asctime)s %(levelname)s : %(message)s' , level = logging.DEBUG) #changing the default level of logging to DEBUG
#format can show date and remove the logger name
#writing more readable code
logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]%(message)s', 
    datefmt = '%d-%m-%Y %H: %M: %S',
    level =logging.DEBUG,
    filename = 'my_logs.txt' #writing and saving the logs in different files
    )
# -*s gives 8 spcaes for the level name
#()s is string format for python

logger = logging.getLogger('books')
#initiate a logger
"""logger = logging.getLogger('__name__')"""
# __name__  to have  different logger for seperate modules
 #getLogger is class of the module logging
#can be used in different file

logger.info('this will not show up')
logger.warning('This shows warning')
logger.debug('this is a debug message')
"""
level of logging
DEBUG (used while developing phase)
INFO
WARNING
ERROR
CRITICAL
""" 
logger = logging.getLogger('books.database') 
#above logger is child logger of books 
#any  config on books logger will be inherited by database logger