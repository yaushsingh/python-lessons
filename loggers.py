import logging
#logging.basicConfig(format = '%(asctime)s %(levelname)s : %(message)s' , level = logging.DEBUG) #changing the default level of logging to DEBUG
#format can show date and remove the logger name
#writing more readable code
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d]%(message)s', level =logging.DEBUG)
# -*s gives 8 spcaes for the level name
#()s is string format for python

#initiate a logger
logger = logging.getLogger('test_logger') #getLogger is class of the module logging
#can be used in different file

logger.info('this will not show up')
logger.warning('This shows warning')

"""
level of logging
DEBUG (used while developing phase)
INFO
WARNING
ERROR
CRITICAL
"""
