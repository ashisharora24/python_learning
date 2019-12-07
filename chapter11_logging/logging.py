'''
    logging the exceptions


CRITICAL    50  represents Very Serious (high attention)
ERROR       40  represents serious error
WARNING     30  represents warning message, some caution is needed
INFO        20  represents message with some important information
DEBUG       10  represents message with debugging information
NOTSET      0   represents level is not set

'''

import logging as log
log.basicConfig(filename="mylog.txt")
log.critical("represents Very Serious (high attention)")
# logging.error("represents serious error")
# logging.warning("represents warning message, some caution is needed")
# logging.info("represents message with some important information")
# logging.debug("represents message with debugging information")
# logging.notset("represents level is not set")
