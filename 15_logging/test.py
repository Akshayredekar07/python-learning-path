import logging
import student

logging.basicConfig(filename='test.log', level=logging.DEBUG)

logging.debug("DEBUG message from test module")
logging.info("INFO message from test module")
logging.warning("WARNING message from test module")
logging.error("ERROR message from test module")
logging.critical("CRITICAL message from test module")


# Problems with root logger
    # 1. Onces we set basic Configuration then that             configuration is final and we cannot change.

    # 2. It will always work only for handler eithwer file or   consloe but not both simultanously.

    # 3. It is not possible to configure logger with different configurations at different levels.

    # 4. We cannot specify multiple log files for multiple modules/classes/methods


def f1():
    pass    

def f2():
    pass

def f3():
    pass


