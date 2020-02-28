import logging

#Create and configure logger
logging.basicConfig(filename="newfile.log",format='%(asctime)s %(message)s',filemode='w')

#Creating an object giving new name if u want to give somthing like heading give in arg
logger=logging.getLogger("Python")

#Setting the threshold of logger to DEBUG setting the level as debug so it will check from the 1st level
# if u give as wraning it will check only warning,error and critical
#level as error error and critical
logger.setLevel(logging.DEBUG)

#Test messages
logger.debug("Harmless debug Message")
logger.info("Just an information")
logger.warning("Its a Warning")
logger.error("Did you try to divide by zero")
logger.critical("Internet is down")

