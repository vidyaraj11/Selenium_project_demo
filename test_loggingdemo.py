import logging

logging.basicConfig(filename="test.log", filemode="w")
h = "hi"
logging.debug("hello")
logging.warning("hello")
logging.warning("this", h)