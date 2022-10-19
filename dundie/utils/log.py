import logging
import os
from logging import handlers

LOG_LEVEL = os.getenv("LOG_LEVEL", "WARNING").upper()
log = logging.getLogger("dundie")
fmt = logging.Formatter(
        '%(asctime)s %(name)s %(levelname)s l:%(lineno)d f:%(filename)s: %(message)s'
    )


def get_logger(logfile="dundie.log"):
    """Retruns a configured logger."""
    # ch = logging.StreamHandler() # Console/Terminalstderr
    # ch.setLevel(LOG_LEVEL)
    fh = handlers.RotatingFileHandler(
        "dundie.log", 
        maxBytes=300, # 10** 6 ~1MB
        backupCount=10,
        )
    fh.setLevel(LOG_LEVEL)
    
    # ch.setFormatter(fmt)
    # log.addHandler(ch)
    fh.setFormatter(fmt)
    log.addHandler(fh)
    return log
