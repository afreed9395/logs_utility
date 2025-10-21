
import logging
import sys
from typing import Optional

def setup_logger(
    name:str ="app",
    log_level: str = "INFO",
    log_file:Optional[str] = None,
    fmt: str = "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
):
    
    logger =  logging.getLogger(name)
    logger.setLevel(log_level.upper())
    
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(fmt)
    
    stream_handler = logging.StreamHandler(sys.stdout)
    
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        
    return logger    